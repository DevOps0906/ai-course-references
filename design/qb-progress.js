/* QB 학습 진행 계산 — 모든 은행의 localStorage(qb:<id>:v1)에서 연속 학습일·히트맵·XP·오답을 계산한다.
   읽기 전용. 저장 형식은 quiz.html의 S = {name, tabs:{id:{score,total,at}}, wrong:{id:{n,at,solved}}, board:[{name,score,at,...}]}.
   시각은 모두 Date.now() 밀리초. 날짜는 브라우저 로컬 시간대 기준. */
(function(root){
'use strict';
function pad(n){return n<10?'0'+n:''+n;}
function dayKey(t){var d=new Date(t);return d.getFullYear()+'-'+pad(d.getMonth()+1)+'-'+pad(d.getDate());}
function sod(t){var d=new Date(t);d.setHours(0,0,0,0);return d;}
function addDays(d,n){var x=new Date(d.getTime());x.setDate(x.getDate()+n);return x;}
function num(v){return typeof v==='number'&&isFinite(v)?v:0;}
function store(o){return (o&&o.storage)||root.localStorage;}
function readBank(o,id){
  try{var r=store(o).getItem('qb:'+id+':v1');if(!r)return null;var s=JSON.parse(r);return s&&typeof s==='object'?s:null;}
  catch(e){return null;}
}
function userName(o){
  if(o&&o.name!=null)return String(o.name).trim();
  try{var u=root.QB&&root.QB.user&&root.QB.user();return u&&u.name?String(u.name).trim():'';}catch(e){return '';}
}
function banksOf(cat,o){
  var out=[];
  ((cat&&cat.stages)||[]).forEach(function(st){(st.courses||[]).forEach(function(c){(c.banks||[]).forEach(function(b){
    if(!o||!o.subject||(b.subject||'it')===o.subject)out.push(b);
  });});});
  return out;
}

var QBP={};
QBP.dayKey=dayKey;
QBP.banks=banksOf;

/* 저장소를 쓸 수 있는지 */
QBP.storageOk=function(o){
  try{var s=store(o),k='qb:__probe';s.setItem(k,'1');s.removeItem(k);return true;}catch(e){return false;}
};

/* 모든 은행을 한 번 읽어 이벤트·은행별 집계·XP 재료를 만든다. */
QBP.snapshot=function(cat,o){
  var name=userName(o),per={},events=[];
  var xpTab=0,xpWrong=0,xpGame=0,gameN=0,avgSum=0,correct=0,total=0;
  banksOf(cat,o).forEach(function(b){
    var s=readBank(o,b.id)||{},p={done:0,tabs:b.tabs||0,correct:0,total:0,open:0,solved:0,lastAt:0};
    var tabs=s.tabs&&typeof s.tabs==='object'?s.tabs:{};
    Object.keys(tabs).forEach(function(tid){
      var r=tabs[tid];if(!r||typeof r!=='object')return;
      p.done++;p.correct+=num(r.score);p.total+=num(r.total);
      if(num(r.at))events.push({at:r.at,bankId:b.id,kind:'tab',tabId:tid,score:num(r.score),total:num(r.total)});
    });
    var wr=s.wrong&&typeof s.wrong==='object'?s.wrong:{};
    Object.keys(wr).forEach(function(qid){
      var w=wr[qid];if(!w||typeof w!=='object')return;
      if(w.solved){p.solved++;if(num(w.at))events.push({at:w.at,bankId:b.id,kind:'wrong-solved',qid:qid});}
      else p.open++;
    });
    (Array.isArray(s.board)?s.board:[]).forEach(function(r){
      if(!r||typeof r!=='object'||!name||String(r.name||'').trim()!==name)return;
      xpGame+=num(r.score)/100;gameN++;avgSum+=num(r.avg);
      if(num(r.at))events.push({at:r.at,bankId:b.id,kind:'game',score:num(r.score),correct:num(r.correct),total:num(r.total),mode:r.mode||''});
    });
    p.pct=p.tabs?Math.round(p.done/p.tabs*100):0;
    xpTab+=p.correct*10;xpWrong+=p.solved*5;correct+=p.correct;total+=p.total;
    per[b.id]=p;
  });
  events.sort(function(a,b){return b.at-a.at;});
  events.forEach(function(e){var p=per[e.bankId];if(p&&e.at>p.lastAt)p.lastAt=e.at;});
  return {per:per,events:events,name:name,correct:correct,total:total,
    xp:{tab:xpTab,wrong:xpWrong,game:Math.round(xpGame),total:Math.round(xpTab+xpWrong+xpGame)},
    gameN:gameN,gameAvg:gameN?Math.round(avgSum/gameN*10)/10:null};
};
/* events(cat): 스냅샷 없이 이벤트 목록만 */
QBP.events=function(cat,o){return QBP.snapshot(cat,o).events;};

/* 합계: 채점한 탭 x/전체, 정답률, 남은 오답 */
QBP.totals=function(snap,cat,o){
  var banks=banksOf(cat,o),done=0,tabs=0,open=0,solved=0;
  banks.forEach(function(b){var p=snap.per[b.id];tabs+=b.tabs||0;if(p){done+=p.done;open+=p.open;solved+=p.solved;}});
  return {doneTabs:done,allTabs:tabs,accuracy:snap.total?Math.round(snap.correct/snap.total*100):null,
    unsolved:open,solved:solved,banks:banks.length,qs:banks.reduce(function(n,b){return n+(b.qs||0);},0)};
};
QBP.xp=function(snap){return snap.xp;};

/* 연속 학습일: 오늘 또는 어제로 끝나는 연속 일수 */
QBP.activeToday=function(events,now){
  var k=dayKey(now==null?Date.now():now);return events.some(function(e){return dayKey(e.at)===k;});
};
QBP.streak=function(events,now){
  var days={};events.forEach(function(e){days[dayKey(e.at)]=1;});
  var d=sod(now==null?Date.now():now);
  if(!days[dayKey(d)])d=addDays(d,-1);
  var n=0;while(days[dayKey(d)]){n++;d=addDays(d,-1);}
  return n;
};

/* 히트맵: 일요일 시작 주 단위, 열 우선(주 × 7). 단계 0~4 (0=없음, 1=1~2, 2=3~5, 3=6~9, 4=10+) */
function level(c){return c<=0?0:c<=2?1:c<=5?2:c<=9?3:4;}
QBP.heatmap=function(events,weeks,now){
  weeks=weeks||16;
  var today=sod(now==null?Date.now():now),count={};
  events.forEach(function(e){var k=dayKey(e.at);count[k]=(count[k]||0)+1;});
  var start=addDays(today,-today.getDay()-(weeks-1)*7),cells=[],active=0,max=0,total=0;
  for(var i=0;i<weeks*7;i++){
    var d=addDays(start,i),k=dayKey(d),future=d.getTime()>today.getTime(),c=future?0:(count[k]||0);
    if(c){active++;total+=c;if(c>max)max=c;}
    cells.push({date:k,count:c,level:level(c),future:future,dow:d.getDay()});
  }
  return {cells:cells,weeks:weeks,activeDays:active,max:max,total:total};
};

/* 최근 활동: 같은 은행·같은 날의 오답 해결은 한 줄로 묶는다 */
QBP.recent=function(events,n){
  var out=[],last=null;
  for(var i=0;i<events.length&&out.length<(n||8);i++){
    var e=events[i];
    if(e.kind==='wrong-solved'&&last&&last.kind==='wrong-solved'&&last.bankId===e.bankId&&dayKey(last.at)===dayKey(e.at)){last.count++;continue;}
    last=Object.assign({},e);if(last.kind==='wrong-solved')last.count=1;out.push(last);
  }
  return out;
};

/* 이어서 풀기: 최근에 푼 은행(전부 채점하지 않은 것) 먼저, 그다음 아직 시작하지 않은 은행을 카탈로그 순서로 */
QBP.continueList=function(cat,n,snap,o){
  snap=snap||QBP.snapshot(cat,o);
  var list=banksOf(cat,o).filter(function(b){var p=snap.per[b.id];return !p||p.done<(b.tabs||0);})
    .map(function(b,i){var p=snap.per[b.id]||{done:0,lastAt:0};return {bank:b,done:p.done,lastAt:p.lastAt||0,i:i};});
  list.sort(function(a,b){return (b.lastAt-a.lastAt)||(a.i-b.i);});
  return list.slice(0,n||3);
};

root.QBP=QBP;
if(typeof module!=='undefined'&&module.exports)module.exports=QBP;
})(typeof window!=='undefined'?window:globalThis);

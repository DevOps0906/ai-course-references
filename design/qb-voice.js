/* qb-voice.js — 음성으로 보기 번호 고르기(Web Speech API) + 문제 읽기(speechSynthesis)
   window.QBVoice: supported · canSpeak · parse · attach · speak · cancelSpeak · isSpeaking · stopListening
   parse()는 순수 함수라 node에서도 테스트한다. */
(function(root){
'use strict';

/* ── 말 → 선택 해석 (순수 함수) ───────────────── */
const SINO={일:1,이:2,삼:3,사:4,오:5,육:6,칠:7,팔:8,구:9,십:10};
const NAT={하나:1,둘:2,셋:3,넷:4,다섯:5,여섯:6,일곱:7,여덟:8,아홉:9,열:10};
const DET={한:1,두:2,세:3,네:4,첫:1};  // 한/두/세/네/첫 은 '번'·'번째'·'째'가 붙을 때만 번호
// 보기 글자 A~H. '이'(E)는 숫자 2와 겹쳐 숫자를 우선하므로 영문 e로만 받는다
const LET={a:1,b:2,c:3,d:4,e:5,f:6,g:7,h:8,에이:1,비:2,씨:3,디:4,에프:6,지:7,에이치:8};

const alt=o=>Object.keys(o).sort((x,y)=>y.length-x.length).join('|');
const PRE='(?:정답은|정답이|정답|답은|답이|답|내답은|제답은|저는|나는|전|선택|번호)?';
const SUF='(?:이에요|이요|예요|이야|이죠|이다|입니다|이라고생각해요|이라고|선택할게요?|선택|할게요?|할래요?|고를게요?|고를래요?|정답|같아요|요|으로|로|을|를|이|가|은|는)*';
const R_DIGIT=new RegExp('^'+PRE+'(\\d{1,2})(?:번째|번|째)?'+SUF+'$');
const R_STD=new RegExp('^'+PRE+'('+alt(Object.assign({},SINO,NAT))+')(?:번째|번|째)?'+SUF+'$');
const R_DET=new RegExp('^'+PRE+'('+alt(DET)+')(?:번째|번|째)'+SUF+'$');
const R_LET=new RegExp('^'+PRE+'('+alt(LET)+')(?:번)?'+SUF+'$');
const R_X=/틀|아니|아닙|아닌|안맞|맞지않|엑스|가위|^x(?:요|입니다)?$/;
const R_O=/^(?:o|오|동그라미|오케이|ok|예|네|응|그래요?|맞.*)(?:요|입니다|이요|예요|야|라고생각해요)?$/;
const R_SUBMIT=/제출|채점|확인|다풀었|다했/;

function norm(s){
  return String(s==null?'':s).normalize('NFKC').toLowerCase().replace(/[\s.,!?'"“”‘’~…·\-_()\[\]]/g,'');
}
function numOf(t){
  let m;
  if((m=R_DIGIT.exec(t)))return +m[1];
  if((m=R_STD.exec(t)))return SINO[m[1]]||NAT[m[1]];
  if((m=R_DET.exec(t)))return DET[m[1]];
  if((m=R_LET.exec(t)))return LET[m[1]];
  return 0;
}
function parseOne(raw,count,type){
  const t=norm(raw);if(!t)return null;
  if(type==='ox'){
    if(R_X.test(t))return {kind:'ox',v:'X'};
    if(R_O.test(t))return {kind:'ox',v:'O'};
    const n=numOf(t);  // ox에서 1번 = O, 2번 = X (게임 모드 키와 같음)
    if(n===1)return {kind:'ox',v:'O'};
    if(n===2)return {kind:'ox',v:'X'};
    return R_SUBMIT.test(t)?{kind:'submit'}:null;
  }
  const n=numOf(t)||numOf(t.replace(/(?:제출|채점|확인).*$/,''));  // '3번 제출'은 번호 우선
  if(n)return n>=1&&n<=count?{kind:'index',i:n-1}:null;  // 범위 밖이면 다음 후보로
  return R_SUBMIT.test(t)?{kind:'submit'}:null;
}
/* text: 문자열 또는 후보 배열. 범위 안에서 해석되는 첫 후보를 돌려준다 */
function parse(text,opt){
  opt=opt||{};
  const count=opt.count>0?opt.count:4, type=opt.type||'mc';
  const list=Array.isArray(text)?text:[text];
  for(const s of list){const r=parseOne(s,count,type);if(r)return r;}
  return null;
}

/* ── 브라우저 부분 ────────────────────────── */
const hasWin=typeof window!=='undefined';
const SR=()=>hasWin?(window.SpeechRecognition||window.webkitSpeechRecognition):null;
const supported=()=>!!SR();
const canSpeak=()=>hasWin&&'speechSynthesis' in window&&typeof SpeechSynthesisUtterance!=='undefined';

const ERR={
  'not-allowed':'마이크 권한이 꺼져 있습니다. 주소창의 마이크 아이콘에서 허용하세요.',
  'service-not-allowed':'마이크 권한이 꺼져 있습니다. 주소창의 마이크 아이콘에서 허용하세요.',
  'network':'음성 인식은 인터넷 연결이 필요합니다.',
  'no-speech':'소리가 들리지 않았습니다. 다시 눌러 말해 주세요.',
  'audio-capture':'마이크를 찾을 수 없습니다.'
};
let active=null;  // 지금 듣는 중인 컨트롤러 (동시에 하나만)
function stopListening(){if(active){active.stop();active=null;}}

function describe(r){
  if(r.kind==='index')return `'${r.i+1}번'으로 들었습니다`;
  if(r.kind==='ox')return `'${r.v}'로 들었습니다`;
  return "'제출'로 들었습니다";
}

/* o: {button, live, getOptions, getType, select, submit, lang, bind}
   button·live는 요소 또는 요소를 돌려주는 함수(카드를 다시 그려도 새 요소를 찾도록).
   select(r): r = {kind:'index',i} | {kind:'ox',v}. submit(): 제출. bind:false면 클릭 리스너를 달지 않는다(위임용) */
function attach(o){
  const get=x=>typeof x==='function'?x():x;
  const ctl={listening:false,toggle(){},stop(){}};
  const b0=get(o.button);
  if(!supported()){if(b0)b0.hidden=true;return ctl;}
  const lang=o.lang||'ko-KR';
  let rec=null, done=false;
  function ui(state,msg){
    const b=get(o.button), l=get(o.live);
    if(b){b.dataset.state=state;b.setAttribute('aria-pressed',state==='listening'?'true':'false');}
    if(l&&msg!=null)l.textContent=msg;
  }
  ctl.stop=function(){
    ctl.listening=false;done=true;
    if(rec){try{rec.abort();}catch(e){}rec=null;}
    ui('idle');
  };
  function finish(state,msg){if(done)return;done=true;ctl.listening=false;rec=null;if(active===ctl)active=null;ui(state,msg);}
  function onResult(alts){
    const count=o.getOptions?o.getOptions():4, type=o.getType?o.getType():'mc';
    let r=parse(alts,{count,type});
    if(r&&r.kind==='submit'&&!o.submit)r=null;
    if(!r){
      const heard=(alts[0]||'').trim().slice(0,24);
      const guide=type==='ox'?"'O' 또는 'X'로 말해 주세요.":`1~${count}번 중에서 말해 주세요.`;
      finish('error',heard?`'${heard}'로 들었습니다. ${guide}`:'소리가 들리지 않았습니다. 다시 눌러 말해 주세요.');
      return;
    }
    finish('heard');
    try{if(r.kind==='submit')o.submit();else o.select(r);}catch(e){}
    ui('heard',describe(r));  // select가 카드를 다시 그렸더라도 새 요소에 상태를 적는다
  }
  ctl.toggle=function(){
    if(ctl.listening){ctl.stop();return;}
    stopListening();cancelSpeak();
    const Ctor=SR();
    try{rec=new Ctor();}catch(e){ui('error','음성 인식을 시작할 수 없습니다.');return;}
    done=false;ctl.listening=true;active=ctl;
    rec.lang=lang;rec.continuous=false;rec.interimResults=false;rec.maxAlternatives=5;
    rec.onresult=ev=>{
      const res=ev.results&&ev.results[0], alts=[];
      if(res)for(let i=0;i<res.length;i++)alts.push(res[i].transcript);
      onResult(alts);
    };
    rec.onerror=ev=>{
      if(ev.error==='aborted')return;
      finish('error',ERR[ev.error]||'음성 인식에 실패했습니다. 다시 눌러 주세요.');
    };
    rec.onend=()=>{if(!done)finish('error',ERR['no-speech']);};
    ui('listening','듣는 중…');
    try{rec.start();}catch(e){finish('error','음성 인식을 시작할 수 없습니다. 잠시 뒤 다시 눌러 주세요.');}
  };
  if(o.bind!==false&&b0)b0.addEventListener('click',ctl.toggle);
  return ctl;
}

/* ── 읽어 주기 ────────────────────────────── */
function pickVoice(lang){
  try{
    const vs=speechSynthesis.getVoices();
    return vs.find(v=>v.lang===lang)||vs.find(v=>v.lang&&v.lang.replace('_','-').toLowerCase().startsWith(lang.slice(0,2).toLowerCase()))||null;
  }catch(e){return null;}
}
function speak(text,lang){
  if(!canSpeak()||!text)return false;
  lang=lang||'ko-KR';
  try{
    speechSynthesis.cancel();
    const u=new SpeechSynthesisUtterance(String(text));
    u.lang=lang;const v=pickVoice(lang);if(v)u.voice=v;
    speechSynthesis.speak(u);return true;
  }catch(e){return false;}
}
function cancelSpeak(){if(canSpeak()){try{speechSynthesis.cancel();}catch(e){}}}
function isSpeaking(){try{return canSpeak()&&speechSynthesis.speaking;}catch(e){return false;}}

const API={supported,canSpeak,parse,attach,speak,cancelSpeak,isSpeaking,stopListening};
if(hasWin)root.QBVoice=API;
if(typeof module!=='undefined'&&module.exports)module.exports=API;
})(typeof window!=='undefined'?window:globalThis);

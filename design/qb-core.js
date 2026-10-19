/* QB 공용 코어 — 저장 키, mock 로그인, 테마, 과목 목록. 비밀번호는 저장하지 않는다. */
(function(){
'use strict';
var KEY_USER='qb:user', KEY_UI='qb:ui:v1', KEY_THEME='qb:theme';
function get(k){try{return localStorage.getItem(k);}catch(e){return null;}}
function set(k,v){try{localStorage.setItem(k,v);return true;}catch(e){return false;}}
function del(k){try{localStorage.removeItem(k);}catch(e){}}
function json(k,d){try{var r=get(k);return r?JSON.parse(r):d;}catch(e){return d;}}
var QB=window.QB={};
QB.SUBJECTS=[
  {id:'it',label:'IT'},{id:'korean',label:'국어'},{id:'english',label:'영어'},
  {id:'science',label:'과학'},{id:'music',label:'음악'},{id:'art',label:'미술'}
];
QB.user=function(){var u=json(KEY_USER,null);return u&&u.v===1&&u.name?u:null;};
QB.login=function(o){
  o=o||{};var prev=json(KEY_USER,null),now=new Date().toISOString();
  var u={v:1,name:String(o.name||'').trim().slice(0,20),email:String(o.email||'').trim(),
    provider:o.provider||'email',createdAt:(prev&&prev.createdAt)||now,lastLoginAt:now};
  set(KEY_USER,JSON.stringify(u));return u;
};
QB.logout=function(){del(KEY_USER);};
QB.rename=function(n){
  var u=QB.user();n=String(n||'').trim().slice(0,20);if(!u||!n)return null;
  u.name=n;set(KEY_USER,JSON.stringify(u));return u;
};
QB.safeNext=function(n){
  n=String(n||'');return /^dashboard\.html(#[A-Za-z0-9\/=&_-]*)?$/.test(n)?n:'dashboard.html';
};
QB.requireUser=function(next){
  var u=QB.user();if(u)return u;
  next=QB.safeNext(next==null?'dashboard.html'+location.hash:next);
  location.replace('login.html?next='+encodeURIComponent(next));return null;
};
QB.theme={
  get:function(){return get(KEY_THEME);},
  apply:function(){var t=get(KEY_THEME),r=document.documentElement;if(t)r.dataset.theme=t;else delete r.dataset.theme;},
  toggle:function(){
    var t=get(KEY_THEME),dark=t?t==='dark':matchMedia('(prefers-color-scheme: dark)').matches;
    set(KEY_THEME,dark?'light':'dark');QB.theme.apply();
  }
};
QB.ui={
  get:function(){var d=json(KEY_UI,null);return d&&typeof d==='object'?d:{sidebar:true,subject:'it'};},
  set:function(p){var d=Object.assign(QB.ui.get(),p||{});set(KEY_UI,JSON.stringify(d));return d;}
};
QB.theme.apply();
})();

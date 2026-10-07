(function(){
  var mq=window.matchMedia('(max-width:640px)');
  var haptic=function(ms){try{if(navigator.vibrate)navigator.vibrate(ms||8)}catch(e){}};

  /* ripple on buttons + tabs */
  document.addEventListener('pointerdown',function(e){
    var el=e.target.closest('.btn,.tabbar a');if(!el)return;
    var r=el.getBoundingClientRect(),s=Math.max(r.width,r.height)*1.6,sp=document.createElement('span');
    sp.className='ripple';sp.style.cssText='width:'+s+'px;height:'+s+'px;left:'+(e.clientX-r.left-s/2)+'px;top:'+(e.clientY-r.top-s/2)+'px';
    el.appendChild(sp);setTimeout(function(){sp.remove()},650);
  });

  /* bottom tab bar */
  var page=location.pathname.split('/').pop()||'index.html';
  var active=/^services/.test(page)?'services.html':/^blog/.test(page)?'blog.html':page;
  var I={
    home:'<path d="M3 11l9-8 9 8M5 10v10h5v-6h4v6h5V10"/>',
    about:'<circle cx="12" cy="8" r="4"/><path d="M4 21c0-4 4-6 8-6s8 2 8 6"/>',
    services:'<rect x="3" y="3" width="7" height="7" rx="2"/><rect x="14" y="3" width="7" height="7" rx="2"/><rect x="3" y="14" width="7" height="7" rx="2"/><rect x="14" y="14" width="7" height="7" rx="2"/>',
    blog:'<path d="M6 3h9l4 4v14H6z"/><path d="M9 12h7M9 16h7"/>',
    contact:'<path d="M4 5h16v11H9l-5 4z"/>'
  };
  var tabs=[['index.html','Home','home'],['about.html','About','about'],['services.html','Services','services'],['blog.html','Blog','blog'],['contact.html','Contact','contact']];
  var bar=document.createElement('nav');bar.className='tabbar';bar.setAttribute('aria-label','Quick navigation');
  var idx=-1,h='<span class="ind"></span>';
  tabs.forEach(function(t,i){
    if(t[0]===active)idx=i;
    h+='<a href="'+t[0]+'"'+(t[0]===active?' class="on"':'')+'><svg viewBox="0 0 24 24">'+I[t[2]]+'</svg>'+t[1]+'</a>';
  });
  bar.innerHTML=h;document.body.appendChild(bar);
  var ind=bar.querySelector('.ind');
  function place(i){if(i<0){ind.style.opacity=0;return}ind.style.opacity=1;ind.style.transform='translateX('+(i*100)+'%)'}
  place(-1);requestAnimationFrame(function(){requestAnimationFrame(function(){place(idx)})});
  bar.addEventListener('click',function(e){
    var a=e.target.closest('a');if(!a)return;haptic(10);
    var i=Array.prototype.indexOf.call(bar.querySelectorAll('a'),a);place(i);
  });

  /* hide bar when scrolling down, show when scrolling up */
  var last=window.scrollY;
  window.addEventListener('scroll',function(){
    var y=window.scrollY;
    if(Math.abs(y-last)<8)return;
    bar.classList.toggle('hide',y>last&&y>200);last=y;
  },{passive:true});

  /* swipe carousels (phones only) */
  function buildCarousels(){
    document.querySelectorAll('.grid').forEach(function(g){
      if(g.dataset.snap)return;
      var kids=g.children;if(kids.length<3)return;
      var k=kids[0].className;
      if(!/(^|\s)(svc|work|quote|post|step)(\s|$)/.test(k))return;
      if(/step/.test(k)&&g.closest('.detail'))return;
      g.dataset.snap='1';g.classList.add('snap');
      var dots=document.createElement('div');dots.className='dots';
      for(var i=0;i<kids.length;i++)dots.appendChild(document.createElement('i'));
      g.insertAdjacentElement('afterend',dots);
      var di=dots.children;di[0].className='on';
      g.addEventListener('scroll',function(){
        var c=g.scrollLeft+g.clientWidth/2,best=0,bd=1e9;
        Array.prototype.forEach.call(g.children,function(el,n){
          var d=Math.abs(el.offsetLeft+el.offsetWidth/2-c);if(d<bd){bd=d;best=n}
        });
        Array.prototype.forEach.call(di,function(x,n){x.className=n===best?'on':''});
      },{passive:true});
      var hint=document.createElement('div');hint.className='swipe-hint';hint.innerHTML='Swipe <span>→</span>';
      dots.insertAdjacentElement('afterend',hint);
      g.addEventListener('scroll',function(){hint.style.display='none'},{once:true,passive:true});
    });
  }
  function toggleCarousels(){
    document.querySelectorAll('.dots,.swipe-hint').forEach(function(d){d.style.display=mq.matches?'':'none'});
  }
  buildCarousels();toggleCarousels();
  (mq.addEventListener?mq.addEventListener('change',toggleCarousels):mq.addListener(toggleCarousels));

  /* collapsible footer columns */
  var cols=document.querySelectorAll('.fgrid>div:not(:first-child)');
  cols.forEach(function(c){
    c.classList.add('col');
    c.querySelector('h4').addEventListener('click',function(){
      if(!mq.matches)return;haptic(6);c.classList.toggle('open');
    });
  });
})();

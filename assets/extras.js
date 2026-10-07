(function(){
  var bar=document.querySelector('.progress'),topBtn=document.querySelector('.top');
  window.addEventListener('scroll',function(){
    var h=document.documentElement,p=h.scrollTop/(h.scrollHeight-h.clientHeight);
    if(bar)bar.style.width=(p*100)+'%';
    if(topBtn)topBtn.classList.toggle('show',h.scrollTop>600);
  },{passive:true});
  if(topBtn)topBtn.addEventListener('click',function(){window.scrollTo({top:0,behavior:'smooth'})});

  document.querySelectorAll('.grid').forEach(function(g){
    Array.prototype.forEach.call(g.children,function(c,i){c.style.transitionDelay=(i*0.12)+'s'});
  });

  var t=document.querySelector('.typed');
  if(t){
    var words=JSON.parse(t.dataset.words),w=0,c=0,del=false;
    (function tick(){
      var word=words[w];
      t.textContent=word.slice(0,c);
      if(!del&&c===word.length){del=true;return setTimeout(tick,1600)}
      if(del&&c===0){del=false;w=(w+1)%words.length}
      c+=del?-1:1;setTimeout(tick,del?45:95);
    })();
  }

  var cv=document.getElementById('particles');
  if(cv&&!window.matchMedia('(prefers-reduced-motion:reduce)').matches){
    var ctx=cv.getContext('2d'),P=[],W,H,mx=-999,my=-999;
    var size=function(){W=cv.width=cv.offsetWidth;H=cv.height=cv.offsetHeight};
    size();window.addEventListener('resize',size);
    cv.parentElement.addEventListener('mousemove',function(e){var r=cv.getBoundingClientRect();mx=e.clientX-r.left;my=e.clientY-r.top});
    for(var i=0;i<60;i++)P.push({x:Math.random()*W,y:Math.random()*H,vx:(Math.random()-.5)*.5,vy:(Math.random()-.5)*.5});
    (function draw(){
      ctx.clearRect(0,0,W,H);
      P.forEach(function(a,i){
        a.x+=a.vx;a.y+=a.vy;
        if(a.x<0||a.x>W)a.vx*=-1;
        if(a.y<0||a.y>H)a.vy*=-1;
        ctx.fillStyle='rgba(180,200,255,.7)';ctx.beginPath();ctx.arc(a.x,a.y,1.8,0,6.3);ctx.fill();
        for(var j=i+1;j<P.length;j++){
          var b=P[j],d=Math.hypot(a.x-b.x,a.y-b.y);
          if(d<120){ctx.strokeStyle='rgba(120,160,255,'+(.22*(1-d/120))+')';ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(b.x,b.y);ctx.stroke()}
        }
        var dm=Math.hypot(a.x-mx,a.y-my);
        if(dm<160){ctx.strokeStyle='rgba(0,194,209,'+(.5*(1-dm/160))+')';ctx.beginPath();ctx.moveTo(a.x,a.y);ctx.lineTo(mx,my);ctx.stroke()}
      });
      requestAnimationFrame(draw);
    })();
  }
})();

(function(){
  var reduce=window.matchMedia('(prefers-reduced-motion:reduce)').matches;
  var fine=window.matchMedia('(hover:hover) and (pointer:fine)').matches;

  /* ---------- aurora wave canvas ---------- */
  var cv=document.getElementById('aurora');
  if(cv&&!reduce){
    var ctx=cv.getContext('2d'),W=0,H=0,dpr=Math.min(window.devicePixelRatio||1,2),mx=-1,my=-1,tx=-1,ty=-1,stars=[],run=true;
    var size=function(){
      W=cv.offsetWidth;H=cv.offsetHeight;cv.width=W*dpr;cv.height=H*dpr;ctx.setTransform(dpr,0,0,dpr,0,0);
      stars=[];for(var i=0;i<Math.round(W/16);i++)stars.push({x:Math.random()*W,y:Math.random()*H*.7,r:Math.random()*1.4+.3,p:Math.random()*6.3,s:Math.random()*.002+.001});
    };
    size();window.addEventListener('resize',size);
    var host=cv.parentElement;
    function pos(x,y){var r=cv.getBoundingClientRect();tx=x-r.left;ty=y-r.top}
    host.addEventListener('mousemove',function(e){pos(e.clientX,e.clientY)});
    host.addEventListener('touchmove',function(e){var t=e.touches[0];pos(t.clientX,t.clientY)},{passive:true});
    host.addEventListener('mouseleave',function(){tx=-1;ty=-1});
    new IntersectionObserver(function(es){run=es[0].isIntersecting;if(run)loop(performance.now())}).observe(host);
    var cols=[['91,75,255','0,194,209'],['0,194,209','91,75,255'],['255,107,154','91,75,255'],['0,194,209','255,107,154']];
    function loop(t){
      if(!run)return;
      ctx.clearRect(0,0,W,H);
      if(tx>=0){mx=mx<0?tx:mx+(tx-mx)*.12;my=my<0?ty:my+(ty-my)*.12}else{mx=-1}
      /* twinkling stars */
      stars.forEach(function(s){
        var a=.25+.55*Math.abs(Math.sin(t*s.s+s.p));
        ctx.fillStyle='rgba(200,220,255,'+a+')';ctx.beginPath();ctx.arc(s.x,s.y,s.r,0,6.3);ctx.fill();
      });
      /* flowing ribbons */
      for(var k=0;k<4;k++){
        var base=H*(.64+k*.075),amp=30+k*8,sp=.00035+k*.00016;
        var g=ctx.createLinearGradient(0,0,W,0);
        g.addColorStop(0,'rgba('+cols[k][0]+',.0)');g.addColorStop(.35,'rgba('+cols[k][0]+',.26)');
        g.addColorStop(.7,'rgba('+cols[k][1]+',.26)');g.addColorStop(1,'rgba('+cols[k][1]+',0)');
        ctx.beginPath();ctx.moveTo(0,H);
        var line=[];
        for(var x=0;x<=W+12;x+=12){
          var y=base+Math.sin(x*.006+t*sp+k*1.7)*amp+Math.sin(x*.014-t*sp*1.6+k)*amp*.45;
          if(mx>=0){var d=Math.hypot(x-mx,y-my);if(d<220){y-=Math.cos(d/220*1.57)*Math.cos(d/220*1.57)*46}}
          line.push([x,y]);ctx.lineTo(x,y);
        }
        ctx.lineTo(W+12,H);ctx.closePath();ctx.fillStyle=g;ctx.fill();
        ctx.beginPath();line.forEach(function(p,i){i?ctx.lineTo(p[0],p[1]):ctx.moveTo(p[0],p[1])});
        ctx.strokeStyle='rgba('+cols[k][1]+',.55)';ctx.lineWidth=1.4;ctx.stroke();
      }
      /* cursor spotlight */
      if(mx>=0){
        var rg=ctx.createRadialGradient(mx,my,0,mx,my,260);
        rg.addColorStop(0,'rgba(0,194,209,.22)');rg.addColorStop(.5,'rgba(91,75,255,.1)');rg.addColorStop(1,'rgba(91,75,255,0)');
        ctx.fillStyle=rg;ctx.fillRect(0,0,W,H);
      }
      requestAnimationFrame(loop);
    }
    loop(performance.now());
  }

  /* ---------- word-by-word headings ---------- */
  if(!reduce){
    document.querySelectorAll('.sec-head h2,.page-hero h1,.split h2,.intro-grid h2,.stext h2,.cta h2').forEach(function(h){
      if(h.children.length||!h.textContent.trim())return;
      var words=h.textContent.trim().split(/\s+/);
      h.textContent='';h.classList.add('wsplit');
      words.forEach(function(w,i){
        var o=document.createElement('span');o.className='w';
        var s=document.createElement('span');s.textContent=w;s.style.setProperty('--i',i);
        o.appendChild(s);h.appendChild(o);if(i<words.length-1)h.appendChild(document.createTextNode(' '));
      });
    });
  }

  if(!fine)return;

  /* ---------- glow cursor ---------- */
  var dot=document.createElement('div'),ring=document.createElement('div');
  dot.className='cur-dot';ring.className='cur-ring';document.body.appendChild(dot);document.body.appendChild(ring);
  var cx=0,cy=0,rx=0,ry=0;
  document.addEventListener('mousemove',function(e){
    cx=e.clientX;cy=e.clientY;document.documentElement.classList.add('cur-on');
    dot.style.transform='translate('+cx+'px,'+cy+'px)';
  });
  document.addEventListener('mouseleave',function(){document.documentElement.classList.remove('cur-on')});
  document.addEventListener('mousedown',function(){ring.classList.add('press')});
  document.addEventListener('mouseup',function(){ring.classList.remove('press')});
  document.addEventListener('mouseover',function(e){
    ring.classList.toggle('big',!!e.target.closest('a,button,.btn,summary,.svc,.work,.post'));
  });
  (function follow(){rx+=(cx-rx)*.16;ry+=(cy-ry)*.16;ring.style.transform='translate('+rx+'px,'+ry+'px)';requestAnimationFrame(follow)})();

  /* ---------- magnetic buttons ---------- */
  document.querySelectorAll('.btn').forEach(function(b){
    b.classList.add('mag');
    b.addEventListener('mousemove',function(e){
      var r=b.getBoundingClientRect(),x=e.clientX-r.left-r.width/2,y=e.clientY-r.top-r.height/2;
      b.style.transform='translate('+(x*.22)+'px,'+(y*.3)+'px)';
    });
    b.addEventListener('mouseleave',function(){b.style.transform=''});
  });

  /* ---------- card spotlight ---------- */
  document.querySelectorAll('.svc,.step,.quote,.ind,.wc').forEach(function(c){
    c.classList.add('spot');
    c.addEventListener('mousemove',function(e){
      var r=c.getBoundingClientRect();
      c.style.setProperty('--mx',(e.clientX-r.left)+'px');c.style.setProperty('--my',(e.clientY-r.top)+'px');
    });
  });
})();

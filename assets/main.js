(function(){
  var nav=document.querySelector('header.nav');
  var onScroll=function(){nav.classList.toggle('scrolled',window.scrollY>40)};
  onScroll();window.addEventListener('scroll',onScroll,{passive:true});

  var burger=document.querySelector('.burger'),menu=document.querySelector('.menu');
  burger.addEventListener('click',function(){menu.classList.toggle('open')});
  menu.addEventListener('click',function(e){if(e.target.tagName==='A')menu.classList.remove('open')});

  var io=new IntersectionObserver(function(es){es.forEach(function(e){
    if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.12});
  document.querySelectorAll('.rv').forEach(function(el){io.observe(el)});

  var co=new IntersectionObserver(function(es){es.forEach(function(e){
    if(!e.isIntersecting)return;co.unobserve(e.target);
    var el=e.target,end=+el.dataset.count,suf=el.dataset.suffix||'',t0=null;
    (function step(t){t0=t0||t;var p=Math.min((t-t0)/1500,1);
      el.textContent=Math.floor(end*(1-Math.pow(1-p,3)))+suf;
      if(p<1)requestAnimationFrame(step)})(performance.now());
  })},{threshold:.5});
  document.querySelectorAll('[data-count]').forEach(function(el){co.observe(el)});

  var form=document.getElementById('contactForm');
  if(form){form.addEventListener('submit',function(e){
    e.preventDefault();
    document.getElementById('formOk').style.display='block';
    form.reset();
  })}
})();

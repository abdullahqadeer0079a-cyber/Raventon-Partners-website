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
})();

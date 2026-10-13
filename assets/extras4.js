(function(){
  var stage=document.getElementById('stage');
  if(!stage||window.matchMedia('(prefers-reduced-motion:reduce)').matches)return;
  var layers=stage.querySelectorAll('.layer'),host=stage.closest('.hero');
  host.addEventListener('mousemove',function(e){
    var r=host.getBoundingClientRect(),x=(e.clientX-r.left)/r.width-.5,y=(e.clientY-r.top)/r.height-.5;
    stage.style.transform='rotateY('+(x*3.5)+'deg) rotateX('+(-y*2.5)+'deg)';
    layers.forEach(function(l){var d=+l.dataset.depth;l.style.transform='translate('+(x*d*-0.6)+'px,'+(y*d*-0.6)+'px)'});
  });
  host.addEventListener('mouseleave',function(){
    stage.style.transform='';layers.forEach(function(l){l.style.transform=''});
  });
  stage.style.transition='transform .3s ease-out';stage.style.transformStyle='preserve-3d';
})();

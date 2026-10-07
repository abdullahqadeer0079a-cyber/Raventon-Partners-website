(function(){
  var burger=document.querySelector('.burger'),menu=document.querySelector('.menu');
  if(!burger||!menu)return;
  var scrim=document.createElement('div');scrim.className='scrim';document.body.appendChild(scrim);
  function set(open){
    menu.classList.toggle('open',open);burger.classList.toggle('on',open);
    scrim.classList.toggle('on',open);document.body.classList.toggle('menu-open',open);
    burger.setAttribute('aria-expanded',open);
  }
  /* replace main.js toggle behaviour with one that also manages scrim/scroll lock */
  var fresh=burger.cloneNode(true);burger.parentNode.replaceChild(fresh,burger);burger=fresh;
  burger.addEventListener('click',function(){set(!menu.classList.contains('open'))});
  scrim.addEventListener('click',function(){set(false)});
  menu.addEventListener('click',function(e){if(e.target.tagName==='A')set(false)});
  document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false)});
  window.addEventListener('resize',function(){if(window.innerWidth>980)set(false)});
})();

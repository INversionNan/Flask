const galleryLightbox = GLightbox({
    selector: '.gallery-lightbox'
});

window.addEventListener('load', () => {
    AOS.init({
      duration: 1000,
      easing: 'ease-in-out',
      once: true,
      mirror: false
    })
  });
  var yj=document.getElementsByClassName('text');
  for(var i=0;i<yj.length;i++){
      yj[i].onmouseover=function(){
      //console.log(i)
      this.style.backgroundColor="rgb(236, 56, 140)"	
  }
  yj[i].onmouseout=function(){
      this.style.backgroundColor="rgb(164, 141, 245)";
  }
}
new Swiper('.testimonialss-slider', {
    speed: 600,
    loop: true,
    autoplay: {
      delay: 5000,
      disableOnInteraction: false
    },
    slidesPerView: 'auto',
    pagination: {
      el: '.swiper-pagination',
      type: 'bullets',
      clickable: true
    },
    breakpoints: {
      320: {
        slidesPerView: 1,
        spaceBetween: 20
      },

      1200: {
        slidesPerView: 3,
        spaceBetween: 20
      }
    }
  });
  window.onload = function(){ 
    var audio1 = document.getElementById('music1');
    var audio2 = document.getElementById('music2');
    var audio3 = document.getElementById('music3');
    var audio4 = document.getElementById('music4');
    var audio5 = document.getElementById('music5');
        audio1.pause();
        audio2.pause();
        audio3.pause();
        audio4.pause();
        audio5.pause();
    }
  function play1() {
    var audio1 = document.getElementById('music1');
    if (audio1.paused) {
        audio1.play();
    }else{
        audio1.pause();
        audio1.currentTime = 0;//音乐从头播放
    }
}
function play2() {
    var audio2 = document.getElementById('music2');
    if (audio2.paused) {
        audio2.play();
    }else{
        audio2.pause();
        audio2.currentTime = 0;//音乐从头播放
    }
}
function play3() {
    var audio3 = document.getElementById('music3');
    if (audio3.paused) {
        audio3.play();
    }else{
        audio3.pause();
        audio3.currentTime = 0;//音乐从头播放
    }
}
function play4() {
    var audio4 = document.getElementById('music4');
    if (audio4.paused) {
        audio4.play();
    }else{
        audio4.pause();
        audio4.currentTime = 0;//音乐从头播放
    }
}
function play5() {
    var audio5 = document.getElementById('music5');
    if (audio5.paused) {
        audio5.play();
    }else{
        audio5.pause();
        audio5.currentTime = 0;//音乐从头播放
    }
}


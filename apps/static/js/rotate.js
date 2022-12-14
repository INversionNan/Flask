var x = 360 / 7;

document.querySelectorAll('#img_3').forEach(function(el, index){
    el.style.transform = "rotateX(0deg) rotateY("+ x * index +"deg) translateZ(350px)"
})
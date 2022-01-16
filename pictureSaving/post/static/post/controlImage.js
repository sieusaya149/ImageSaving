function plusSlides(n,postId) {
    showSlides(slideIndex += n,postId);
}

function currentSlide(n,postId) {
    showSlides(slideIndex = n,postId);
}

function showSlides(n,postId) {
    console.log("running"+ postId.toString())
    var i;
    var classSlide = "mySlides" + postId.toString();
    var classDot="dot" + postId.toString();
    var slides = document.getElementsByClassName(classSlide);
    if(slides.length > 1){
    var dots = document.getElementsByClassName(classDot);
    }
    if (n > slides.length) {slideIndex = 1}    
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";  
    }
    if(slides.length > 1){
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    }
    slides[slideIndex-1].style.display = "block";  
    if(slides.length > 1){
        dots[slideIndex-1].className += " active";
    }
}
 // For post reviewing
 class DialogeSlide{

 }


 DialogeSlide.prototype.plusSlides = function (n){
    this.showSlides(slideIndex += n);
 }
 DialogeSlide.prototype.currentSlide = function (n){
    this.showSlides(slideIndex = n);
 }
 DialogeSlide.prototype.showSlides = function (n){
     console.log('dialog handle')
    var i;
    var slides = document.getElementsByClassName("mySlides-dialog");
    var dots = document.getElementsByClassName("dot-dialog");
    if (n > slides.length) {slideIndex = 1}
    if (n < 1) {slideIndex = slides.length}
    for (i = 0; i < slides.length; i++) {
        slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
        dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slideIndex-1].style.display = "block";
    dots[slideIndex-1].className += " active";
 }

 var handleImageDialog = new DialogeSlide();



   

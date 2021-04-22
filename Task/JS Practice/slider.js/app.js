/* function myFunction() {
    var list = document.getElementById("myList");
    list.removeChild(list.childNodes[2]);
}
 */



/* function myFunction() {
    var textnode = document.createTextNode("Water");
    var item = document.getElementById("myList");
    item.replaceChild(textnode, item.childNodes[0]);
} */




//////////////////////// slider ///////////////////

let leftArrow = document.querySelector("#left-arrow")
let rightArrow = document.querySelector("#right-arrow")
let imageSlide = document.querySelector(".image-slides")
let imagesDiv = document.querySelector(".imagesDiv")
let slider = document.querySelector(".slider")
let slideTXt = document.querySelectorAll(".slide-text")
let width = imagesDiv.offsetWidth;

let slideNum = document.querySelectorAll(".slide").length

i = 0;
let a

rightArrow.addEventListener('click', function() {
    if (i != -((slideNum - 1) * width)) {
        i -= width;
        imageSlide.style.transform = `translateX(${i}px)`

        /*   for (a = 0; a < slideTXt.length; a++) {

              slideTXt[a].classList.toggle("active")
          } */
    }
    /* else {
           rightArrow.classList.add("disable")
       }
    */


})


leftArrow.addEventListener('click', function() {
    if (i != 0) {
        i += width;
        imageSlide.style.transform = `translateX(${i}px)`

    }
    /* else {
           leftArrow.classList.add("disable")
       }
    */




})
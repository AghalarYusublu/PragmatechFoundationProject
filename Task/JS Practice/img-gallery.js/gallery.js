let imageItem = document.querySelector(".image-item")
let img = document.querySelector(".image-item img")
let overlay = document.querySelector(".overlay")
let closeBtn = document.querySelector(".close")
let gallery = document.querySelector(".gallery")
imageItem.addEventListener('click', function() {
    img.style.transform = `scale(1.5) rotate(360deg)`;
    overlay.style.opacity = `1`
    closeBtn.style.opacity = `1`
})

closeBtn.addEventListener('click', function(elem) {
    gallery.remove();
})
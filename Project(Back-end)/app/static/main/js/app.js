/////////////Navbar-fixed////////
let mainMenu = document.querySelector("#main-menu")
let navbarMenu = document.querySelector(".navbar-menu")
let preloader = document.querySelector(".preloader")
let index = 0
document.addEventListener('scroll', function() {
        if ((window.scrollY > 10)) {
            mainMenu.classList.add("active")
            navbarMenu.classList.add("active")
        } else {
            mainMenu.classList.remove("active")
            navbarMenu.classList.remove("active")
        }
    })
    ///////////Scroll-top///////////////
let scrollTop = document.querySelector(".scroll-top")

document.addEventListener("scroll", function() {
    if (window.scrollY > 550) {
        scrollTop.classList.add("active")
    } else {
        scrollTop.classList.remove("active")
    }
})






////////////////////////////////////

let programs = document.querySelector("#programs")
let about = document.querySelector("#about")
let clients = document.querySelector("#clients")
let btnAbout = document.querySelector("#about")

function scrollPrograms() {
    document.documentElement.scrollTo(0, 0)

}

function scrollAbout() {
    document.documentElement.scrollTo(0, 847)
}

function scrollClients() {
    document.documentElement.scrollTo(0, 3879)
}

window.addEventListener('load', function() {
    document.documentElement.scrollTo(0, 0)
    setTimeout(() => {
        preloader.classList.remove("loaded")
        loaded()

    }, 2000);
})

function loaded() {
    preloader.classList.add("loaded")
}

let orderDiv = document.querySelector(".navbar-orderDiv")
let btnOrderDiv = document.querySelector(".btn-navbar-aside-open-toggle")


btnOrderDiv.addEventListener('click', function() {
    orderDiv.classList.toggle("active")
    btnOrderDiv.classList.toggle("active")
})



///////Testemonials-Slider///////
let pagDots = document.querySelector(".pagination-dots")
let pagDot = document.querySelector(".page-dot")
let owlDots = document.querySelector(".owl-dot")

let testemonialsSlides = document.querySelector(".testemonials-slides")
let testemonialsOwl = document.querySelector(".testemonials-owl")
let width = testemonialsOwl.offsetWidth;

let slideNum = document.querySelectorAll(".slide").length

/* i = 0; */

/* for (let a = 0; a < owlDots.length; a++) {
    owlDots[a].addEventListener('click', function() {
        if (i != -((slideNum - 1) * width)) {
            i -= width;
            testemonialsSlides.style.transform = `translateX(${i}px)`

        } else {
            i += width;
            testemonialsSlides.style.transform = `translateX(${i}px)`
            console.log(i)
        }


    })
} */

/* function pageSlide(element) {
    index = element.id;
    changeSlide();

} */


/* function updateCircleIndecator() {
    for (let b; b < pagDots.children.length; b++) {
        pagDots.children[i].firstElementChild.classList.remove("active")
    }
    pagDots.children[index].firstElementChild.classList.add("active")
}
updateCircleIndecator() */


/*  if (i != 0) {
     i += width;
     testemonialsSlides.style.transform = `translateX(${i}px)`

 } */






/////////////SLIDER-BANNER///////////////
let bannerSlider = document.querySelector(".banner-slider").children
let bannerSlide = document.querySelector(".banner-slide")
let decorativeCircle = document.querySelector(".decorative-circle")
let btnSlide = document.querySelector(".btn-slide")
let pageNum = document.querySelector(".pagination").children
let carouselInner = document.querySelector(".carousel-inner").children


/* btnSlide.addEventListener("click", function() { */
/*   circle.style.width = "3038px"
  circle.style.height = "3038px"
  circle.style.left = "759.5px"
  circle.style.top = "425px"
  circle.style.zIndex = "99999" */
/*   if (index == bannerSlider.length - 1) {
      index = 0
  } else {
      index++
  }
  console.log(index)
  changeSlide(); */
/* }) */

/* left: 759.5px;
    top: 425px;
    width: 3038px;
    height: 3038px;
 */

bannerSlider[0].classList.add("active")
carouselInner[0].classList.add("active")
setInterval(function() {
    if (index == bannerSlider.length - 2) {
        index = 0
    } else {
        index++
    }
    changeSlide();
}, 4000)

function changeSlide() {
    for (let s = 0; s < bannerSlider.length; s++) {
        bannerSlider[s].classList.remove("active")
            /*  decorativeCircle.classList.remove("active") */
    }
    for (let p = 0; p < pageNum.length; p++) {
        pageNum[p].classList.remove("active")
    }
    bannerSlider[index].classList.add("active")
    pageNum[index].classList.add("active")
        /*   decorativeCircle.classList.add("active")

          circle.style.width = "3038px"
          circle.style.height = "3038px"
          circle.style.left = "759.5px"
          circle.style.top = "425px"
          circle.style.zIndex = "99999" */
}


//////////BTN ORDER NOW////////
let btnOrder = document.querySelectorAll(".btn-order")

for (let b = 0; b < btnOrder.length; b++) {
    btnOrder[b].addEventListener("click", function(e) {
        e.preventDefault()
        orderDiv.classList.toggle("active")
        btnOrderDiv.classList.toggle("active")
    })
}
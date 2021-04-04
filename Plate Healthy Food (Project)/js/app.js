let mainMenu = document.querySelector("#main-menu")
let navbarMenu = document.querySelector(".navbar-menu")


document.addEventListener('scroll', function() {
    if ((window.scrollY > 10)) {
        mainMenu.classList.add("active")
        navbarMenu.classList.add("active")
    } else {
        mainMenu.classList.remove("active")
        navbarMenu.classList.remove("active")
    }
})

let programs = document.querySelector("#programs")
let about = document.querySelector("#about")
let clients = document.querySelector("#clients")

function scrollPrograms() {
    window.scrollTo(0, 0)
}

function scrollAbout() {
    window.scrollTo(0, 847)
    console.log(window.scrollTo(0, 847))
}

function scrollClients() {
    window.scrollTo(0, 3879)
}
window.addEventListener('load', function() {
    window.scrollTo(0, 0)
})

let orderDiv = document.querySelector(".navbar-orderDiv")
let btnOrderDiv = document.querySelector(".btn-navbar-aside-open-toggle")


btnOrderDiv.addEventListener('click', function() {
    orderDiv.classList.toggle("active")
    btnOrderDiv.classList.toggle("active")
})
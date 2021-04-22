function closeOverlay(elem) {
    document.body.removeChild(elem.parentElement)
}

function showBigImage(elem) {
    // console.log(elem.getAttribute('src'))
    let overlayContent = `
    <div class="overlay">
        <div class="close" onclick="closeOverlay(this)">
            <i class="bi bi-x-square"></i>
        </div>
        <img src="${elem.getAttribute('src')}" alt="">
    </div>
    `
    document.body.innerHTML += overlayContent
}
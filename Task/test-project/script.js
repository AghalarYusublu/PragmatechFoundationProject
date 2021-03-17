/* let a = Number(prompt("1-ci ededi daxil edin"));
let b = Number(prompt("2-ci ededi daxil edin"));

let c = a + b

function topla() {

    document.write(a + " + " + b + " = " + c)
}

topla(); */



/////////////////////////////////////////////////


/* let ededler = [23, 34, 45, 2, 19, 44, 56, 67]

function goster() {

    console.log(ededler[2] + ededler[5])
}
goster() */


////////////////////////////

/* let user1 = {
    ad: "Aghalar",
    soyad: "Yusublu",
    yas: 20,
}

let user2 = {
    ad: "Isgender",
    soyad: "Hasilov",
    yas: 22,
} */

function users(_ad, _soyad, _yas) {
    return {
        ad: _ad,
        soyad: _soyad,
        yas: _yas
    }

}

user1 = users('Aghalar', 'Yusublu', 20)
user2 = users('Isgender', 'Hasilov', 22)


console.log(user1.ad + " " + user1.soyad + " " + user1.yas)
console.log(user2.ad + " " + user2.soyad + " " + user2.yas)
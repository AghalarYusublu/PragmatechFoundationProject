let p = document.querySelector("p")



let Name = ['Subhan Ahmedov', 'Xanlarova Fidan', 'Isgandar Hasilov', 'Ulker Memmedli', 'Mirzeyev Mehman', 'Ismayilzade Senan', 'Orucov Murad', 'Aida Shiraliyeva', 'Ağalar Yusublu']


function RandomName() {
    p.innerHTML = Name[Math.floor(Math.random() * Name.length)]

}
RandomName()
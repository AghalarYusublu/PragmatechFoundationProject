import data

def saveData(name, surname, age):
    user={
        'ad':name,
        'soyad':surname,
        'yas':age
    }     
    data.users.append(user)
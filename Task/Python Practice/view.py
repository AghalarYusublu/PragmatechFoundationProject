import data
import controller



ad = input("Ad daxil edin : ")
soyad = input("Soyad daxil edin : ")
yas = input("Yaş daxil edin : ")

controller.saveData(ad, soyad, yas)

emr= input('Istofadeci melumatlarini gormek isteyirsiniz mi? Yes/No :')

if emr == 'Yes':
    for user in data.users:
        print(user['ad'] + ' | '+user['soyad'] + ' | ' + user['yas'])

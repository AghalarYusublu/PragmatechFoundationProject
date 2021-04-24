import data
import controller

print("--Salam mini HR proqramına xoş gəlmisiniz--")


def Secimler():
    print(" ---> Zəhmət olmasa sizə uyğun seçimi edin <--- ")
    print("1- Yeni işçi əlavə et")
    print("2- İstifadəçi məlumatlarına bax")
    print("3- Ümumi maaş cəmini göstər")
    print("4- İşçi sayını göstər")
    print("5- Ən köhnə işçini göstər")
    print("6- Ən yeni işçini göstər")
    print("7- Əsas menyuya qayıt")


while True:
    Secimler()
    secim = input("Seçiminizi daxil edin: ")
    if secim == '1':
        ad = input("İşçinin adını daxil edin : ")
        soyad = input("İşçinin soyadını daxil edin : ")
        maas = int(input("İşçinin maaşını daxil edin : "))
        controller.DataSave(ad, soyad, maas)
        for worker in data.Workers:
            print("İşçinin Adı: " + worker['ad'] + " | " + "İşçinin Soyadı: " +
                  worker['soyad'] + " | " + "İşçinin maaşı: " + str(worker['maas']) + " Azn")
            print("İşçi əlavə olundu")
    elif secim == '2':
        for worker in data.Workers:
            print("İşçinin Adı: " + worker['ad'] + " | " + "İşçinin Soyadı: " +
                  worker['soyad'] + " | " + "İşçinin maaşı: " + str(worker['maas']) + " Azn")
    elif secim == '3':
        salary_sum = 0
        for salary in data.Workers:
            salary_sum += salary['maas']            
            print("Ümumi maaş: " + str(salary_sum))
    elif secim == '4':
        print("İşçi sayı: " + len(data.Workers))
    elif secim == '5':
        old_worker = list(data.Workers)[0]
        print("Ən köhnə işçi:  " + old_worker['ad'] + " " + old_worker['soyad'])
    elif secim == '6':
        latter_worker = list(data.Workers)[-1]
        print("Ən yeni işçi:  " + latter_worker['ad'] + " " + latter_worker['soyad'])
    elif secim == '7':
         Secimler()
    
    else:
        print("Daxil etdiyiniz sorğuya uyğun nəticə tapılmadı, zəhmət olmasa seçimlər siyahısından düzgün seçim edin! ")


            

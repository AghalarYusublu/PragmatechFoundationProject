bucaq1 = int(input("1ci bucagi daxil edin: "))
bucaq2 = int(input("2ci bucagi daxil edin: "))
bucaq3=0
UmumiBucaq = 180

if bucaq1+bucaq2+bucaq3 < bucaq1 and bucaq2:
    print("Yeniden deger daxil edin!")

else:
    bucaq3 = UmumiBucaq-(bucaq1+bucaq2)
    print("3cu bucaq: {}".format(bucaq3))

cumle = "Apple növbəti təqdimat tədbirinin keçirilmə tarixini elan edib"
saitler = ["a", "e", "ə", "i", "ı", "o", "ö", "u", "ü"]

count=0
for herf in cumle:
    for sait in saitler:
        if herf == sait:
            count+=1
print(count)

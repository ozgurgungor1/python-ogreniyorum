mesaj = 'Merhaba benim  adim . Özgür Güngör'


# mesaj = mesaj.upper()       # tüm harfleri büyük harf yapar

# mesaj = mesaj.lower()       # küçük harf yapar

# mesaj = mesaj.title()       # bütün kelimelerin baş harfini büyük yapar

# mesaj = mesaj.capitalize()  # sadece baş harfi büyük yapar 

# mesaj = mesaj.strip()       # başta boşluk varsa siler

# mesaj = mesaj.split()       # cümleyi dizilere ayirir

# mesaj = mesaj.split('.')


# mesaj= '---'.join(mesaj)


# print(mesaj)


# index = mesaj.find('Özgür')      # aramada kaçıncı satırda olduğunu söyler

# isFound = mesaj.startswith('M')  # M ile başlayıp başlamadığını kontrol eder

# isFound = mesaj.endswith('r')      # r ile mi bitiyor kontrol ediyor

# mesaj = mesaj.replace('Özgür','Mahmut')   #  değistirme islemi

# mesaj = mesaj.replace(' ','*')           # bosluk yerine * gelmesini sağladı


mesaj = mesaj.center(50,'*')  # 50 karaktere tamamlamak için başına ve sonuna yıldız ekledi

print(mesaj)

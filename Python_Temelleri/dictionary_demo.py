ogrenciler = {}

number = input("öğrenci no: ")
name = input("öğrenci adi: ")
surname = input("Öğrenci soyadi: ")
phone = input("öğrencinin telefonu: ")

# ogrenciler[number] = {
#     'ad': name,
#     'soyad': surname,
#     'telefon': phone 
# }




ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})




number = input("öğrenci no: ")
name = input("öğrenci adi: ")
surname = input("Öğrenci soyadi: ")
phone = input("öğrencinin telefonu: ")


ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})





number = input("öğrenci no: ")
name = input("öğrenci adi: ")
surname = input("Öğrenci soyadi: ")
phone = input("öğrencinin telefonu: ")


ogrenciler.update({
    number: {
        'ad': name,
        'soyad': surname,
        'telefon': phone
    }
})




print(ogrenciler)



print('*'*50)


ogrNo = input('ögrenci no: ')
ogreci = ogrenciler[ogrNo]



print(f"Aradiginiz {ogrNo} nolu ögrencinin adi {ogreci['ad']} soyadı: {ogreci['soyad']} ve telefonu ise {ogreci['telefon']}")

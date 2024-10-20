# Sayi1 = int(input('1.Sayi: '))
# Sayi2 = int(input('2.Sayi: '))


# result = (Sayi1 > Sayi2)
# print(f'a: {Sayi1} b: {Sayi2} den büyüktür {result}')






# vize1 = float(input('1.Vize: '))
# vize2 = float(input('2.Vize: '))

# final = float(input('Final:  '))


# ortalama = (((vize1 + vize2) /2) * 0.6) + (final * 0.4)

# print(f'not ortalamanız : {ortalama} ve dersten geçme durumunuz: {ortalama>=50}')






# sayi = int(input('sayi: '))
# tekcift =(sayi % 2 == 0)
# print(f'girilen sayi çift olma duruumu: {tekcift}')






email = 'ozgurgungoor@gmail.com'
password = '123'

girilenEmail = input('email: ')
girilenPassword = input('parola: ')

isEmail = (email == girilenEmail.lower().strip())
isPassword = (password == girilenPassword.lower().strip())  

print(f'Email doğrumu: {isEmail} ve parola: {isPassword}')

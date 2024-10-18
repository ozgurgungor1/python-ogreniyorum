# sehirler = ['kocaeli','istambul']
# plaklar = [41, 34]

# print(plaklar[sehirler.index('istambul')])


# plakalar = { 'Kocaeli': 41, 'İstambul': 34 }

# print(plakalar['Kocaeli'])

# print(plakalar['İstambul'])


# plakalar['ankara'] = 6   # listeye veri ekleme

# plakalar['İstambul'] = 'degisiklik'


# print(plakalar)



users = {
    'ozgurgungor':{
        'age': 21,
        'roles': ['user'],
        'email': 'ozgurgugoor@icloud.com',
        'address': 'Ankara',
        'phone': '12345678911',
    },

    'cinarturan':{
        'age': 24,
        'roles': ['admin','user'],
        'email': 'cınarturan@icloud.com',
        'address': 'Kastamonu',
        'phone': '98765432114',
    },
}



print(users['cinarturan']['age'])
print(users['cinarturan']['email'])
print(users['cinarturan']['address'])
print(users['cinarturan']['phone'])


print(users['cinarturan']['roles'][0])
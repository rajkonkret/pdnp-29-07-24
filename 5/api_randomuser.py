import requests as re

url = 'https://randomuser.me/api/'

response = re.get(url)
print(response.text)
data_resp = response.json()
user = data_resp['results'][0]
print(user)
# {'gender': 'male', 'name': {'title': 'Mr', 'first': 'Sudivoy', 'last': 'Povazhniy'},
#  'location': {'street': {'number': 3599, 'name': 'Chumachenka'}, 'city': 'Saki', 'state': 'Hersonska',
#               'country': 'Ukraine', 'postcode': 23663,
#               'coordinates': {'latitude': '76.3611', 'longitude': '-123.2086'},
#               'timezone': {'offset': '-10:00', 'description': 'Hawaii'}}, 'email': 'sudivoy.povazhniy@example.com',
#  'login': {'uuid': 'da153cd2-c793-4bb1-ba8b-2f54df51b766', 'username': 'orangepeacock265', 'password': 'peterpan',
#            'salt': 'VEJmQSgn', 'md5': 'c5676ac7287317cf93b48b80f4d5e773',
#            'sha1': '742e81b9185f516335f8dc5c46ce3427c4b7005a',
#            'sha256': '6b904dbb72b63cdedaa8bc190d4d2bdd9b65085fba8c2758e357589320cb46d9'},
#  'dob': {'date': '2001-05-25T04:58:08.933Z', 'age': 23},
#  'registered': {'date': '2009-05-24T10:23:05.472Z', 'age': 15},
#  'phone': '(098) Z30-7433', 'cell': '(068) L50-8670', 'id': {'name': '', 'value': None},
#  'picture': {'large': 'https://randomuser.me/api/portraits/men/30.jpg',
#              'medium': 'https://randomuser.me/api/portraits/med/men/30.jpg',
#              'thumbnail': 'https://randomuser.me/api/portraits/thumb/men/30.jpg'}, 'nat': 'UA'}
# wyciagniemy name
print(user['name'])  # {'title': 'Miss', 'first': 'Lucile', 'last': 'Nguyen'}
print(f"Imię: {user['name']['first']}")
print(f"Nazwisko: {user['name']['last']}")
# Imię: Jantje
# Nazwisko: Zomerdijk
print(f"E-mail: {user['email']}")  # E-mail: virgil.stevens@example.com
# "picture": {"large": "https://randomuser.me/api/portraits/women/77.jpg",
#                           "medium": "https://randomuser.me/api/portraits/med/women/77.jpg",
#                           "thumbnail": "https://randomuser.me/api/portraits/thumb/women/77.jpg"}, "nat": "MX"}],
photo_url = user['picture']['large']
print(f"Link do zdjęcia {photo_url}")

response_photo = re.get(photo_url)
with open('user_photo.jpg', 'wb') as f:
    f.write(response_photo.content)

print("Zdjęcie zostało zapisane")

# REST API - sposób komunikacji i wymiany danych pomiędzy klientem i serwerem
# Zasób jest podstawowym pojęciem dla API REST.
# Zasób jest obiektem, który ma typ, powiązane dane,
# relacje z innymi zasobami i zestaw metod, które na nim działają.
# Jest bardzo podobny do idei obiektów w programowaniu,
# chociaż zdefiniowanych jest tylko kilka standardowych metod,
# typowych dla HTTP GET, POST, PUT/PATCH i DELETE.
# Zasoby mogą istnieć same lub w zbiorach, które same są zasobami.
# Działanie	      Instrukcja SQL	HTTP	            DDS
# Create	           INSERT	        PUT / POST	        write
# Read (Retrieve)	   SELECT	        GET	                read / take
# Update	           UPDATE	        POST / PUT / PATCH	write
# Delete (Destroy)     DELETE	        DELETE	            dispose
import requests

# pip install requests
url = 'http://api.open-notify.org/astros.json'

# GET - przeglądarka standardowo uzywa tej metody, pobranie z zasobu
response = requests.get(url)
print(response)  # <Response [200]>
# 200 - ok
# 3xx - przekierowanie
# 4xx - 404 - brak zasobu, 400 Bad Request - błedne rzadanie
# 5xx - błedy po stronie serwera
print(response.text)
print(type(response.text))  # <class 'str'>
response_data = response.json()  # zamiana jsona na słownik
print(type(response_data))  # <class 'dict'>
print(response_data)

# wypisac klucze ze słownika
# klucze i wartości
for k, v in response_data.items():
    print(k, "=>", v)
# people = > [{'craft': 'ISS', 'name': 'Oleg Kononenko'}, {'craft': 'ISS', 'name': 'Nikolai Chub'},
#             {'craft': 'ISS', 'name': 'Tracy Caldwell Dyson'}, {'craft': 'ISS', 'name': 'Matthew Dominick'},
#             {'craft': 'ISS', 'name': 'Michael Barratt'}, {'craft': 'ISS', 'name': 'Jeanette Epps'},
#             {'craft': 'ISS', 'name': 'Alexander Grebenkin'}, {'craft': 'ISS', 'name': 'Butch Wilmore'},
#             {'craft': 'ISS', 'name': 'Sunita Williams'}, {'craft': 'Tiangong', 'name': 'Li Guangsu'},
#             {'craft': 'Tiangong', 'name': 'Li Cong'}, {'craft': 'Tiangong', 'name': 'Ye Guangfu'}]
# number = > 12
# message = > success
print(response_data['people'])
print(response_data['people'][0])  # {'craft': 'ISS', 'name': 'Oleg Kononenko'}
for i, p in enumerate(response_data['people']):
    print(i, p['name'])
# 0 Oleg Kononenko
# 1 Nikolai Chub
# 2 Tracy Caldwell Dyson
# 3 Matthew Dominick
# 4 Michael Barratt
# 5 Jeanette Epps
# 6 Alexander Grebenkin
# 7 Butch Wilmore
# 8 Sunita Williams
# 9 Li Guangsu
# 10 Li Cong
# 11 Ye Guangfu

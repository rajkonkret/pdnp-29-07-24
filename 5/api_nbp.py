import requests

url = 'http://api.nbp.pl/api/exchangerates/rates/A/EUR/'
response = requests.get(url)
print(response.text)

# {
#   "table": "A",
#   "currency": "euro",
#   "code": "EUR",
#   "rates": [
#     {
#       "no": "149/A/NBP/2024",
#       "effectiveDate": "2024-08-01",
#       "mid": 4.2924
#     }
#   ]
# }
data = response.json()
print(data['table'])
print(data['currency'])
print(data['rates'])  # [{'no': '149/A/NBP/2024', 'effectiveDate': '2024-08-01', 'mid': 4.2924}]
print(data['rates'][0]['no'])  # 149/A/NBP/2024
print(data['rates'][0]['effectiveDate'])  # 2024-08-01
print(data['rates'][0]['mid'])  # 4.2924

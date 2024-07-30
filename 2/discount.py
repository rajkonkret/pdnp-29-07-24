from datetime import date, datetime, timedelta

today = date.today()
print(today)  # 2024-07-30
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print("Aktualny czas", time)  # Aktualny czas 2024-07-30 15:38:53.667659

# tomorrow = today + 1  # TypeError: unsupported operand type(s) for +: 'datetime.date' and 'int'
# days=0, seconds=0, microseconds=0,
#                 milliseconds=0, minutes=0, hours=0, weeks=0
tomorrow = today + timedelta(days=1)
print(tomorrow)  # 2024-07-31

print(time.time())
print(today.day)
print(time.hour)
# 15:41:31.076738
# 30
# 15

formatted_date = datetime.now().strftime("%d/%m/%Y")
print("Sformatowana data", formatted_date)  # Sformatowana data 30/07/2024

formatted_time = datetime.now().strftime("%H:%M")
print("Sformatowany czas", formatted_time)  # Sformatowany czas 15:45

formatted_12h = datetime.now().strftime("%I:%M %p")
print("Godzina w zegarze 12 godzinnym", formatted_12h)  # Godzina w zegarze 12 godzinnym 03:47 PM

# zamina stringa na obiekt datatime
data_object = datetime.strptime("30/07/2024", "%d/%m/%Y")
print(data_object)  # 2024-07-30 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>

products = [
    {'sku': 1, 'exp_date': today, 'price': 100},
    {'sku': 2, 'exp_date': today, 'price': 200},
    {'sku': 3, 'exp_date': tomorrow, 'price': 100.0},
    {'sku': 4, 'exp_date': today, 'price': 7.50},
    {'sku': 5, 'exp_date': tomorrow, 'price': 50},
]

# print(products)
print(type(products))  # <class 'list'>
for i in products:
    # print(i)
    # print(type(i))  # <class 'dict'>
    # print(i['exp_date'])  # 2024-07-31
    # if i['exp_date'] == today:
    #     i['price'] *= 0.8
    if i['exp_date'] != today:
        continue  # wraca na początek pętli, pętla węźmie kolejny element
    i['price'] *= 0.8
    print(f"""Price for sku {i['sku']}
is now {i['price']}""")
# Price for sku 1
# is now 80.0
# Price for sku 2
# is now 160.0
# Price for sku 4
# is now 6.0

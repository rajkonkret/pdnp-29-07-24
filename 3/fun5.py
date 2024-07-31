# stworzyć funkcję kantor
# ma posiadać dwie funkcje wewnętrzne usd, eur
# w zależności od parametru ma zwracać wybraną funkcję (adres funkcji)
# możliwość przekazania dowolnej kwoty do wymiany
def kantor(waluta):
    print("Uruchomienie kantoru", waluta)

    def usd(kwota=0):
        print("Wymieniam dolary", kwota * 4.01)

    def eur(kwota=0):
        print("Wymieniam euro", kwota * 4.30)

    if waluta == "eur":
        return eur
    else:
        return usd


zenek = kantor("eur")
zenek(1000)
# Uruchomienie kantoru eur
# Wymieniam euro 4300.0
mirek = kantor('usd')
mirek(1000)
# Uruchomienie kantoru usd
# Wymieniam dolary 4010.0
kantor_usd = kantor("usd")
kantor_usd(600)
# Uruchomienie kantoru usd
# Wymieniam dolary 2406.0

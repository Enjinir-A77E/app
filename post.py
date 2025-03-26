import requests
import json

while True:
    mittaus = list()
    mittaus.append(input("Syötä päivä: "))
    mittaus.append(input("Syötä mittaus: "))

    lahetys = {"mittaus":mittaus}
    viesti = json.dumps(lahetys)
    print(viesti)

    vastaus = requests.post()
    
    print(vastaus)
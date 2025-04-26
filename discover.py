import requests
from sys import argv

ddd = argv[1]

try:
        response = requests.get(f"https://brasilapi.com.br/api/ddd/v1/{ddd}").json()
        print(response["state"])
        print("-" * 14)
        for city in response["cities"]:
                print(city)

except Exception as err:
        print(err)
import json
import requests

habbokeko= input("Escribe el keko: ")
response = requests.get(f"https://www.habbo.es/api/public/users?name={habbokeko}")

mission = response.json()["motto"]
if mission:
    mission=f"{mission}"
else:
    mission="No tiene mission"




print(f"{mission}")
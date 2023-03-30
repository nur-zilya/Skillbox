import requests
import json


my_req = requests.get('https://swapi.dev/api/people/3/')
# print(my_req.text)

data = json.loads(my_req.text) #десериализация
data['name']='Zilya'

something = requests.get(data['homeworld'])
# print(something.text)

data_new = json.loads(something.text)
with open('new_site.json', 'w') as file:
    json.dump(data_new, file, indent=4)


with open('my_test.json', 'w') as file:
    json.dump(data, file, indent=4) #сериализация json

with open('my_test.json', 'r') as file:
    data = json.load(file)


import swapi
import requests
import json

result = requests.get("https://swapi.dev/api/films/1/")

json_dict = json.loads(result.text)

print(json_dict["opening_crawl"])

import requests
import json

url = "https://api.jikan.moe/v4/anime/1"
response = requests.get(url)
# print(response.text)
data = json.loads(response.text)
genres = data["data"]["genres"]
title = data["data"]["title"]
rating = data["data"]["rating"]
description = data["data"]["synopsis"]
for g in genres:
    print(g['name'])
print(title, "\n", rating, "\n", description)


with open("anime_details.txt", "w", encoding='utf-8') as file:
    file.write(f"Name - {title} {'\n'}Rating - {rating} {'\n'}Description -  {description}")
# How to write genres to file?

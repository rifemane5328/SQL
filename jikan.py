from bs4 import BeautifulSoup
import requests

url = "https://myanimelist.net/anime/genre/10/Fantasy"
response = requests.get(url)
print(response.text)

soup = BeautifulSoup(response.text, "html.parser")

quotes = soup.find_all("span", class_="js-title")

for quote in quotes:
    print(quote.text)


# print(films)


# with open("anime_by_genre.txt", "w", encoding='utf-8') as file:
#     for film in films:
#         file.write(film + "\n")

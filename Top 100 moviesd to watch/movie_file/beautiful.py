import requests
from bs4 import BeautifulSoup

link = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(link)
html_file = response.text

soup = BeautifulSoup(html_file, 'html.parser')

title = soup.find_all(name="h3", class_="title")
movie_list = [item.get_text() for item in title]
movies = movie_list[::-1]   

with open("movies.txt", mode="w",  encoding="utf-8") as file:
    for item in movies:
        file.write(f"{item}\n")



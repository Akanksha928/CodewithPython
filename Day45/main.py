from bs4 import BeautifulSoup
import requests

#Get the Data
response = requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
webpage = response.text
response.raise_for_status()

# Make Soup
soup = BeautifulSoup(webpage, "html.parser")
list_of_movies = soup.findAll(name="h3", class_="title")
movies = [movie.getText() for movie in list_of_movies]
movies.reverse()

# Write the Data
with open('movieslist.txt', 'w') as file:
    for movie in movies:
        file.write(movie + "\n")


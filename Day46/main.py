from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

client_ID = "12699de2b5564a45b55110c2f40746bb"
client_secret = "85e6171afbf64a0d981091ed87a50133"
redirect_URI = "http://example.com"
id = "31dze4e35vs323yf4sbpgfouwlqa"

date_input = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
year = date_input.split("-")

URL = 'https://www.billboard.com/charts/hot-100/' + date_input + "/"
response = requests.get(URL)
webpage = response.text
response.raise_for_status()

soup = BeautifulSoup(webpage, "html.parser")
songs = soup.findAll(name="h3", id="title-of-a-story")
songs_list = [song.getText() for song in songs]
top_twenty = songs_list[slice(2, 22)]
final_list = []
for song in top_twenty:
    temp = song.split("\n")
    final_list.append(temp[1])

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_ID,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_URI,
                                               scope="playlist-modify-private",
                                               show_dialog=True,
                                               cache_path=".cache"))

uri_list = []
for song in final_list:
    try:
        result = sp.search(q=f"track:{song} year:{year[0]}", type="track")
        uri_list.append(result["tracks"]["items"][0]["uri"])
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


user_id = sp.me()["id"]
playlist_deets = sp.user_playlist_create(user=user_id, name=f"Billboard Top 20 {date_input}", public=False, collaborative=False)

new_id = playlist_deets["id"]
sp.playlist_add_items(playlist_id=new_id, items=uri_list, position=None)




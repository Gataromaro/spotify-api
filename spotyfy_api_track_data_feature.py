import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import pandas as pd
import csv

#入力パート
artist_url = ''
album_url =''
track_url = 'https://open.spotify.com/track/3ciqhcLmXP4hVGBD98QlEj'

output_filename = 'track_data.csv' #.csv形式で名前を入力
#認証パート
my_id ='0000000000000000000000' #client ID
my_secret = '0000000000000000000000' #client secret
ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)

results = spotify.audio_features(track_url)
result = results[0]
for key, val in result.items():
    print(f'{key} : {val}')
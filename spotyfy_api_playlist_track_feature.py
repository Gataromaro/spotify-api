import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time
import pandas as pd
import csv

#入力パート Input part
playlist_url = '' #input playllist URL
output_filename = 'test.csv' # input filename as .csv

#認証パート Authentication part
my_id ='0000000000000000000000' #client ID
my_secret = '0000000000000000000000' #client secret
ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)

list_data = spotify.playlist_tracks(playlist_url)
track_num = list_data['total']
if track_num > 100:
    track_num = 100
urls_list =[]
for i in range(track_num):
    track_url = list_data['items'][i]['track']['external_urls']['spotify']
    urls_list.append(track_url)

time.sleep(1) #1sec stop

track_df = pd.DataFrame(index=[],
                        columns=['Track', 'Artist', 'danceability', 'energy',
                        'key', 'loudness', 'mode', 'speechiness', 'acousticness',
                        'instrumentalness', 'liveness', 'valence','tempo', 'type', 'URL'])
for i in range(len(urls_list)):
    track_data = spotify.track(urls_list[i])
    time.sleep(1) #1sec stop
    track_feature = spotify.audio_features(urls_list[i])[0]
    time.sleep(1) #1sec stop
    track_df = track_df.append({
        'Track' : track_data['name'], 
        'Artist' : track_data['album']['artists'][0]['name'], 
        'danceability' : track_feature['danceability'], 
        'energy' : track_feature['energy'], 
        'key' : track_feature['key'], 
        'loudness' : track_feature['loudness'], 
        'mode' : track_feature['mode'], 
        'speechiness' : track_feature['speechiness'], 
        'acousticness' : track_feature['acousticness'],
        'instrumentalness' : track_feature['instrumentalness'], 
        'liveness' : track_feature['liveness'], 
        'valence' : track_feature['valence'], 
        'tempo' : track_feature['tempo'], 
        'type' : track_feature['type'], 
        'URL' : urls_list[i]}, ignore_index=True)
track_df.to_csv(output_filename, encoding='utf-8') #csvファイル出力
with open(output_filename, 'a', newline='') as f:
    writer = csv.writer(f)
print('finish')

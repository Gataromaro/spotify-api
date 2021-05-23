import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import time

#入力パート Input part
track_url = 'https://open.spotify.com/track/6KqiVlOLfDzJViJVAPym1p?si=6d8a82bb46034ed2'

#認証パート Authentication part
my_id ='0000000000000000000000' #client ID
my_secret = '0000000000000000000000' #client secret
ccm = SpotifyClientCredentials(client_id = my_id, client_secret = my_secret)
spotify = spotipy.Spotify(client_credentials_manager = ccm)

track_data = spotify.track(track_url)
time.sleep(1) #STOP 1sec
results = spotify.audio_features(track_url)
result = results[0]
pitch_class = {0:'C', 1:'C#', 2:'D', 3:'D#', 4:'E', 5:'F',
               6:'F#', 7:'G', 8:'G#', 9:'A', 10:'A#', 11:'B'}
mode_dec = {0:'Minor', 1:'Major'}
ptich = pitch_class[result['key']]
mode_m = mode_dec[result['mode']] #Minor ot Major
track_ms = result['duration_ms'] #track duration msec
track_s = track_ms/1000 #曲長さ sec track duration sec
track_min = track_s//60 #曲長さ min track duration min
track_min_sec = track_s -60 * track_min #曲長さ min track duration min
print('artist  :  ' + track_data['album']['artists'][0]['name'])
print('track  :  ' + track_data['name'])
print('popularity  :  ' + str(track_data['popularity']))
print(f'track time  :  {int(track_min)}min {track_min_sec:.1f}sec')
print('pitch  :  ' + ptich + ' ' + mode_m)
print('tempo(BPM)  :  ' + str(result['tempo']))
print('beat  :  ' + str(result['time_signature']))
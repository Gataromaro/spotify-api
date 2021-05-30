import spotipy
import spotipy.util as util
import time

#入力パート Input part
addition_playlist = 'TRACK_ADDITIONAL_PLAYLIST_URL_' #track adding playlist
original_play_list = 'SEARCH PLAYLIST_URL' #search playlist
set_tempo = 120 #center tempo
set_tempo_range = 5 # +- tempo range

#認証パート Authentication part
username = 'YOUR USER NAME'
my_id ='0000000000000000000000' #client ID
my_secret = '0000000000000000000000' #client secret
redirect_uri = 'Redirect URI' 

#アプリの権限付与に使用する
#https://developer.spotify.com/documentation/general/guides/scopes/
scope = 'user-library-read user-read-playback-state playlist-read-private user-read-recently-played playlist-read-collaborative playlist-modify-public playlist-modify-private'

token = util.prompt_for_user_token(username, scope, my_id, my_secret, redirect_uri)
spotify = spotipy.Spotify(auth = token)


def set_tempo_track(original_play_list, set_tempo, set_tempo_range):
    list_data = spotify.playlist_tracks(original_play_list)
    track_num = list_data['total']
    urls_list =[]
    for i in range(track_num):
        track_url = list_data['items'][i]['track']['external_urls']['spotify']
        urls_list.append(track_url)
    time.sleep(1) #1sec stop
    tempo_urls_list =[]
    for i in range(len(urls_list)):
        track_url = urls_list[i]
        track_feature = spotify.audio_features(track_url)[0]
        time.sleep(1)
        tempo = track_feature['tempo']
        if (set_tempo-set_tempo_range) <= tempo <= (set_tempo + set_tempo_range):
            tempo_urls_list.append(track_url)
        else:
            pass
    return(tempo_urls_list)

tempo_urls_list = set_tempo_track(original_play_list, set_tempo, set_tempo_range)
time.sleep(1)
spotify.user_playlist_add_tracks(username, addition_playlist, tempo_urls_list)
print('finish')

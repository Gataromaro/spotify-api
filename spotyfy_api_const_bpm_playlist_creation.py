import spotipy
import spotipy.util as util
import time

#入力パート Input part
creat_playlist = 'CREAT_PLAYLIST_NAME'
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


def creat_play_list(list_name):
    spotify.user_playlist_create(username, name = list_name)
    list_data = spotify.user_playlists(user = username)
    for i in range(list_data['total']):
        play_list_name = list_data['items'][i]['name']
        if play_list_name == list_name:
            url = list_data['items'][i]['external_urls']['spotify']
        else:
            pass
    return(url)


def set_tempo_track(original_play_list, set_tempo, set_tempo_range):
    list_data = spotify.playlist_tracks(original_play_list)
    track_num = list_data['total']
    if track_num > 100:
        track_num = 100
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

play_list = creat_play_list(creat_playlist)
tempo_urls_list = set_tempo_track(original_play_list, set_tempo, set_tempo_range)
time.sleep(1)
spotify.user_playlist_add_tracks(username, play_list, tempo_urls_list)
print('finish')

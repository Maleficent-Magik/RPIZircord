import requests.exceptions
import spotipy as spotify

scope = 'user-read-currently-playing', 'user-read-playback-state'

try:
    token = "BQDKdb0629Jobkyh5rNW0W2KvIo05WwfbcqbQ83i_cRUbaggvwDv79x6o_8dncZJoZV2eGn8UAmpyxR2SaCaBtCGb-jmhspenaYqgwdarxv_oITYMtrifpihFfXVgWfB0za9fIxPjkZNFVbfj5Ekv04RdwsigP9pYFZeNlo"
except spotify.SpotifyException(spotify.exceptions.SpotifyException(401, -1)):
    print("Acces Token Stoped")

def musicprinter():
    sp = spotify.Spotify(auth=token)
    current_song = sp.currently_playing()
    d = sp.devices()
    try:
        return current_song['item']['name']

    except TypeError:
        return "No music is currently playing! Please check your Spotify!"


print(musicprinter())


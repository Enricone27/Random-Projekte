import os
import sys
import json
import spotipy
import webbrowser
from json.decoder import JSONDecodeError
from spotipy.oauth2 import SpotifyOAuth




username = "enricone03"
scope = 'playlist-modify-private'
#enricone03

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope))

#crate spotifyObject
#spotipyobject = spotipy.Spotify(auth=token)

user = sp.current_user()

#print(json.dumps(user , indent=4))

displayname = user['display_name']
followers = user['followers']['total']


while True:
    
    print()
    print("0 exit\n1 artis\n2 current song\n3 playlists\n4 alligatoah")

    choice = input("number? ")
    if choice == "1":
        querry = input("artist?")
        result = sp.search(querry, limit=1, type='artist')
        #print(json.dumps(result, indent=4))
        artist = result ['artists']['items'][0]
        print(artist['name'])
        for i in artist["genres"]:
            print(i)
        #webbrowser.open(artist["images"][0]["url"])
        Id = artist['id']

        album = sp.artist_albums(Id, "album")['items']
        for albums in album:
            print(albums['id']+albums['name'])
        #print(json.dumps(album, indent=4))
    if choice == "0":
        break
    if choice == "2":
        song =sp.current_user_playing_track()['item']
        #print(json.dumps(song, indent=4))
        print(song['artists'][0]['name'] + " - " +song['name'])
        print()


    if choice == "3":
        play = sp.current_user_playlists(10)
        for i in play['items']:
            print(i["name"])

        print(json.dumps(sp.playlist("38EcWP6EEIsOcQtCC0M9LD"), indent=4))


    if choice == "4":

        plid=(sp.user_playlist_create(username , name="alligatoahtracks")['id'])
        #print(plid)
        #sp.user_playlist()
        album = sp.artist_albums('0r0R5nIjDY04TfxRM10Bcb', "album")['items']
        for albums in album:
            #print(albums['id']+albums['name'])
            
            tracks = sp.album_tracks(albums['id'])
            for track in tracks['items']:
                ids = []
                ids.append(track['id'])
                #print(ids)
                sp.playlist_add_items(plid,ids)

    if choice == "5":
        result =(sp.search("alligatoah" , limit=10, type='playlist')['playlists']['items'])
        print(json.dumps(result, indent=4))

#print 
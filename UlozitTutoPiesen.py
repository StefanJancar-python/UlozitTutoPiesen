#!/usr/bin/env python

import os
import youtube_dl
import spotipy
import spotipy.util as util
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.oauth2 as oauth2
from youtube_search import YoutubeSearch
import json
import webbrowser

## YouTube downloader options
ydl_opts = {
    'format': 'bestaudio/best',
     'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },
            {'key': 'FFmpegMetadata'},
        ],
}

'''
# you'll need this to download songs on spotify
CLIENT_ID=
CLIENT_SECRET=
'''

songs = [] # list of songs from spotify playlist
urls = []  # yt links of all the songs from the urls array

# Authorizes and gets the track names from the playlist
def downloadFromPlaylist(Playlist, CID, secret):

### for auth
    credentials = oauth2.SpotifyClientCredentials(
            client_id=CID,
            client_secret=secret)

    token = credentials.get_access_token()
    spotify = spotipy.Spotify(auth=token)

### looks for spotify playlist

    PID = Playlist.rsplit('/', 1)[1]
    items = spotify.playlist_tracks(PID)

### gets the artist name and song name from playlist and adds them to the array 'songs'
    for item in items['items']:
        for artist in item['track']['album']['artists']:
            artistName = artist['name']
        songName = item['track']['name']
        ### added 'lyrics' at the end so it's easier to find the song on yt later
        searchQuery = songName + ' ' + artistName + ' lyrics'
        songs.append(searchQuery)

def UrlFinder(song):
    print('Looking for song: ', song, 'on YouTube')
    results = YoutubeSearch(song, max_results=1).to_json()
    data = json.loads(results)
    for v in data['videos']:
        videoID = v['id']
        baseUrl = 'https://www.youtube.com/watch?v='
        videoURL = baseUrl + videoID
        urls.append(videoURL)


### function that downloads songs from the 'songs' array using the urls in the urls array with youtube-dl
def download_song(song_url):
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(song_url, download=True)


def downloadFromLinks(urlList):
    for url in urls:
        print("Downloading song " + str(urls.index(url) + 1) + "/" + str(len(urls)) + "...")
        try:
            download_song(url)
        except:
            print("Failed to download song " + url)


print('''
        ##############################################################
        ##################  SPOTIFY DOWNLOADER  ######################
       ---------------------------------------------------------------
          Tento program vám umožňuje stahovat skladby zo spotify zdarma
       ---------------------------------------------------------------
        ##################  SPOTIFY DOWNLOADER  ######################
        ##############################################################
Menu:
1. Stahujte skladby zo soznamu skladieb Spotify.
2. Stahujte skladby zo soznamu skladieb YouTube.
3. Stiahnite si skladby zo zoznamu skladieb.
4. Stiahnite si jednu skladbu.
5. Pomoc
      ''')

choice = input("Zadajte svoj výber: ")

if choice == '1':

    if "SPOTIFY_CLIENT_ID" and "SPOTIFY_CLIENT_SECRET" in os.environ:
        print('Nájdené SPOTIFY_CLIENT_ID a SPOTIFY_CLIENT_SECRET! :D')
        client_ID = os.environ['SPOTIFY_CLIENT_ID']
        client_Secret = os.environ['SPOTIFY_CLIENT_SECRET']
        playlistLink = input("Zadajte odkaz na zoznam skladieb: ")
        downloadFromPlaylist(playlistLink, client_ID, client_Secret)
        for song in songs:
            try:
                UrlFinder(song)
            except:
                print("Couldn't find: " + song + " on YouTube")

        downloadFromLinks(urls)

    else:
        print('Ak chcete sťahovať skladby zo zoznamu skladieb Spotify, potrebujete svoj Spotify Client_ID a CLIENT_SECRET.')
        ch = input("Máte ich pri sebe? (y/n): ")
        if ch == 'a' or ch == 'A' or ch == 'áno':
                client_ID = input("Zadajte svoje ID klienta: ")
                client_Secret = input("Zadajte svoje klientske Secret: ")
                print('''
Note:
Nabudúce ich nezabudnite pridať ako premenné prostredia do svojho operačného systému, aby ste ich nemuseli zadávať zakaždým, keď si chcete zo Spotify stiahnuť zoznam skladieb. Pokyny, ako to urobiť, nájdete na mojej webovej stránke alebo na mojom Githube, ku ktorým je prístup z ponuky „Pomoc“ v hlavnej ponuke. :)
                    ''')

                playlistLink = input("Enter the playlist link: ")
                downloadFromPlaylist(playlistLink, client_ID, client_Secret)
                for song in songs:
                    UrlFinder(song)
                downloadFromLinks(urls)

        elif ch == 'n' or ch == 'N' or ch == 'no':
            print('''
Pokyny, ako získať svoje Spotify Client_ID a Secret, nájdete na mojej webovej stránke alebo na mojom Githube. Skontrolujte to výberom možnosti „Pomoc“ v ponuke. Nie je to vôbec zložité a nezaberie to viac ako 10 minút. :) ''')


elif choice == '2':
    ytPlaylistLink = input("Zadajte odkaz na zoznam videí na youtube: ")
    download_song(ytPlaylistLink)

elif choice == '3':
    userlist = input('Zadajte názov súboru (s príponou): ')
    with open(userlist, 'r') as file:
        listOfSongs = file.readlines()
        for song in listOfSongs:
            UrlFinder(song)
        downloadFromLinks(urls)

elif choice == '4':
    songName = input("Zadajte názov skladby: ")
    UrlFinder(songName)
    downloadFromLinks(urls)

elif choice == '5':

    spotify = 'https://stefan222.pythonanywhere.com/'
    github = 'https://github.com/vianoce/UlozitTutoPiesen'
    youtube = ''

    print('''
    1. Ako získať ID a Secret klienta zo služby Spotify
    2. Webová stránka autora
    3. Videonávod (YouTube)
    ''')


    ch = input("Zadajte svoj výber: ")

    if ch == '1':
        webbrowser.open(spotify)
    elif ch == '2':
        webbrowser.open(github)
    elif ch == '3':
        webbrowser.open(youtube)

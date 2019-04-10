import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy.util as util

def getTracks(username,client_id,client_secret,redirect_uri, getNames = False):

    #set up scope 
    scope = 'playlist-read-private,playlist-read-collaborative,playlist-modify-public'

    token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri)

    if token:
        #  spotify object 
        sp = spotipy.Spotify(auth=token)


        # use to get user id
        currentUser = sp.current_user()

        #the user id is everything after the backslash
        fullUserID = currentUser['external_urls']['spotify']
        takeTwo = fullUserID.split('user/')
        userID = takeTwo[1]

        #get the users playlists 
        playlists = sp.user_playlists(userID)

        #get the playlist id's 
        playlistIDs = getPlaylistIds(playlists)

        # go into each playlist and put the track ids into a lsit
        idList = []
        tracks = []
        nameList = []
        #go through each playlist and get the track id 
        for x in playlistIDs:
            # track info for playlist x
            tracks = get_playlist_tracks(userID,x,sp)
            count = 0
            # goes through all the tracks and puts the id in idlist
            while count < len(tracks):
                idList.append(tracks[count]['track']['id'])
                nameList.append(tracks[count]['track']['name'])
                count = count + 1

        if getNames:
            return nameList
        else:
            return idList
        
    else:
        return []

def getPlaylistIds(playlists):
    playlistID = []
    for playlist in playlists['items']:

        #take everything after the last / for the playlist id
        #get the playlist id everything after the last slash
        fullPLID = playlist['external_urls']['spotify']

        #playlist ID has all the ids of my playlists
        playlistID.append(fullPLID.split('playlist/')[1])
    
    return playlistID


def get_playlist_tracks(userId,playlist_id,sp):
    #gets a dict of the tracks in a playlist  
    results = sp.user_playlist_tracks(userId,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
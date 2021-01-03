import spotipy
import spotipy.util as util

def get_tracks(username, client_id, client_secret, redirect_uri, get_names = False):

    #set up scope 
    scope = 'playlist-read-private,playlist-read-collaborative,playlist-modify-public'

    token = util.prompt_for_user_token(username, scope, client_id, client_secret, redirect_uri)

    if token:
        #  spotify object 
        sp = spotipy.Spotify(auth=token)

        # use to get user id
        current_user = sp.current_user()

        #the user id is everything after the backslash
        full_user_id = current_user['external_urls']['spotify']
        take_two = full_user_id.split('user/')
        user_id = take_two[1]

        #get the users playlists 
        playlists = sp.user_playlists(user_id)

        #get the playlist id's 
        playlist_ids = get_playlist_ids(playlists)

        # go into each playlist and put the track ids into a lsit
        id_list = []
        tracks = []
        name_list = []
        #go through each playlist and get the track id 
        for x in playlist_ids:
            # track info for playlist x
            tracks = get_playlist_tracks(user_id, x, sp)
            count = 0
            # goes through all the tracks and puts the id in idlist
            while count < len(tracks):
                id_list.append(tracks[count]['track']['id'])
                name_list.append(tracks[count]['track']['name'])
                count = count + 1

        if get_names:
            return name_list
        else:
            return id_list
        
    else:
        return []

def get_playlist_ids(playlists):
    playlist_ids = []
    for playlist in playlists['items']:
        #take everything after the last / for the playlist id
        #get the playlist id everything after the last slash
        full_PLID = playlist['external_urls']['spotify']

        #playlist ID has all the ids of my playlists
        playlist_ids.append(full_PLID.split('playlist/')[1])
    
    return playlist_ids


def get_playlist_tracks(user_id, playlist_id, sp):
    #gets a dict of the tracks in a playlist  
    results = sp.user_playlist_tracks(user_id,playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks
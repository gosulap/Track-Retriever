[![Downloads](https://static.pepy.tech/personalized-badge/trackretriever?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/trackretriever?versions=1.0.1&versions=1.0.0)
# Track Retriever

Built to make it easier for people to work with the tracks in their Spotify playlists 

### Prerequisites

I assume that you have already made a Spotify project, if not you can do that [here](https://developer.spotify.com/dashboard/)

```
You'll need your: username, client_id, client_secret, redirect_uri and user_id 
```

### Installing

```
pip install trackretriever
``` 

## Functions 

I made get_playlist_ids and get_playlist_tracks as helpers for get_tracks but you are more than welcome to use them

```
get_tracks(username, client_id, client_secret, redirect_uri, get_names = False)

All the parameters should be input as string except getNames
When getNames is set to True getTracks will return a list of the names of the tracks in your playlists
When getNames is set to False getTracks will return a list of the track id's of the tracks in your playlists 
```

```
get_playlist_ids(playlists)

This will get the playlist id's of your playlists 
playlists = sp.user_playlists(user_id) *user_id is not your username* 
```

```
get_playlist_tracks(user_id, playlist_id, sp)

sp is the spotify object created by spotipy.Spotify(auth=token)
playlist_id is the id of the playlist you want to retrieve the tracks for 
```

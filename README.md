[![Downloads](https://static.pepy.tech/personalized-badge/trackretriever?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/trackretriever?versions=1.0.1&versions=1.0.0)
# Track Retriever

Built to make it easier for everyone to work with their Spotify playlists.

## Prerequisites

I assume that you have already made a Spotify project, if not you can do that [here](https://developer.spotify.com/dashboard/)

```
You'll need your: username, client_id, client_secret, redirect_uri and user_id 
```

## Installing

```bash
pip install trackRetriever
```

## Usage

```python
import trackRetriever

'''
Gets the names/track_ids of the songs in a users playlists

When get_names is set to True get_tracks will return a list of the names of the tracks in your playlists
When get_names is set to False get_tracks will return a list of the track_ids of the tracks in your playlists

Parameters:
    username - Spotify username
    client_id - From spotify project 
    client_secret - From spotify project 
    redirect_uri - From spotify project 
    get_names - True when names of tracks need to be returned, False otherwise 

Note: All the parameters should be strings except get_names
'''


trackRetriever.get_tracks(username, client_id, client_secret, redirect_uri)
trackRetriever.get_tracks(username, client_id, client_secret, redirect_uri, True)


'''
Gets the playlist_ids of the users playlists

Parameters:
    playlists - user playlists

Note: playlists = sp.user_playlists(user_id) *user_id is not your username*  
'''


trackRetriever.get_playlist_ids(playlists) 


'''
Gets the tracks in the specified playlist

Parameters:
    sp - spotify object created by spotipy.Spotify(auth=token)
    playlist_id - id of the target playlist

Note: playlist_id should be a string
'''


trackRetriever.get_playlist_tracks(user_id, playlist_id, sp)


```

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)


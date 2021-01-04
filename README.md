[![Downloads](https://static.pepy.tech/personalized-badge/trackretriever?period=total&units=international_system&left_color=grey&right_color=blue&left_text=Downloads)](https://pepy.tech/project/trackretriever?versions=1.0.1&versions=1.0.0)
# Track Retriever

Built to make it easier for people to work with the tracks in their Spotify playlists 

### Prerequisites

I assume that you have already made a Spotify project, if not you can do that [here](https://developer.spotify.com/dashboard/)

```
You'll need your: username, client_id, client_secret, redirect_uri and user_id 
```

### Installing

```bash
pip install trackRetriever
```

## Usage

```python
import trackRetriever

'''
Gets the names/track-ids of the songs in a users playlists

When get_names is set to True get_tracks will return a list of the names of the tracks in your playlists
When get_names is set to False get_tracks will return a list of the track-ids of the tracks in your playlists

Note: All the parameters should be input as string except get_names
'''
trackRetriever.get_tracks(username, client_id, client_secret, redirect_uri)
trackRetriever.get_tracks(username, client_id, client_secret, redirect_uri, True)

'''
Gets the playlist id's the users playlists

Note: playlists = sp.user_playlists(user_id) *user_id is not your username*  
'''
trackRetrieverget_playlist_ids(playlists) 

'''
Gets the tracks in the specified playlist

sp is the spotify object created by spotipy.Spotify(auth=token)
playlist_id is the id of the playlist you want to retrieve the tracks for 
'''
trackRetriever.get_playlist_tracks(user_id, playlist_id, sp)
```

## Contributing
Pull requests are welcome.

## License
[MIT](https://choosealicense.com/licenses/mit/)


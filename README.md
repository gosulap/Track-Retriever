# track-retriever

I built this to make it easier for people to work with the tracks that exist in their Spotify playlists 

### Prerequisites

I assume that you have already made a Spotify project, if not you can do that [here](https://developer.spotify.com/dashboard/)

```
You'll need your: username, client_id, client_secret and redirect_uri
```

### Installing

```
pip install trackRetriever
```

Just import it into your project after that 

## Functions 

```
getTracks(username, client_id, client_secret,redirect_uri,getNames = False)

All the parameters should be input as string except getNames
When getNames is set to True getTracks will return a list of the names of the tracks in your playlists
When getNames is set to False getTracks will return a list of the track id's of the tracks in your playlists
```

```
getPlaylistIds()
```

```
get_playlist_tracks()
```
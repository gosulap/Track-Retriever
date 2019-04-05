# track-retriever

This module is meant to make it easy for people to get the songs in their spotify playlists
I assume that you already have set up a project in the Spotify developer console

You'll need:
    -   Your client id 
    -   Your client secret
    -   The redirect uri
    -   Your username (hopefully already know this)

There are three functions:

getTracks(username,client_id,client_secret,redirect_uri)
getPlaylistIds(playlists)
get_playlist_tracks(userId,playlist_id,sp)
# track-retriever

<p>
    This module is meant to make it easy for people to get the songs in their spotify playlists
    I assume that you already have set up a project in the Spotify developer console
</p>

You'll need:
<br/>
    -   Your client id 
<br/>
    -   Your client secret
<br/>
    -   The redirect uri
<br/>
    -   Your username (hopefully already know this)

There are three functions:

<br/>
getTracks(username,client_id,client_secret,redirect_uri)
<br/>
getPlaylistIds(playlists)
<br/>
get_playlist_tracks(userId,playlist_id,sp)
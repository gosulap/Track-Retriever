# track-retriever

This module is meant to make it easy for people to get the songs in their spotify playlists
<br/>
I assume that you already have set up a project in the Spotify developer console

You'll need:
<br/>
    -   Your client id 
<br/>
    -   Your client secret
<br/>
    -   The redirect uri
<br/>
    -   Your username

There are three functions:
<br/>
getTracks(username,client_id,client_secret,redirect_uri,getNames)
<br/>
        <p>
        - This will return all the tracks in your playlists
        </p>
    <br/>
        <p>
        - All the parameters are strings except getNames which is a boolean
        </p>
    <br/>
        <p>
        - If set to True getNames will make getTracks return a list of the names of the tracks in your playlists
          otherwise you'll get a list of the track ids of the songs in your playlists 
        </p>
    <br/>
      
<br/>
getPlaylistIds(playlists)
<br/>
get_playlist_tracks(userId,playlist_id,sp)
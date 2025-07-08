import json
import os
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import boto3
from datetime import datetime

def lambda_handler(event, context):
    # TODO implement
    client_id = os.environ.get("client_id")
    client_secret = os.environ.get("client_secret")
    client_credential_manager = SpotifyClientCredentials(client_id = client_id , client_secret = client_secret)
    sp = spotipy.Spotify(client_credentials_manager = client_credential_manager)
    # playlist = sp.user_playlist('spotify')

    playlist_link = "https://open.spotify.com/playlist/6VOedaf3eNWDOVpa9Qdlvg?si=sU-uTK_cRnegQ6xiYpB7kg"

    playlist_uri = playlist_link.split("/")[-1].split("?")[0]
    spotify_data = sp.playlist_tracks(playlist_uri)
    

    client = boto3.client('s3')
    file_name = 'spotify_raw_' + str(datetime.now()) + '.json'
    client.put_object(
        Bucket = 'aws-etl-project-anuj',
        Key = 'raw_data/to_processed/'+file_name,
        Body = json.dumps(spotify_data)
    )
import decouple
import spotipy


def search(query):
    client_id = decouple.config('SPOTIFY-CLIENT-ID')
    client_secrete_id = decouple.config('SPOTIFY-CLIENT-SECRET-ID')
    client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_secrete_id)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        print(results)
        track_id = results['tracks']['items'][0]['id']
        return f'https://open.spotify.com/track/{track_id}'
    else:
        return None
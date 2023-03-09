import decouple
import spotipy
import discord


def search(query):
    client_id = decouple.config('SPOTIFY-CLIENT-ID')
    client_secrete_id = decouple.config('SPOTIFY-CLIENT-SECRET-ID')
    client_credentials_manager = spotipy.SpotifyClientCredentials(client_id=client_id, client_secret=client_secrete_id)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    results = sp.search(q=query, type='track', limit=1)
    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        embed = discord.Embed(title=track['name'], url=track['external_urls']['spotify'], color=0x1DB954)
        embed.set_thumbnail(url=track['album']['images'][0]['url'])
        embed.add_field(name='Artista', value=track['artists'][0]['name'], inline=False)
        embed.add_field(name='Álbum', value=track['album']['name'], inline=False)
        embed.set_footer(text='Spotify', icon_url='https://i.imgur.com/vBYxuV9.png')
        return embed
    else:
        return None
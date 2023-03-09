import asyncio
import random
import discord
import decouple

from spotify import search

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

TOKEN = decouple.config('TOKEN')
GUILD = decouple.config('DISCORD-GUID')


@client.event
async def on_ready():
    for guild in client.guilds:
        print(guild)
        if guild.name == GUILD:
            break
    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    _99_frases_aleatorias = [
        'Espero que estés disfrutando al &#x1f4af;.',
        'Hola!!!! &#x1f609;',
        'Amigo, aquí estamos para disfrutar'
    ]
    if message.content == '99!':
            _99_frases_aleatorias = [
                'Espero que estés disfrutando al maximo;.',
                'Hola!!!! 😁;',
                'Amigo, aquí estamos para disfrutar'
            ]
            response = random.choice(_99_frases_aleatorias)
            await message.channel.send(response)

    elif message.content == 'hola':
        response = f'hola {message.author}'
        await message.channel.send(response)

    elif message.content == '!spotify':
        await message.channel.send('habla claro ¿cual buscas?')
        def check(msg):
             return msg.author == message.author and msg.channel == message.channel
        try:
            query = await client.wait_for('message', check=check, timeout=30.0)
            song_link = search(query.content)
            if song_link:
                  await message.channel.send(song_link)
            else:
                await message.channel.send('No se encontró ninguna canción con ese nombre.')
        except asyncio.TimeoutError:
            await message.channel.send('Tiempo de espera agotado. Vuelve a intentarlo.')



client.run(TOKEN)

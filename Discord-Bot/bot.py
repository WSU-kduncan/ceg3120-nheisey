import os

import discord
import random
from dotenv import load_dotenv

load_dotenv()
#print(os.getenv('DISCORD_TOKEN'))
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    brooklyn_99_quotes = [
        'I\'m the human form of the 💯 emoji.',
        'Bingpot!',
        (
            'Cool. Cool cool cool cool cool cool cool, '
            'no doubt no doubt no doubt no doubt.'
        ),
    ]

    pixy = [
        'You and I are opposite sides of the same coin. When we face each other, we can finally see our true selves. There may be a resemblance, but we never face the same direction.',
        'Those who survive a long time on the battlefield start to think they are invincible. I bet you do, too, Buddy.',
        'Yo buddy, still alive? And thanks friend. See you again',
        'So, tell me. Have you found a reason to fight yet? Buddy.',
	'While you were up here "fighting for peace," tons of blood is being shed on the ground. Some "peace," kid.',
	'Can you see any borders from here? What has borders given us? We\'re going to start over from scratch. That\'s what V2 is for.',
	'Too bad, Buddy. This twisted game needs to be reset. We\'ll start over from "zero" with this V2 and entrust the future to the next generation.',
	'When we face each other, we can finally see our true selves. There may be a resemblance, but we never face the same direction.',
	'Fire away, coward!',
	'Now we find out who\'s number one.'

    ]

    if message.content == '!pixy':
        #response = random.choice(brooklyn_99_quotes)
        response = random.choice(pixy)
        await message.channel.send(response)

client.run(TOKEN)

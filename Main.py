import keep_alive
import discord
import time
from discord.ext import tasks

Token = "<enter your bots token here>"

client = discord.Client(command_prefix='',intents=discord.Intents.default())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="<write anything here>"))
    send_message.start()
    print('logged in as {0.user}'.format(client))


@tasks.loop(seconds = 1)
async def send_message():
  x = 0
  for i in range(1,<after how long do you want it to send the messages, in seconds>):
    x = x + 1
    time.sleep(1)
    await client.get_channel(<enter channel id of channel you want the bot to count in>).send(x)
  await client.get_channel(<channel id of channel you want it to send the message in>).send(<what you want to be sent at the end of the given time>)

keep_alive.keep_alive()
client.run(token)

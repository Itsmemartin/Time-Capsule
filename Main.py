import keep_alive
import discord
import time
from discord.ext import tasks

Token = "<enter your bots token here>"

client = discord.Client(command_prefix='',intents=discord.Intents.default())

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Opening Capsules..."))
    print('logged in as {0.user}'.format(client))

@client.tree.command(name='Setup', description="Set time and message for the time capsule")
async def caliberate_id(interaction: discord.Interaction, time_in_days: int, message: str, count_channel:str, message_channel: str):
    Global time_in_days, message, count_channel, message_channel
    time_in_days = time_in_days
    message = message
    count_channel = count_channel
    message_channel = message_channel

    await interaction.response.send_message(f"The Capsule will open in {time_in_days} days in {message_channel}")
    send_message.start()

@tasks.loop(seconds = 1)
async def send_message():
  x = 0
  for i in range(1, time_in_days*24*3600):
    x = x + 1
    time.sleep(1)
    await client.get_channel(count_channel).send(x)
  await client.get_channel(message_channel).send(message)

keep_alive.keep_alive()
client.run(token)

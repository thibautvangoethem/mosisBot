import os

import discord
from discord.ext import commands
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!', help_command=None)


@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')


if __name__ == '__main__':
    from mosis_bot import MosisBot

    bot.add_cog(MosisBot(bot))
    bot.run(TOKEN)

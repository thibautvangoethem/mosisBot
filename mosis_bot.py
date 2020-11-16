import discord
from discord.ext import commands
import requests
import datetime

class MosisBot(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='pray',aliases=['p'])
    async def pray(self, ctx):
        await ctx.send(":pray:<:hans:760816272426139658>:pray:")

    @commands.command(name='assignment',aliases=['a'])
    async def assignment(self, ctx):
        page = requests.get('http://msdl.cs.mcgill.ca/people/hv/teaching/MoSIS/')
        pageString = page.content.decode("utf-8", errors="ignore")
        loc = pageString.find("<!-- a href=\"assignments/CBD/part2_html\" -->")
        if(loc != -1):
            thePromisedTuesday = datetime.datetime(2020, 11, 10)
            today = datetime.datetime.now()
            await ctx.send("It has been %s days since the promised tuesday"%str((today-thePromisedTuesday).days))
            await ctx.send("And the assignment has not yet arrived")
            await ctx.send("Let us !pray in the hope that it will one day come")
        else:
            await ctx.send(":partying_face: THE ASSIGNMENT HAS ARRIVED!!! :partying_face: ")

    @commands.command(name='riot', aliases=['r'])
    async def riot(self,ctx):
        await ctx.send("We have been scammed, time for a riot :fire: :house_abandoned: :fire:")
import traceback
import typing

import discord
from discord.ext import commands


class Owner(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def cog_check(self, ctx):
        return await self.bot.is_owner(ctx.author)

    @commands.command(brief="Adds to music videos")
    async def add_music(self, ctx, url: typing.Optional[str] = None, user : typing.Optional[discord.User] = None, service : typing.Optional[str] = None):

        user = user or ctx.author
        service = service or "YouTube"

        if not url:
            return await ctx.send("Url must exist, it cannot be None.")

        url_check = await self.bot.db.fetchrow("SELECT * from music where url = $1", url)
        if url_check:
            return await ctx.send(f"{url} already in music videos.")

        await self.bot.db.execute("INSERT INTO music VALUES($1, $2, $3)", user.id, url, service)
        return await ctx.send(f"{url} added to music.")
    
    @commands.command(brief="Removes music videos")
    async def remove_music(self, ctx, url: typing.Optional[str] = None):
        if not url:
            return await ctx.send("Url cannot be None")
        
        url_check = await self.bot.db.fetchrow("SELECT * from music where url = $1", url)

        if not url_check:
            return await ctx.send(f"{url} must be in database")
        
        await self.bot.db.execute("DELETE FROM music WHERE url = $1", url)
        return await ctx.send(f"Removed {url} from database")

    @commands.command(brief="Adds to watched_videos videos")
    async def add_watched_videos(self, ctx, url: typing.Optional[str] = None, user : typing.Optional[discord.User] = None, service : typing.Optional[str] = None):

        user = user or ctx.author
        service = service or "YouTube"

        if not url:
            return await ctx.send("Url must exist, it cannot be None.")

        url_check = await self.bot.db.fetchrow("SELECT * from watched_videos where url = $1", url)
        if url_check:
            return await ctx.send(f"{url} already in watched_videos videos.")

        await self.bot.db.execute("INSERT INTO watched_videos VALUES($1, $2, $3)", user.id, url, service)
        return await ctx.send(f"{url} added to watched_videos")
    
    @commands.command(brief="Removes watched videos")
    async def remove_watched_videos(self, ctx, url: typing.Optional[str] = None):
        if not url:
            return await ctx.send("Url cannot be None")
        
        url_check = await self.bot.db.fetchrow("SELECT * from watched_videos where url = $1", url)

        if not url_check:
            return await ctx.send(f"{url} must be in database")
        
        await self.bot.db.execute("DELETE FROM watched_videos WHERE url = $1", url)
        return await ctx.send(f"Removed {url} from database")

    @commands.command(brief="Adds to to_watch videos")
    async def add_to_watch(self, ctx, url: typing.Optional[str] = None, user : typing.Optional[discord.User] = None, service : typing.Optional[str] = None):

        user = user or ctx.author
        service = service or "YouTube"

        if not url:
            return await ctx.send("Url must exist, it cannot be None.")

        url_check = await self.bot.db.fetchrow("SELECT * from to_watch where url = $1", url)
        if url_check:
            return await ctx.send(f"{url} already in to_watch videos.")

        await self.bot.db.execute("INSERT INTO to_watch VALUES($1, $2, $3)", user.id, url, service)
        return await ctx.send(f"{url} added to to_watch")

    @commands.command(brief="Removes to_watch videos")
    async def remove_to_watch(self, ctx, url: typing.Optional[str] = None):
        if not url:
            return await ctx.send("Url cannot be None")
        
        url_check = await self.bot.db.fetchrow("SELECT * from to_watch where url = $1", url)

        if not url_check:
            return await ctx.send(f"{url} must be in database")
        
        await self.bot.db.execute("DELETE FROM to_watch WHERE url = $1", url)
        return await ctx.send(f"Removed {url} from database")

    @commands.command(brief="Adds idk videos")
    async def add_idk(self, ctx, url: typing.Optional[str] = None, user : typing.Optional[discord.User] = None, service : typing.Optional[str] = None):

        user = user or ctx.author
        service = service or "YouTube"

        if not url:
            return await ctx.send("Url must exist, it cannot be None.")

        url_check = await self.bot.db.fetchrow("SELECT * from idk_videos where url = $1", url)
        if url_check:
            return await ctx.send(f"{url} already in idk_videos.")

        await self.bot.db.execute("INSERT INTO idk_videos VALUES($1, $2, $3)", user.id, url, service)
        return await ctx.send(f"{url} added to idk_videos")

    @commands.command(brief="Removes idk videos")
    async def remove_idk_videos(self, ctx, url: typing.Optional[str] = None):
        if not url:
            return await ctx.send("Url cannot be None")
        
        url_check = await self.bot.db.fetchrow("SELECT * from idk_videos where url = $1", url)

        if not url_check:
            return await ctx.send(f"{url} must be in database")
        
        await self.bot.db.execute("DELETE FROM idk_videos WHERE url = $1", url)
        return await ctx.send(f"Removed {url} from database")
    
    
    async def cog_command_error(self, ctx, error):
        await ctx.send(error)
        traceback.print_exc(error)

    # error stuff lol

    # idk about remove stuff so idk.
        
    # good everything good here.


async def setup(bot):
    await bot.add_cog(Owner(bot))
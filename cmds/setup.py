import discord
from discord.utils import get
from discord.ext import commands

client = discord.Client(intents = discord.Intents.all())

class Setup(commands.Cog, name = "setup"):
    def __init__(self, bot):
        self.bot = bot

    text = 'A command to quickly set up your collabrative environment. Input you connections separated by commas'
    @commands.hybrid_command(name = 'setup', with_app_command = True, description = text,)
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx, connections):

        await ctx.send('Beginning your server setup!')

        # Delete all initial categories, then delete the remaining channels
        for channel in ctx.guild.channels:
            await channel.delete()
        for category in ctx.guild.categories:
            await category.delete()


        # Setup the categories to hold the channels
        updates = await ctx.guild.create_category(name='Updates', position = 0, reason = 'New update channel')
        tracker = await ctx.guild.create_category(name = 'Schedule/Calendar', position = 1, reason = 'New tracking channel')
        ticket = await ctx.guild.create_category(name = 'Tickets', position = 2, reason = 'New ticketing channel')
        voice = await ctx.guild.create_category(name = 'Voice Channels', position = 3, reason = 'New Voice Channels')

        # Create the actual channels within the new categories
        conList = connections.split(',')
        general = await updates.create_text_channel(name = 'General')
        for connect in conList:
            channelName = connect.replace(' ', '')
            await updates.create_text_channel(name = channelName + '-updates')

        await tracker.create_text_channel(name = 'Team-member-scheduler')
        await tracker.create_text_channel(name = 'Upcoming meetings')

        await ticket.create_text_channel(name = 'Submit-a-ticket')

        for i in range(1, 6):
            await voice.create_voice_channel(name = 'Voice ' + str(i))

        await general.send('Your server is now setup!')

async def setup(bot):
    await bot.add_cog(Setup(bot))
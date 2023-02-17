import discord
from discord.ext import commands

text = 'A command to quickly set up your collabrative environment. Input you connections separated by commas'
@commands.hybrid_command(name = 'setup', with_app_command = True, description = text)
async def setup(interaction: discord.Interaction, guild: discord.Guild, connections):
    await interaction.response.send_message('Beginning your server setup!')

    # Setup the categories to hold the channels
    updates = guild.create_category('Updates')
    tracker = guild.create_category('Schedule/Calendar')
    ticket = guild.create_category('Tickets')
    voice = guild.create_category('Voice Channels')

    # Create the actual channels within the new categories
    conList = connections.split(',')
    for connect in conList:
        channelName = connect.replace(' ')
        updates.create_text_channel(name = channelName + '-updates')

    tracker.create_text_channel(name = 'Team-member-scheduler')
    tracker.create_text_channel(name = 'Upcoming meetings')

    ticket.create_text_channel(name = 'Submi-a-ticket')

    for i in range(1, 6):
        voice.create_voice_channel(name = 'Voice ' + i)

    await interaction.response.send_message('Your server is now setup!')
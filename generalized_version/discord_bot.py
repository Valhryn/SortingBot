import discord

import dotenv

import generalized_version.main

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot

@bot.event
async def on_ready():
    print(f"Bot has logged in!")

@bot.slash_command(guild_ids="1081362341767168112")
async def create_player(ctx, name, days, min_hour: discord.option(int), max_hour: discord.option(int), role):
    file = open("player.txt", "w")
    data = "Name: " + name
    data += "\nGuild: " + ctx.guild
    data += "\nDays: " + str(days)
    data += "\nTimes" + str([min_hour, max_hour])[1:-1]
    data += "\nRoles: " + role
    file.write(data)
    await ctx.send(name + " is made!")

@bot.slash_command(guild_ids="1081362341767168112")
async def form_parties(ctx):
    generalized_version.main.start()
    member_list = generalized_version.main.set_members(ctx.guild)
    parties = generalized_version.main.create_parties(member_list)
    file = generalized_version.main.end_file(parties)

    await ctx.send(file)




bot.run(token)
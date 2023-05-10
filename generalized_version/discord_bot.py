import os
import discord
from discord import guild_only
import dotenv
import sorter

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))

bot = discord.Bot()


@bot.event
async def on_ready():
    print(f"Bot has logged in!")


@bot.slash_command(guild_ids=[1081362341767168112])
@guild_only()
async def create_player(ctx, name, days, min_hour: discord.Option(int), max_hour: discord.Option(int), role):
    file = open("test_player.txt", "w")
    data = "Name: " + name
    data += "\nGuild: " + str(ctx.guild.id)
    data += "\nDays: " + str(days)
    data += "\nTimes: " + str([min_hour, max_hour])[1:-1]
    data += "\nRoles: " + role
    file.write(data)
    await ctx.respond(name + " is made!")


@bot.slash_command(guild_ids=[1081362341767168112])
@guild_only()
async def form_parties(ctx):
    file = open("players.txt", "w")
    member_list = sorter.set_members(file, ctx.guild)
    parties = sorter.create_parties(member_list)
    file = sorter.end_file(parties)

    await ctx.respond(file)


bot.run(os.getenv("TOKEN"))

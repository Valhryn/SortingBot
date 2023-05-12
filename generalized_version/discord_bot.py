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

@bot.slash_command(guild_ids=[os.getenv("GUILD_ID")])
@guild_only()
async def create_player(ctx, name, days, min_hour: discord.Option(int), max_hour: discord.Option(int), role):
    file = open("test_player.txt", "a+")
    data = "Name: " + name
    data += "\nGuild: " + str(ctx.guild.id)
    data += "\nDays: " + str(days)
    data += "\nTimes: " + str([min_hour, max_hour])[1:-1]
    data += "\nRoles: " + role
    file.write(data + "\n\n")
    await ctx.respond(name + " is made!")


@bot.slash_command(guild_ids=[os.getenv("GUILD_ID")])
@guild_only()
async def form_parties(ctx):
    file = open("test_player.txt", "r")
    member_list = sorter.set_members(file, ctx.guild.id)
    print("Length of member_list:",len(member_list))
    parties = sorter.create_parties(member_list)
    print("Amount of parties:",len(parties))
    output_file = sorter.end_file(parties)

    await ctx.respond(output_file.read())


bot.run(os.getenv("TOKEN"))

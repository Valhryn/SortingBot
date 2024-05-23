import os
import discord
from discord import guild_only
import dotenv
import sorter
import sqlite3

dotenv.load_dotenv()
token = str(os.getenv("TOKEN"))
players = sqlite3.connect("players.db") #Store character information
# groups = sqlite3.connect("groups.db") #Store who is in each group and related information (will not use rn, will write to server)
bot = discord.Bot()
database_access = players.cursor()

@bot.event
async def on_ready():
    print(f"Bot has logged in!")
    database_access.execute('CREATE TABLE IF NOT EXISTS characters(name TEXT, server INTEGER, days TEXT, min_hour INTEGER, max_hour INTEGER, role TEXT)')
    # For optimization, can query here for characters

@bot.slash_command(guild_ids=[os.getenv("GUILD_ID")])
@guild_only()
async def create_player(ctx, name, days, min_hour: discord.Option(int), max_hour: discord.Option(int), role):
    server = str(ctx.guild.id)
    list_of_days = str(days)

    character = (name, server, list_of_days, min_hour, max_hour, role)
    database_access.execute("INSERT INTO characters VALUES(?, ?, ?, ?, ?, ?)", character)
    players.commit()

    await ctx.respond(name + " is made!")

@bot.slash_command(guild_ids=[os.getenv("GUILD_ID")])
@guild_only()
async def form_parties(ctx):
    # file = open("players.txt", "w")
    # member_list = sorter.set_members(file, ctx.guild)
    # parties = sorter.create_parties(member_list)
    # file = sorter.end_file(parties)

    file = open("output.txt", "w")
    data = database_access.execute(f"SELECT * FROM characters WHERE server MATCH {ctx.guild}")
    file.write(data)
    file.close()
    # member_list = sorter.set_members()
    # parties = sorter.create_parties(member_list)
    # file = sorter.end_file(parties)

    await ctx.respond("Parties Created")

@bot.slash_command(guild_ids=[os.getenv("GUILD_ID")])
@guild_only()
async def get_players(ctx):
    await ctx.respond(database_access.execute(f"SELECT * FROM characters").fetchall())

@bot.slash_command(guild_ids=[os.getenv("GUILD_ID")])
@guild_only()
async def delete_player(ctx, name):
    delete_statement = "DELETE FROM characters WHERE name = ?"

    database_access.execute(delete_statement, (name,))
    players.commit()

    await ctx.respond(f"{name} has been deleted")

bot.run(os.getenv("TOKEN"))

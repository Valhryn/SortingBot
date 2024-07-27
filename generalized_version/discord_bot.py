import os
import discord
from discord import guild_only, default_permissions
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

@bot.slash_command()
@guild_only()
async def create_player(ctx, name, days, min_hour: discord.Option(int), max_hour: discord.Option(int), role):
    server = str(ctx.guild.id)
    list_of_days = str(days)

    character = (name, server, list_of_days, min_hour, max_hour, role)
    database_access.execute("INSERT INTO characters VALUES(?, ?, ?, ?, ?, ?)", character)
    players.commit()

    await ctx.respond(name + " is made!")

@bot.slash_command()
@guild_only()
async def form_parties(ctx):
    data = database_access.execute(f'SELECT * FROM characters WHERE server={ctx.guild.id}')
    augh = data.fetchall()
    member_list = sorter.set_members(augh)
    parties = sorter.create_parties(member_list)
    file = sorter.end_file(parties)

    await ctx.respond(f"{file}Parties Created")

@bot.slash_command()
@guild_only()
async def get_players(ctx):
    current_players = database_access.execute(f"SELECT * FROM characters").fetchall()
    response = "No players found"

    if current_players:
        response = current_players
    await ctx.respond(response)

@bot.slash_command()
@guild_only()
async def delete_player(ctx, name):
    delete_statement = "DELETE FROM characters WHERE name = ?"

    database_access.execute(delete_statement, (name,))
    players.commit()

    await ctx.respond(f"{name} has been deleted")

@bot.slash_command()
@guild_only()
@default_permissions(administrator=True)
async def clear_players(ctx):
    delete_statement = "DELETE FROM characters WHERE server = ?"
    database_access.execute(delete_statement, (ctx.guild.id, ))

    players.commit()
    await ctx.respond("All characters have been deleted")

bot.run(os.getenv("TOKEN"))

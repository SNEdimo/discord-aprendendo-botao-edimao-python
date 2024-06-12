import discord

bot = discord.client()

bot.run("token do bot vai aqui")

@bot.event
async def on_ready():
    print("Bot is Online")

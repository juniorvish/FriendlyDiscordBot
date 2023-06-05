import discord
from discord.ext import commands
from config import TOKEN
from openai_api import get_gpt_response

bot = commands.Bot(command_prefix="-")

@bot.event
async def on_ready():
    print(f"{bot.user.name} is online!")

@bot.command(name="gpt")
async def gpt(ctx, *, user_message):
    prompt = f"User: {user_message}\nAI Developer:"
    message = [
        {"role": "system", "content": "You are a friendly AI Developer"},
        {"role": "user", "content": prompt}
    ]

    gpt_message = get_gpt_response(message)
    await ctx.send(gpt_message)

bot.run(TOKEN)
from discord.ext import commands
import discord
import openai
from dotenv import load_dotenv
import os

# Load the discord bot TOKEN and OpenAI API key
load_dotenv("bots.env")
TOKEN = os.getenv("chatGPT_TOKEN")
openai.api_key = os.getenv("OPENAI_API_KEY")

# Create the bot
bot = commands.Bot(command_prefix="!",intents=discord.Intents.all())

# Prints that the bot has connected to Discord so that
# You can make sure everything started properly
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')

# One a command like !chatgpt, take the message and get a response
# From OpenAI's chatGPT.
@bot.command()
async def chatgpt(ctx, *, message_text: str):

  # Use the ChatGPT model to generate a response
  model_engine = "text-davinci-003"

  # The actual prompt sent to chatGPT
  prompt = (f"{ctx.message.author.name}: {message_text}\nBot: ")

  # Gets the response. See https://beta.openai.com/docs/api-reference/completions/create
  # For more details.
  completions = openai.Completion.create(
    engine=model_engine, 
    prompt=prompt, 
    max_tokens=1024, 
    n=1,
    stop=None,
    temperature=0.5)
  bot_response = completions.choices[0].text

  # Send the response to the channel
  await ctx.send(bot_response)


#Run the bot
bot.run(TOKEN)
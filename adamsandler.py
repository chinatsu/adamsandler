import discord
from discord.ext import commands
import traceback
import sys

bot = commands.Bot(command_prefix="!")
startup_extensions = ['divinity']

@bot.event
async def on_ready():
    print('Logged in as')
    print('------')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.event
async def on_command_error(exception, context):
    if type(exception) != commands.errors.CommandNotFound:
        traceback.print_exception(type(exception), exception, exception.__traceback__, file=sys.stderr)
        await bot.send_message(context.message.channel, exception)

@bot.event
async def on_message(message):
    await bot.process_commands(message)

if __name__ == "__main__":
    for ext in startup_extensions:
        try:
            bot.load_extension(ext)
        except Exception as e:
            exc = '{}: {}'.format(type(e).__name__, e)
            print('Failed to load extensions {}\n{}'.format(ext, exc))
    bot.run('get-your-own-token')

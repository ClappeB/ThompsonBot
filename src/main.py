import os
import _env

import discord
from bot import Bot


bot = Bot()
bot.add_channel(1022494749560684554, 'sandbox')
bot.run(os.environ.get('TOKEN'))


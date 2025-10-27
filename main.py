from javascript import require, On
import time

def ready(name, ip, server_port_over, game_version):
    mineflayer = require('mineflayer')
    pathfinder = require('mineflayer-pathfinder')

    RANGE_GOAL = 1
    BOT_USERNAME = name

    bot = mineflayer.createBot({
    'host': ip,
    'port': server_port_over,
    'username': BOT_USERNAME
    })



    bot.loadPlugin(pathfinder.pathfinder)
    print("Started mineflayer")

    @On(bot, 'spawn')
    def handle(*args):
        time.sleep(10*60*60)
        bot.quit()
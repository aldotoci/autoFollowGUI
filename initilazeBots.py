from data.userPasses import userPasses
from bot import Bot

def initialise():
    print("Program initializing ...")
    bots_list = []
    for userPass in userPasses:
        bots_list.append(Bot(userPass['username'], userPass['password']))

    return bots_list
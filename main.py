from data.convertData import usernamesToFollow
import datetime
from initilazeBots import initialise
import time

bots = initialise()

# bots[0].follow('hgleek.24')

def waitForTheRightTime():
    currHour = datetime.datetime.now().hour+4 
    if(currHour <= 7 and currHour >= 21):
        return
    else:
        time.sleep(0.1)

for index,username in enumerate(usernamesToFollow):
    start_time = time.time()
    for bot in bots:
        waitForTheRightTime()
        bot.follow(username)

def main():
    start_time = time.time()
    currentAcc = 0
    numOfTargetsDone = 0
    for index, username in enumerate(usernamesToFollow):
        waitForTheRightTime()
        bot[currentAcc].follow(username)
        if(currentAcc == len(bots)-1):
            currentAcc = 0
        else:
            currentAcc +=1

        if(numOfTargetsDone//len(bots) == 5): #Post per user
            time.sleep(60*60-int(time.time() - start_time))
            start_time = time.time()
        numOfTargetsDone += 1

main()
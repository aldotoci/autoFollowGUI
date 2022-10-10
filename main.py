from data.convertData import usernamesToFollow
import datetime
from initilazeBots import initialise
import time
import datetime

bots = initialise()

# bots[0].follow('hgleek.24')

waiting = True
def waitForTheRightTime():
    currHour = datetime.datetime.now().hour+4 
    while(currHour <= 7 or currHour >= 21):
        waiting = True
        time.sleep(1)
        return

def sleepUntilNextPosts(timeTosleep, start_time):
    if(timeTosleep > time.time() - start_time):
        time.sleep(1)
        print(str(datetime.timedelta(seconds=int(timeTosleep-int(time.time() - start_time)))), end="\r")
        sleepUntilNextPosts(timeTosleep, start_time)

def main():
    start_time = time.time()
    currentAcc = 0
    numOfTargetsDone = len(bots)
    for index, username in enumerate(usernamesToFollow):
        waitForTheRightTime()
        followed = bots[currentAcc].follow(username)
        if(followed):
            if(currentAcc == len(bots)-1):
                currentAcc = 0
            else:
                currentAcc +=1
            numOfTargetsDone += 1

        if((numOfTargetsDone//len(bots))%5 == 0): #Post per user
            timeTosleep = (60*60-int(time.time() - start_time))
            start_time = time.time()
            print('Sleeping Time left: ')
            sleepUntilNextPosts(timeTosleep, start_time)
            start_time = time.time()
            
main()
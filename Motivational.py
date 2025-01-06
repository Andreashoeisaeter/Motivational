import random
import datetime
import schedule
import time
import winsound

def messages():

    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)
    now = datetime.datetime.now()
    print(now)
    with open("Messages.txt") as f:
            lines = f.readlines()
    print(random.choice(lines))

messages()

my_schedule = schedule.Scheduler()
my_schedule.every(1).hours.do(messages)

while True:
    my_schedule.run_pending()
    time.sleep(1)


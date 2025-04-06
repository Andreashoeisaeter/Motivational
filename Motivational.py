import random
import datetime
import schedule
import time
import winsound
from colorama import init, Fore

init()

BLUE = Fore.BLUE
RESET = Fore.RESET
YELLOW = Fore.YELLOW

def messages():

    frequency = 2500
    duration = 1000
    winsound.Beep(frequency, duration)
    now = datetime.datetime.now()
    print(f"{BLUE}{now.strftime("%c")}{RESET}")
    with open("Messages.txt") as f:
            lines = f.readlines()
    print(f"{YELLOW}{random.choice(lines)}{RESET}")

messages()

my_schedule = schedule.Scheduler()
my_schedule.every(1).hours.do(messages)

while True:
    my_schedule.run_pending()
    time.sleep(1)




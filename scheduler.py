import time
import webbrowser
from random import choice

url = "https://www.youtube.com/"

breaks = int(input('How many breaks would you need today? '))
counter = 0
gap = int(input("How long should your pomodoro sessions be? (in minutes) "))*60

messages = ['Time for a break!', 'Break time!']

print("All work and no play makes Jack a dull boy!")

while counter < breaks:
    time.sleep(gap)
    print(choice(messages))
    webbrowser.open(url)
    counter += 1
print("Back to work buddy!")
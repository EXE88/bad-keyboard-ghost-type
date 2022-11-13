
from keyboard import press_and_release , write
from time import sleep
import sys

press_and_release("left windows + R")
sleep(0.5)
write("notepad")
sleep(0.5)
press_and_release("enter")
sleep(0.5)
list1 = ['g','h','o','s','t',' ','t','y','p','e','',':)']
for i in list1:
    write(i)
    sleep(0.7)
else:
    sys.exit()

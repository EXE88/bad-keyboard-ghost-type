
from keyboard import press_and_release , write
from time import sleep

command = "pip list"

press_and_release("left windows + R") # Press And Release WINDOWS + R -> OPEN Run
sleep(0.5)
write("cmd") # Write cmd on RUN
press_and_release("enter") # Press Enter For Open Cmd
sleep(0.5)
write(command) # write command in cmd
press_and_release("enter") # Run Command in cmd
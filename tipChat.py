# tipChat from Adventure 6

# Import required modules:
import mcpi.minecraft as minecraft
import time
import random

# connect to minecraft
mc = minecraft.Minecraft.create()

# Set a constant for the tips filename
FILENAME = "tips.txt"

# open the tips file:
f = open(FILENAME, "r")
# read all the tips into a list
tips = f.readlines()
# Close file when we're done with it
f.close()

# The game loop that waits a random length of time between 3 and 7 seconds:
while True:
    time.sleep(random.randint(3,7))
    msg = random.choice(tips)
    mc.postToChat(msg.strip())

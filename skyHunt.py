# A treasure hunting game

# Import required modules:
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import random

# Connect to Minecraft:
mc = minecraft.Minecraft.create()

# Initialise a score variable:
score = 0

# Set the number of blocks away from the player the treasure will be hidden:
RANGE = 5

# Initialise the coordinates of the treasure
treasure_x = None

def placeTreasure():
    print("placeTreasure")

def checkHit():
    print("checkHit")

def homingBeacon():
    print("homingBeacon")

bridge = []

def buildBridge():
    print("buildBridge")

while True:
    time.sleep(1)

    if treasure_x == None and len(bridge) == 0:
        placeTreasure()

    checkHit()
    homingBeacon()
    buildBridge()

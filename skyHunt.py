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
treasure_y = None
treasure_z = None

def placeTreasure():
    global treasure_x, treasure_y, treasure_z
    # Get the player's position
    pos = mc.player.getTilePos()
    # randomly place the  treasure no more than RANGE away.
    treasure_x = random.randint(pos.x, pos.x + RANGE)
    treasure_y = random.randint(pos.y +2, pos.y + RANGE)
    treasure_z = random.randint(pos.z, pos.z + RANGE)
    mc.setBlock(treasure_x, treasure_y, treasure_z, block.DIAMOND_BLOCK.id)

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

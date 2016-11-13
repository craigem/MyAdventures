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
    # Pull in the global variables that we need:
    global score
    global treasure_x
    # Check for hit events:
    events = mc.events.pollBlockHits()
    # Process each event:
    for e in events:
    # Get the hit coordinates:
        pos = e.pos
        # Check the position of the hit vs position of the treasure:
        if pos.x == treasure_x and pos.y == treasure_y and pos.z == treasure_z:
            mc.postToChat("HIT!")
            # Add points to score for hitting the treasure:
            score  = score + 10
            # Make the treasure disappear:
            mc.setBlock(treasure_x, treasure_y, treasure_z, block.AIR.id)
            treasure_x = None

# Create a timer variable that counts 10 loops of the game loop
TIMEOUT = 10
timer = TIMEOUT

# Define a function that displays the homing beacon on the Minecraft chat
def homingBeacon():
    global timer
    if treasure_x != None:
        timer = timer - 1
        if timer == 0:
            timer = TIMEOUT
            # Get the position of the player
            pos = mc.player.getTilePos()
            # Calculate a rough number that estimates distance to the treasure
            diffx = abs(pos.x - treasure_x)
            diffy = abs(pos.y - treasure_y)
            diffz = abs(pos.z - treasure_z)
            diff = diffx + diffy + diffz
            # Display score and estimate to treasure location on the Minecraft chat
            mc.postToChat("score: " + str(score) + " treasure: " + str(diff))

# initialise the bridge array
bridge = []

# Define a function to build a bridge of gold blocks
def buildBridge():
    # List the score variable as global
    global score
    # Get the position of the player
    pos = mc.player.getTilePos()
    # Get the id of the block directly below the player
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)

    # Has the treasure been found and deleted?
    if treasure_x == None:
        # Are there still blocks remaining in the gold bridge?
        if len(bridge) > 0:
            # Remove the last coordinate of the bridge from the bridge list
            coordinate = bridge.pop()
            # Delete that block of the bridge by setting it to AIR
            mc.setBlock(
                coordinate[0], coordinate[1], coordinate[2], block.AIR.id)
            # Display a helpful countdown message on the Minecraft chat
            mc.postToChat("bridge: " + str(len(bridge)))
            # Delay for a while, so that the bridge disappears slowly
            time.sleep(0.25)
    elif b != block.GOLD_BLOCK.id:
        # There is treasure, and you are not already standing on gold
        # build another gold block below your player
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GOLD_BLOCK.id)
        # Remember the coordinate of this new gold block...
        coordinate = [pos.x, pos.y - 1, pos.z]
        # ...by adding it to the end of the bridge list
        bridge.append(coordinate)
        # You loose one point for each block of the bridge that is built
        score = score - 1

while True:
    time.sleep(0.1)

    if treasure_x == None and len(bridge) == 0:
        placeTreasure()

    checkHit()
    homingBeacon()
    buildBridge()

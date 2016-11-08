# Sense when a block has been hit

# Import required modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# Obtain player position
diamond_pos = mc.player.getTilePos()

# Set the diamond slightly away from the player
diamond_pos.x = diamond_pos.x + 1

# Build the treasure block
mc.setBlock(
    diamond_pos.x, diamond_pos.y, diamond_pos.z,
    block.DIAMOND_BLOCK.id
    )

mc.postToChat("HIT that block!")


# function to check for right-click sword hits
def checkHit():
    # Check for hit events
    events = mc.events.pollBlockHits()
    # Process each event
    for e in events:
        # Get the hit coordinates
        pos = e.pos
        # Check the position of the hit vs position of the diamond
        if pos.x == diamond_pos.x and pos.y == diamond_pos.y and pos.z == diamond_pos.z:
            if e.face == 1:
                mc.postToChat("HIT on the top side!")
            elif e.face == 2:
                mc.postToChat("HIT on the North side!")
            elif e.face == 3:
                mc.postToChat("HIT on the South side!")
            elif e.face == 4:
                mc.postToChat("HIT on the West side!")
            elif e.face == 5:
                mc.postToChat("HIT on the East side!")
            else:
                mc.postToChat("HIT on the bottom side! (ooh-er)")

# Game loop
while True:
    time.sleep(1)
    checkHit()

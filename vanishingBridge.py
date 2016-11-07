# Keep the players feet on safely on a bridge

# import required modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# Initialise the bridge list
bridge = []

# The buildBridge function:
def buildBridge():
    # get the player's position
    pos = mc.player.getTilePos()
    # get the block under the player's feet
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)
    # Work out if the player is safe or not
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GLASS.id)
        coordinate = [pos.x, pos.y - 1, pos.z]
        bridge.append(coordinate)
    elif b != block.GLASS.id:
        if len(bridge) > 0:
            coordinate = bridge.pop()
            mc.setBlock(coordinate[0], coordinate[1],
                coordinate[2], block.AIR.id)
            time.sleep(0.25)

while True:
    time.sleep(0.25)
    buildBridge()

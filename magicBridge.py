# Keep the players feet on safely on a bridge

# import required modules
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# The buildBridge function:
def buildBridge():
    # get the player's position
    pos = mc.player.getTilePos()
    # get the block under the player's feet
    b = mc.getBlock(pos.x, pos.y - 1, pos.z)
    # Work out if the player is safe or not
    if b == block.AIR.id or b == block.WATER_STATIONARY.id or b == block.WATER_FLOWING.id:
        mc.setBlock(pos.x, pos.y - 1, pos.z, block.GLASS.id)

while True:
    buildBridge()

# Clear some space near you.

# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to Minecraft
mc = minecraft.Minecraft.create()

# Get your position:
pos = mc.player.getTilePos()

# Get the size of the space to clear
size = int(raw_input("Size of area to clear? ")) / 2

# Clear a space by setting it to AIR
mc.setBlocks(
    pos.x - size, pos.y - 2, pos.z - size,
    pos.x + size, pos.y + 100, pos.z + size,
    block.AIR.id
    )

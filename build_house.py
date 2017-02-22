""" Build a simple house. """

# Import necessary modules.
import MyAdventures.mcpi.minecraft as minecraft
import MyAdventures.mcpi.block as block

# Connect to Minecraft.
MC = minecraft.Minecraft.create()

# Set a base size for the house.
SIZE = 20

# Get your position:
POS = MC.player.getTilePos()

# Store your coordinates.
X = POS.x + 2
Y = POS.y
Z = POS.z

# Calculate the midpoints, used to position doors and windows.
MIDX = X + SIZE / 2
MIDY = Y + SIZE / 2

# Build the outer shell.
MC.setBlocks(
    X, Y, Z,
    X + SIZE, Y + SIZE, Z + SIZE,
    block.COBBLESTONE.id
    )

# Carve out the inside of the house.
MC.setBlocks(
    X + 1, Y, Z + 1,
    X + SIZE - 2, Y + SIZE - 1, Z + SIZE - 2,
    block.AIR.id
    )

# Carve out the doorway.
MC.setBlocks(
    MIDX - 1, Y, Z,
    MIDX + 1, Y + 3, Z,
    block.AIR.id
    )

# Carve out two windows.
MC.setBlocks(
    X + 3, Y + SIZE - 3, Z,
    MIDX - 3, MIDY + 3, Z,
    block.GLASS.id
    )
MC.setBlocks(
    MIDX + 3, Y + SIZE - 3, Z,
    X + SIZE - 3, MIDY + 3, Z,
    block.GLASS.id
    )

# Add the roof
MC.setBlocks(
    X, Y + SIZE + 1, Z,
    X + SIZE, Y + SIZE + 1, Z + SIZE,
    block.WOOD.id)

# Add some carpet
MC.setBlocks(
    X + 1, Y - 1, Z + 1,
    X + SIZE - 2, Y - 1, Z + SIZE - 2,
    block.WOOL.id, 14)

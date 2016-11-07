# Build a simple house.

# Import necessary modules.
import mcpi.minecraft as minecraft
import mcpi.block as block
import random

# Connect to Minecraft.
mc = minecraft.Minecraft.create()

# Set a base size for the house.
SIZE = 20

# Create the house function.
def house():

    # Calculate the midpoints, used to position doors and windows.
    midx = x + SIZE / 2
    midy = y + SIZE / 2

    # Build the outer shell.
    mc.setBlocks(
        x, y, z,
        x + SIZE, y + SIZE, z + SIZE,
        block.COBBLESTONE.id
        )

    # Carve out the inside of the house.
    mc.setBlocks(
        x + 1, y, z + 1,
        x + SIZE - 2, y + SIZE - 1, z + SIZE - 2,
        block.AIR.id
        )

    # Carve out the doorway.
    mc.setBlocks(
        midx - 1, y, z,
        midx + 1, y + 3, z,
        block.AIR.id
        )

    # Carve out two windows.
    mc.setBlocks(
        x + 3, y + SIZE - 3, z,
        midx - 3, midy + 3, z,
        block.GLASS.id
        )

    mc.setBlocks(
        midx + 3, y + SIZE - 3, z,
        x + SIZE - 3, midy + 3, z,
        block.GLASS.id
        )

    # Add the roof
    mc.setBlocks(
        x, y + SIZE + 1, z,
        x + SIZE, y + SIZE + 1, z + SIZE,
        block.WOOD.id
        )

    # Add some carpet
    c = random.randint(0, 15)
    mc.setBlocks(
        x + 1, y - 1, z + 1,
        x + SIZE - 2, y - 1, z + SIZE - 2,
        block.WOOL.id, c
        )

# Create the second house function.
def house2():

    # Calculate the midpoints, used to position doors and windows.
    midx = x + SIZE / 2
    midy = y + SIZE / 2

    # Build the outer shell.
    mc.setBlocks(
        x, y, z,
        x + SIZE, y + SIZE, z + SIZE,
        block.GLOWSTONE_BLOCK.id
        )

    # Carve out the inside of the house.
    mc.setBlocks(
        x + 1, y, z + 1,
        x + SIZE - 2, y + SIZE - 1, z + SIZE - 2,
        block.AIR.id
        )

    # Carve out the doorway.
    mc.setBlocks(
        midx - 1, y, z,
        midx + 1, y + 3, z,
        block.AIR.id
        )

    # Carve out two windows.
    mc.setBlocks(
        x + 3, y + SIZE - 3, z,
        midx - 3, midy + 3, z,
        block.GLASS.id
        )

    mc.setBlocks(
        midx + 3, y + SIZE - 3, z,
        x + SIZE - 3, midy + 3, z,
        block.GLASS.id
        )

    # Add the roof
    mc.setBlocks(
        x, y + SIZE + 1, z,
        x + SIZE, y + SIZE + 1, z + SIZE,
        block.WOOD.id
        )

    # Add some carpet
    c = random.randint(0, 15)
    mc.setBlocks(
        x + 1, y - 1, z + 1,
        x + SIZE - 2, y - 1, z + SIZE - 2,
        block.WOOL.id, c
        )

# Create the third house function.
def house3():

    # Calculate the midpoints, used to position doors and windows.
    midx = x + SIZE / 2
    midy = y + SIZE / 2

    # Build the outer shell.
    mc.setBlocks(
        x, y, z,
        x + SIZE, y + SIZE, z + SIZE,
        block.MOSS_STONE.id
        )

    # Carve out the inside of the house.
    mc.setBlocks(
        x + 1, y, z + 1,
        x + SIZE - 2, y + SIZE - 1, z + SIZE - 2,
        block.AIR.id
        )

    # Carve out the doorway.
    mc.setBlocks(
        midx - 1, y, z,
        midx + 1, y + 3, z,
        block.AIR.id
        )

    # Carve out two windows.
    mc.setBlocks(
        x + 3, y + SIZE - 3, z,
        midx - 3, midy + 3, z,
        block.GLASS.id
        )

    mc.setBlocks(
        midx + 3, y + SIZE - 3, z,
        x + SIZE - 3, midy + 3, z,
        block.GLASS.id
        )

    # Add the roof
    mc.setBlocks(
        x, y + SIZE + 1, z,
        x + SIZE, y + SIZE + 1, z + SIZE,
        block.WOOD.id
        )

    # Add some carpet
    c = random.randint(0, 15)
    mc.setBlocks(
        x + 1, y - 1, z + 1,
        x + SIZE - 2, y - 1, z + SIZE - 2,
        block.WOOL.id, c
        )

# Get your position:
pos = mc.player.getTilePos()

# Store your coordinates.
x = pos.x + 2
y = pos.y
z = pos.z

for h in range(5):
    c = random.randint(0, 2)
    if c == 0:
        house()
    elif c == 1:
        house2()
    else:
        house3()
    x = x + SIZE

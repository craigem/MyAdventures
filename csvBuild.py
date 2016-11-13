# csvBuild from Adventure 6.

# import required modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# connect to minecraft
mc = minecraft.Minecraft.create()

# define some constants
GAP = block.AIR.id
WALL = block.GOLD_BLOCK.id
FLOOR = block.GRASS.id

# Open the file containing maze data
FILENAME = "maze1.csv"
f = open(FILENAME, "r")

# Get the player position:
pos = mc.player.getTilePos()

# Work out coordinates for the bottom corner and avoid the player
ORIGIN_X = pos.x + 1
ORIGIN_Y = pos.y
ORIGIN_Z = pos.z + 1

# Initialise the z value
z = ORIGIN_Z

# Loop through every line in the maze file
for line in f.readlines():
    # Remove pesky new lines and any other unwanted whitespace
    line = line.rstrip()
    # split the line every time a comma is reached
    data = line.split(",")
    # reset the x coordinate
    x = ORIGIN_X
    # draw the whole row
    for cell in data:
        # Differentiate between gap and wall
        if cell == "0":
            b = GAP
        else:
            b = WALL
        # build the wall
        mc.setBlock(x, ORIGIN_Y, z, b)
        mc.setBlock(x, ORIGIN_Y + 1, z, b)
        mc.setBlock(x, ORIGIN_Y - 1, z, FLOOR)
        # Update x for the next cell
        x = x + 1
    # update z for the next row
    z = z + 1

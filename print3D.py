# 3D Printer from Adventure 6

# Import required modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Create a connection to Minecraft
mc = minecraft.Minecraft.create()

# Create a constant for the data file
FILENAME = "object01.csv"


# Define the print3D funtion
def print3D(filename, originx, originy, originz):
    # Open the file in readonly mode
    f = open(filename, "r")
    lines = f.readlines()

    # Split the coordinates
    coords = lines[0].split(",")
    sizex = int(coords[0])
    sizey = int(coords[1])
    sizez = int(coords[2])

    # Set a lineidx variable to remember the index of the line
    lineidx = 1

    for y in range(sizey):
        # Print the progress of the printing
        mc.postToChat(str(y))

        # Skip the blank line by incrementing lineidx
        lineidx = lineidx + 1

        # Read the next line and split on a comma
        for x in range(sizex):
            line = lines[lineidx]
            lineidx = lineidx + 1
            data = line.split(",")

            # Scan the lines and build them in Minecraft
            for z in range(sizez):
                blockid = int(data[z])
                mc.setBlock(originx + x, originy + y, originz + z, blockid)


# Read the player position
pos = mc.player.getTilePos()

# Print just to the side of where you're standing
print3D(FILENAME, pos.x + 1, pos.y, pos.z + 1)

# Import required modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to the game
mc = minecraft.Minecraft.create()

# Create constants for the CSV file and the area to scan.
FILENAME = "tree.csv"
SIZEX = 5
SIZEY = 5
SIZEZ = 5

def scan3D(filename, originx, originy, originz):
    # Open the file in write mode
    f = open(filename, "w")
    # Write the metadata
    f.write(str(SIZEX) + "," + str(SIZEY) + "," + str(SIZEZ) + "\n")
    # Scan blocks in the area specified in SIZEX|Y|Z
    for y in range(SIZEY):
        f.write("\n")
        for x in range(SIZEX):
            line = ""
            for z in range(SIZEZ):
                blockid = mc.getBlock(originx + x, originy + y, originz + z)
                if line != "":
                    line = line + ","
                line = line + str(blockid)
            f.write(line + "\n")
        f.close()

# Read the player position
pos = mc.player.getTilePos()

# Run the 3D scanner
scan3D(FILENAME, pos.x - (SIZEX/2), pos.y, pos.z - (SIZEZ / 2))

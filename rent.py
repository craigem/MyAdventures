import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

X1 = 24
Z1 = -19
X2 = 34
Z2 = -9

rent = 0

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()
    if pos.x>X1 and pos.x<X2 and pos.z>Z1 and pos.z<Z2:
        rent = rent + 1
        mc.postToChat("You owe rent: " + str(rent))

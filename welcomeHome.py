import mcpi.minecraft as minecraft
import time

mc = minecraft.Minecraft.create()

while True:
    time.sleep(1)
    pos = mc.player.getTilePos()

    if pos.x == 59 and pos.y == -1 and pos.z == -11:
        mc.postToChat("Welcome home!")

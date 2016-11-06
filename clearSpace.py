import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()

pos = mc.player.getTilePos()
size = int(raw_input("Size of area to clear? "))

mc.setBlocks(
    pos.x, pos.y, pos.z, pos.x + size, pos.y + size, pos.z + size, block.AIR.id)

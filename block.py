""" Set a block in minecraft """

import MyAdventures.mcpi.minecraft as minecraft
import MyAdventures.mcpi.block as block

MC = minecraft.Minecraft.create()

POS = MC.player.getTilePos()

MC.setBlock(POS.x + 3, POS.y, POS.z, block.STONE.id)

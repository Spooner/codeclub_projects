from mcpi import minecraft, block
mc=minecraft.Minecraft.create()
mc.postToChat("BOOGI")

x, y, z = mc.player.getPos()
print(dir(block))
mc.setBlocks(x+3, y, z, x+13, y+5, z+5, block.LAPIS_LAZULI_BLOCK.id)
mc.setBlocks(x+4, y+1, z+1, x+12, y+5, z+4, block.WATER_STATIONARY.id)
from mcpi import minecraft, block
mc=minecraft.Minecraft.create()
mc.postToChat("BOOGI")

mc.setBlock(x+6, y+1, z+1, block.PUMPKIN.id)
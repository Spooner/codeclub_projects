from mcpi import minecraft, block

mc = minecraft.Minecraft.create()

print "Sending hello..."
mc.postToChat("Hello")

x, y, z = mc.player.getPos()

mc.setBlock(x + 3, y, z, block.STONE.id)

mc.setBlocks(x + 1, y + 1, z + 1, x + 11, y + 11, z + 11, block.TNT.id)
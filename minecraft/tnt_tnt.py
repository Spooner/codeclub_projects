from mcpi import minecraft, block

mc = minecraft.Minecraft.create()

print("Sending hello...")
mc.postToChat("Hello")

x, y, z = mc.player.getPos()

mc.setBlock(x + 1, y + 1, z + 1, x + 1, y + 1, z + 1, 1)
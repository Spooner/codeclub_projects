from mcpi import minecraft, block
mc=minecraft.Minecraft.create()
mc.postToChat("BOOGI")

x, y, z = mc.player.getPos()
print(dir(block))

def make_corridor(x, y, z, width=4, height=4, depth=10):
    mc.setBlocks(x, y, z, x+width+2, y+height, z+depth, block.STONE_BRICK.id) # outside
    mc.setBlocks(x+1, y+1, z+1, x+width-1, y+height-1, z+depth-1, block.AIR.id)
    
    mc.setBlocks(x, y+1, z+depth/2-1, x+width, y+2, z+depth/2+1, block.AIR.id)
    mc.setBlocks(x+width/2-1, y+1, z, x+width/2+1, y+2, z+depth, block.AIR.id)
    
    mc.setBlock(x+1, y+height, z+depth, block.AIR.id)
    mc.setBlock(x+width-1, y, z+1, block.TORCH.id)
    mc.setBlock(x+width+3, y, z+1, block.TORCH.id)
    mc.setBlock(x+width+3, y, z+depth, block.TORCH.id)

#make_corridor(x, y, z)
make_corridor(x + 10, y, z)
#make_corridor(x + 20, y, z)
#make_corridor(x + 30, y, z)
#make_corridor(x + 40, y, z)
#make_corridor(x + 50, y, z)
#make_corridor(x + 60, y, z)
#make_corridor(x + 70, y, z)
#make_corridor(x + 80, y, z)
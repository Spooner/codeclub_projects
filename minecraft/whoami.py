from mcpi.minecraft import Minecraft
from mcpi import block

mc = Minecraft.create()
        
mc.postToChat('Python connected!')
pos = mc.player.getPos()
print('Player at: %s' % pos)

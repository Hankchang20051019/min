# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:47:31 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()
x,y,z=Hank.player.getTilePos()
a=Hank.getBlock(x+1,y,z)
b=Hank.getBlock(x-1,y,z)
c=Hank.getBlock(x,y,z-1)
d=Hank.getBlock(x,y,z-2)

if a==8 or a==9 or b==8 or b==9 or c==8 or c==9 or d==8 or d==9:
    Hank.setBlock(x+1,y-1,z+1,x-1,y-1,z-1)

# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 15:40:19 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

x,y,z=Hank.player.getTilePos()

Hank.setblocks(x-1,y+3,z-1,x+1,y+5,z+1,161)
Hank.setBlock(x,y,z,x,y+4,z,17)
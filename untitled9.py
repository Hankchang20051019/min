# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 14:39:47 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

x,y,z=Hank.player.getTilePos()

for i in range(50):
    Hank.setBlock(x+i,y-1,z+i,1)
    Hank.setBlock(x+i,y-1,z+i+1,1)
    Hank.setBlock(x+i+1,y-1,z+i,1)
    
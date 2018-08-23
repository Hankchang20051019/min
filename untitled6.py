# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 15:34:26 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

x,y,z=Hank.player.getTilePos()

a = 0
while a<50:
    Hank.setBlocks(x,y-1,z+30,x,y-30,z-30,19)
    x=x+5
    a=a+1
    
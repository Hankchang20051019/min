# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 09:33:40 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()
time.sleep(3)
x,y,z=Hank.player.getTilePos()
while y<=101:
    Hank.setBlock(x,y-1,z,42)
    time.sleep(0.3)
    Hank.setBlock(x+1,y-1,z,42)
    time.sleep(0.3)
    Hank.setBlock(x+2,y-1,z,42)
    time.sleep(0.3)
    Hank.setBlock(x+2,y-1,z-1,42)
    time.sleep(0.3)
    Hank.setBlock(x+2,y-1,z-2,42)
    time.sleep(0.3)
    Hank.setBlock(x+1,y-1,z-2,42)
    time.sleep(0.3)
    Hank.setBlock(x,y-1,z-2,42)
    time.sleep(0.3)
    Hank.setBlock(x,y-1,z-1,42)
    time.sleep(0.3)
    y=y+1
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 14:29:00 2018

@author: NTPU
"""

import time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()
while True:
    import time
from mcpi.minecraft import Minecraft
x,y,z=Hank.player.getTilePos()
    Hank.setBlock(x,y,z,11)
    time.sleep(0.5)
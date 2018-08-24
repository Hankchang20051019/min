e# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 11:26:29 2018

@author: NTPU
"""
import random
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

x,y,z=Hank.player.getTilePos()
for i in range(20):
    r=random.randrange(1,7)
    c=random.randrange(1,16)
    l=random.randrange(2,16)
    if r==1:
        Hank.setblock(x,y,z,x+l,y,z,35,c)
        x=x+l
    elif r==2:
        Hank.setblock(x,y,z,x-l,y,z,35,c)
        x=x-l
    elif r==3:
        Hank.setblock(x,y,z,x,y,z+l,35,c)
        z=z+l
    elif r==4:
        Hank.setblock(x,y,z,x,y,z-l,35,c)
        z=z-l
    elif r==5:
        Hank.setblock(x,y-l,z,x,y,z,35,c)
        y=y-l
    elif r==6:
        Hank.setblock(x,y+l,z,x,y,z,35,c)
        y=y-l
    elif r==7:
        Hank.setblock(x,y+l,z,x,y,z,35,c)
        y=y-l
    elif r==8:
        Hank.setblock(x,y+l,z,x,y,z,35,c)
        y=y-l
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 11:00:55 2018

@author: NTPU
"""
from random import randrange
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

list2=[[1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],
       [1,1,1,1,1,1,1,1,1,1,1],]
myID=Hank.getPlayerEntityId(Hank)
x,y,z=Hank.entity.getTilePos(myID)
H=x
for list1 in list2:
    for i in list1:
        Hank.setBlock(x,y,z,i)
        x=x+1
    H=x
    z=z+1

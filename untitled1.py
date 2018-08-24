# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:43:10 2018

@author: NTPU
"""

from random import choice
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

list2=[[103,41,14]
       ,[35,73,86]]
myID=Hank.getPlayerEntityId("Hank")
x,y,z=Hank.player.getTilePos(myID)
H=x
for list1 in list2:
    for i in list1:
        Hank.setBlock(x,y,z,i)
        x=x+1
    H=x
    z=z+1
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 10:14:11 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()



x,y,z=Hank.player.getTilePos()

width=80
length=40
height=8

block=5
air=0

Hank.setBlocks(x,y,z,x+width,y+height,z+length,block)
Hank.setBlocks(x+1,y+1,z+1,x+width-1,y+height-1,z+length-1,air)

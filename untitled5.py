# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:13:14 2018

@author: NTPU
"""
from random import randrange
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()



for j in range(10):
    x,y,z=Hank.player.getTilePos()
    x=x+j
    for i in range(10):
        r=randrange(0,16)
        Hank.setBlock(x,y,z,35,r)
        z=z+1
Hank.postToChat("")
r=randrange(0,16)
while True:
    hit = Hank.events.pollBlockHits()
    if len(hit)>0:
        h=hit[0]
        
        block=Hank.getBlockWithData(h.pos)
        date=block.data
    if date==r:
        Hank.postToChat("恭喜你找到了")
        Hank.setBlock(h.pos,57)
    elif date<r:
        Hank.postToChat("找錯了!!要找更大的")
    elif date>r:
        Hank.postToChat("找錯了!!要找更小的")
        
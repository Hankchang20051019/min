# -*- coding: utf-8 -*-
"""
Created on Tue Aug 21 16:06:49 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

while True:
    x,y,z=Hank.player.getTilePos()
    try:
        block=int(input("請輸入方塊ID:"))
        Hank.setBlock(x,y,z,block)
    except:
dw adwa        Hank.postToChat("只能夠輸入數字!!!!!!!!!")
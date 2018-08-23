# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 09:17:50 2018

@author: NTPU
"""

mc.setBlocks(x1, y1, z1, x2, y1, z2, 24)


def a(x,y,z,base=18):
    
    height = (base//2)+1

    for i in range(height):
        x1 = x + i
        y1 = y + i
        z1 = z + i
        
        x2 = x + base - i
        #y與y2相同
        z2 = z + base - i
        mc.setBlocks(x1, y1, z1, x2, y1, z2, 24)
        if i!=0 and i!=height-1:e
            mc.setBlocks(x1+1, y1, z1+1, x2-1, y1, z2-1, 24)
        
x,y,z = mc.player.getTilePos()
a(x,y,z,30)

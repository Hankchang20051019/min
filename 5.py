# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 09:44:01 2018

@author: NTPU
"""

from mcpi.minecraft import Minecraft
Hank=Minecraft.create()
while True:
    hits = Hank.events.pollProjectileHits()
    if len(hits)>0:
        hit = hits[0]
        x,y,z = hit.pos.x,hit.pos.y,hit.pos.z
        Hank.createExplosion(x,y,z,100)

# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 14:17:38 2018

@author: NTPU
"""
import time
from mcpi.minecraft import Minecraft
Hank=Minecraft.create()

while True:
    Hank.executeCommand("time add 10")
    time.sleep(0.01)
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 22:15:44 2017

@author: Pedro da Luz
"""

import pygame, random
from game import my

class EventHandler:
    """Classe para lidar com os eventos do jogo"""
    def __init__(self):
        pass
    
    def update(self):
        """Roda a cada frame do jogo"""
        my.input.get()
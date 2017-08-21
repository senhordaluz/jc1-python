# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:59:46 2017

@author: Pedro da Luz
"""

import pygame
from pygame.locals import *
from game import input
from game import my
from game import Background
from game import event

class Engine:
    """Roda o jogo"""
    def __init__(self):
        my.jogoRodando = True
        my.pause = False
        my.input = input.Input()
        my.event = event.EventHandler()
        
        my.screen = pygame.display.set_mode(my.SIZE)
        
        self.background = Background.Imagem_de_Fundo()
        
        
    def update(self):
        my.event.update()
        
        my.FASE.update()
        
        pygame.display.update()
        my.FPSCLOCK.tick(my.FPS)
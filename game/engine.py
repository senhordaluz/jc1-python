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
from game import sound

class Engine:
    """Roda o jogo"""
    def __init__(self):
        my.jogoRodando = True
        my.pause = False
        my.input = input.Input()
        my.event = event.EventHandler()
        
        my.screen = pygame.display.set_mode(my.SIZE)
        
        Background.Inicializa_Fase()
        
        sound.fase_01()
        
        
    def update(self):
        """Roda uma vez a cada frame do jogo"""
        my.event.update()
        
        my.FASE.update()
        my.FASE.draw(my.screen)
        
        pygame.display.update()
        my.FPSCLOCK.tick(my.FPS)
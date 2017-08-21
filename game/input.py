# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:47:46 2017

@author: Pedro da Luz
"""

import pygame, sys
from game import my
from pygame.locals import *

class Input:
    """Classe para lidar com todas as entradas de input"""
    def __init__(self):
        self.pressedKeys = []
        self.mousePressed = False
        self.mouseUnpressed = False
        self.mousePos = (0,0)
        
    def get(self):
        """Atualiza variaveis"""
        self.checkForQuit()
        self.checkResize()
        self.mouseUnpressed = False
        self.unpressedKeys = []
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.event.post(event)
            elif event.type == KEYDOWN:
                self.pressedKeys.append(event.key)
            elif event.type == KEYUP:
                for key in self.pressedKeys:
                    if event.key == key:
                        self.pressedKeys.remove(key)
                    self.unpressedKeys.append(key)
            elif event.type == MOUSEMOTION:
                self.mousePos = event.pos
            elif event.type == MOUSEBUTTONDOWN:
                self.mousePressed = event.button
                self.mouseUnpressed = False
            elif event.type == MOUSEBUTTONUP:
                self.mousePressed = False
                self.mouseUnpressed = event.button
            elif event.type == VIDEORESIZE:
                pygame.event.post(event)
        
    def checkForQuit(self):
        """Fecha"""
        for event in pygame.event.get(QUIT): # get all the QUIT events
            self.terminate() # terminate if any QUIT events are present
        for event in pygame.event.get(KEYUP): # get all the KEYUP events
            if event.key == K_ESCAPE:
                self.terminate() # terminate if the KEYUP event was for the Esc key
            pygame.event.post(event) # put the other KEYUP event objects back
    
    def checkResize(self):
        """Redimenciona a tela"""
        for event in pygame.event.get(VIDEORESIZE):
            if event.type == VIDEORESIZE:
                my.screen = pygame.display.set_mode(
                        event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                my.SIZE = my.screen.get_size()
        
    def terminate(self):
        """Fecha o jogo"""
        my.jogoRodando = False
        pygame.quit()
        sys.exit()
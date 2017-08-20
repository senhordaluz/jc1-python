# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:18:21 2017

@author: Pedro da Luz
"""
import pygame

from game import SIZE, SCREEN_WIDTH, SCREEN_HEIGHT

class Imagem_de_Fundo(pygame.sprite.Sprite):
    """Classe para instanciar o sprite do plano de fundo"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fase = 1
        self.image = pygame.image.load(self._get_image())
        self.image = pygame.transform.scale(self.image, SIZE)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0,0]
    
    def _get_image(self):
        from game import ARTE_MAPAS_PATH
        if self.fase == 1:
            mapa = ''.join([ARTE_MAPAS_PATH, 'fundo01.jpg'])
        elif self.fase == 2:
            mapa = ''.join([ARTE_MAPAS_PATH, 'fundo02.jpg'])
        elif self.fase == 3:
            mapa = ''.join([ARTE_MAPAS_PATH, 'fundo03.jpg'])
        elif self.fase == 4:
            mapa = ''.join([ARTE_MAPAS_PATH, 'fundoB1.jpg'])
        else:
            mapa = ''.join([ARTE_MAPAS_PATH, 'fundo01.jpg'])
        return mapa
    
    def _troca_fase(self):
        self.image = pygame.image.load(self._get_image())
        self.image = pygame.transform.scale(self.image, SIZE)
        
    def proxima_fase(self):
        if self.fase == 4:
            self.fase = 1
        else:
            self.fase += 1
        self._troca_fase()
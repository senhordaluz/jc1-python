# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:18:21 2017

@author: Pedro da Luz
"""
import pygame
from game import my

my.FASES = ['Primeira Fase', 'Segunda Fase', 'Terceira Fase', 'Boss']
my.FASE = pygame.sprite.Group()

class Imagem_de_Fundo(pygame.sprite.Sprite):
    """Classe para instanciar o sprite do plano de fundo"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.fase = 1
        self.image = pygame.image.load(self._get_image())
        self.image = pygame.transform.scale(self.image, my.SIZE)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = [0,0]
        self.add(my.FASE)
    
    def _get_image(self):
        if self.fase == 1:
            mapa = ''.join([my.ARTE_MAPAS_PATH, 'fundo01.jpg'])
        elif self.fase == 2:
            mapa = ''.join([my.ARTE_MAPAS_PATH, 'fundo02.jpg'])
        elif self.fase == 3:
            mapa = ''.join([my.ARTE_MAPAS_PATH, 'fundo03.jpg'])
        elif self.fase == 4:
            mapa = ''.join([my.ARTE_MAPAS_PATH, 'fundoB1.jpg'])
        else:
            mapa = ''.join([my.ARTE_MAPAS_PATH, 'fundo01.jpg'])
        return mapa
    
    def _troca_fase(self):
        self.image = pygame.image.load(self._get_image())
        self.image = pygame.transform.scale(self.image, my.SIZE)
        
    def proxima_fase(self):
        if self.fase == 4:
            self.fase = 1
        else:
            self.fase += 1
        self._troca_fase()
    
    def update(self):
        my.screen.blit(self.image, self.rect)
        self.proxima_fase()
        
class Portal(pygame.sprite.Sprite):
    """Classe para instanciar os portais da fase
        tipo: cima, baixo, esquerda, direita"""
    def __init__(self, tipo):
        pygame.sprite.Sprite.__init__(self)
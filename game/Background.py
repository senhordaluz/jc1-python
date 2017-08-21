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
        try:
            self.image = pygame.image.load(self._get_image())
        except (pygame.error):
            print('Falha ao carregar imagem:', self._get_image())
            raise SystemExit
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
        self.proxima_fase()
        
class Portal(pygame.sprite.Sprite):
    """Classe para instanciar os portais da fase
        tipo: cima, baixo, esquerda, direita"""
    def __init__(self, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.fase = 1
        self.tipo = tipo
        try:
            self.image = pygame.image.load(self._get_image())
        except (pygame.error):
            print('Falha ao carregar imagem:', self._get_image())
            raise SystemExit
        self.rect = self.image.get_rect()
        self._posiciona_portal()
        self.add(my.FASE)
        
    def _get_image(self):
        if self.fase == 1:
            if self.tipo == 'baixo':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'vermelho_baixo.png'])
            elif self.tipo == 'cima':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'vermelho_cima.png'])
            elif self.tipo == 'esquerda':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'vermelho_esquerda.png'])
            elif self.tipo == 'direita':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'vermelho_direita.png'])
        elif self.fase == 2:
            if self.tipo == 'baixo':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'azul_baixo.png'])
            elif self.tipo == 'cima':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'azul_cima.png'])
            elif self.tipo == 'esquerda':
              portal = ''.join([my.ARTE_PORTAL_PATH, 'azul_esquerda.png'])
            elif self.tipo == 'direita':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'azul_direita.png'])
        elif self.fase == 3:
            if self.tipo == 'baixo':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'cinza_baixo.png'])
            elif self.tipo == 'cima':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'cinza_cima.png'])
            elif self.tipo == 'esquerda':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'cinza_esquerda.png'])
            elif self.tipo == 'direita':
                portal = ''.join([my.ARTE_PORTAL_PATH, 'cinza_direita.png'])
        return portal
    
    def _posiciona_portal(self):
        if self.tipo == 'cima':
            self.rect.left, self.rect.top = [80,50]
            self.rect.x, self.rect.y = [362,0]
            pass
        elif self.tipo == 'baixo':
            self.rect.left, self.rect.top = [59,30]
            self.rect.x, self.rect.y = [362,550]
            pass
        elif self.tipo == 'esquerda':
            self.rect.left, self.rect.top = [30,59]
            self.rect.x, self.rect.y = [0,0]
            pass
        elif self.tipo == 'direita':
            self.rect.left, self.rect.top = [30,59]
            self.rect.x, self.rect.y = [0,0]
            pass
        
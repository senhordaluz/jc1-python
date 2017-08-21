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
        self.proxima_fase()
        
class Portal(pygame.sprite.Sprite):
    """
        Classe para instanciar os portais da fase
        tipo: cima, baixo, esquerda, direita"""
    def __init__(self, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.fase = 1
        self.tipo = tipo
        '''try:
            self.sheet = pygame.image.load(self._get_image_sheet())
        except (pygame.error):
            print('Falha ao carregar imagem:', self._get_image_sheet())
            raise SystemExit
        self.rect = self.sheet.get_rect()
        self.sheetRect = self.sheet.get_rect()
        self._posiciona_portal()
        self.image = pygame.Surface(self.sheetRect.size).convert()
        self.image.blit(self.sheet, (0,0), self.sheetRect)'''
        self.spritesheet = spritesheet(self._get_image_sheet())
        self.image = self.spritesheet.image_at([0,0,59,30], -1)
        self.rect = self.image.get_rect()
        self.sheetRect = self.image.get_rect()
        self._posiciona_portal()
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.add(my.FASE)
        
    def _get_image_sheet(self):
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
            self.sheetRect.left, self.rect.top = [59,30]
            self.sheetRect.x, self.rect.y = [0,0]

        elif self.tipo == 'baixo':
            self.rect.left, self.rect.top = [80,50]
            self.rect.x, self.rect.y = [362,550]
            self.sheetRect.left, self.rect.top = [59,30]
            self.sheetRect.x, self.rect.y = [0,0]

        elif self.tipo == 'esquerda':
            self.rect.left, self.rect.top = [50,80]
            self.rect.x, self.rect.y = [0,0]
            self.sheetRect.left, self.rect.top = [30,59]
            self.sheetRect.x, self.rect.y = [0,0]

        elif self.tipo == 'direita':
            self.rect.left, self.rect.top = [50,80]
            self.rect.x, self.rect.y = [0,0]
            self.sheetRect.left, self.rect.top = [30,59]
            self.sheetRect.x, self.rect.y = [0,0]
            pass
        
    def update(self):
        pass
    

class spritesheet(object):
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()

    # Load a specific image from a specific rectangle
    def image_at(self, rectangle, colorkey = None):
        "Loads image from x,y,x+offset,y+offset"
        rect = pygame.Rect(rectangle)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        "Loads multiple images, supply a list of coordinates" 
        return [self.image_at(rect, colorkey) for rect in rects]
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
        
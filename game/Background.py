# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 19:18:21 2017

@author: Pedro da Luz
"""
import pygame
from game import my
from game import camera

my.FASES = ['Primeira Fase', 'Segunda Fase', 'Terceira Fase', 'Boss']
my.FASE = pygame.sprite.Group()

def Inicializa_Fase():
    """Carrega todos os elementos basicos da fase no
        grupo de sprites salvo em my.FASE"""
    background = Imagem_de_Fundo()
    portalCima = Portal('cima')
    portalBaixo = Portal('baixo')
    portalEsquerda = Portal('esquerda')
    portalDireita = Portal('direita')

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
    
    def update(self):
        """Roda a cada frame do jogo"""
        self.image = pygame.transform.scale(self.image, my.SIZE)
        ##self.proxima_fase()
        pass
    
    def _get_image(self):
        """Retorna local do arquivo do mapa"""
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
        """Troca o arquivo de imagem do fundo da tela para o
            da próxima fase"""
        self.image = pygame.image.load(self._get_image())
        self.image = pygame.transform.scale(self.image, my.SIZE)
        
    def proxima_fase(self):
        """Carrega próxima fase"""
        if self.fase == 4:
            self.fase = 1
        else:
            self.fase += 1
        self._troca_fase()
        
class Portal(pygame.sprite.Sprite):
    """
        Classe para instanciar os portais da fase
        tipo: cima, baixo, esquerda, direita
    """
    def __init__(self, tipo):
        pygame.sprite.Sprite.__init__(self)
        self.fase = 2
        self.tipo = tipo

        self.spritesheet = camera.SpriteSheet(self._get_image_sheet())
        self._posiciona_portal()
        
        self.image = self.spritesheet.image
        
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.add(my.FASE)
        
    def update(self):
        """Roda a cada frame do jogo"""
        self._troca_sprite()
        self.image = self.spritesheet.image
        self.redimencionar()
        self.image = pygame.transform.scale(self.image, self.rect.size)
        
    def _get_image_sheet(self):
        """Retorna local do arquivo do portal"""
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
        """Salva o rect com a posição do portal em tela
            além da posição a ser cortada no spritesheet
        """
        self._set_sheetRect()
        self.redimencionar()
            
    def _troca_sprite(self):
        """Troca o sprite de animação do portal"""
        if self.tipo == 'cima' or self.tipo == 'baixo':
            if self.spritesheet.rect.x >= 413:
                self.spritesheet.rect.x = 0
            
            else:
                self.spritesheet.rect.x += 59
            
        elif self.tipo == 'esquerda' or self.tipo == 'direita':
            if self.spritesheet.rect.y >= 413:
                self.spritesheet.rect.y = 0
            
            else:
                self.spritesheet.rect.y += 59
    
    def _set_sheetRect(self):
        if self.tipo == 'cima':
            self.spritesheet.rect = pygame.Rect(0,0,59,30)

        elif self.tipo == 'baixo':
            self.spritesheet.rect = pygame.Rect(0,0,59,30)

        elif self.tipo == 'esquerda':
            self.spritesheet.rect = pygame.Rect(0,0,30,59)

        elif self.tipo == 'direita':
            self.spritesheet.rect = pygame.Rect(0,0,30,59)
            
    def redimencionar(self):
        """Redimenciona o tamanho do portal para se adaptar
            ao tamanho da tela"""
        width, height = my.SIZE
        x = width/800
        y = height/600
        if self.tipo == 'cima':
            self.rect = pygame.Rect(362*x,0*y,80*x,50*y)

        elif self.tipo == 'baixo':
            self.rect = pygame.Rect(362*x,550*y,100*x,50*y)

        elif self.tipo == 'esquerda':
            self.rect = pygame.Rect(0*x,285*y,70*x,50*y)

        elif self.tipo == 'direita':
            self.rect = pygame.Rect(728*x,265*y,70*x,55*y)
            
    def _troca_fase(self):
        """Troca o arquivo de imagem do portal para o
            da próxima fase"""
        self.spritesheet = camera.SpriteSheet(self._get_image_sheet())
        self._set_sheetRect()
        self.image = self.spritesheet.image
        self.image = pygame.transform.scale(self.image, self.rect.size)
        
    def proxima_fase(self):
        """Carrega o portal da proxima fase"""
        if self.fase == 3:
            self.fase = 1
        else:
            self.fase += 1
        self._troca_fase()
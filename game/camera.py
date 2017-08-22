# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 22:33:58 2017

@author: Pedro da Luz
"""

import pygame

class SpriteSheet(object):
    """
        Classe para lidar com sprites animados
        reatangulo = (x, y, x + offset, y + ofset)
    """
    def __init__(self, filename):
        self.sheet = pygame.image.load(filename).convert()
    
    @property
    def rect(self):
        """Retorna rect da posição a ser cordada do sprite"""
        return self._rect
    
    @rect.setter
    def rect(self, value):
        """Grava rect da posição a ser cordata do sprite"""
        self._rect = value
    
    @property
    def image(self):
        """Retorna a imagem cortada a partir do rect salvo na classe"""
        return self.image_at(self.rect, -1)

    # Load a specific image from a specific rectangle
    def image_at(self, retangulo, colorkey = None):
        """Loads image from x,y,x+offset,y+offset"""
        rect = pygame.Rect(retangulo)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, pygame.RLEACCEL)
        return image
    
    # Load a whole bunch of images and return them as a list
    def images_at(self, rects, colorkey = None):
        """Loads multiple images, supply a list of coordinates"""
        return [self.image_at(rect, colorkey) for rect in rects]
    
    # Load a whole strip of images
    def load_strip(self, rect, image_count, colorkey = None):
        "Loads a strip of images and returns them as a list"
        tups = [(rect[0]+rect[2]*x, rect[1], rect[2], rect[3])
                for x in range(image_count)]
        return self.images_at(tups, colorkey)
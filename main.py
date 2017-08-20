# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:39:56 2017

@author: Pedro da Luz
"""
import pygame, game
from pygame.locals import *
from sys import exit
from game import Sprite

import configparser
config = configparser.ConfigParser()
config.read('data/config.ini')
fps = config.getint('DEFAULT', 'FPS')
size = width, height = config.getint('DEFAULT', 'SCREEN_WIDTH'), config.getint('DEFAULT', 'SCREEN_HEIGHT')

if __name__ == '__main__':
    pygame.init()
               
    screen = pygame.display.set_mode(game.SIZE)
    
    clock = pygame.time.Clock()
    
    pygame.display.set_caption(game.GAME_NAME)
    
    background = Sprite.Imagem_de_Fundo()
    group = pygame.sprite.Group()
    group.add(background)
    
    pygame.display.flip()
    
    while True:
        pygame.event.pump()
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)
            elif event.type == VIDEORESIZE:
                screen = pygame.display.set_mode(
                        event.dict['size'], HWSURFACE | DOUBLEBUF | RESIZABLE)
                background.image = pygame.transform.scale(background.image, event.dict['size'])
        screen.blit(background.image, background.rect)
        pygame.display.update()
        time_passed = clock.tick(fps)
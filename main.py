# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:39:56 2017

@author: Pedro da Luz
"""
import pygame, game
from pygame.locals import *
from sys import exit

import configparser
config = configparser.ConfigParser()

if __name__ == '__main__':
    config.read('data/config.ini')
    fps = config.getint('DEFAULT', 'FPS')
    
    pygame.init()
               
    screen = pygame.display.set_mode((640, 480), 0, 32)
    
    clock = pygame.time.Clock()
    
    pygame.display.set_caption(str(config['DEFAULT']['NOME_DO_JOGO']))
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit(0)
        screen.blit(pygame.Surface(screen.get_size()), (0,0))
        pygame.display.update()
        time_passed = clock.tick(fps)
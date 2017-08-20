# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:39:56 2017

@author: Pedro da Luz
"""
import pygame
from pygame.locals import *
from sys import exit

if __name__ == '__main__':
    pygame.init()
               
    screen = pygame.display.set_mode((640, 480), 0, 32)
    
    clock = pygame.time.Clock()
    
    pygame.display.set_caption('Hello World')
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
        screen.blit(pygame.Surface(screen.get_size()), (0,0))
        pygame.display.update()
        time_passed = clock.tick(30)
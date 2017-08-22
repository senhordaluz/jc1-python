# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:39:56 2017

@author: Pedro da Luz
"""
import pygame, os
from pygame.locals import *
from game import my
from game import engine

os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.init()
pygame.display.set_icon(pygame.image.load('data/arte/icone/aranha1.png'))
pygame.display.set_caption(my.GAME_NAME)

def main():
    """Roda o jogo"""
    runGame()
    
def runGame():
    """Instancia a engine e dá início ao loop do jogo"""
    Engine = engine.Engine()
    while my.jogoRodando:
        Engine.update()

if __name__ == '__main__':
    main()
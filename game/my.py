# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:07:10 2017

@author: Pedro da Luz
"""

import pygame

pygame.mixer.pre_init(44100,-16,2, 1024)
pygame.init()

GAME_NAME = "SUPER SMASH ARANHA-MORCEGO"

SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = [1200,900]
FPS = 30
FPSCLOCK = pygame.time.Clock()
muted = False

# Colours     R    G    B  ALPHA
WHITE     = (255, 255, 255, 255)
BLACK     = (  0,   0,   0, 255)
RED       = (230,  70,  70, 255)
BRIGHTRED = (255,   0,   0, 255)
DARKRED   = (220,   0,   0, 255)
BLUE      = (  0,   0, 255, 255)
SKYBLUE   = (135, 206, 250, 255)
YELLOW    = (255, 250,  17, 255)
GREEN     = (110, 255, 100, 255)
ORANGE    = (255, 165,   0, 255)
DARKGREEN = ( 60, 160,  60, 255)
DARKGREY  = ( 60,  60,  60, 255)
LIGHTGREY = (180, 180, 180, 255)
BROWN     = (139,  69,  19, 255)
DARKBROWN = (100,  30,   0, 255)
BROWNBLACK= ( 50,  0,    0, 255)
GREYBROWN = (160, 110,  90, 255)
CREAM     = (255, 255, 204, 255)
COLOURKEY = (  1,   2,   3, 255)
BLUETRANS = (  0,   0, 255, 100)

# Artes
ARTE_MAPAS_PATH = 'data/arte/fundo/'
ARTE_PORTAL_PATH = 'data/arte/portal/'
ARTE_MENU_PATH = 'data/arte/menu/'
ARTE_ARAQUESL_PATH = 'data/arte/ataques/'
ARTE_ICONE_PATH = 'data/arte/icone/'
ARTE_JOGADOR1_PATH = 'data/arte/personagens/jogador1/'
ARTE_JOGADOR2_PATH = 'data/arte/personagens/jogador2/'
ARTE_BOSS01_PATH = 'data/arte/personagens/boss01/'
ARTE_VILAO01_PATH = 'data/arte/personagens/vilao01/'
ARTE_VILAO02_PATH = 'data/arte/personagens/vilao03/'
ARTE_VILAO03_PATH = 'data/arte/personagens/vilao03/'
ARTE_VILAO04_PATH = 'data/arte/personagens/vilao04/'
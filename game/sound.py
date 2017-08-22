# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 23:30:00 2017

@author: Pedro da Luz
"""

import pygame, random
from game import my

SOUND = {}

# Sons de inimigos
for filename in ['esqueleto', 'orc']: # .wav files only
    SOUND[filename] = pygame.mixer.Sound('data/sons/efeitos/inimigo/%s.wav' %(filename))

def play(sound, volume=0.8, varyVolume=True ,loops=0):
    """Toca o som dado por ums string com o nome do arquivo de audio"""
    if not my.muted:
        if varyVolume:
            volume -= random.uniform(0.0, 0.4)
            if volume < 0.0: volume == 0.1
            SOUND[sound].set_volume(volume)
        SOUND[sound].play(loops)

def stop():
    """Encerra todos os sons do jogo"""
    pygame.mixer.stop()

def stop_music():
    """Encerra a musia que está tocando"""
    pygame.mixer.music.stop()

def pause_music():
    """Pausa a música"""
    pygame.mixer.music.pause()
    
def unpause_music():
    """Recomeça música após o pause"""
    pygame.mixer.music.unpause()

def fadeout_music():
    """Encerra a música tocando com um fade out"""
    pygame.mixer.music.fadeout()

def fase_01():
    """Toca música da primeira fase"""
    pygame.mixer.music.load('data/sons/musicas/field01.mp3')
    pygame.mixer.music.play(-1)
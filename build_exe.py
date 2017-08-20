# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:44:53 2017

@author: Pedro da Luz
"""

from distutils.core import setup
import py2exe
import os
import glob
from calc import add

def find_data_files(source,target,patterns):
    """Locates the specified data-files and returns the matches
    in a data_files compatible format.

    source is the root of the source data tree.
        Use '' or '.' for current directory.
    target is the root of the target data tree.
        Use '' or '.' for the distribution directory.
    patterns is a sequence of glob-patterns for the
        files you want to copy.
    """
    if glob.has_magic(source) or glob.has_magic(target):
        raise ValueError("Magic not allowed in src, target")
    ret = {}
    for pattern in patterns:
        pattern = os.path.join(source,pattern)
        for filename in glob.glob(pattern):
            if os.path.isfile(filename):
                targetpath = os.path.join(target,os.path.relpath(filename,source))
                path = os.path.dirname(targetpath)
                ret.setdefault(path,[]).append(filename)
    return sorted(ret.items())

MyData_files = [('images', ['W:/Python3/jc1-python/arte/personagens/jogador1/Archer w'])]

setup(
      name = "JC1",
      version = "1.0",
      description = "Melhor jogo do mundo",
      author = "Pedro da Luz",
      windows = ["main.py"],
      data_file = find_data_files(
              'data',
              'data', [
                  'fontes/*',
                  'arte/ataques/*',
                  'arte/fundo/*',
                  'arte/icone/*',
                  'arte/menu/*',
                  'arte/personagens/*',
                  'arte/portal/*',
                  'sons/musicas/*',
                  'sons/efeitos/boss/*',
                  'sons/efeitos/clima/*',
                  'sons/efeitos/dano/*',
                  'sons/efeitos/inimigo/*',
                  'sons/efeitos/item/*',
                  'sons/efeitos/magia/*',
                  'sons/efeitos/menu/*',
                  'sons/efeitos/passo/*',
                  'sons/efeitos/personagem/*',
                  ]
            ),
    )
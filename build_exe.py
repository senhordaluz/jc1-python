# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 00:44:53 2017

@author: Pedro da Luz
"""

from distutils.core import setup
import py2exe
from calc import add

setup(console=["main.py"])
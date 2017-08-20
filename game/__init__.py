# -*- coding: utf-8 -*-
"""

MIT License

Copyright (c) 2017 Pedro da Luz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

GAME_NAME = "SUPER SMASH ARANHA-MORCEGO"

version_info = (1, 0, 0, "dev0")

__version__ = ".".join(map(str, version_info))
__license__ = __doc__
__project_url__ = 'https://github.com/senhordaluz/jc1-python'

import os
# Diretório do arquivo
_PATH = os.path.dirname(os.path.abspath(__file__))
__dir__ = os.path.abspath(os.path.join(_PATH, os.pardir))
DATA_PATH = ''.join([__dir__, '/data'])
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

SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = [800,600]

def get_versions(reporev=True):
    """Obtem informações para os componentes"""
    import sys
    import platform
    
    return {
            cfg['config']['NOME_DO_JOGO']: __version__,
            'python': platform.python_version(),
            'bitness': 64 if sys.maxsize > 2**32 else 32,
            'system': platform.system(),
            }
    
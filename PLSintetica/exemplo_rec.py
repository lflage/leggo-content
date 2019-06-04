# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:10:18 2019

@author: lucas
"""

import numpy as np

l= []
l.append((3, []))
obj = (3, l)

ll = []
ll.append(obj)
# =============================================================================
# print(ll)
# =============================================================================


PL = []
PL.append(('art',()))

alineas1 = ('texto1','texto2','texto3')
alineas2 = ('texto1','texto2')

inciso1 = ('textoinciso1',alineas1)
inciso2 = ('textoinciso2', alineas2)

paragrafo = ('textoPar',inciso1,inciso2 )

art = ('textoArt', paragrafo )
print(art[1][0])
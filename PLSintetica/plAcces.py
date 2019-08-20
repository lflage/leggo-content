# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 18:28:06 2019

@author: lucas
"""

import plObjFunc as pl

mpv = pl.PlObjCreate('./teste/mpv870/MPV870_txt_site.txt')

artigo = input()
paragrafo = input()
inciso = input()
alinea = input()

lista_in = []
for i in artigo, paragrafo, inciso, alinea:
    try:
        lista_in.append(int(i))
    except:
        lista_in.append(None)


# =============================================================================
# try:
#     map()
# for i in niveis:
# =============================================================================
    
if artigo and paragrafo and inciso and alinea:
    try:
        print(mpv[1][lista_in[0]][lista_in[1]][1][lista_in[2]][1][lista_in[3]])
    except:
        print("não existe, caso1")

if artigo and paragrafo and inciso and not alinea:
    try:
        print(mpv[1][lista_in[0]][lista_in[1]][1][lista_in[2]][0])
    except:
        print("não existe")
        
if artigo and paragrafo and not inciso and not alinea:
    try:
        print(mpv[1][lista_in[0]][lista_in[1]])
    except:
        print("não existe")
# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:52:27 2019

@author: lucas
"""
import re

IndexList = []
PlObj = []
PlArt = []
PlPar = []
PlInc = []
PlAli = []

with open ('teste/MPV870_txt_site.txt', 'r', encoding = 'utf-8') as pl:
    texto = pl.read()
    NvAtual = 0
    NvPrx = 0
    while texto:
        NvAtual = NvPrx
        
        ArtSearch = re.search(r'(\nArt\. \dº|\nArt\. \d+)',texto)
        ParSearch = re.search(r'§ \d',texto)
        AliSearch = re.search(r'(\n[a-z]\)|\n[a-z][a-z]\))',texto)
        IncSearch = re.search(r'[MDCLXVI]+\ -',texto)
        
        if IndexList.count(None) == 1:
            print("acabou")
            break        

        IndexList = [ArtSearch.start(),ParSearch.start(),IncSearch.start(),AliSearch.start()]
        
        
        if min(IndexList) == ArtSearch.start():
            NvPrx = 0
            print('Artigo: ',ArtSearch[0])
            print(texto[:ArtSearch.start()])
            texto = texto[ArtSearch.end():]
        
        if min(IndexList) == ParSearch.start():
            NvPrx = 1
            print('Paragrafo: ', ParSearch[0])
            print(texto[:ParSearch.start()])
            texto = texto[ParSearch.end():]
        
        if min(IndexList) == IncSearch.start():
            NvPrx = 2
            print('Inciso: ', IncSearch[0])
            print(texto[:IncSearch.start()])
            texto = texto[IncSearch.end():]
        
            
        if min(IndexList) == AliSearch.start():
            NvPrx = 3
            print('alinea:',AliSearch[0])
            print(texto[:AliSearch.start()])
            texto = texto[AliSearch.end():]
            
        
        if NvAtual != 0 and NvPrx ==0:
            print('subiu de nível')
            

            
    
texto.strip()
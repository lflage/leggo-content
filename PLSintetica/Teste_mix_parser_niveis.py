# -*- coding: utf-8 -*-

"""
Created on Tue May 14 13:52:27 2019

@author: lucas
"""
import re

def nextLevelSearch(strInput):
    indexList = []    
    tup = (
    ("ArtSearch" , re.search(r'\nArt\. \dº|\nArt\. \d+',strInput)),        
    ("ParSearch" , re.search(r'§ \d',strInput)),
    ("AliSearch" , re.search(r'\n[a-z]\)|\n[a-z][a-z]\)',strInput)),
    ("IncSearch" , re.search(r'[MDCLXVI]+\ -',strInput)),
    )
    
    for key,value in tup:
        try:
            index = value.start()
            indexList.append(index)
        except:
            pass

    for key,value in tup:
        try:            
            if min(indexList) == value.start():
                return (value) 
        except:
            pass
    return('')


IndexList = []
PlObj = []
PlArt = []
PlPar = []
PlInc = []
PlAli = []

artPat = re.compile(r'\nArt\. \dº. +|\nArt\. \d+. +')
parPat = re.compile(r'\n§ \d+º|\nParágrafo único\.')
incPat = re.compile(r'\n[MDCLXVI]+\ -')
aliPat = re.compile(r'\n[a-z]\)|\n[a-z][a-z]\)')

pars = []

with open ('teste/MPV870_txt_site.txt', 'r', encoding = 'utf-8') as pl:
    texto = pl.read()
        
    arts = re.split(artPat,texto)
    for art in arts:
        if arts.index(art) == 0:
            PlObj.append(art)
# =============================================================================
#         else:
#             PlArt.append(re.match(r'.+\b',art.strip())[0])
# =============================================================================
                      
        
        paragraphs = re.split(parPat,art)   
        pars.append(paragraphs)         
        for paragraph in paragraphs:
            if paragraphs.index(paragraph) == 0:
                PlPar.append(re.match(r'.+\b',art.strip())[0])
            else:
                PlPar.append(re.match(r'.+\b',paragraph.strip())[0])
                
            incisos = re.split(incPat,paragraph)
            for inciso in incisos:
                if incisos.index(inciso) == 0:
                    continue
                else:
                    PlInc.append(re.match(r'.+\b',inciso.strip())[0])
                    
                    
                
                alineas = re.split(aliPat,inciso)
                if len(alineas) > 1:
                    for alinea in alineas:
                        PlAli.append(re.match(r'.+\b',alinea.strip())[0])
                        
                if PlAli:
                    PlInc.append(PlAli)
                PlAli=[]
            
            if PlInc:
                PlPar.append(PlInc)
            PlInc = []
        if PlPar:    
            PlArt.append(PlPar)
        PlPar = []
        
    PlObj.append(PlArt)

                        
                    
                    
                    
                
        
# =============================================================================
#         PlArt.append[art[:x.start()]] 
# =============================================================================
# =============================================================================
#         if IndexList.count(None) == 1:
#             print("acabou")
#             break        
# 
#         IndexList = [ArtSearch.start(),ParSearch.start(),IncSearch.start(),AliSearch.start()]
# =============================================================================
        
        

            

            
    

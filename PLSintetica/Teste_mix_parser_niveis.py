# -*- coding: utf-8 -*-
"""
Created on Thu Jun 13 16:19:31 2019

@author: lucas
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:52:27 2019

@author: lucas
"""
import re

def nextLevelSearch(strInput):
    indexList = []
    notNoneList = []
    dic = {
    "ArtSearch" : re.search(r'(\nArt\. \dº|\nArt\. \d+)',strInput),        
    "ParSearch" : re.search(r'§ \d',strInput),
    "AliSearch" : re.search(r'(\n[a-z]\)|\n[a-z][a-z]\))',strInput),
    "IncSearch" : re.search(r'[MDCLXVI]+\ -',strInput),
    }
    
    for key,value in dic:
        try:
            index = value.start()
            notNoneList.append(value)
            indexList.append(index)
        except:
            pass
        
    for key,value in dic:
        if min(indexList) == value.start():
            return (key,value) 
    


IndexList = []
PlObj = []
PlArt = []
PlPar = []
PlInc = []
PlAli = []

artPat = re.compile(r'(\nArt\. \dº|\nArt\. \d+)')
parPat = re.compile(r'§ \d')
aliPat = re.compile(r'(\n[a-z]\)|\n[a-z][a-z]\))')
incPat = re.compile(r'[MDCLXVI]+\ -')

with open ('teste/MPV870_txt_site.txt', 'r', encoding = 'utf-8') as pl:
    texto = pl.read()

    while texto:
        
        ArtSearch = re.search(r'\nArt\. \dº|\nArt\. \d\d',texto)
        ParSearch = re.search(r'§ \d',texto)
        AliSearch = re.search(r'\n[a-z]\)|\n[a-z][a-z]\)',texto)
        IncSearch = re.search(r'[MDCLXVI]+\ -',texto)
        
        arts = re.split(r'(\nArt\. \dº|\nArt\. \d+)',texto)
        for art in arts:
            
            ParSearch = re.search(parPat,texto)
            AliSearch = re.search(aliPat,texto)
            
            PlArt.append()
            
            paragraphs = re.split(r'§ \d',texto)
            
# =============================================================================
#             for paragraph in paragraphs:
# =============================================================================
                
        

# =============================================================================
#         if IndexList.count(None) == 1:
#             print("acabou")
#             break        
# 
#         IndexList = [ArtSearch.start(),ParSearch.start(),IncSearch.start(),AliSearch.start()]
# =============================================================================
        
        

            

            
    

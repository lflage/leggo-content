# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 19:22:48 2019

@author: lucas
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:52:27 2019

@author: lucas
"""
import re

IndexList = []
PlObj = []

# Defining regex Patterns



# função níveis ok
def nextLevelSearch(strInput):
    indexList = []
    notNoneList = []
    
    tup = (
    ("ArtSearch" , re.search(r'\nArt\. \dº|\nArt\. \d+',strInput)),        
    ("ParSearch" , re.search(r'§ \d',strInput)),
    ("AliSearch" , re.search(r'\n[a-z]\)|\n[a-z][a-z]\)',strInput)),
    ("IncSearch" , re.search(r'[MDCLXVI]+\ -',strInput)),
    )
    
    for key,value in tup:
        try:
            index = value.start()
            notNoneList.append(value)
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
    


with open ('teste/MPV870_txt_site.txt', 'r', encoding = 'utf-8') as pl:
    texto = pl.read()
    NvAtual = 0
    NvPrx = 0
    while texto:
        x = nextLevelSearch(texto)
        if x:
            print(texto[x.end():])
            texto = texto[x.end():]
        else:
            break
        

            
    

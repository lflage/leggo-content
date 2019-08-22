# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 20:44:29 2019

@author: lucas
"""
import sys
print(sys.path)
import ClassificadorDeEmendas as clfe
import pandas as pd

emendas = clfe.cria_pd_df("./dados/tagFiles")
print("teste2")
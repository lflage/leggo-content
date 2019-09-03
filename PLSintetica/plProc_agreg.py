# -*- coding: utf-8 -*-
"""
Created on Mon Sep  2 19:20:25 2019

@author: lucas
"""
import os
import re
import plObjFunc as pl

emd_dir_path = '../parser_itens/emd_pars_agreg'


bet_quote = re.compile(r"\'(.*?)\'", flags = re.IGNORECASE)


files = []
for dirpath, dirnames, filenames in os.walk(emd_dir_path):
    for filename in filenames:
        files.append(os.path.normpath(os.path.join(dirpath,filename)))


for file in files:
    
    with open(file, mode = 'r', encoding = "utf8") as emenda:
        lista_de_itens_alterados = []
        
        emd = emenda.read()

        # Processa emendas pós agregado
        existe_agreg = False
        if re.search('__INICIO_AGREGADOR__',emd):
            nxt = emd.split("__INICIO_AGREGADOR__\n")[1]
            if re.search(r'.+\n(?=__FIM_AGREGADOR__)',nxt):
                ent = nxt.split('__FIM_AGREGADOR__')[0] 
                existe_agreg = True
        
        lista_indices = []
        if existe_agreg:
            for item in ent.splitlines():
                item = re.findall(bet_quote,item)
                pl_index = []
                #Le todos os casos, cria uma lista com os indices para o 
                # obj pl
                for nr,index in enumerate(item):
                    try:
                        if nr == 0 or nr == 1:
                            pl_index.append(int(index.split('_')[1]))
                        if nr == 2:
                            pl_index.append(pl.roman_to_int(index.split('_')[1]))
                        if nr == 3:
                            pl_index.append(pl.ali_to_num(index.split('_')[1]))
                    except:
                        pl_index.append(None)                        
                        
                # Tratamento de casos especiais
                # Desconsidera caso não exista artigo
                if not pl_index[0]:
                    continue
                # Caso receba somente artigo e não parágrafo, use o 
                # parágrafo 0
                if pl_index[0] and not pl_index[1] and pl_index[2]:
                    pl_index[1] = 0
                # Caso receba somente artigo e alinea 
                if pl_index[0] and not pl_index[1] and not pl_index[3] and pl_index[3]:
                    pl_index[1] = 0
                    pl_index[2] = 1
                
                # Retira valores None e inserir indices para correta localização
                pl_index = filter(None,pl_index)
                if len(pl_index) == 4:
                    pl_index.insert(2,1)
                    pl_index.insert(-1,1)
                if len(pl_index) == 3:
                    pl_index.insert(-1,1)
                
                
                lista_indices.append(pl_index)
                print(pl_index)
        
            
                    
                    
        
            
        
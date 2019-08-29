# -*- coding: utf-8 -*-
"""
Created on Wed Aug 28 13:00:28 2019

@author: lucas
"""
import re
import os
import ClassificadorDeEmendas as clfe
import plObjFunc as pl

mpv = pl.PlObjCreate('./teste/mpv870/MPV870_txt_site.txt')

emd_dir_path = '../parser_itens/testes_lucas/7911197.pdf_teor.tags'


files = []
for dirpath, dirnames, filenames in os.walk(emd_dir_path):
    for filename in filenames:
        files.append(os.path.normpath(os.path.join(dirpath,filename)))

tipos_de_emenda = clfe.preve_emenda(emd_dir_path)


for file,tipo_emenda in zip(files,tipos_de_emenda):
    # Checa o tipo de emenda   
    if tipo_emenda == 'O':
        continue
    
    with open(file, mode = 'r', encoding = "utf8") as emenda:
        lista_de_itens_alterados = []
        
        #item_alterado = {'artigo': '', 'paragrafo':'','inciso':'', 'alinea': ''}
        emd = emenda.read()
        if re.search('__INICIO_AGREGADOR__',emd):
            ent = emd.split("__INICIO_AGREGADOR__\n")[1].split('\n__FIM_AGREGADOR__')[0]
        else:
            continue
        texto_emd = emd.split("!@#$%")[0]
        
        
        for item in ent.splitlines():
            indices = re.sub(r"('|\(|\))",'',item).split(',')
            pl_index = []
            for i in indices:
                try:
                    pl_index.append(i.split('_')[1])
                except:
                    pl_index.append(None)
                    
            if pl_index[0]:
                pl_index[0] = int(pl_index[0])
            if pl_index[1]:
                try:
                    pl_index[1] = int(pl_index[1])
                except:
                    pl_index[1] = pl.roman_to_int(pl_index[1])
            if pl_index[2]:
                try:
                    pl_index[2] = pl.roman_to_int(pl_index[2])
                except:
                    if not pl_index[3] and pl_index[2].isalpha():
                        pl_index[3] = pl_index[2]
                        pl_index[2] = None
            if pl_index[3]:
                pl_index[3] = pl.ali_to_num(pl_index[3])
                
            lista_de_itens_alterados.append(pl_index)
        
        for alteracao in lista_de_itens_alterados:
            try:
                if tipo_emenda == "ADD":
                    if alteracao[0] and alteracao[1] and alteracao[2] and not alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][1].append(texto_emd)
                        print(mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][1])
        
                    if alteracao[0] and alteracao[1] and not alteracao[2] and not alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]].append(texto_emd)
                        print(mpv[1][alteracao[0]][alteracao[1]])
    
                    if alteracao[0] and not alteracao[1] and alteracao[2] and not alteracao[3]:
                        mpv[1][alteracao[0]][0][1][alteracao[2]].append(texto_emd)
            
                if tipo_emenda == "MOD":
                    if alteracao[0] and alteracao[1] and alteracao[2] and alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][1][alteracao[3]] = texto_emd
                        print(mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][1][alteracao[3]])
        
                    if alteracao[0] and alteracao[1] and alteracao[2] and not alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][0] = texto_emd
                
                    if alteracao[0] and alteracao[1] and not alteracao[2] and not alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]][0]  = texto_emd
    
                if tipo_emenda == "SUP":
                    if alteracao[0] and alteracao[1] and alteracao[2] and alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][1][alteracao[3]] = ''
        
                    if alteracao[0] and alteracao[1] and alteracao[2] and not alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][0] = ''
        
                    if alteracao[0] and alteracao[1] and not alteracao[2] and not alteracao[3]:
                        mpv[1][alteracao[0]][alteracao[1]][0]  = ''
            except:
                print("Índice não encontrado no objeto")
            
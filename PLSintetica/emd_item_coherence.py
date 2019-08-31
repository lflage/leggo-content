# -*- coding: utf-8 -*-


import re
import os
import ClassificadorDeEmendas as clfe
import plObjFunc as pl
import pandas as pd
from gensim.models import KeyedVectors
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords
from unicodedata import normalize



mpv = pl.PlObjCreate('./teste/mpv870/MPV870_txt_site.txt')

emd_dir_path = '../parser_itens/emendas_processadas_em_blocos'

modelPath = '../coherence/languagemodel/vectors_new.bin'

stop_word = stopwords.words('portuguese')
tokenizer = CountVectorizer(stop_words=stopwords.words('portuguese')).build_tokenizer()
model = KeyedVectors.load_word2vec_format(modelPath, binary=True)


files = []
for dirpath, dirnames, filenames in os.walk(emd_dir_path):
    for filename in filenames:
        files.append(os.path.normpath(os.path.join(dirpath,filename)))

tipos_de_emenda = clfe.preve_emenda(emd_dir_path)

to_df_row = []
for file,tipo_emenda in zip(files,tipos_de_emenda):
    # Checa o tipo de emenda   
    if tipo_emenda == 'O':
        continue
    
    with open(file, mode = 'r', encoding = "utf8") as emenda:
        lista_de_itens_alterados = []
        
        emd = emenda.read()
        texto_emd = tokenizer(emd.split("!@#$%")[0].lower())
        # Processa emendas pós agregador    
        if re.search('__INICIO_AGREGADOR__',emd):
            nxt = emd.split("__INICIO_AGREGADOR__\n")[1]
            if re.search(r'.+\n(?=__FIM_AGREGADOR__)',nxt):
                ent = nxt.split('__FIM_AGREGADOR__')[0] 
        else:
            continue
        # cria lista com indices
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
                if tipo_emenda == "MOD":
# =============================================================================
#                     if alteracao[0] and alteracao[1] and alteracao[2] and alteracao[3]:
#                         texto_pl = mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]][1][alteracao[3]]
#                         texto_pl = ' '.join(list(pl.flatten(texto_pl)))
#                         
#                     if alteracao[0] and alteracao[1] and alteracao[2] and not alteracao[3]:
#                         texto_pl = mpv[1][alteracao[0]][alteracao[1]][1][alteracao[2]]
#                         texto_pl = ' '.join(list(pl.flatten(texto_pl)))
#                 
#                     if alteracao[0] and alteracao[1] and not alteracao[2] and not alteracao[3]:
#                         texto_pl = mpv[1][alteracao[0]][alteracao[1]]
#                         texto_pl = ' '.join(list(pl.flatten(texto_pl)))
#                     
#                     if alteracao[0] and not alteracao[1] and not alteracao[2] and not alteracao[3]:
#                         texto_pl = mpv[1][alteracao[0]]
#                         texto_pl = remover_acentos(' '.join(list(pl.flatten(texto_pl))).lower())
# =============================================================================
                    # Procura posição no plObj
                    texto_pl = pl.nested_lookup(mpv[1],list(filter(None, alteracao)))
                    
                    # Cria uma string inteira com todos os textos na posição encontrada
                    texto_pl = ' '.join(list(pl.flatten(texto_pl))).lower()
                    
                    texto_pl = tokenizer(texto_pl)
                    try:
                        dist = model.distance(texto_pl,texto_emd)
                    except:
                        print('erro no modelo')
                    to_df_row.append([file,' '.join(alteracao),dist])      
                       
                
                
            except:
                
                pass
df = pd.DataFrame(to_df_row)
df.to_csv('df_csv.csv')
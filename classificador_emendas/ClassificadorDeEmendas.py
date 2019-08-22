# -*- coding: utf-8 -*-
"""
Created on Wed Aug 21 19:51:33 2019

@author: lucas
"""
import os
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import RandomOverSampler
from joblib import dump

def cria_pd_df(ner_out_path):
    # função deve receber o caminho para uma pasta contendo os arquivos de
    # saída do segmentador (tagFiles)
    tagList = ["I-","E-","B-"]
    files = []
    for dirpath, dirnames, filenames in os.walk(ner_out_path):
        for filename in filenames:
            files.append(os.path.normpath(os.path.join(dirpath,filename)))

    emendas = pd.DataFrame(columns = ['text','emdType'])
    tupEmd = []


    for file in files:
        with open(file, encoding = "utf-8") as f:
            emdTxt = []
            previousType = None
            for line in f.readlines():
                token,emdType = line.split()
                if any(x in emdType for x in tagList):
                    emdType = emdType[2:]
                    if previousType != emdType and previousType != None:
                        tupEmd.append([" ".join(emdTxt), previousType])
                        emdTxt = []
                
                emdTxt.append(token)
                previousType = emdType
                tupEmd.append([" ".join(emdTxt), emdType])


    for index in range(len(tupEmd)):
        emendas.loc[index,'text'] = tupEmd[index][0]
        emendas.loc[index,'emdType'] = tupEmd[index][1]
    return(emendas)
    
def cria_modelo(dataframe):
    
    # O modelo utiliza como entrada um bag-of-words, um vetor que contem 
    # o numero de ocorrencias de cada palavra em todas as emendas
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(dataframe['text'])
    y = dataframe['emdType']
    
    # Separacao das bases
    X_train, X_test, y_train, y_test = train_test_split( 
            X, y, test_size=0.33, random_state=42)
    
    # Oversampling e realizado pois ha poucas ocorrencias de emendas ADD
    ros = RandomOverSampler(random_state=0)
    X_resampled, y_resampled = ros.fit_resample(X, y)
    
    clf = SVC(gamma = 'auto')
    clf.fit(X_resampled,y_resampled)

    dump(clf,"classificador_de_emendas")
    return(clf)

    

# -*- coding: utf-8 -*-

'''
Created on 30/03/2020

@author: Daniel Bonilla
@author: Luis Felipe Tejada
@author: Sebastian  Ceballos

'''

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import re
from string import punctuation


# stopword list to use
spanish_stopwords = stopwords.words('spanish')
# spanish stemmer
stemmer = SnowballStemmer('spanish')

# punctuation to remove
non_words = list(punctuation)
# we add spanish punctuation
non_words.extend(['¿', '¡'])
non_words.extend(map(str, range(10)))

stemmer = SnowballStemmer('spanish')


def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed


def obtenerPalabras(dataFrame):
    palabrasInteres = ""
    # Se recorre el archivo

    for dato in dataFrame["text"]:
        # Se cambia el dato a un String
        dato = str(dato)
        # print(str(dato.encode("utf8")))
        dato.lower()
        # Se hace un split
        palabras = dato.split()

        for palabra in palabras:
            palabrasInteres = palabrasInteres + palabra + ' '

    # Remover links
    palabrasInteres = re.sub(r"http\S+", "https", palabrasInteres)
    # remove repeated characters
    palabrasInteres = re.sub(r'(.)\1+', r'\1\1', palabrasInteres)
    return palabrasInteres


def filtrarStopWords(palabrasInteres):
    # remove links from tweets
    palabrasInteres = re.sub(r"http\S+", "https", palabrasInteres)
    # remove punctuation
    palabrasInteres = ''.join(
        [c for c in palabrasInteres if c not in non_words])
    # remove repeated characters
    palabrasInteres = re.sub(r'(.)\1+', r'\1\1', palabrasInteres)
    important_words = []
    # tokenize
    #tokens = word_tokenize(palabrasInteres)
    tokens = palabrasInteres.split(" ")
    for word in tokens:
        if word not in spanish_stopwords:
            important_words.append(word)
    # stem
    try:
        stems = stem_tokens(important_words, stemmer)
    except Exception as e:
        print(e)
        stems = ['']
    return important_words


def main():

    # Se carga el archivo en un dataFrame
    dataFrame = pd.read_csv(
        r"NubePalabras\plebiscito.csv", encoding="utf8")
    #print("El dataframe es \n")
    # print(dataFrame)
    palabrasInteres = obtenerPalabras(dataFrame)

    limpiarStopWords = filtrarStopWords(palabrasInteres)
    print(limpiarStopWords)
    # generarNube(palabrasInteres)

    # TODO para pipe acuerdese de configurar los stopwords para español
    # en esa pagina explican cualquier cosa me dice https://blog.hacemoscontactos.com/2018/08/21/analisis-de-palabras-frecuentes-usando-python/


if __name__ == '__main__':
    main()

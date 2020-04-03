# -*- coding: utf-8 -*-

'''
Created on 30/03/2020

@author: Daniel Bonilla
@author: Luis Felipe Tejada
@author: Sebastian  Ceballos

'''

import matplotlib.pyplot as plt
import pandas as pd
from wordcloud import WordCloud
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

    return palabrasInteres


def filtrarStopWords(palabrasInteres):
    # remove links from tweets
    palabrasInteres = re.sub(r"http\S+", "https", palabrasInteres)
    palabrasInteres=palabrasInteres.replace("https","")
    # remove punctuation
    palabrasInteres = ''.join(
        [c for c in palabrasInteres if c not in non_words])
    # remove repeated characters
    palabrasInteres = re.sub(r'(.)\1+', r'\1\1', palabrasInteres)
    important_words = []
    # tokenize
    # tokens = word_tokenize(palabrasInteres)
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
    return stems


def generarNube(palabrasInteres):

    stopwords = set(spanish_stopwords)
    nubePalabras = WordCloud(width=700, height=700,
    background_color='white',
    stopwords=stopwords,
    min_font_size=10).generate(palabrasInteres)

    # Se hace el gr�fico de la nube de palabras
    # facecolor  es el color de fondo
    plt.figure(figsize=(7, 7), facecolor=None)
    plt.imshow(nubePalabras)
    plt.axis("on")
    plt.tight_layout(pad=0)
    plt.show()


def convertirAString(lista):
    palabrasInteres = ""
    # Se recorre el archivo

    for palabra in lista:
        palabrasInteres = palabrasInteres + palabra + ' '
    return palabrasInteres


def main():

    # Se carga el archivo en un dataFrame
    dataFrame = pd.read_csv(r"NubePalabras\plebiscito.csv", encoding="utf8")
    # print("El dataframe es \n")
    # print(dataFrame)

    

    palabrasInteres = obtenerPalabras(dataFrame)

   
    limpiarStopWords = filtrarStopWords(palabrasInteres)
    # print(limpiarStopWords)

    palabrasInteres=convertirAString(limpiarStopWords)

    generarNube(palabrasInteres)

    # TODO para pipe acuerdese de configurar los stopwords para español
    # en esa pagina explican cualquier cosa me dice https://blog.hacemoscontactos.com/2018/08/21/analisis-de-palabras-frecuentes-usando-python/




if __name__ == '__main__':
    main()

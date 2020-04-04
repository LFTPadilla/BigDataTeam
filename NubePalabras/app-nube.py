# -*- coding: utf-8 -*-

'''
Created on 30/03/2020

@author: Daniel Bonilla
@author: Luis Felipe Tejada
@author: Sebastian  Ceballos

'''

import matplotlib.pyplot as plt
import pandas as pd
from nltk.corpus import stopwords
from nltk import word_tokenize
from nltk.stem import SnowballStemmer
import re
from string import punctuation
import collections


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

'''
Fundion que define el stemming del token
'''
def stem_tokens(tokens, stemmer):
    stemmed = []
    for item in tokens:
        stemmed.append(stemmer.stem(item))
    return stemmed

'''
Funcion encargada de cargar el texto de los diferentes archivos
 
 @return palabrasInteres; variable con todas las palabras del texto
'''
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



'''
Funcion encargada de filtrar los stop Words eliminando palabras 
como al, el,como,a ,y etc

@return important_words; variable con el texto filtrado
'''
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


'''
Funcion encargada de iniciar el programa
'''
def main():

    # Se carga el archivo en un dataFrame
    dataFrame = pd.read_csv(r"NubePalabras\plebiscito.csv", encoding="utf8")
    #print("El dataframe es \n")
    # print(dataFrame)
    palabrasInteres = obtenerPalabras(dataFrame)
    limpiarStopWords = filtrarStopWords(palabrasInteres)

    # Ordena los datos del mas repetido al menor
    listaRepeticiones =collections.Counter(limpiarStopWords)
    # Permite sacar el numero de elemntos que necesite de la lista 
    elemento=listaRepeticiones.most_common(9)
    
    print(elemento[0])
    #print(limpiarStopWords)
    # generarNube(palabrasInteres)


    fig = plt.figure(u'Gráfica de barras') # Figure
    ax = fig.add_subplot(111) # Axes
    nombres = [listaRepeticiones.most_common(1),'Ana','Pablo','Ximena','Jorge']
    datos = [650,88,78,94,93]
    xx = range(len(datos))
    ax.bar(xx, datos, width=0.8, align='center')
    ax.set_xticks(xx)
    ax.set_xticklabels(nombres)

    plt.show()

    # TODO para pipe acuerdese de configurar los stopwords para español
    # en esa pagina explican cualquier cosa me dice https://blog.hacemoscontactos.com/2018/08/21/analisis-de-palabras-frecuentes-usando-python/


if __name__ == '__main__':
    main()

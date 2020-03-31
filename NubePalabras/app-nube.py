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


def obtenerPalabras(dataFrame):
    palabrasInteres = ""
    # Se recorre el archivo
     
    for dato in dataFrame["text"]:
        # Se cambia el dato a un String
        dato = str(dato) 
        print(str(dato.encode("utf8")))
  
        dato.lower()
        # Se hace un split
        palabras = dato.split()
          
        for palabra in palabras: 
            palabrasInteres = palabrasInteres + palabra + ' '
    return palabrasInteres

def main(): 

    # Se carga el archivo en un dataFrame
    dataFrame = pd.read_csv(r"NubePalabras\plebiscito-plebiscito-colombia-2016-QueryResult.csv", encoding="utf8") 
    #print("El dataframe es \n")
    #print(dataFrame)
    palabrasInteres=obtenerPalabras(dataFrame)
    #generarNube(palabrasInteres)


    #TODO para pipe acuerdese de configurar los stopwords para español
    #en esa pagina explican cualquier cosa me dice https://blog.hacemoscontactos.com/2018/08/21/analisis-de-palabras-frecuentes-usando-python/

if __name__ == '__main__':
    main()
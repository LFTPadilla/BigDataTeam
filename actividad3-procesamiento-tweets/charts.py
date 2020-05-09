from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter



# Funcion que permite crear la nube de palabras de los tweets
def generarNube(palabrasInteres):


    nubePalabras = WordCloud(width=700, height=700,
    background_color='white',
    min_font_size=10).generate(palabrasInteres)

    # Se hace el gr�fico de la nube de palabras
    # facecolor  es el color de fondo
    plt.figure(figsize=(7, 7), facecolor=None)
    plt.imshow(nubePalabras)
    plt.axis("on")
    plt.tight_layout(pad=0)
    plt.show()

#Funcion que crea las diferentes graficas de los datos 
def graficas(palabrasInteres,tweetsSentimiento):

    p=palabrasInteres.split()

    # Grafico 1: Numero de tweets que hablan del covid o de la cuarentena.
    
    indices = np.array([0,0])
    for i in range(0, len(p)):
        if(p[i]=="coronavirus" or p[i]=="covid-19" or p[i]=="covid19" or p[i]=="covid"  ):
            indices[0]+=1
        if(p[i]=="quarantine" or p[i]=="lockdown" ):
            indices[1]+=1

    rango = ("Covid","Quarentena")
    posicion_y = np.arange(len(rango))
    plt.barh(posicion_y, indices, align="center")
    plt.title("Numero de tweets Que hablan de la cuarentena o del covid")
    plt.yticks(posicion_y,rango, rotation=45)
    plt.xlabel('Tweets')
    plt.show()
    

    # Grafico 2 grafico de pastes que muestra el porcentaje de las 10 palabras mas repetidas
    
    contador=Counter(p)
    palabraMasRepetida=contador.most_common(10)
    print(palabraMasRepetida)
    palabra = list(('','','','','','','','','',''))
    frecuencia = np.array([0,0,0,0,0,0,0,0,0,0])
    for i in range(0,10):
        p=palabraMasRepetida[i][0]
        palabra[i]=p
        frecuencia[i]=int(palabraMasRepetida[i][1])
    
    colores = ('red', 'blue', 'green', 'yellow','pink','black','purple','violet','orange','white')
    plt.pie(frecuencia, colors=colores, labels=palabra, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Grafico porcentual de las 10 palabras mas repetidas")
    plt.show()
    

    # Grafico 3 grafico de barras que muestra la recuencia de las 10 palabras mas repetidas
    
    fig,ax=plt.subplots()
    plt.title("Grafico de barras con las 10 palabras mas repetidas")
    ax.bar(palabra,frecuencia)
    plt.show()

    
    # Grafico 4 histograma sobre el sentimiento de los tweets
    
    tweetsSentimiento['clase'].plot.hist()
    plt.title("Histograma de Sentimentalidad ")
    plt.xlabel("Sentimiento")
    plt.show()
    

    # Grafico 5 curva que representa el sentimientos de los tweets 
    
    tweetsSentimiento['clase'].plot.kde()
    plt.title("Curva de Sentimentalidad")
    plt.xlabel("Sentimiento")
    plt.show()
    
    
    # grafico 6 numero de palabras relacionadas con el cov y su sntimiento 

    claseSentimientos= np.array(tweetsSentimiento['clase'])
    tweetSentimientos= np.array(tweetsSentimiento['tweet'])
    n=0
    frecuencia = np.array([0,0,0])
    sentimientoF = ("Negativo","Neutral","Positivo")

    for i in range(0, len(claseSentimientos)):
        p=tweetSentimientos[i].split()
        for j in range(0,len(p)):
            if(p[j]=="coronavirus" or p[j]=="covid-19" or p[j]=="covid19" or p[j]=="covid" ):
                n+=1
        if(str(claseSentimientos[i])=='-1'):
            frecuencia[0]+=n
        if(str(claseSentimientos[i])=='0'):
            frecuencia[1]+=n
        if(str(claseSentimientos[i])=='1'):
            frecuencia[2]+=n
        n=0
    plt.plot(sentimientoF,frecuencia)
    plt.title("Sentiento relacionado con #palabrasCovid")
    plt.xlabel("Sentimiento")
    plt.ylabel("Frecuencia de palabras")
    plt.show()

    # Gafico 7 Cantidad de palabras que se redactan por sentimeentalidad de tweets

    frecuencia = np.array([0,0,0])
    sentimientoF = ("Negativo","Neutral","Positivo")

    for i in range(0, len(claseSentimientos)):
        p=tweetSentimientos[i].split()
        if(str(claseSentimientos[i])=='-1'):
            frecuencia[0]+= len(p)
        if(str(claseSentimientos[i])=='0'):
            frecuencia[1]+= len(p)
        if(str(claseSentimientos[i])=='1'):
            frecuencia[2]+= len(p)
    fig,ax=plt.subplots()
    plt.title("Numero de palabras por Sentimentalidad")
    ax.bar(sentimientoF,frecuencia)
    plt.show()
    

    

    



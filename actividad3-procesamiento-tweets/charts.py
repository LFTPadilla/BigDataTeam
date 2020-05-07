from wordcloud import WordCloud
import matplotlib.pyplot as plt


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

import pandas as pd
from matplotlib import pyplot as plt
import numpy as np
import limpiezaColumnas
import limpiezaFilas
import limpiezaNegativos
from scipy import stats
import seaborn as sns


'''
Funcion que nos permite conocer los tipos de datos que tenemos en el dataset
'''


def describirDatos():
    df = pd.read_csv(r"Actividad2-limpieza/info/comprar_alquilarConRuido.csv")
    df = df.astype({"estado_civil": str, "trabajo": str, "comprar": str})

    print("-------TIPOS DE VARIABLES-------")
    print(df.dtypes)
    print("-------DATOS RESULTANTES-------")
    print(df.describe(percentiles=[], include='all'))
    print("-------MEDIANAS-------")
    print(df.median(numeric_only=True))
    


'''
'''





def limpieza():
    limpiezaFilas.limpiar()
    limpiezaColumnas.limpiar()
    limpiezaNegativos.limpiar()

    df = pd.read_csv(
        r"Actividad2-limpieza/info/comprar_alquilarSinNegativos.csv")

    df = df.astype({"estado_civil": str, "trabajo": str, "comprar": str})
    df = df.fillna(df.mean())

    # Se observa los cuartiles y los outliers con boxplot y se eliminan a mano
    df_numeric = df.select_dtypes(include=[np.number])
    numeric_cols = df_numeric.columns.values

    print(df_numeric.describe())
    # box plot.

    # for col in numeric_cols:
    #     df.boxplot(column=[col])
    #     plt.show()
    
     
    

    #Se observa que ningún dato está es considerable como outlier por lo tanto no se elimina nada
    #se almacena el data set ya completamente limpio
    df.to_csv(r'Actividad2-limpieza/info/comprar_alquilarLimpio.csv',index=False)

'''
Funcion que realiza los diferentes tipos de graficas
'''


def graficar():

    df = pd.read_csv(
        r"Actividad2-limpieza/info/comprar_alquilarSinNegativos.csv")

    #df = df.astype({"estado_civil": str, "trabajo": str, "comprar": str})

    # 1 Grafico de  densidad de comprar Categorica
    
    df["comprar"].plot.kde()
    plt.xlabel("comprar")
    plt.show()

    # 2 Cantidad de personas por estado civil categorico

    df['estado_civil'].plot.hist()
    plt.xlabel("estado civil")
    plt.show()

    # 3 cantidad de personas con cada tipo de trabajo categorico
    trabajo = np.array(df['trabajo'])
    trabajoT = np.array([0, 0, 0, 0, 0, 0, 0, 0])
    for i in range(0, len(trabajo)):
        if(trabajo[i] == 0):
            trabajoT[0] += 1
        if(trabajo[i] == 2):
            trabajoT[1] += 1
        if(trabajo[i] == 3):
            trabajoT[2] += 1
        if(trabajo[i] == 4):
            trabajoT[3] += 1
        if(trabajo[i] == 5):
            trabajoT[4] += 1
        if(trabajo[i] == 6):
            trabajoT[5] += 1
        if(trabajo[i] == 7):
            trabajoT[6] += 1
        if(trabajo[i] == 8):
            trabajoT[7] += 1
    plt.plot(trabajoT)
    plt.title("Grafica")
    plt.xlabel("Tipo de trabajo")
    plt.ylabel("Frecuencia")
    plt.show()

    # 4 Grafico de personas por precio de la vivienda Numerico
    vivienda = np.array(df['vivienda'])
    plt.title('vivienda')
    plt.hist(vivienda, bins=60)
    plt.xlabel("Costo vivienda")
    plt.ylabel("Frecuencia")
    plt.grid(True)
    plt.show()
    plt.clf()

    # 5 Grafico porcentaje de personas por rangos de ingresos Numerico
    rangos = (("[0,3502)", "[3502,4996)",
               "[4996,6490)", "[6490,inf)"))
    ingresos = np.array(df['ingresos'])
    arreglo = np.array([0, 0, 0, 0])
    for i in range(0, len(ingresos)):
        if(ingresos[i] < 3502):
            arreglo[0] += 1
        if(ingresos[i] >= 3502 and ingresos[i] < 4996):
            arreglo[1] += 1
        if(ingresos[i] >= 4996 and ingresos[i] < 6490):
            arreglo[2] += 1
        if(ingresos[i] >= 6490):
            arreglo[3] += 1
    colores = ('red', 'blue', 'green', 'yellow')
    plt.pie(arreglo, colors=colores, labels=rangos, autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Grafico Ingresos")
    plt.show()

    # 6 numero de personas con un rango de gastos numerico
    gastoscomunes = np.array(df['gastos_comunes'])
    rango = ("menos 300", "gatos entre 300 y 600",
             "gatos entre 600 y 900", "gatos entre 900 y 1200", "mas de 1200")
    posicion_y = np.arange(len(rango))

    arreglo = np.array([0, 0, 0, 0, 0])
    for i in range(0, len(gastoscomunes)):
        if(gastoscomunes[i] < 300):
            arreglo[0] += 1
        if(gastoscomunes[i] >= 300 and gastoscomunes[i] < 600):
            arreglo[1] += 1
        if(gastoscomunes[i] >= 600 and gastoscomunes[i] < 900):
            arreglo[2] += 1
        if(gastoscomunes[i] >= 900 and gastoscomunes[i] < 1200):
            arreglo[3] += 1
        if(gastoscomunes[i] >= 1200):
            arreglo[4] += 1

    plt.barh(posicion_y, arreglo, align="center")
    plt.yticks(posicion_y, rango, rotation=45)
    plt.xlabel('Frecuencia')
    plt.title("Gastos")
    plt.show()

    # 7 Numero de personas que ahorran en cada rango
    sns.lmplot('ingresos', 'pago_coche', df, hue='comprar', fit_reg=False)
    fig = plt.gcf()
    fig.set_size_inches(15, 10)
    plt.show()


'''
'''


def main():
    describirDatos()
    limpieza()
    graficar()


if __name__ == '__main__':
    main()

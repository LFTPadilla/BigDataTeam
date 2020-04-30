import pandas as pd
from matplotlib import pyplot as plt
import numpy as np





'''
Funcion que nos permite conocer los tipos de datos que tenemos en el dataset
'''
def describirDatos():
    df = pd.read_csv(r"Actividad2-limpieza/info/comprar_alquilarConRuido.csv")
    df = df.astype({"estado_civil": str, "trabajo": str,"comprar": str})


    print("-------TIPOS DE VARIABLES-------")
    print(df.dtypes)
    print("-------DATOS RESULTANTES-------")
    print(df.describe(percentiles=[],include='all'))
    print("-------MEDIANAS-------")
    print(df.median(numeric_only=True))
    return df
'''
'''
def eliminarAtipicos(df):
    print("-------GRAFICO DE CAJAS Y BIGOTES-------")
    #TODO Identifique y elimine filas con datos atípicos.
    
    '''
    cols=list(df._get_numeric_data().columns)
    print(df.boxplot(column=cols))#obtengo boxplot
     
    # si valor<cuartil1-3*rangoIntercuartil ó  valor>cuartil2+3*rangoIntercuartil se elimina la fila
    cuartiles=df.quantile([.25,.75],numeric_only=True).toList()#aquí obtengo los cuartiles 1 y 3
    """ rangoIntercuartil=
    print(list(df.quantile([.25,.75],numeric_only=True)))
    front
    #formular para datos atipicos
    
    for col in cols:
        
    new_df = new_df.join(df[(df[col] > P[0]]) & (df[col] < P[1])], how='inner') """
    ''' 
    return

def limpieza(df):
    print("-------CAMPOS VACIOS-------")
    print(df.isna().sum())
    print("-------SE LLENAN LOS CAMPOS VACIOS CON LA MEDIA-------")
    df=df.fillna(df.mean())
    # print(df.isna().sum())
    #TODO eliminar filas si tienen muchos campos vacios (no necesaria para esta actividad)
    #TODO Eliminar columnas con mas del 30% de datos faltantes (no necesaria para esta actividad)
    #TODO Revisar diapositivas para revisar que otras medidas se pueden tomar
    return eliminarAtipicos(df)


'''
Funcion que realiza los diferentes tipos de graficas
'''
def graficar():

    df = pd.read_csv(r"Actividad2-limpieza/info/comprar_alquilarConRuido.csv")
    
    #Grafico de  hijos respecto al estado civil Categorica
    estado_civil=np.array(df['estado_civil'])
    hijos=np.array(df['hijos'])
    plt.bar(estado_civil,hijos)
    plt.title("Numero de hijos variando el esta civil")
    plt.xlabel("estado_civil")
    plt.ylabel("hijos")
    plt.show()

    #Cantidad de personas por estado civil categorico
    estado_civil=np.array(df['estado_civil'])
    plt.title('estado_civil')
    plt.hist(estado_civil, bins = 60)
    plt.xlabel("estado civil")
    plt.ylabel("Cantidad de usuarios por estado civil")
    plt.grid(True)
    plt.show()
    plt.clf()

    #cantidad de personas con cada tipo de trabajo categorico
    trabajo=np.array(df['trabajo'])
    trabajoT=np.array([0,0,0,0,0,0,0,0])
    for i in range(0,len(trabajo)):
        if(trabajo[i] ==0):
            trabajoT[0]+=1
        if(trabajo[i] ==2):
            trabajoT[1]+=1
        if(trabajo[i] ==3):
            trabajoT[2]+=1
        if(trabajo[i] ==4):
            trabajoT[3]+=1
        if(trabajo[i] ==5):
            trabajoT[4]+=1
        if(trabajo[i] ==6):
            trabajoT[5]+=1
        if(trabajo[i] ==7):
            trabajoT[6]+=1
        if(trabajo[i] ==8):
            trabajoT[7]+=1
    plt.plot(trabajoT)
    plt.title("Grafica")
    plt.xlabel("Tipo de trabajo")
    plt.ylabel("Personas")
    plt.show()






    #Grafico de personas por precio de la vivienda Numerico
    vivienda=np.array(df['vivienda'])
    plt.title('vivienda')
    plt.hist(vivienda, bins = 60)
    plt.xlabel("Costo vivienda")
    plt.ylabel("Numero Usuarios")
    plt.grid(True)
    plt.show()
    plt.clf()
    

    #Grafico porcentaje de personas por rangos de ingresos Numerico
    rangos=(("menor 4000","ingresos entre 4000 y 5000","5000 >= ingresos < 6000","mayor 6000"))
    ingresos=np.array(df['ingresos'])
    arreglo=np.array([0,0,0,0])
    for i in range(0,len(ingresos)):
        if(ingresos[i] < 4000):
            arreglo[0]+=1
        if(ingresos[i] >= 4000 and ingresos[i] < 5000):
            arreglo[1]+=1
        if(ingresos[i] >= 5000 and ingresos[i] < 6000):
            arreglo[2]+=1
        if(ingresos[i] >= 6000):
            arreglo[3]+=1
    colores=('red','blue','green','yellow')
    plt.pie(arreglo, colors=colores, labels=rangos,autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Grafico Pastel")
    plt.show()   
        
    
    # numero de personas con un rango de gastos numerico
    gastoscomunes=np.array(df['gastos_comunes'])
    rango = ("menos 300","gatos entre 300 y 600","gatos entre 600 y 900", "gatos entre 900 y 1200","mas de 1200")
    posicion_y = np.arange(len(rango))

    arreglo=np.array([0,0,0,0,0])
    for i in range(0,len(gastoscomunes)):
        if(gastoscomunes[i] < 300):
            arreglo[0]+=1
        if(gastoscomunes[i] >= 300 and gastoscomunes[i] < 600):
            arreglo[1]+=1
        if(gastoscomunes[i] >= 600 and gastoscomunes[i] < 900):
            arreglo[2]+=1
        if(gastoscomunes[i] >= 900 and gastoscomunes[i] < 1200):
            arreglo[3]+=1
        if(gastoscomunes[i] >= 1200):
            arreglo[4]+=1

    plt.barh(posicion_y, arreglo, align = "center")
    plt.yticks(posicion_y, rango)
    plt.xlabel('Unidades vendidas')
    plt.title("Gastos")
    plt.show()
   

    #Numero de personas que ahorran en cada rango
    rangos=(("menor 300"," entre 300 y 600"," entre 600 y 900","mayor 900"))
    ahorros=np.array(df['ahorros'])
    arreglo=np.array([0,0,0,0])
    for i in range(0,len(ahorros)):
        if(ahorros[i] < 45000):
            arreglo[0]+=1
        if(ahorros[i] >= 45000 and ahorros[i] < 55000):
            arreglo[1]+=1
        if(ahorros[i] >= 55000 and ahorros[i] < 65000):
            arreglo[2]+=1
        if(ahorros[i] >= 65000 ):
            arreglo[3]+=1
    plt.bar(rangos,arreglo)
    plt.title("Ahorro")
    plt.xlabel("ahorros")
    plt.ylabel("persona")
    plt.show()

    

'''
'''
def main():
    #df=describirDatos()
    #df=limpieza(df)
    graficar()


if __name__ == '__main__':
    main()
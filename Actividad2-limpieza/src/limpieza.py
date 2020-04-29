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
    '''
    estado_civil=np.array(df['estado_civil'])
    hijos=np.array(df['hijos'])
    plt.bar(estado_civil,hijos)
    plt.title("Numero de hijos variando el esta civil")
    plt.xlabel("estado_civil")
    plt.ylabel("hijos")
    plt.show()


    vivienda=np.array(df['vivienda'])
    plt.title('vivienda')
    plt.hist(vivienda, bins = 60)
    plt.xlabel("Costo vivienda")
    plt.ylabel("Numero Usuarios")
    plt.grid(True)
    plt.show()
    plt.clf()
    '''



    ingresos=np.array(df['ingresos'])
    i=np.array([0,0,0,0])
    for i in range(0,len(ingresos)):
        if(ingresos[i]>=0 or ingresos[i]<2000  ):
            i[:0]=str(1)
        if(ingresos[i]>= 2000 or ingresos[i]<4000  ):
            i[:1]=i[:1]+1
        if(ingresos[i]>=4000 or ingresos[i]<6000  ):
            i[:2]=i[:2]+1
        if(ingresos[i]>=6000 or ingresos[i]<8000  ):
            i[:3]=i[:3]+1

    print(i)
   
    '''
    for i in range(0,len(ingresos)):
        if(comprar[i]==1):
            ingresos
    
    '''

    #print(gastosComunes)
    '''
    hijos=((0,1,2,3))
    cantidadHijos=((12,23,10,2))
    colores=('red','blue','green','yellow')
    plt.pie(cantidadHijos, colors=colores, labels=hijos,autopct='%1.1f%%')
    plt.axis('equal')
    plt.title("Grafico Pastel")
    plt.show()


    plt.plot(hijos,cantidadHijos)
    plt.title("Grafica")
    plt.xlabel("X")
    plt.ylabel("T")
    plt.show()


    plt.bar(hijos,cantidadHijos)
    plt.title("Grafica barras ")
    plt.xlabel("X")
    plt.ylabel("T")
    plt.show()
    '''
    

'''
'''
def main():
    #df=describirDatos()
    #df=limpieza(df)
    graficar()


if __name__ == '__main__':
    main()
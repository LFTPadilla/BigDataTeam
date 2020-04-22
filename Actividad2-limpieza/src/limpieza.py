import pandas as pd
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

def eliminarAtipicos(df):
    print("-------GRAFICO DE CAJAS Y BIGOTES-------")
    #TODO Identifique y elimine filas con datos atípicos.
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

def graficar(df):
    """ TODO Realice gráficos diferentes para variables categóricas y 
    4 diferentes para variables numéricas. Explicar cada uno de los gráficos. """
    return


def main():
    df=describirDatos()
    df=limpieza(df)
    graficar(df)


if __name__ == '__main__':
    main()
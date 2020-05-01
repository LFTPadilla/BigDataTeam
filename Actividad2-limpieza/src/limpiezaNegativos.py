import csv
import numpy
import os
import re
from pathlib import Path
def limpiar():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, r"../info/comprar_alquilarConRuido.csv")
    reader = csv.reader(open(filename, "r"), delimiter=",")
    x = list(reader)
    head = numpy.array(x)[0]
    result = numpy.array(x)[1:]


    for i in range(len(result)):
        for j in range(len(result[i])):     
            if result[i][j]!="" and int(result[i][j]) < 0:
                result[i][j] = int(result[i][j])*-1
                

    result = numpy.vstack([head, result])

    filename2 = os.path.join(dirname, r"../info/comprar_alquilarSinNegativos.csv")

    numpy.savetxt(filename2, result, fmt='%s', delimiter=",")

limpiar()
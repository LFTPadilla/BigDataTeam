import csv
import numpy
import os
import re
import array
from pathlib import Path


def limpiar():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(
        dirname, r'../info/comprar_alquilarFilasLimpias.csv')
    reader = csv.reader(open(filename, "r"), delimiter=",")
    x = list(reader)
    result = numpy.array(x).astype("str")

    tolerancia = 3
    encontrado = 0
    extra = 0
    result2 = result

    for i in range(len(result[0])):
        for j in range(len(result)):
            if result[j][i] == '':
                encontrado = encontrado+1
        if encontrado > tolerancia:
            result2 = numpy.delete(result2, i-extra, 1)
            extra = extra+1

        encontrado = 0

    filename2 = os.path.join(
        dirname, r'../info/comprar_alquilarColumnasLimpias.csv')
    numpy.savetxt(filename2, result2, fmt='%s', delimiter=",")


limpiar()
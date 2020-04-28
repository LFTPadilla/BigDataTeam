import csv
import numpy
import os
from pathlib import Path

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'comprar_alquilarSinNegativos.csv')
reader = csv.reader(open(filename, "r"), delimiter=",")
x = list(reader)
result = numpy.array(x).astype("str")

tolerancia=0
encontrado=0
extra=0
result2 = result

for i in range(len(result)):
    for j in range(len(result[i])):
        if result[i][j] == '':
            encontrado=encontrado+1
    if encontrado > tolerancia:
        result2 = numpy.delete(result2, i-extra, 0)
        extra=extra+1
    encontrado=0

filename2 = os.path.join(dirname, 'comprar_alquilarFilasLimpias.csv')

numpy.savetxt(filename2, result2, fmt='%s', delimiter=",")
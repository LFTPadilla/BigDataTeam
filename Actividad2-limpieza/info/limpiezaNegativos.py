import csv
import numpy
import os
import re
from pathlib import Path

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'comprar_alquilarConRuido.csv')
reader = csv.reader(open(filename, "r"), delimiter=",")
x = list(reader)
result = numpy.array(x).astype("str")

pattern = re.compile(r'^-.$')

for i in range(len(result)):
    for j in range(len(result[i])):
        if pattern.search(result[i][j]):
            result[i][j] = ''


filename2 = os.path.join(dirname, 'comprar_alquilarSinNegativos.csv')

numpy.savetxt(filename2, result, fmt='%s', delimiter=",")
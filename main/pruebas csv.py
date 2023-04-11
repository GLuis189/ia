import csv
import numpy as np
from pathlib import Path

json_store_path = str(Path.home()) + r"\PycharmProjects\ia\csv/"
apagado = json_store_path + "Apagado.csv"
encendido = json_store_path + "Encendido.csv"
vfile = json_store_path + "vfile.csv"
C_ENCENDIDO = 1
C2_APAGADO = 1

"""with open(apagado, "r", newline='') as csvfile:
    reader = csv.reader(csvfile)
with open(encendido, "r", newline='') as csvfile:
    reader = csv.reader(csvfile)"""

matrix_on = np.loadtxt(encendido, delimiter=',')
matrix_off = np.loadtxt(apagado, delimiter=',')

with open(vfile, "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    b = True
    for row in matrix_on:
        if b:
            b = False
        else:
            writer.writerow([row[0], 0])

matrix_v = np.loadtxt(vfile, delimiter=',')
np.insert(matrix_v, 0, 6.3)
print(matrix_v)



end = False
#while not end:



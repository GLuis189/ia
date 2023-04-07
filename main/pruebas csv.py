import csv
import numpy as np
from pathlib import Path

json_store_path = str(Path.home()) + r"\PycharmProjects\ia\csv/"
off = json_store_path + "OFF.csv"
on = json_store_path + "OFF.csv"
apagado = json_store_path + "Apagado.csv"
encendido = json_store_path + "Encendido.csv"

with open(apagado, newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

"""matrix = np.loadtxt(apagado, delimiter=',')
for row in matrix:
    print(row)"""
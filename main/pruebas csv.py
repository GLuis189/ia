import csv
from pathlib import Path

csv_store_path = str(Path.home()) + r"\PycharmProjects\ia\csv/"
apagado = csv_store_path + "Apagado.csv"
encendido = csv_store_path + "Encendido.csv"
vfile = csv_store_path + "vfile.csv"
C_ENCENDIDO = 1
C2_APAGADO = 1
def printm(matrix):
    for row in matrix:
        print(row)

def tofloat(matrix):
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] = float(matrix[row][column])

with open(apagado, "r", newline='') as csvfile:
    reader = csv.reader(csvfile)
    matrix_off = list(reader)

with open(encendido, "r", newline='') as csvfile:
    reader = csv.reader(csvfile)
    matrix_on = list(reader)

tofloat(matrix_on)
tofloat(matrix_off)

with open(vfile, "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in matrix_on:
        writer.writerow([row[0], 0])

with open(vfile, "r", newline='') as csvfile:
    reader = csv.reader(csvfile)
    matrix_v = list(reader)

tofloat(matrix_v)

"""print("Matriz ON  ----------------------------------------")
printm(matrix_on)
print("Matriz OFF ----------------------------------------")
printm(matrix_off)
print("Matriz V ----------------------------------------")
printm(matrix_v)"""

def bellman():
    for i in range(len(matrix_on)):
        suma_on = C_ENCENDIDO
        suma_off = C2_APAGADO
        if i != 12:
            for j in range(len(matrix_on[i])):
                if matrix_on[i][j] != 0:
                    suma_on += matrix_on[i][j] * matrix_v[j][-1]
                if matrix_off[i][j] != 0:
                    suma_off += matrix_off[i][j] * matrix_v[j][-1]
            v = round(min(suma_on, suma_off), 3)
            matrix_v[i].append(v)
        else:
            matrix_v[i].append(0)


def calcular_v():
    fin = True
    while fin:
        if matrix_v[0][-1] == matrix_v[0][-2]:
            fin = False
        else:
            bellman()

calcular_v()

with open(vfile, "w", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    for row in matrix_v:
        writer.writerow(row)

#printm(matrix_v)

v_final = []
for i in range(len(matrix_v)):
    v_final.append(matrix_v[i][-1])

print(v_final)

def politica(v_final):
    politica = []
    for i in range(len(matrix_on)):
        suma_on = C_ENCENDIDO
        suma_off = C2_APAGADO
        for j in range(len(matrix_on[i])):
            if matrix_on[i][j] != 0:
                suma_on += matrix_on[i][j] * v_final[j]
            if matrix_off[i][j] != 0:
                suma_off += matrix_off[i][j] * v_final[j]
        if suma_on<suma_off:
            politica.append("On")
        elif suma_on>suma_off:
            politica.append("Off")
        """elif suma_on==suma_off and suma_on != 0:
            if C_ENCENDIDO<C2_APAGADO:
                politica.append("On")
            else:
                politica.append("Off")"""

    return politica

print(politica(v_final))


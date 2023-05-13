import csv
import random as rnd
from pathlib import Path

csv_store_path = str(Path.home()) + r"\PycharmProjects\ia\csv/"
apagado = csv_store_path + "Apagado.csv"
encendido = csv_store_path + "Encendido.csv"
vfile = csv_store_path + "vfile.csv"
C_ENCENDIDO = 2.0
C_APAGADO = 0.5
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

matrix_v = []
i= 0
for row in matrix_on:
    matrix_v.append([16.0 + i, 0.0])
    i += 0.5

"""print("Matriz ON  ----------------------------------------")
printm(matrix_on)
print("Matriz OFF ----------------------------------------")
printm(matrix_off)
print("Matriz V ----------------------------------------")
printm(matrix_v)"""

def bellman():
    for i in range(len(matrix_on)):
        suma_on = C_ENCENDIDO
        suma_off = C_APAGADO
        if i != 12:
            for j in range(len(matrix_on[i])):
                if matrix_on[i][j] != 0:
                    suma_on += matrix_on[i][j] * matrix_v[j][-1]
                if matrix_off[i][j] != 0:
                    suma_off += matrix_off[i][j] * matrix_v[j][-1]
            v = round(min(suma_on, suma_off), 2)
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
print("-------------------------------------------------------------------")
print("Los valores V estabilizados son: ")
print(v_final)

politica = []
def c_politica(v_final):
    for i in range(len(matrix_on)):
        suma_on = C_ENCENDIDO
        suma_off = C_APAGADO
        for j in range(len(matrix_on[i])):
            if matrix_on[i][j] != 0:
                suma_on += matrix_on[i][j] * v_final[j]
            if matrix_off[i][j] != 0:
                suma_off += matrix_off[i][j] * v_final[j]
        if suma_on<suma_off:
            politica.append("On")
        elif suma_on>suma_off:
            politica.append("Off")

c_politica(v_final)

print("-------------------------------------------------------------------")
print("La política óptima es: ")
print(politica)

print("-------------------------------------------------------------------")
for i in range(len(politica)):
    print("Si hace " + str(16+0.5*i) + "º, el termostato debería hacer la acción: " + str(politica[i]) + ".")

print("-------------------------------------------------------------------")

temperatura = 0
while not isinstance(temperatura, float) or (temperatura * 10) % 5 != 0:
    try:
        temperatura = float(input("Introduce la temperatura que hace: "))
    except:
        print("La temperatura debe ser un flotante.")

excepcion = 0
ventana = str(input("¿Quiere introducir el caso de que se pueda abrir una ventana aleatoriamente? (S/N): "))
while ventana != "S" and ventana != "N":
    print("Responde S o N")
    ventana = str(input("¿Quiere introducir el caso de que se pueda abrir una ventana aleatoriamente? (S/N): "))
if ventana == "S":
    excepcion = str(input("¿Hace frío o calor fuera de la casa? (F/C): "))
    while excepcion != "F" and excepcion != "C":
        print("Responde F o C")
        excepcion = str(input("¿Hace frío o calor fuera de la casa? (F/C): "))


def cambio_temp(estado, matriz):
    probabilidad = []
    estados = []
    for i in range(len(matriz[estado])):
        if matriz[estado][i] != 0:
            probabilidad.append(matriz[estado][i])
            estados.append(i)
    return rnd.choices(estados, weights=probabilidad)[0]

def simular(temperatura,excepcion):
    if temperatura == 22.0:
        print("Se ha alcanzado la temperatura ideal.")
        return
    if temperatura<16.0 or temperatura>25.0:
        print("La temperatura no está en el rango del termostato por lo que ha dejado de funcionar.")
        return
    if ventana != 0:
        if excepcion == "F" and temperatura >= 18:
            if rnd.random() < 0.05:
                print("Accidentalemnte se ha abirto una ventana y al hacer frío fuera, la temperatura a bajado 2 grados")
                temperatura -= 2
        if excepcion == "C" and temperatura <= 23:
            if rnd.random() < 0.05:
                print("Accidentalemnte se ha abirto una ventana y al hacer calor fuera, la temperatura a subido 2 grados")
                temperatura += 2
    estado = 0
    for i in range(len(politica)):
        if temperatura == 16+i*0.5:
            estado = i
    accion = politica[estado]
    matriz = None
    if accion == "On":
        matriz = matrix_on
    else:
        matriz = matrix_off
    temperatura2 = 16 + cambio_temp(estado, matriz) * 0.5
    print("Hace " + str(temperatura) + "º, por lo que el termostato toma la acción " + str(accion) + " y pasa a " + str(temperatura2) + "º.")
    return simular(temperatura2, excepcion)

simular(temperatura, excepcion)

print("-------------------------------------------------------------------")


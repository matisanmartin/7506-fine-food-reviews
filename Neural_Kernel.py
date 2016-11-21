import math
import random

import numpy as np

import read_and_process
import svm


def norma(v):
    return math.sqrt(sum(p * q for p, q in zip(v, v)))

def kernel_polinomico(x,w):
    c = 1
    b = 2
    return ((np.inner(x, w) + c) ** b)


train = read_and_process.leer_archivo('./files/train10lines.csv')
test = read_and_process.leer_archivo('./files/test10lines.csv')

COLUMNAS = 293 #7919
FILAS = len(train)  # 11000#len(train) #568454
vector_Id = []
matrix = []
vector_Prediction = []
w = []
for i in range(COLUMNAS):
       w.append(random.random())

for i in range(FILAS):
    matrix.append([])
    for j in range(COLUMNAS):
        matrix[i].append(0)

for indice in range(FILAS):
 vector_Id.append(train[indice]['Id'])
 vector_Prediction.append(float(train[indice]['Prediction']))
 texto = train[indice]['Text'].split()
 for j in range(len(texto)):
     hash_val = hash(texto[j]) % COLUMNAS
     matrix[indice][hash_val] = 1
print(indice)

## Entrenamiento

cantidad_ciclos = 0
factor_aprendizaje = 0.00001
error_cm = 10

while(cantidad_ciclos < 100 and error_cm > 1):

    cantidad_ciclos += 1
    error_c = 0
    print(cantidad_ciclos)
    for i in range(FILAS):
        error = 0
        #salida_obtenida = sum(p * q for p, q in zip(matrix[i], w))
        salida_obtenida = np.inner(matrix[i], w)
        error = vector_Prediction[i] - salida_obtenida
        for j in range(COLUMNAS):
            w[j] += 2 * factor_aprendizaje * error * matrix[i][j]

        error_c += error * error

    error_cm = error_c / FILAS
    print('error promedio: ', error_cm)

matrix.clear()
print('Fin entrenamiento - Kernel Neuron')

## Test

test_Id = []
salida_predicciones = []
mat_aux = []
COLUMNAS2 = COLUMNAS #7919
FILAS2 = len(test) #568454
matriz = []

for i in range(FILAS2):
    matriz.append([])
    for j in range(COLUMNAS2):
        matriz[i].append(0)

for indice in range(FILAS2):
 test_Id.append(test[indice]['Id'])
 texto = test[indice]['Text'].split()
 for j in range(len(texto)):
     hash_val = hash(texto[j]) % COLUMNAS2
     matriz[indice][hash_val] = 1

for j in range(FILAS2):
    #resul = sum(p * q for p, q in zip(matriz[j], w))
    resul = np.inner(matriz[j], w)
    mat_aux.append(resul)

predicciones_svm = svm.calcular_svm()

for i in range(FILAS2):
    prediccion = (0.2 * mat_aux[i] + 0.8 * predicciones_svm[i]['Prediction'])
    salida_predicciones.append({'Id': test_Id[i], 'Prediction': prediccion})

read_and_process.generar_archivo(salida_predicciones)
matriz.clear()

print('Fin test - Kernel Neuron')





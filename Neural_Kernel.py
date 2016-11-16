import file_reading
import math
import random

def norma(v):
    return math.sqrt(sum(p * q for p, q in zip(v, v)))

train = file_reading.leer_archivo('train.csv')
test = file_reading.leer_archivo('test.csv')

COLUMNAS = 293 #7919
FILAS = len(train) #568454
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
error = 1
factor_aprendizaje = 0.001
error_cm = 1

while(cantidad_ciclos < 5 and error_cm > 0.5):

    cantidad_ciclos += 1
    error_c = 0
    print(cantidad_ciclos)
    for i in range(FILAS):
        salida_obtenida = (sum(p * q for p, q in zip(matrix[i], w)))
        error = vector_Prediction[i] - salida_obtenida
        for j in range(COLUMNAS):
            w[j] = w[j] + (2 * factor_aprendizaje * error * matrix[i][j])

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
    resul = sum(p * q for p, q in zip(matriz[j], w))
    mat_aux.append(resul)

for i in range(FILAS2):
    prediccion = mat_aux[i]
    salida_predicciones.append({'Id': test_Id[i], 'Prediction': prediccion})

file_reading.generar_archivo(salida_predicciones)
matriz.clear()

print('Fin test - Kernel Neuron')



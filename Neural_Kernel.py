import math
import random
import numpy as np
import read_and_process
import svm

COLUMNAS = 331  # 7919
FILAS = 100000  # len(train) #568454
predicciones_svm = []
mat_aux = []

def kernel_polinomico(x,w):
    c = 1
    b = 2
    return np.inner(x, w)

def calcular_Nk():
    train = read_and_process.leer_archivo('./files/train.csv','train')
    test = read_and_process.leer_archivo('./files/test.csv','test')

    print('Se leyeron los archivos')
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
        texto = train.Text[indice].split()
        for j in range(len(texto)):
            hash_val = hash(texto[j]) % COLUMNAS
            matrix[indice][hash_val] = 1
    print('Se cargaron los datos')

    ## Entrenamiento

    cantidad_ciclos = 0
    factor_aprendizaje = 0.00001
    error_cm = 10

    while(cantidad_ciclos < 10 and error_cm > 1):

        cantidad_ciclos += 1
        error_c = 0
        print('Ciclo nro: ', cantidad_ciclos)
        for i in range(FILAS):
            error = 0
            salida_obtenida = kernel_polinomico(matrix[i],w)
            error = train.Prediction[i] - salida_obtenida
            for j in range(COLUMNAS):
                w[j] += 2 * factor_aprendizaje * error * matrix[i][j]

            error_c += error * error

        error_cm = error_c / FILAS

    matrix.clear()
    print('Fin entrenamiento - Kernel Neuron')

    ## Test

    salida_predicciones = []
    COLUMNAS2 = COLUMNAS #7919
    FILAS2 = len(test) #568454
    matriz = []

    for i in range(FILAS2):
        matriz.append([])
        for j in range(COLUMNAS2):
            matriz[i].append(0)

    for indice in range(FILAS2):
        texto = test.Text[indice].split()
        for j in range(len(texto)):
            hash_val = hash(texto[j]) % COLUMNAS2
            matriz[indice][hash_val] = 1

    for j in range(FILAS2):
        resul = kernel_polinomico(matriz[j],w)
        mat_aux.append(resul)

    print('Fin test - Kernel Neuron')
    matriz.clear()
    print('Fin - Kernel Neuron')

    predicciones_svm = svm.calcular_svm(train, test)

    for i in range(FILAS2):
        prediccion = (0.1 * mat_aux[i] + 0.9 * predicciones_svm[i]['Prediction'])
        salida_predicciones.append({'Id': test.Id[i], 'Prediction': prediccion})
    #read_and_process.generar_archivo(salida_predicciones)
    return salida_predicciones


def prediccion_Nk(indice):    # indice que va de 0 a len(test) NO ES EL ID!
    prediccion = (0.1 * mat_aux[indice] + 0.9 * predicciones_svm[indice]['Prediccion'])
    return prediccion

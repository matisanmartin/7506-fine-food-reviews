from sklearn import svm
import file_reading

train = file_reading.leer_archivo('train.csv')
test = file_reading.leer_archivo('test.csv')

COLUMNAS = 331 #7919
FILAS = 6000 #454759#len(train) #568454

def calcular_svm():

    matrix = []
    vector_Prediction = []

    for i in range(FILAS):
        matrix.append([])
        for j in range(COLUMNAS):
            matrix[i].append(0)

    for indice in range(FILAS):
        vector_Prediction.append((float(train[indice]['Prediction'])))
        texto = train[indice]['Text'].split()
    for j in range(len(texto)):
        hash_val = hash(texto[j]) % COLUMNAS
        matrix[indice][hash_val] += 1

    clf = svm.SVR()
    clf.fit(matrix, vector_Prediction)
    matrix.clear()
    vector_Prediction.clear()

###### Test

    test_Id = []
    salida_predicciones = []
    COLUMNAS2 = COLUMNAS #7919
    FILAS2 = len(test) #568454

    for i in range(FILAS2):
        matrix.append([])
        for j in range(COLUMNAS2):
            matrix[i].append(0)

    for indice in range(FILAS2):
        test_Id.append(test[indice]['Id'])
        texto = test[indice]['Text'].split()
        for j in range(len(texto)):
            hash_val = hash(texto[j]) % COLUMNAS2
            matrix[indice][hash_val] += 1

    mat_aux = clf.predict(matrix)
    for i in range(FILAS2):
        prediccion = mat_aux[i]
        salida_predicciones.append({'Id': test_Id[i], 'Prediction': prediccion})

    file_reading.generar_archivo(salida_predicciones)
    matrix.clear()

print('Fin')
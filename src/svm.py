from sklearn import svm


# train = read_and_process.leer_archivo('./files/train10lines.csv')
# test = read_and_process.leer_archivo('./files/test10lines.csv')

# COLUMNAS = 331 #7919
#FILAS = len(train)  # 6000 #454759#len(train) #568454

def calcular_svm(train, test):
    COLUMNAS = 331  # 7919
    FILAS = 6000  # 6000 #454759#len(train) #568454
    matrix = []
    vector_Prediction = []

    for i in range(FILAS):
        matrix.append([])
        for j in range(COLUMNAS):
            matrix[i].append(0)

    for indice in range(FILAS):
        vector_Prediction.append((float(train['Prediction'][indice])))
        texto = train['Text'][indice].split()
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
    COLUMNAS2 = 331  #7919
    FILAS2 = len(test) #568454

    for i in range(FILAS2):
        matrix.append([])
        for j in range(COLUMNAS2):
            matrix[i].append(0)

    for indice in range(FILAS2):
        test_Id.append(test['Id'][indice])
        texto = test['Text'][indice].split()
        for j in range(len(texto)):
            hash_val = hash(texto[j]) % COLUMNAS2
            matrix[indice][hash_val] += 1

    mat_aux = clf.predict(matrix)
    for i in range(FILAS2):
        prediccion = mat_aux[i]
        salida_predicciones.append({'Id': test_Id[i], 'Prediction': prediccion})

    matrix.clear()
    return salida_predicciones


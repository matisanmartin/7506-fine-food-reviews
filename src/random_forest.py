import pandas as pd
from sklearn.ensemble import RandomForestClassifier


def do_random_forest(test, train):
    COLUMNAS = 7919
    matrix = []
    matrix1 = []
    vector_Prediction = []
    print("Starting Random Forest")
    FILAS = len(train)
    ###### Preparando los datos para tenerlo en el formato correcto-------------------------
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

    ###### Utilizamos la implementacion para entrenar el algoritmo----------------------
    rf = RandomForestClassifier(bootstrap=True, criterion='gini',
                                max_depth=None, max_features='auto',
                                min_samples_leaf=1, min_samples_split=2,
                                n_estimators=200, n_jobs=1,
                                oob_score=False, random_state=None, verbose=0)
    rf.fit(matrix, vector_Prediction)

    ###### Test--------------------------------------------------------------------------

    test_Id = []
    salida_predicciones = []
    COLUMNAS2 = COLUMNAS  # 7919
    FILAS2 = len(test)  # 568454

    for i in range(FILAS2):
        matrix1.append([])
        for j in range(COLUMNAS2):
            matrix1[i].append(0)

    for indice in range(FILAS2):
        test_Id.append(test['Id'][indice])
        texto = test['Text'][indice].split()
        for j in range(len(texto)):
            hash_val = hash(texto[j]) % COLUMNAS2
            matrix1[indice][hash_val] += 1

    ###### Predecir :)------------------------------------------------------------------------
    mat_aux = rf.predict(matrix1)

    ###### Generar salida para submittear-----------------------------------------------------
    for i in range(FILAS2):
        prediccion = mat_aux[i]
        salida_predicciones.append({'Id': test_Id[i], 'Prediction': prediccion})
    print("Finished Random Forest")
    return pd.DataFrame(salida_predicciones)

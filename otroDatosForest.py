from sklearn.ensemble import RandomForestClassifier 
import pandas as pd
from numpy import savetxt
import numpy as np
import matplotlib.pyplot as plt

# CARGAR DATASET -----------------------------------------------------------------
train = pd.read_csv('train10lines.csv')
test = pd.read_csv('test10lines.csv')
featureAPredecir = 'Prediction' # Nombre del feature a predecir
headers = train.columns.values.tolist()
headers.remove(featureAPredecir)

# TRAIN y TEST-------------------------------------------------------------------
columnas = ['Id','HelpfulnessNumerator','HelpfulnessDenominator','Summary','Text'] 
colResultado = ['Prediction']
data_train  = train.as_matrix(columnas)
data_test   = test.as_matrix(columnas)
clase_train = train.as_matrix(colResultado)
clase_test  = test.as_matrix(colResultado)

# Preparando los datos :)-------------------------------------------------------
# Aplicar el tokenizado a los strings
for fil in range(0,(len(data_train))):
	for col in range(0,5):
		if (col == 3):	
			data_train[fil][col] = data_train[fil][col].split()
		if (col == 4):	
			data_train[fil][col] = data_train[fil][col].split()
for fil in range(0,(len(data_test))):
	for col in range(0,5):
		if (col == 3):	
			data_test[fil][col] = data_test[fil][col].split()
		if (col == 4):	
			data_test[fil][col] = data_test[fil][col].split()

# Entrenando el algoritmo :)-------------------------------------------------------
rf = RandomForestClassifier(
 random_state      = 1,   # semilla inicial de aleatoriedad del algoritmo
 n_estimators      = 100, # cantidad de arboles a crear
 min_samples_split = 2,   # cantidad minima de observaciones para dividir un nodo
 min_samples_leaf  = 1,   # observaciones minimas que puede tener una hoja del arbol
 n_jobs            = 1    # tareas en paralelo. para todos los cores disponibles usar -1
 )
rf.fit(X = data_train, y = clase_train)

# A predecir :o--------------------------------------------------------------------
prediccion = rf.predict(data_test)

#Guardamos el archivo para el submission-------------------------------------------
np.savetxt('sampleSubmissionUNO.csv', np.c_[range(1,len(test)+1),prediccion], delimiter=',', header = 'Id,Prediction', comments = '', fmt='%f')


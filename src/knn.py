####################################################################################
# Modulo con funciones de KNN
####################################################################################
import operator


# Devuelve los k vecinos mas cercanos
# @params:
#   test_point: Punto de prueba
#   data: Listado de puntos a comparar
#   k: Cantidad de vecinos
#   distance: Distancia a utilizar
# @returns:
#   una lista de los k vecinos ordenada descendientemente
def knn(test_point, data, k, distance):
    selected = k
    dist = [{'Id': d['Id'],
             'Prediction': d['Prediction'],
             'Distance': distance(test_point, d['Text'])} for d in data]
    if len(dist) < k:
        selected = len(dist)
    return sorted(dist, key=operator.itemgetter('Distance'), reverse=True)[:selected]


# Calcula el promedio de las predicciones para los k vecinos mas cercanos
# @params
#   nearest_neighbours: Los k vecinos mas cercanos
# @returns:
#   la prediccion
def calculate_prediction(nearest_neighbours):
    # Calificacion por defecto si no hay vecinos mas cercanos
    if len(nearest_neighbours) == 0:
        return 5
    prediction = float(sum([neighbour['Prediction'] for neighbour in nearest_neighbours])) / len(nearest_neighbours)
    return prediction


# Devuelve un set de shingles
# @params:
#   text: texto a procesar
#   shingle_length: longitud del shingle
# @returns:
#   set de shingles
def get_shingles(text, shingle_length):
    return set([text[i:i + shingle_length] for i in range(len(text) - shingle_length + 1)])


# Implementacion de distancia de jaccard
# PRE: sh1 y sh2 es un vector de shingles sin repetidos
# @params:
#   s1, s2: puntos a calcular la distancia
# @returns:
#   la distancia
def jaccard_distance(s1, s2):
    shingle_length = 4
    set1 = get_shingles(s1, shingle_length)
    set2 = get_shingles(s2, shingle_length)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return 1 - (float(len(intersection)) / len(union))
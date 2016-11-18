####################################################################################
# Modulo con funciones de KNN
####################################################################################


# Devuelve los k vecinos mas cercanos
# @params:
#   test_point: Punto de prueba
#   data: Listado de puntos a comparar
#   k: Cantidad de vecinos
#   distance: Distancia a utilizar
# @returns:
#   una lista de los k vecinos ordenada descendientemente
def knn(test_point, data, k, distance):
    distances = []
    test_shingles = get_shingles(test_point, 3)
    for d in data:
        d_shingles = get_shingles(d, 3)
        dist = distance(test_shingles, d_shingles)
        distances.append({d['Id'], dist})

    if len(distances) < k:
        k = len(distances)

    return sorted(distances, key=operator.itemgetter('Id'), reverse=True)[:k]


# Calcula el promedio de las predicciones para los k vecinos mas cercanos
# @params
#   nearest_neighbours: Los k vecinos mas cercanos
# @returns:
#   la prediccion
def calculate_prediction(nearest_neighbours):
    sum = 0
    for neighbour in nearest_neighbours:
        sum += neighbour
    return float(sum) / len(nearest_neighbours)


# Devuelve un set de shingles
# @params:
#   text: texto a procesar
#   shingle_length: longitud del shingle
# @returns:
#   set de shingles
def get_shingles(text, shingle_length):
    return set([text[i:i + shingle_length] for i in range(len(text) - shingle_length + 1)])


# Implementacion de distancia de Levenshtein
# @params:
#   s1,s2: puntos a calcular la distancia
# @returns:
#   la distancia
def levenshtein_distance(s1, s2):
    # TODO IMPLEMENTAR
    return ""


# Implementacion de distancia de jaccard
# PRE: sh1 y sh2 es un vector de shingles sin repetidos
# @params:
#   s1,s2: puntos a calcular la distancia
# @returns:
#   la distancia
def jaccard_distance(s1, s2):
    shingle_length = 4
    set1 = get_shingles(s1, shingle_length)
    set2 = get_shingles(s2, shingle_length)
    intersection = set1.intersection(set2)
    union = set1.union(set2)
    return 1 - (float(intersection) / union)


# Implementacion de distancia Most Frequent K chars
# @params:
#   s1,s2: puntos a calcular la distancia
# @returns:
#   la distancia
def most_frequent_k_chars_distance(s1, s2):
    # TODO IMPLEMENTAR
    return ""

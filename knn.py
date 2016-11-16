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
    distances = []
    test_shingles = get_shingles(test_point, 3)
    for d in data:
        d_shingles = get_shingles(d, 3)
        dist = distance(test_shingles, d_shingles)
        distances.append({d['Id'], dist})
    return sorted(distances, key=operator.itemgetter('Id'), reverse=True)[:k]


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


# Calcula la eficiencia de cada k
# Comienza en K=2 y sigue hasta N-1
# Evita el caso NN y el caso donde K = N
# params:
#   text = [{id,prediction, text}]
#   data = [{id, prediction, text}]
# returns:
#   el diccionario con las eficiencias para cada K
def grid_search(test, data, distance):
    num_of_assertions = 0
    efficiency_dict = {}
    for k in range(2, data.length - 1):
        for t in test:
            actual_prediction = knn(t, data, k, distance)
            expected_prediction = t['Prediction']
            if actual_prediction == expected_prediction:
                num_of_assertions += 1

        efficiency_dict[k] = float(num_of_assertions) / t.length
        num_of_assertions = 0
    return efficiency_dict


# Realiza el grid search para cada funcion de distancia
# Toma la maxima eficiencia para cada distancia y el valor de k asociado
# La escribe a un archivo txt
# @params:
#   test: Set de prueba
#   data: Set
# @returns:
#   -
def grid_search_func(test, data):
    # Efficiency for jaccard_distance for all k
    efficiency_dict_k_jaccard = grid_search(test, data, jaccard_distance)
    max_k_jaccard = max(efficiency_dict_k_jaccard.iteritems(), key=operator.itemgetter(1))[0]
    max_eff_jaccard = max(efficiency_dict_k_jaccard.iteritems(), key=operator.itemgetter(1))[1]

    # Efficiency for levenshtein distance for all k
    efficiency_dict_k_levenshtein = grid_search(test, data, levenshtein_distance)
    max_k_levenshtein = max(efficiency_dict_k_levenshtein.iteritems(), key=operator.itemgetter(1))[0]
    max_eff_levenshtein = max(efficiency_dict_k_levenshtein.iteritems(), key=operator.itemgetter(1))[1]

    # Efficiency for most frequent k distance for all k
    efficiency_dict_k_most_freq = grid_search(test, data, most_frequent_k_chars_distance)
    max_k_most_freq = max(efficiency_dict_k_most_freq.iteritems(), key=operator.itemgetter(1))[0]
    max_eff_most_freq = max(efficiency_dict_k_most_freq.iteritems(), key=operator.itemgetter(1))[1]

    max_eff_dict = {'jaccard': max_k_jaccard + ',' + max_eff_jaccard,
                    'levenshtein': max_k_levenshtein + ',' + max_eff_levenshtein,
                    'most_frequent_k_chars': max_k_most_freq + ',' + max_eff_most_freq}

    with open('max_efficiency_distances.txt', 'w') as result_file:
        result_file.write(str(max_eff_dict))

import operator

import lsh_knn

from src import knn


# Calcula la eficiencia de cada k
# Comienza en K=2 y sigue hasta N-1
# Evita el caso NN y el caso donde K = N
# params:
#   text = [{id,prediction, text}]
#   data = [{id, prediction, text}]
# returns:
#   el diccionario con las eficiencias para cada K
def grid_search(test, data, distance, n_vec, b):
    num_of_assertions = 0
    efficiency_dict = {}
    for k in range(2, data.length - 1):
        for t in test:
            tables = lsh_knn.load_test_file(test, n_vec, b)
            result = lsh_knn.lsh_knn(t['Text'], tables, n_vec, k, distance)
            actual_prediction = result['Prediction']
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
    n_vec = []  # TODO inicializar
    b = 2  # TODO inicializar
    # Efficiency for jaccard_distance for all k
    efficiency_dict_k_jaccard = grid_search(test, data, knn.jaccard_distance, n_vec, b)
    max_k_jaccard = max(efficiency_dict_k_jaccard.iteritems(), key=operator.itemgetter(1))[0]
    max_eff_jaccard = max(efficiency_dict_k_jaccard.iteritems(), key=operator.itemgetter(1))[1]

    # Efficiency for levenshtein distance for all k
    efficiency_dict_k_levenshtein = grid_search(test, data, knn.levenshtein_distance, n_vec, b)
    max_k_levenshtein = max(efficiency_dict_k_levenshtein.iteritems(), key=operator.itemgetter(1))[0]
    max_eff_levenshtein = max(efficiency_dict_k_levenshtein.iteritems(), key=operator.itemgetter(1))[1]

    # Efficiency for most frequent k distance for all k
    efficiency_dict_k_most_freq = grid_search(test, data, knn.most_frequent_k_chars_distance, n_vec, b)
    max_k_most_freq = max(efficiency_dict_k_most_freq.iteritems(), key=operator.itemgetter(1))[0]
    max_eff_most_freq = max(efficiency_dict_k_most_freq.iteritems(), key=operator.itemgetter(1))[1]

    max_eff_dict = {'jaccard': max_k_jaccard + ',' + max_eff_jaccard,
                    'levenshtein': max_k_levenshtein + ',' + max_eff_levenshtein,
                    'most_frequent_k_chars': max_k_most_freq + ',' + max_eff_most_freq}

    with open('max_efficiency_distances.txt', 'w') as result_file:
        result_file.write(str(max_eff_dict))

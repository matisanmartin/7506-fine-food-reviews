####################################################################################
# Modulo con funciones de LSH
# URL para buscar numeros primos: http://primes.utm.edu/lists/small/millions/
####################################################################################
import numpy as np

from src import knn

# numero de funciones de hash por grupo
r = 3

# numero de tablas
b = 2

# numero total de funciones de hashing
N = r * b

# Numero primo (ver de buscar uno mas grande)
p = 32416187567

# Constante para Funcion de Carter-Wegman de vectores
a_cw_vec = np.array(
    [19178834524, 8344704755, 15698913317, 4719604898, 19883937217, 5284153007, 21023730824, 25818413334,
     146242782, 11187741669, 11385602053, 20132032496, 2705376234, 10540204876, 31420354654, 29963935299,
     10948069430, 15033652456, 25723612166, 31342713515])

# Constantes para Funcion de Carter-Wegman de enteros
a_cw_int = 27857283472
c_cw_int = 12422354607

# Constantes para Funcion de Carter-Wegman de strings
a_cw_str = 2562270000
c_cw_str = 7112175649


# Funcion de Carter-Weigman para numeros
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_int(x, n):
    return (a_cw_int * x + c_cw_int % p) % n


# Funcion de Carter-Weigman para strings
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_str(x, n):
    return h_cw_int(sum([ord(x[i]) * (a_cw_str ** i) for i in range(0, len(x))]) % p, n)


# Funcion de Carter Weigman para vectores
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_vec(x, n):
    return (sum([c * a for c, a in zip(x, a_cw_vec)]) % p) % n


# Funcion que obtiene el vector de minhashes de un dato
# @params:
#   d: dato a hashear, el texto
#   n_vec: Contiene los valores de N para las funciones de hashing universal
# @returns:
#   el vector de minhashes del dato
def get_minhashes(d, n_vec):
    mh = []
    i = 0
    shingles = knn.get_shingles(d, 4)
    for n in n_vec:
        hashes = np.array([h_cw_str(s, n) for s in shingles])
        # np.insert(mh, [i], [hashes.min()])
        mh.append(min(hashes))
        i += 1
    return mh


# Funcion que calcula los hashes (posicion) en cada tabla de las r tablas
# para los grupos de r funciones de hash
# @params:
#   d: dato a hashear
#   n_vec: Contiene los valores de N para las funciones de hashing universal
# @returns:
#   Vector con los hash de cada grupo de minhashes
def get_hash_of_minhashes(d, n_vec):
    minhashes = get_minhashes(d, n_vec)
    group_of_hashes = get_group_of_hashes(minhashes, r)
    n = 100000  # TODO cambiar
    hashes = []
    for group in group_of_hashes:
        hashes.append(h_cw_vec(group, n))
    return hashes


# Divide los hashes en grupos de r funciones
# Cortesia de: http://stackoverflow.com/questions/4119070/how-to-divide-a-list-into-n-equal-parts-python
# @params:
#   lst: lista con los hashes
#   sz: tamaño maximo de cada grupo
# @returns:
#   vector de vector de minhashes
def get_group_of_hashes(lst, sz):
    return [lst[i:i + sz] for i in range(0, len(lst), sz)]


# Agrega el dato a cada tabla.
# Se asume que el vector de hashes y el vector de tables son corespondientes
# @params:
#   tables: tablas
#   hashes: los valores de los hashes
# @returns:
#   -
def add_data_to_tables(tables, d, n_vec):
    hashes = get_hash_of_minhashes(d['Text'], n_vec)
    temp_dict = {'Id': d['Id'], 'Text': d['Text'], 'Prediction': d['Prediction']}
    for table, hash_value in zip(tables, hashes):
        try:
            table[hash_value].append(temp_dict)
        except KeyError:
            table[hash_value] = [temp_dict]


# Obiene todos los documentos candidatos de todas las tablas
# @params:
#   minhashes: lista de minhashes del dato
#   tables: lista de tablas
# @returns:
#   todos los candidatos
def get_candidates_from_tables(minhashes, tables):
    candidates = []
    for table, hash_value in zip(tables, minhashes):
        if hash_value in table:
            candidates.extend(table[hash_value])
    return candidates

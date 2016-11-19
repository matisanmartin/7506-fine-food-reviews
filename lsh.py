####################################################################################
# Modulo con funciones de LSH
# URL para buscar numeros primos: http://primes.utm.edu/lists/small/millions/
####################################################################################

# numero de funciones de hash por grupo
r = 2

# numero de tablas
b = 2

# numero total de funciones de hashing
N = r * b

# Numero primo (ver de buscar uno mas grande)
p = 32416187567

a_cw_vec = [19178834524, 8344704755, 15698913317, 4719604898, 19883937217, 5284153007, 21023730824, 25818413334,
            146242782, 11187741669, 11385602053, 20132032496, 2705376234, 10540204876, 31420354654, 29963935299,
            10948069430, 15033652456, 25723612166, 31342713515]

a_cw_int = 27857283472
c_cw_int = 12422354607

a_cw_str = 2562270000
c_cw_str = 7112175649


# Funcion de Carter-Weigman para numeros
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_int(x, n):
    # a = randint(1, p - 1)
    # c = randint(1, p - 1)
    return (a_cw_int * x + c_cw_int % p) % n


# Funcion de Carter-Weigman para strings
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_str(x, n):
    h = 0  # TODO h = init_value
    # a = randint(1, p - 1)
    #    for c in x:
    #        h = (h * a_cw_str + ord(c)) % p

    # c = randint(1, p-1)
    for i in (0, len(x) - 1):
        h += c_cw_str * (a_cw_str ** i)
    return h_cw_int(h % p, n)
    #return h


# Funcion de Carter Weigman para vectores
# @params:
#   x: dato a hashear
#   n: valor para particularizar la funcion
# @returns:
#   el hash
def h_cw_vec(x, n):
    accum = 0
    #a = [randint(1, p - 1) for _ in range(0, len(x))]

    for i in range(0, len(x)):
        accum += a_cw_vec[i] * x[i]
    h = (accum % p) % n
    return h


# Funcion que obtiene el vector de minhashes de un dato
# @params:
#   d: dato a hashear, el texto
#   n_vec: Contiene los valores de N para las funciones de hashing universal
# @returns:
#   el vector de minhashes del dato
def get_minhashes(d, n_vec):
    mh = []
    for i in range(0, len(n_vec)):
        mh.append(h_cw_str(d, n_vec[i]))
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
    group_of_minhashes = get_group_of_minhashes(minhashes, r)
    hashes = []
    n = 1000  # TODO cambiar
    for group in group_of_minhashes:
        hashes.append(h_cw_vec(group, n))
    return hashes


# Divide los minhashes en grupos de r funciones
# Cortesia de: http://stackoverflow.com/questions/4119070/how-to-divide-a-list-into-n-equal-parts-python
# @params:
#   lst: lista con los minhashes
#   sz: tamaño maximo de cada grupo
# @returns:
#   vector de vector de minhashes
def get_group_of_minhashes(lst, sz):
    return [lst[i:i + sz] for i in range(0, len(lst), sz)]


# Agrega el dato a cada tabla.
# Se asume que el vector de hashes y el vector de tables son corespondientes
# @params:
#   tables: tablas
#   hashes: los valores de los hashes
# @returns:
#   -
def add_data_to_tables(tables, d, n_vec):
    hashes = get_hash_of_minhashes(d, n_vec)
    for table, hash_value in zip(tables, hashes):
        if hash_value in table:
            current_list = table[hash_value]
            current_list.append(d)
            table[hash_value] = current_list
        else:
            table[hash_value] = [d]


# Obiene todos los documentos candidatos de todas las tablas
# @params:
#   minhashes: lista de minhashes del dato
#   tables: lista de tablas
# @returns:
#   todos los candidatos
def get_candidates_from_tables(minhashes, tables):
    candidates = []
    for table, hash_value in zip(tables, minhashes):
        candidates.extend(table[hash_value])
    return candidates

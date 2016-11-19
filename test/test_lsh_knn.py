from random import randint

import lsh
import lsh_knn

# Constantes
p = 32416187567
a_vec = [randint(1, p - 1) for _ in range(0, 20)]
a = randint(1, p - 1)
c = randint(1, p - 1)
a_2 = randint(1, p - 1)
c_2 = randint(1, p - 1)
print(a_vec)
print(a_2)
print(c)

# Prueba de hash de CW STR
text = "Hola que tal"
hash_text = lsh.h_cw_str(text, 1000)
hash_text2 = lsh.h_cw_str(text, 1000)
print(hash_text)
print(hash_text2)

# Prueba de hash de CW de VEC
arr2 = [100000, 200000, 30000]
hash_arr2 = lsh.h_cw_vec(arr2, 1000)
hash_arr = lsh.h_cw_vec(arr2, 1000)
print(hash_arr2)
print(hash_arr)

# Creacion de tablas
tables = lsh_knn.create_tables(2)
print(tables)

# Agregado de dato hasheado a tablas
lsh.add_data_to_tables(tables, text, [1000, 2000, 3000, 4000])
print(tables)

# Obtencion de candidatos a partir de los hashes
candidates = lsh.get_candidates_from_tables([203, 534], tables)
print(candidates)

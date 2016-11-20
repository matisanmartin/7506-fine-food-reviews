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
data = {"Id": 1, "Text": "Hola que tal", "Prediction": 4}
hash_text = lsh.h_cw_str(data['Text'], 1000)
hash_text2 = lsh.h_cw_str(data['Text'], 1000)
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
lsh.add_data_to_tables(tables, data, [1000, 2000, 3000, 4000])
print(tables)

d1 = 0.8
d2 = 0.6
r = 5
b = 3
# p1 = 1 - (1-(1-d1)**r)**b
# p2 = 1 - (1-(1-d2)**r)**b

for r in range(1, 6):
    for b in range(1, 6):
        p1 = 1 - (1 - d1 ** r) ** b
        p2 = 1 - (1 - d2 ** r) ** b
        print('r: ' + str(r) + ' b: ' + str(b) + ' p1: ' + str(p1) + ' p2: ' + str(p2))

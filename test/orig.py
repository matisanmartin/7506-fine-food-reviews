def get_minhashes(d, n_vec):
    mh = []
    min_hash = 10000000000000000000000000000
    for i in range(0, len(n_vec)):
        for c in d:
            temp_hash = h_cw_str(c, n_vec[i])
            if temp_hash < min_hash:
                min_hash = temp_hash
        mh.append(min_hash)
    return mh


def h_cw_vec(x, n):
    accum = 0
    for i in range(0, len(x)):
        accum += a_cw_vec[i] * x[i]
    h = (accum % p) % n
    return h


def h_cw_str(x, n):
    h = 0  # TODO h = init_value
    for i in (0, len(x) - 1):
        h += c_cw_str * (a_cw_str ** i)
    return h_cw_int(h % p, n)


def add_data_to_tables(tables, d, n_vec):
    hashes = get_hash_of_minhashes(d['Text'], n_vec)
    temp_dict = {'Id': d['Id'], 'Text': d['Text'], 'Prediction': d['Prediction']}
    for table, hash_value in zip(tables, hashes):
        if hash_value in table:
            current_list = table[hash_value]
            current_list.append(temp_dict)
            table[hash_value] = current_list
        else:
            table[hash_value] = [temp_dict]


def knn(test_point, data, k, distance):
    distances = []
    for d in data:
        dist = distance(test_point, d['Text'])
        distances.append({'Id': d['Id'], 'Prediction': d['Prediction'],
                          'Distance': dist})
    if len(distances) < k:
        k = len(distances)

    return sorted(distances, key=operator.itemgetter('Distance'), reverse=True)[:k]

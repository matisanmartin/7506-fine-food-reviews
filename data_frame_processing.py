import string

def procesar_data_frame_train(dft):
    return ""


def procesar_data_frame_test(dft):
    return ""


def procesar_frame(frame):
    return ""


def pre_procesar_frame(frame):
    # Cargo las stopwords
    with open('english_stopwords.txt', 'rb') as f:
        stopwords = [line.rstrip() for line in f]
    stopwords_set = set(stopwords)

    # Defino el set de caracteres permitidos en las palabras
    whitelist = string.letters + string.digits + ' ' + '\''

    # Filtro por el whitelist y las stopwords
    filtered_string = ''.join(c for c in frame['Text'].lower() if c in whitelist).split()
    result_with_no_stopwords = [i for i in filtered_string if i not in stopwords_set]

    return result_with_no_stopwords

import string

import pandas as pd


# Genera un arreglo donde cada elemento es un par {clave, valor}
# nombreArchivo = String con el path del archivo a leer
# header = las columnas que posee el archivo.
def leer_archivo(nombre_archivo, mode):
    # Lectura del CSV
    if (mode == 'train'):
        raw_data = pd.read_csv(nombre_archivo, encoding='utf-8', usecols=['Id', 'Text', 'Prediction'])

    if (mode == 'test'):
        raw_data = pd.read_csv(nombre_archivo, encoding='utf-8', usecols=['Id', 'Text'])

    data_frame = pd.DataFrame(data=raw_data)

    # Pre procesamiento
    data_frame['Text'] = data_frame['Text'].map(lambda x: pre_procesar_frame(x))

    # Conversion a dict list
    # frame_list = data_frame.to_dict('records')

    # return frame_list
    return data_frame


def generar_archivo_submission(df):
    df.to_csv('./kaggle/grupo16.csv', columns=["Id", "Prediction"], index=False)


# Pre procesa un frame
# Mantiene caracteres permitidos
# Convierte a minusculas
# Elimina stopwords (nltk)
# @param:
#   el texto a procesar
# @returns:
#   El string procesado
def pre_procesar_frame(text):
    # Defino el set de caracteres permitidos en las palabras
    whitelist = string.ascii_letters + string.digits + ' ' + '\''
    # Filtro por el whitelist y las stopwords
    filtered_by_whitelist = ''.join(c for c in text if c in whitelist)
    splitted = filtered_by_whitelist.lower().split()

    # filtered_by_stopwords = filter(lambda c: c not in stopwords.words('english'), splitted)
    # text = ' '.join(list(filtered_by_stopwords))
    # return text
    return filtered_by_whitelist

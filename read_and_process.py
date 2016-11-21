import csv
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
    # data_frame['Text'] = data_frame['Text'].map(lambda x: pre_procesar_frame(x))

    # Conversion a dict list
    # frame_list = data_frame.to_dict('records')

    # return frame_list
    return data_frame


# Método para guardar los Id´s y Prediction´s
def generar_archivo(data):
    with open('./kaggle/grupo16.csv', 'w') as outfile:
        fieldnames = ['Id', 'Prediction']
        submission_writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        submission_writer.writeheader()
        submission_writer.writerows(data)

    outfile.close()


def generar_archivo_submission(df):
    df.to_csv('./kaggle/grupo16.csv', columns=["Id", "Prediction"], index=False)


# Método para testear el método "generar_archivo(data)"
def test_generar_Archivo():
    dict_array = [{'Id': 1, 'Prediction': 1}, {'Id': 8, 'Prediction': 3}, {'Id': 9, 'Prediction': 2.5},
                  {'Id': 10, 'Prediction': 4.5}]
    generar_archivo(dict_array)
    archivo = open("submission.csv", "r")
    contenido = archivo.read()

    print(contenido)


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

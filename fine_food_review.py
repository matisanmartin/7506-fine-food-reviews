import argparse

import read_and_process
import utils

parser = argparse.ArgmumentParser(description='Fine food reviews')
parser.add_argument('i', '--input', help='Archivo a procesar', required=True)
parser.add_argument('o', '--output', help='Archivo de salida', required=True)
parser.add_argument("m", '--mode', help='Modo: train/test', required=False, default='train')

args = vars(parser.parse_args())

if args['mode'] == 'train':
    data_frame_train = read_and_process.leer_archivo(args.i, utils.header_train)
    read_and_process.procesar_data_frame_train(data_frame_train)
elif args['mode'] == 'test':
    data_frame_test = read_and_process.leer_archivo(args.i, utils.header_test)
    read_and_process.procesar_data_frame_test(data_frame_test)



# Obtener estructuras con datos relevantes

# Procesar datos relevantes

# Generar archivo de salida

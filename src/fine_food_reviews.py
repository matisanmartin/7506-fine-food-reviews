import time

import src.neural_kernel as nk
import src.random_forest as rf
from src import read_and_process

# Leo archivo
print("Reading train.")
# df_train_1000 = read_and_process.leer_archivo("./files/train1000lines.csv", 'train')
df_train = read_and_process.leer_archivo("../files/train.csv", 'train')
print("Done reading train.")
print("Reading test.")
df_test = read_and_process.leer_archivo("../files/test.csv", 'test')
print("Done reading test.")
print("Starting.")
start = time.time()
df_neural_kernel_result = nk.do_neural_kernel(df_test, df_train)
df_random_forest_result = rf.do_random_forest(df_test, df_train)
# tables = lsh_knn.load_test_file(df_train.head(1000))
# df_test['Prediction'] = df_test.apply(lambda row: lsh_knn.do_lsh_knn(row['Text'], tables), axis=1)

predictions_nk = df_neural_kernel_result['Prediction']
predictions_rf = df_random_forest_result['Prediction']
predictions_knn = df_test['Prediction']
result_temp = predictions_nk.add(predictions_rf)
# df_result = predictions_nk.add(predictions_rf)
df_result = result_temp.add(predictions_knn)
df_result['Id'] = df_test.apply(lambda row: row['Id'])
df_result['Prediction'] = df_test.apply(lambda row: row['Prediction'] / float(3))
print(time.time() - start)
print("Finished. ")
print("Writing out file.")
read_and_process.generar_archivo_submission(df_result)
print("Finished.")

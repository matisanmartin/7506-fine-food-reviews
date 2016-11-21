import time

import knn
import lsh_knn
import read_and_process

# Cargo stopwords
# nltk.download('stopwords');

# Leo archivo
print("KNN: Reading train.")
df_train = read_and_process.leer_archivo("./files/train10lines.csv", 'train')
print("KNN: Done reading train")
print("KNN: Reading test.")
df_test = read_and_process.leer_archivo("./files/test10lines.csv", 'test')
print("KNN: Done reading test")

n_vec = [461,
         599,
         733,
         827,
         103,
         997]
k = 5
b = 2
print("KNN: Starting method. ")
start = time.time()
df_result = lsh_knn.do_lsh_knn(df_test, df_train, n_vec, k, knn.jaccard_distance, b)
print(time.time() - start)
print("KNN: Finished. ")
print("Writing out file.")
read_and_process.generar_archivo_submission(df_result)
print("Finished.")

import knn
import lsh_knn
import read_and_process

# Cargo stopwords
# nltk.download('stopwords');

# Leo archivo
train_frame = read_and_process.leer_archivo("../files/train10lines.csv", 'train')
test_frame = read_and_process.leer_archivo("../files/train1line.csv", 'test')

n_vec = [1000, 2000, 3000, 4000, 5000, 6000]
k = 5
b = 2
result = lsh_knn.do_lsh_knn(test_frame, train_frame, n_vec, k, knn.jaccard_distance, b)
print(result)
result.to_csv('../kaggle/grupo16_test.csv', columns=["Id", "Prediction"], index=False)

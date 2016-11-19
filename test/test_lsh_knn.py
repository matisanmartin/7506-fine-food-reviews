import knn
import lsh_knn

# Test lsh-knn
data = [{'Id': 3, 'Text': "Hola que tal"}]
test1 = {"Id": 1, "Text": "Hola que tal", "Prediction": 4}
test2 = {"Id": 2, "Text": "Hola que tal", "Prediction": 4}
test = [test1, test2]
n_vec = [1000, 2000, 3000, 4000]
k = 5
result = lsh_knn.do_lsh_knn(data, test, n_vec, k, knn.jaccard_distance, 2)
print(result)

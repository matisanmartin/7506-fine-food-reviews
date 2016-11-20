import file_reading
import knn
import lsh_knn

train_array = file_reading.leer_archivo("train10lines.csv")
test_array = [{"Id": 492346,
               "Text": "I got them in a very timely manner and they're all very large and green. There seems to be an inordinate amount of the seeds that come out a weird beige color, but it still tastes great and is a much better deal than any of the Indian markets in town. Cheers to Frontier.",
               "Prediction": 5}]

n_vec = [1000, 2000, 3000, 4000, 5000, 6000]
k = 5
b = 2
result = lsh_knn.do_lsh_knn(test_array, train_array, n_vec, k, knn.jaccard_distance, b)
for r in result:
    print(r)

file_reading.generar_archivo(result)

from src import knn

# Prueba distancia Jaccard 0
text = "Hola que tal"
set_ = [c for c in text]
distancia_jaccard = knn.jaccard_distance(text, text)
print(distancia_jaccard)

# Prueba distancia Jaccard 1
text = "AAAAAAAA"
text2 = "BBBBBBBB"
distancia_jaccard = knn.jaccard_distance(text, text2)
print(distancia_jaccard)

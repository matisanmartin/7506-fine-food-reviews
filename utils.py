# Cada dato tiene la siguiente informacion:
# Id = id de calificacion
# ProductId = id del producto calificado
# UserId = id del usuario
# ProfileName = nombre de usuario
# HelpfulnessNumerator = cantidad de usuarios a los que les sirvió el review
# HelpfulnessDenominator = cantidad de usuarios que hicieron un review
# Prediction = Resultado a predecir
# Time = Timestamp en el que se hizo el review
# Summary = Resumen del review
# Text = Review completo

header_train = ["Id", "ProductId", "UserId", "ProfileName", "HelpfulnessNumerator", "HelpfulnessDenominator",
                "Prediction", "Time", "Summary", "Text"]

header_test = ["Id", "ProductId", "UserId", "ProfileName", "HelpfulnessNumerator", "HelpfulnessDenominator", "Time",
               "Summary", "Text"]

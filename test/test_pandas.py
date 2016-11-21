import pandas as pd


def get_prediction():
    return 5


train = pd.read_csv('../files/train10lines.csv')
test = pd.read_csv('../files/test10lines.csv')

df_train = pd.DataFrame(data=train)
df_test = pd.DataFrame(data=test)

train_arr = df_train.to_dict('records')
test_arr = df_test.to_dict('records')

prediction = 5

print(train_arr)
print(test_arr)

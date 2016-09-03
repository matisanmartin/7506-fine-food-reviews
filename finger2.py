import re

import file_reading

data_test = file_reading.leer_archivo('test10lines.csv')
text_list = []
for row in data_test:
    result = re.sub('([.,!?()])', r' \1 ', row['Text'])
    result = re.sub('\s{2,}', ' ', result)
    text_list.append(result.lower().replace(':', 'COLON').replace('|', 'PIPE'))

print(text_list)

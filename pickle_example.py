# 7.5. Сериализация обьектов

import pickle

data = {'1': (1, 2, 3), '2':['a', 'd', 'c'], '3': {0, 1, 2, 0}}
print(data)

# Делаем сериализацию
print('   Делаем сериализацию')

with open('data.pickle', 'wb') as f:
    pickle.dump(data, f)

# ДеСириализация
with open('data.pickle', 'rb') as f:
    data_load = pickle.load(f)

print(data_load)


# 7.3. Формат CSV

import csv

''''
функция csv.reader - чтение в лист
функция csv.writer - запись из листа
класс csv.Dictwriter - класс записи в словарь
класс csv.DictReader - класс чтения в словарь

'''

# csv.writer
print('   csv.writer')

car_data = [['brand', 'price', 'year'],['Volvo', 1.5, 2017],['Lada', 0.5, 2018],['Audi', 2.0, 2018]]

with open('example.csv', 'w') as f:
    writer = csv.writer(f, delimiter = '&') # delimiter = '&'
    writer.writerows(car_data)
print('Writing complete')


print()
# csv.reader
print('   csv.reader')

with open('example.csv') as f:
    reader = csv.reader(f, delimiter = '&')
    for row in reader:
        print(row)

print()
# csv.Dictwriter
print('   csv.Dictwriter')

data_dict = [{'Name': 'Dima', 'age': '28'},
             {'age': '29', 'Name': 'Kate'},
             {'Name': 'Mike', 'age': '31'}]

fieldnames = ['Name', 'age']

with open('example_1.csv', 'w') as f:
    writer = csv.DictWriter(f, delimiter = '&', fieldnames = fieldnames)
    writer.writeheader()
    for i in range (len(data_dict)):
        writer.writerow(data_dict[i])

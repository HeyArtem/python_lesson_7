# 1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
print('   1) Вручную создать текстовый файл с данными')
print(' Я создал фаил template')


# 2) Создать doc шаблон, где будут использованы данные параметры.
print('   2) Создать doc шаблон, где будут использованы данные параметры.')

print()
# 3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).
print('   3) Автоматически сгенерировать отчет о машине в формате doc (как в видео 7.2).')
import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context(label, model, fuel, price):  # возвращает словарь аргументов
    return {
        'label': label,
        'model': model,
        'fuel': fuel,
        'price': price
    }


def from_template(label, model, fuel, price, template, signature):
    template = DocxTemplate(template)  # Формируем сам шаблон
    context = get_context(label, model, fuel, price)  # Dict с обьектами в словаре, получает контекст, используемый
    # для визуализации документа

    img_size = Cm(15)  # устанавливает размер изображения
    acc = InlineImage(template, signature, img_size)  # Обьект картинки

    context['acc'] = acc  # добавляет объект InlineImage в контекст
    template.render(context)  # Передаем картинку в обьект шаблона
    template.save(
        label + '_' + model + '_' + str(datetime.datetime.now().date()) + '_' 'report.docx')  # Сохраням обьект шаблона


def generate_report(label, model, fuel, price):
    template = 'template.docx'
    signature = 'avt.jpg'
    from_template(label, model, fuel, price, template, signature)


generate_report('Mazda', 'X-9', '11,5', '1900000')


print()
# 4) Создать csv файл с данными о машине.
print('   4) Создать csv файл с данными о машине.')


import csv
''''

функция csv.reader -> Чтение в тип list
функция csv.writer -> Запись из листа
класс csv.Dictwriter -> Класс, запись в обьект типа словарь
класс csv.DictReader -> Класс, чтение в обьект типа словарь

'''

car_data = [['brand', 'model', 'volume', 'fuel'], ['Kia', 'Rio', '1,4', '8'], ['Reno', 'Fluence', '1,6', '8,5'], ['Volkswagen', 'Polo', '1,5', '8,7'], ['Hyundai', 'solaris', '1,4', '7,8']]



with open('data_auto.csv', 'w', newline='') as f: # newline-> делает, что бы запись делалась каждую строку, а не через одну
    writer = csv.writer(f, delimiter = '>')  # Разделитель(delimiter), по умолчанию ','
    writer.writerows(car_data)
print('Writing complete!')

print(' * ')

with open('data_auto.csv') as f:
    читаю = csv.reader(f, delimiter = '>')
    for row in читаю:
        print(row)

print(' * ')

data_school_dict = [{'Name':'Dima', 'age':'10', 'Grade':'A'},
               {'Name':'Vasia', 'age':'11', 'Grade':'C'},
               {'Name':'Hasim', 'age':'13', 'Grade':'f'},
               {'Grade':'B', 'Name':'Zoy', 'age':'14'}]
fieldnames = ['Name', 'age', 'Grade']
with open('Список_учеников.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, delimiter = '-', fieldnames=fieldnames)
    writer.writeheader()
    for i in range(len(data_school_dict)):
        writer.writerow(data_school_dict[i])
print('   Writing Список_учеников.csv complete!')

print(' * ')

with open ('Список_учеников.csv') as f:
    reader = csv.DictReader(f, delimiter = '-')
    for row in reader:
        print(row) #  У меня выведется dict, у преподавателя tuple   ( [('Name','Dima'),('age','10')] )


print(' * ')

import pandas as pd
проба_pandas_from_csv = pd.read_csv('Список_учеников.csv', sep = '-')
print(type(проба_pandas_from_csv))
print(проба_pandas_from_csv)






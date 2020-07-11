# 1) Вручную создать текстовый файл с данными (например, марка авто, модель авто, расход топлива, стоимость).
print('   1) Вручную создать текстовый файл с данными')
print(' Я создал фаил template')


# 2) Создать doc шаблон, где будут использованы данные параметры.
print('   2) Создать doc шаблон, где будут использованы данные параметры.')

import datetime

from docxtpl import DocxTemplate
from docxtpl import InlineImage
from docx.shared import Cm
from docxtpl import DocxTemplate, InlineImage

def get_context(label, model, fuel, price): #возвращает словарь аргументов
    return {
        'label' : label,
        'model' : model,
        'fuel' : fuel,
        'price' : price,
    }

def from_template(label, model, fuel, price, template, signature):
    template =DocxTemplate(template)
    context = get_context(label, model, fuel, price) # получает контекст, используемый для визуализации документа

    img_size = Cm(15) # устанавливает размер изображения
    acc = InlineImage(template, signature, img_size)

    context['acc'] = acc # добавляет объект InlineImage в контекст
    template.render(context)

    template.save(label + '_' + model+ '_' + str(datetime.datetime.now().date()) + '_report.docx')

def generate_report(label, model, fuel, price):
    template = 'report.docx'
    signature = 'acc.jpg'
    document = from_template(label, model, fuel, price, template, signature)

def toFixed(numObj, digits=0):
    return f"{numObj:.{digits}f}"

generate_report('Kia', 'Sorento', '12', '2000000')
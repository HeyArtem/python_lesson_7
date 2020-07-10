# 7.2. Автомати-я генерация отчетов в формате doc

# Препод сказал, не набивать код, почему??? Есть непонятне доки в дереве проекта (report? ass.png)? я не знаю
# откуда  они взялись

import datetime

from docxtpl import DocTempLate
from docxtpl import InLineImage
from docxtpl import Cm
from docxtpl import DocTempLate, InLineImage

def get_context(company, result_sku_list): # фунция возвращает словарь аргументов
    return {
        'retailer': company,
        'sku_list': result_sku_list,
    }
def from_template(company, result_sku_list, template, signature):
    template = DocxTempLate(template)
    context = get_context(company, result_sku_list)

    img size = Cm(15)
    acc = InLineImage(template, signature, img_size)
    context['acc'] = acc

    template.render(context)
    template.save(company + ' ' + str(datetime, datetime.now().date()) + 'report.docx')

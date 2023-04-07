
from pprint import pprint
## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re
with open("phonebook_raw.csv", encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)




# 1. # Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно. 
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
# По первому пункту можно сначала соединить содержимое первых трех элементов и разбить по пробелам, 
# вы получите список 2-3 элементов. Его интегрируете в запись.

for item in contacts_list:
  for i in item:
    fio = item[0:2]
    print(item) 


#2 # Привести все телефоны в формат +7(999)999-99-99. 
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.


# def format_number(contacts_list):
#   phone_pattern = r'(\+7|8)\D*(495)\D*(\d+)\D*(\d{2})\D*(\d{2})(\W*( доб.\s*\d+)\)*)?'
#   replace = r'+7(\2)\3-\4-\5\7'
#   contacts_list_updated = list()
#   for card in contacts_list:

#3 # Объединить все дублирующиеся записи о человеке в одну.



## 1. Выполните пункты 1-3 задания:
## Ваш код

## 2. Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')
  
## Вместо contacts_list подставьте свой список:
#   datawriter.writerows(contacts_list)
from pprint import pprint

## Читаем адресную книгу в формате CSV в список contacts_list:
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

print(contacts_list)

# 1. # Поместить Фамилию, Имя и Отчество человека в поля lastname, firstname и surname соответственно.
# В записной книжке изначально может быть Ф + ИО, ФИО, а может быть сразу правильно: Ф+И+О.
# По первому пункту можно сначала соединить содержимое первых трех элементов и разбить по пробелам,
# вы получите список 2-3 элементов. Его интегрируете в запись.

def fix_columns(some_list):
    for row in contacts_list:
        temp = ''.join(row[:3])
        temp_list = temp.split()
        for i in range(len(temp_list)):
            row[i] = temp_list[i]
    return some_list

# fix_columns(contacts_list)

# 2 # Привести все телефоны в формат +7(999)999-99-99.
# Если есть добавочный номер, формат будет такой: +7(999)999-99-99 доб.9999.

def format_number(some_list):
  current_pattern = r'(\+7|8)\D*(495)\D*(\d+)\D*(\d{2})\D*(\d{2})(\W*( доб.\s*\d+)\)*)?'
  replace_pattern = r'+7(\2)\3-\4-\5\7'
  for row in some_list:
    result = re.sub(current_pattern, replace_pattern, row[-2])
    row[-2] = result

  return some_list

# format_number(contacts_list)


# 3 # Объединить все дублирующиеся записи о человеке в одну.

# 3й пункт лучше делать через словарь. 
# Ключом делайте ФИ и при добавлении очередного элемента (записи) делайте проверку на наличие ключа в словаре. 
# Если ключ есть, то нужно объединить 2 записи, если нет, то добавляете новую в словарь.

# def merge_doubles(some_list):
   


## Сохраните получившиеся данные в другой файл.
## Код для записи файла в формате CSV:
# with open("phonebook.csv", "w") as f:
#   datawriter = csv.writer(f, delimiter=',')

## Вместо contacts_list подставьте свой список:
#   datawriter.writerows(contacts_list)

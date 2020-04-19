# -*- coding: utf-8 -*-
print('Домашняя работа к ЗАНЯТИЮ №3')
print('====================================================')
print('задание 3.1 заменяем все знаки препинания на пробелы')
print('====================================================')
# работа с текстом через строки
file_name = 'text.txt'
with open(file_name, 'r', encoding="UTF8") as file_text:
    # contents = file_text.read()
    # print(contents)
    lines = file_text.readlines()
    # print(lines)
# формируем весь текст в одну строку
temp_str = ''
for line in lines:
    temp_str +=line.rstrip()

# заменяем все знаки препинания на пробелы
temp_str = temp_str.replace('.',' ')
temp_str = temp_str.replace(',', ' ')
temp_str = temp_str.replace('—', ' ')
temp_str = temp_str.replace('—', ' ')
temp_str = temp_str.replace(')', ' ')
temp_str = temp_str.replace('(', ' ')
temp_str = temp_str.replace('«', ' ')
temp_str = temp_str.replace('»', ' ')
temp_str = temp_str.replace('!', ' ')
temp_str = temp_str.replace('?', ' ')
temp_str = temp_str.replace(';', ' ')
temp_str = temp_str.replace(':', ' ')
print(temp_str)

print('=============================================')
print('задание 3.2 формируем list со словами (split)')
print('=============================================')
# формируем list со словами (split)
temp_list_1 = temp_str.split()
print(temp_list_1)

print('=======================================================')
print('задание 3.3 приводим все слова к нижнему регистру (map)')
print('=======================================================')
#приводим все слова к нижнему регистру (map)
temp_list_lower = list(map(str.lower, temp_list_1))
print(temp_list_lower)

print('==========================================================================================================================')
print('задание 3.4 получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте')
print('==========================================================================================================================')
#получить из list пункта 3 dict, ключами которого являются слова, а значениями их количество появлений в тексте;
dict_text = dict.fromkeys(temp_list_lower, 0)
for key in temp_list_lower:
    dict_text[key] +=1

print(dict_text)

print('=============================================================================================================')
print('задание 3.5 вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)')
print('=============================================================================================================')
#вывести 5 наиболее часто встречающихся слов (sort), вывести количество разных слов в тексте (set)
list_value = list(dict_text.items())
list_value.sort(key=lambda i: i[1])
# print(list_value)
count = len(list_value)
print('5-ть наиболее часто встречающихся слов и частота вхождений в этот текст = ', list_value[count-5:count+1])
print('-----------')
print('количество уникальных слов в этом тексте =', count)

set_text = set(temp_list_lower)
count_set = len(set_text)
print('количество уникальных слов в этом тексте через (set)=', count_set)

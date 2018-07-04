#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fileencoding=utf-8



sortList = ['u', 'cc', 'bbb']



# Создаем "внешнюю" функцию, которая будет сортировать список в алфавитном порядке:
def sortByAlphabet(inputStr):
        return inputStr[0] # Ключом является первый символ в каждой строке, сортируем по нему

# Вторая функция, сортирующая список по длине строки:
def sortByLength(inputStr):
        return len(inputStr) # Ключом является длина каждой строки, сортируем по длине

print (u'Исходный список: ', sortList) # >>> ['a', 'cc', 'bbb']

sortList.sort(key=sortByAlphabet) # Каждый элемент массива передается в качестве параметра функции
print (u'Отсортировано в алфавитном порядке: ', sortList) # >>> ['a', 'bbb', 'cc']

sortList.sort(key=sortByLength) # Каждый элемент массива передается в качестве параметра функции
print (u'Отсортировано по длине строки: ', sortList) # >>> ['a', 'cc', 'bbb']

# Теперь отсортируем по длине строки, но в обратном порядке:
sortList.sort(key=sortByLength, reverse=True) # В обратном порядке
print (u'Отсортировано по длине строки, в обратном порядке: ', sortList) # >>> ['bbb', 'cc', 'a']



'''
Обратите внимание, что метод .sort() производит действия с исходным списком,
 переставляя элементы внутри него самого, и НЕ возвращает отсортированную копию исходного списка. 
 Для получения отсортированной копии нужно использовать метод sorted:

newList = sorted(sortList)

— либо такой же вариант, но с параметром key (аналогично описанному выше):

newList = sorted(sortList, key=sortByLength)
'''
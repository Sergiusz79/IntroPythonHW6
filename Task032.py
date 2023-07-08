# Задача 32: 
# Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

from random import randint

def enter_elements(text):
    try:
        n = int(input(f'Enter the {text} \n' + ':> '))
    except:
        print("Error! This is not integer number!")
    return n

def fill_list1(n):
    l1 = [randint(1,100) for i in range(n)] 
    return l1

def mini_maxi(mini, maxi, list1):
    index_list = []
    for i in range(len(list1)):
        if mini <= list1[i] <= maxi:
            index_list.append(i)
    return index_list

def task():
    n = enter_elements('number of list elements')
    mini = enter_elements('minimum number')
    maxi = enter_elements('maximum number')
    list1 = fill_list1(n)
    index_list = mini_maxi(mini, maxi, list1)
    print('--------------------------------------------------------------')
    print('elements of the original list :>  ' + ' '.join(map(str, list1)))
    print('--------------------------------------------------------------')
    print('Indexes of list elements lying within min and max :>  ' + ' '.join(map(str, index_list)))
    print('--------------------------------------------------------------')

task()

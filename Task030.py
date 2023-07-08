# Задача 30:  
# Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

def enter_elements(text):
    try:
        n = int(input(f'Enter the {text}:> \n'))
    except:
        print("Error! This is not integer number!")
    return n


def fill_progress(a, n, d):
    p = []
    for i in range(n):
        p.append(a + i*d)
    return p

def task():
    a = enter_elements('firs number of arithmetic progression')
    n = enter_elements('number of elements of an arithmetic progression')
    d = enter_elements('difference of an arithmetic progression')
    progress = fill_progress(a, n, d)
    print(progress)
    print('Arithmetic progression :>  ' + ' '.join(map(str, progress)))

task()
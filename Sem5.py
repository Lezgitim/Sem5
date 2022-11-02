# Задача 1. Задайте список случайных чисел от 1 до 10, выведите все элементы больше 5.
# Используйте для решения лямбда-функцию. 2, 3, 4, 6, 7, 8 -> 6, 7, 8

from random import randint


def Bol():
    from random import randint

    n = [randint(1, 10) for i in range(10)]
    li = list(filter(lambda x: x > 5, n))
    print(n)
    print(li)


# Задача 2. Дан список случайных чисел. Создайте список, в который попадают числа,
# описывающие возрастающую последовательность. Порядок элементов менять нельзя.
# [1, 5, 2, 3, 4, 6, 1, 7] =>[1, 2, 3] или [1, 7] или [1, 6, 7] и т.д.

def Spis():
    n = [randint(1, 10) for i in range(10)]
    print(n)

    spisok = []

    for i in range(len(n)-1):
        if n[i] < n[i+1]:
            spisok.append(n[i])
            spisok.append(n[i+1])
            print(spisok)
        if len(spisok) > 0:
            spisok.clear()


# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего
# совпадающих элементов есть в списке.Удалите все повторяющиеся элементы.

def Povtor():
    n = [randint(1, 10) for i in range(10)]
    print(n)
    print(set(n))
    spisok = []
    k = 0
    for g in range(len(n)):
        for i in range(len(n)):
            if n[g] == n[i] and g != i and n[g] <= 10:
                n[i] *= 100
                k += 1
    print('Общее количеcтво совпадающих элементов в списке:', k)

# Задача 4*. Игра в крестики-нолики.

def Strashno_smotret_no_rabotaet():

    n = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    print("Игра в крестики нолики")
    print()
    [print(i) for i in n]
    print()
    a = n[0]
    b = n[1]
    c = n[2]
    for i in range(6):
        print('Икрок №1')
        print('Введите номер строки: ')
        stroka = int(input())
        print('Введите номер столбца: ')
        stolbec = int(input())

        while (stroka < 1 or stroka > 3 or stolbec < 1 or
            stolbec > 3 or stolbec == 1 and stroka == 1 and a[0] == 2
            or stolbec == 2 and stroka == 1 and a[1] == 2
            or stolbec == 3 and stroka == 1 and a[2] == 2
            or stolbec == 1 and stroka == 2 and b[0] == 2 
            or stolbec == 2 and stroka == 2 and b[1] == 2
            or stolbec == 3 and stroka == 2 and b[2] == 2
            or stolbec == 1 and stroka == 3 and c[0] == 2 
            or stolbec == 2 and stroka == 3 and c[1] == 2
            or stolbec == 3 and stroka == 3 and c[2] == 2
            or stolbec == 1 and stroka == 1 and a[0] == 1 
            or stolbec == 2 and stroka == 1 and a[1] == 1
            or stolbec == 3 and stroka == 1 and a[2] == 1 
            or stolbec == 1 and stroka == 2 and b[0] == 1 
            or stolbec == 2 and stroka == 2 and b[1] == 1 
            or stolbec == 3 and stroka == 2 and b[2] == 1
            or stolbec == 1 and stroka == 3 and c[0] == 1 
            or stolbec == 2 and stroka == 3 and c[1] == 1
            or stolbec == 3 and stroka == 3 and c[2] == 1):

            while stroka < 1 or stroka > 3 or stolbec < 1 or stolbec > 3:
                print('Такой строки или столбца нет!')
                print('Икрок №1')
                print('Введите номер строки: ')
                stroka = int(input())
                print('Введите номер столбца: ')
                stolbec = int(input())

            while (stolbec == 1 and stroka == 1 and a[0] == 2 
                or stolbec == 2 and stroka == 1 and a[1] == 2
                or stolbec == 3 and stroka == 1 and a[2] == 2 
                or stolbec == 1 and stroka == 2 and b[0] == 2 
                or stolbec == 2 and stroka == 2 and b[1] == 2 
                or stolbec == 3 and stroka == 2 and b[2] == 2
                or stolbec == 1 and stroka == 3 and c[0] == 2 
                or stolbec == 2 and stroka == 3 and c[1] == 2
                or stolbec == 3 and stroka == 3 and c[2] == 2):
                print('Данное поле уже заполнено другим игроком!')
                print('Икрок №1')
                print('Введите номер строки: ')
                stroka = int(input())
                print('Введите номер столбца: ')
                stolbec = int(input())

            while (stolbec == 1 and stroka == 1 and a[0] == 1 
                or stolbec == 2 and stroka == 1 and a[1] == 1
                or stolbec == 3 and stroka == 1 and a[2] == 1 
                or stolbec == 1 and stroka == 2 and b[0] == 1 
                or stolbec == 2 and stroka == 2 and b[1] == 1 
                or stolbec == 3 and stroka == 2 and b[2] == 1
                or stolbec == 1 and stroka == 3 and c[0] == 1 
                or stolbec == 2 and stroka == 3 and c[1] == 1
                or stolbec == 3 and stroka == 3 and c[2] == 1):
                print('Данное поле Вами было заполнено ранее!')
                print('Икрок №1')
                print('Введите номер строки: ')
                stroka = int(input())
                print('Введите номер столбца: ')
                stolbec = int(input())

        if stroka == 1:
            if stolbec == 1:
                a[0] = 1
                n[0] = a
                print()
                [print(i) for i in n]
                print()
            if stolbec == 2:
                a[1] = 1
                n[0] = a
                print()
                [print(i) for i in n]
                print()
            if stolbec == 3:
                a[2] = 1
                n[0] = a
                print()
                [print(i) for i in n]
                print()
        
            if a[0] == a[1] == a[2] == 1:
                print('Игрок № 1 выиграл!')
                exit()

        if stroka == 2:
            if stolbec == 1:
                b[0] = 1
                n[1] = b
                print()
                [print(i) for i in n]
                print()
            if stolbec == 2:
                b[1] = 1
                n[1] = b
                print()
                [print(i) for i in n]
                print()
            if stolbec == 3:
                b[2] = 1
                n[1] = b
                print()
                [print(i) for i in n]
                print()
            
            if b[0] == b[1] == b[2] == 1:
                print('Игрок № 1 выиграл!')
                exit()

        if stroka == 3:
            if stolbec == 1:
                c[0] = 1
                n[2] = c
                print()
                [print(i) for i in n]
                print()
            if stolbec == 2:
                c[1] = 1
                n[2] = c
                print()
                [print(i) for i in n]
                print()
            if stolbec == 3:
                c[2] = 1
                n[2] = c
                print()
                [print(i) for i in n]
                print()
        
            if c[0] == c[1] == c[2] == 1:
                print('Игрок № 1 выиграл!')
                exit()

        if a[0] == b[1] == c[2] == 1 or a[2] == b[1] == c[0] == 1:
            print('Игрок № 1 выиграл!')
            exit()

        if a[0] == b[0] == c[0] == 1 or a[1] == b[1] == c[1] == 1 or a[2] == b[2] == c[2] == 1:
            print('Игрок № 1 выиграл!')
            exit()

        if i == 4:
            print('Поле заполнено полностью. Конец игры.')
            exit()

        print('Икрок №2')
        print('Введите номер строки: ')
        stroka = int(input())
        print('Введите номер столбца: ')
        stolbecigrok2 = int(input())

        while (stroka < 1 or stroka > 3 or stolbecigrok2 < 1 or stolbecigrok2 > 3
            or stolbecigrok2 == 1 and stroka == 1 and a[0] == 1 
            or stolbecigrok2 == 2 and stroka == 1 and a[1] == 1
            or stolbecigrok2 == 3 and stroka == 1 and a[2] == 1
            or stolbecigrok2 == 1 and stroka == 2 and b[0] == 1 
            or stolbecigrok2 == 2 and stroka == 2 and b[1] == 1
            or stolbecigrok2 == 3 and stroka == 2 and b[2] == 1 
            or stolbecigrok2 == 1 and stroka == 3 and c[0] == 1 
            or stolbecigrok2 == 2 and stroka == 3 and c[1] == 1
            or stolbecigrok2 == 3 and stroka == 3 and c[2] == 1
            or stolbecigrok2 == 1 and stroka == 1 and a[0] == 2 
            or stolbecigrok2 == 2 and stroka == 1 and a[1] == 2
            or stolbecigrok2 == 3 and stroka == 1 and a[2] == 2
            or stolbecigrok2 == 1 and stroka == 2 and b[0] == 2 
            or stolbecigrok2 == 2 and stroka == 2 and b[1] == 2
            or stolbecigrok2 == 3 and stroka == 2 and b[2] == 2
            or stolbecigrok2 == 1 and stroka == 3 and c[0] == 2 
            or stolbecigrok2 == 2 and stroka == 3 and c[1] == 2
            or stolbecigrok2 == 3 and stroka == 3 and c[2] == 2):
            
            while stroka < 1 or stroka > 3 or stolbecigrok2 < 1 or stolbecigrok2 > 3:
                print('Такой строки или столбца нет!')
                print('Икрок №2')
                print('Введите номер строки: ')
                stroka = int(input())
                print('Введите номер столбца: ')
                stolbecigrok2 = int(input())

            while (stolbecigrok2 == 1 and stroka == 1 and a[0] == 1 
                or stolbecigrok2 == 2 and stroka == 1 and a[1] == 1
                or stolbecigrok2 == 3 and stroka == 1 and a[2] == 1
                or stolbecigrok2 == 1 and stroka == 2 and b[0] == 1 
                or stolbecigrok2 == 2 and stroka == 2 and b[1] == 1
                or stolbecigrok2 == 3 and stroka == 2 and b[2] == 1
                or stolbecigrok2 == 1 and stroka == 3 and c[0] == 1 
                or stolbecigrok2 == 2 and stroka == 3 and c[1] == 1
                or stolbecigrok2 == 3 and stroka == 3 and c[2] == 1):
                print('Данное поле уже заполнено другим игроком!')
                print('Икрок №2')
                print('Введите номер строки: ')
                stroka = int(input())
                print('Введите номер столбца: ')
                stolbecigrok2 = int(input())

            while (stolbecigrok2 == 1 and stroka == 1 and a[0] == 2 
                or stolbecigrok2 == 2 and stroka == 1 and a[1] == 2
                or stolbecigrok2 == 3 and stroka == 1 and a[2] == 2
                or stolbecigrok2 == 1 and stroka == 2 and b[0] == 2 
                or stolbecigrok2 == 2 and stroka == 2 and b[1] == 2
                or stolbecigrok2 == 3 and stroka == 2 and b[2] == 2
                or stolbecigrok2 == 1 and stroka == 3 and c[0] == 2 
                or stolbecigrok2 == 2 and stroka == 3 and c[1] == 2
                or stolbecigrok2 == 3 and stroka == 3 and c[2] == 2):
                print('Данное поле Вами было заполнено ранее!')
                print('Икрок №2')
                print('Введите номер строки: ')
                stroka = int(input())
                print('Введите номер столбца: ')
                stolbecigrok2 = int(input())

        if stroka == 1:
            if stolbecigrok2 == 1:
                a[0] = 2
                n[0] = a
                print()
                [print(i) for i in n]
                print()
            if stolbecigrok2 == 2:
                a[1] = 2
                n[0] = a
                print()
                [print(i) for i in n]
                print()
            if stolbecigrok2 == 3:
                a[2] = 2
                n[0] = a
                print()
                [print(i) for i in n]
                print()
            
            if a[0] == a[1] == a[2] == 2:
                print('Игрок № 2 выиграл!')
                exit()

        if stroka == 2:
            if stolbecigrok2 == 1:
                b[0] = 2
                n[1] = b
                print()
                [print(i) for i in n]
                print()
            if stolbecigrok2 == 2:
                b[1] = 2
                n[1] = b
                print()
                [print(i) for i in n]
                print()
            if stolbecigrok2 == 3:
                b[2] = 2
                n[1] = b
                print()
                [print(i) for i in n]
                print()
            
            if b[0] == b[1] == b[2] == 2:
                print('Игрок № 2 выиграл!')
                exit()

        if stroka == 3:
            if stolbecigrok2 == 1:
                c[0] = 2
                n[2] = c
                print()
                [print(i) for i in n]
                print()
            if stolbecigrok2 == 2:
                c[1] = 2
                n[2] = c
                print()
                [print(i) for i in n]
                print()
            if stolbecigrok2 == 3:
                c[2] = 2
                n[2] = c
                print()
                [print(i) for i in n]
                print()

            if c[0] == c[1] == c[2] == 2:
                print('Игрок № 2 выиграл!')
                exit()

        if a[0] == b[1] == c[2] == 2 or a[2] == b[1] == c[0] == 2:
            print('Игрок № 2 выиграл!')
            exit()

        if a[0] == b[0] == c[0] == 2 or a[1] == b[1] == c[1] == 2 or a[2] == b[2] == c[2] == 2:
            print('Игрок № 2 выиграл!')
            exit()

   

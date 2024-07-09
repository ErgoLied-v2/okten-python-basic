# strings

# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через кому,
# наприклад:
# st = 'as 23 fdfdg544' введена строка
# 2,3,5,4,4        #вивело в консолі.

print('----- TASK 1')
# string1 = input('Enter a string: ')
string1 = 'qwe123rty456 34ert 345 ert 0'
print(','.join(i for i in string1 if i.isdigit()))

# ################################################################################
# 2)написати прогу яка вибирає зі введеної строки числа і виводить їх
# так як вони написані
# наприклад:
# st = 'as 23 fdfdg544 34' #введена строка
# 23, 544, 34              #вивело в консолі

print('----- TASK 2')
print('not ready')

# #################################################################################
#
# list comprehension
#
# 1)є строка:
# greeting = 'Hello, world'
# записати кожний символ як окремий елемент списку і зробити його заглавним:
# ['H', 'E', 'L', 'L', 'O', ',', ' ', 'W', 'O', 'R', 'L', 'D']

print('----- TASK 3')
greeting = 'Hello, world'
print([i.capitalize() for i in greeting])

#
# 2) з диапозону від 0-50 записати тільки не парні числа при цьому піднести їх до квадрату
# приклад:
# [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, ...]

print('----- TASK 4')
print([i ** 2 for i in range(50) if i % 2])

#
# function
#
# - створити функцію яка виводить ліст

print('----- TASK 5')


def print_list(data: list):
    if isinstance(data, list):
        print(data)
    else:
        print('it`s not a list')


print_list([1, 2, 3])
print_list('1,2,3')

# - створити функцію яка приймає три числа та виводить та повертає найбільше.

print('----- TASK 6')


def check_max(a, b, c):
    print(a, b, c)
    print('max = ', max(a, b, c))


check_max(5, 2, 3)

# - створити функцію яка приймає будь-яку кількість чисел, повертає найменьше, а виводить найбільше

print('----- TASK 7')


def min_max(*args):
    print('max = ', max(args))
    return min(args)


print(min_max(1, 2, 3))

# - створити функцію яка повертає найбільше число з ліста
print('----- TASK 8')


def max_from_list(array):
    return max(array)


print('max = ', max_from_list([1, 2, 3]))

# - створити функцію яка повертає найменьше число з ліста
print('----- TASK 9')


def min_from_list(array):
    return min(array)


print('min = ', min_from_list([1, 2, 3]))

# - створити функцію яка приймає ліст чисел та складає значення елементів ліста та повертає його.
print('----- TASK 10')


def sum_from_list(array):
    return sum(array)


print('sum = ', sum_from_list([1, 2, 3]))

# - створити функцію яка приймає ліст чисел та повертає середнє арифметичне його значень.
print('----- TASK 11')


def avg_from_list(array):
    return sum(array) / len(array)


print('avg = ', avg_from_list([1, 2, 3]))
#
#
#
#
# ################################################################################################
# 1)Дан list:
# some_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
# - знайти мін число
# - видалити усі дублікати
# - замінити кожне 4-те значення на 'X'
# 2) вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції
# 3) вывести табличку множення за допомогою цикла while
# 4) переробити це завдання під меню

print('----- TASK 12')


def remove_duplicates(array):
    return list(set(array))


def change_x(array):
    new_array = array.copy()
    return [item if (index + 1) % 4 else 'x' for index, item in enumerate(new_array)]


# print(change_x([11, 22, 33, 44, 55, 66, 77, 88, 99, 0, 44, 44, 44, 44]))


def create_square(side):
    for i in range(side):
        if i == 0 or i == side - 1:
            print('*' * side)
        else:
            print('*' + ' ' * (side - 2) + '*')


# create_square(4)

# square table made with 'for'
# def square_table():
#     size = 10
#     for i in range(1, size + 1):
#         for j in range(1, size + 1):
#             print(f'{i * j : 4}', end='')
#             j += 1
#         print('\n')
#         i += 1
def square_table():
    size = 10
    i = 1
    while i <= size:
        j = 1
        while j <= size:
            print(f'{i * j:4}', end='')
            j += 1
        print('\n')
        i += 1


# square_table()


while True:
    some_list = [22, 3, 5, 2, 8, 2, -23, 8, 23, 5]
    print('list = ', some_list)
    print('1. знайти мін число')
    print('2. видалити усі дублікати')
    print('3. замінити кожне 4-те значення на \'X\'')
    print('4. вивести на екран пустий квадрат з "*" сторона якого вказана як агрумент функції')
    print('5. вивести табличку множення за допомогою цикла while')
    print('6. exit')

    case = input('choose something: ')

    if case == '1':
        print('min = ', min_from_list(some_list))
    elif case == '2':
        print(remove_duplicates(some_list))
    elif case == '3':
        print(change_x(some_list))
    elif case == '4':
        size = input('set side size = ')
        create_square(int(size))
    elif case == '5':
        square_table()
    elif case == '6':
        break
    else:
        print('wrong choose')

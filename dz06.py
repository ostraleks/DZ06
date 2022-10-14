# 1. Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше
# предыдущего элемента. Use comprehension.
# in
# 9
#
# out
# [15, 16, 2, 3, 1, 7, 5, 4, 10]
# [16, 3, 7, 10]
#
# in
# 10
#
# out
# [28, 20, 10, 5, 1, 24, 7, 15, 23, 25]
# [24, 15, 23, 25]

from random import randint
def new_list(num=int(input("Введите количество цифр "))):
    list = [randint(1, 100) for _ in range(num)]
    print(f'Входящий список:\n{list}')
    return list
def out_list(in_list=new_list()):
    out_l = [in_list[i] for i in range(1, len(in_list)) if int(
        in_list[i - 1]) < int(in_list[i])]
    return out_l

print(f'Исходящий список:\n{out_list()}')


# 2. Для чисел в пределах от 20 до N найти числа, кратные 20 или 21. Use comprehension.
# in
# 100
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100]
#
# in
# 424
#
# out
# [20, 21, 40, 42, 60, 63, 80, 84, 100, 105, 120, 126, 140, 147, 160, 168, 180, 189, 200, 210,
#  220, 231, 240, 252, 260, 273, 280, 294, 300, 315, 320, 336, 340, 357, 360, 378, 380, 399, 400, 420]

# in_list = [i for i in range(20, int(input("Введите конечное число "))+1)]
# print(*[x for x in in_list if x % 20 == 0 or x % 21 == 0])


# 3. Написать функцию, аргументы имена сотрудников, возвращает словарь, ключи — первые буквы имён,
# значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# in
# "Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"
#
# out
#
# {'А': ['Алина'], 'Б': ['Бибочка'], 'И': ['Иван', 'Илья'], 'М': ['Марина', 'Мария'], 'П': ['Петр', 'Петр']}


# def list_staff(name_staff):
#     dic_st = {}
#     for stroka in name_staff:
#         list = []
#         if dic_st.get(stroka[0]):
#             list = dic_st[stroka[0]]
#             list.append(stroka)
#             dic_st[stroka[0]] = list
#         else:
#             list.append(stroka)
#             dic_st[stroka[0]] = list
#     return dic_st

# staff = ["Иван", "Мария", "Петр", "Илья", "Марина", "Петр", "Алина", "Бибочка"]
# print(list_staff(staff))

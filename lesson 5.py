#Рекурсия с факториалом

# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return factorial(n-1) * n
#
#
# print(factorial(100))
#
# print(5**1000)

#Менеджер контекста

# class ManagerContext:
#     def __enter__(self):
#         print ("Отработал вход")
#         return 1
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Отработал выход")
#
# with ManagerContext() as f:
#     print ("Тело ManagerContext")
#
# print(f)

# search_list = [5, 7, 10, 11, 12, 15, 19, 20, 21]
# b = [len(a)//2]
# print(b)
import os
search_list = [5, 7, 10, 11, 12, 15, 19, 20, 21]

def recoursive_binary_serach(search_list, find):
    left_index = 0
    right_index = len(search_list) - 1
    median_index = len(search_list) // 2
    # median_index = (left_index+right_index) // 2

    if find < search_list[median_index]:
       right_index = median_index
       # search_list = search_list[:right_index] : делит список на 2
       search_list = search_list[:right_index]
       recoursive_binary_serach(search_list, find)

    elif find > search_list[median_index]:
        left_index = median_index
        # search_list = search_list[left_index:] делит список на 2
        search_list = search_list[left_index:]
        recoursive_binary_serach(search_list, find)
    elif find == search_list[median_index]:
        print(search_list[median_index])
        print("Нашли")

try:
    recoursive_binary_serach(search_list = search_list, find = 15)
except RecursionError:
    print("Элемент нет в списке")



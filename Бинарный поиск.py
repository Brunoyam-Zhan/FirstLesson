# a = [6, 7, 8, 2, 1, 15, 667, 83, 34, 56]
# find = 34
#
# def recoursive_binary(a, find):
#     left_index = 0
#     right_index = len(a) - 1
#     middle_index = len(a)//2
#
#     if find < a[middle_index]:
#         right_index = middle_index
#         a = a[:right_index]
#         recoursive_binary(a, find)
#     elif find > a[middle_index]:
#         left_index = middle_index
#         a = a[left_index:]
#         recoursive_binary(a, find)
#     elif find == a[middle_index]:
#         print(a[middle_index])
#         print("Нашли")
#
# try:
#     recoursive_binary(a = a, find = )
# except RecursionError:
#     print("Не найдено")

# find = 7
# a = [1, 2, 3, 4, 5, 6, 7]
# left_index = 0
# right_index = len(a) - 1
# counter = 0
# # middle_index = len(a)//2 ??
# while left_index <= right_index:
#     counter += 1
#     median = (left_index+right_index)//2
#     if a[median] == find:
#         print(a[median])
#         break
#     elif find < a[median]:
#         right_index = median - 1
#
#     elif find > a[median]:
#         left_index = median + 1

# Сортировка пузырьковым методом

# a = [3, 1, 5, 2, 17]
#
# for j in range (len(a)-1):
#     for i in range(len(a)-1-j):
#         if a[i] > a[i + 1]:
#             a[i], a[i + 1] = a[i + 1], a[i]
# print(a)

# a = [6, 34, 213, 235, 546, 5456, 1, 67, 0]
# less = a[0]
# b = []
#
# def Less1(a):
#     less = a[0]
#     for i in range(len(a)):
#         if a[i] < less:
#             less = a[i]
#     return less
# while len(a) != 0:
#     v = Less1(a)
#     b.append(v)
#     a.remove(v)
# print(b)
#







# при каждой итерации переменная less
# сравнивается с каждом элементов в списке, соответственно когда доходит до того что определенный элемент м
# еньше чем переменная less, она будет равнятся саммому меньшему числу в списке


# a = [34, 30, 26, 65, 78]
# for j in range(len(a)-1):
#     for i in range(len()-1):

# a = [34, 30, 26, 65, 78]
# less_num = a[0]
# for i in range(len(a)):
#     if less_num > a[i]:
#         less_num = a [i]
#
# print(less_num)

# a = [34, 30, 26, 65, 78]
# less_num = a[0]
# b = []
# def Less(a):
#     less_num = a[0]
#     for i in range(len(a)):
#         if less_num > a[i]:
#             less_num = a [i]
#     return less_num
#
# while len(a) != 0:
#     c = Less(a)
#     b.append(c)
#     a.remove(c)
# print(b)

# алгоритм сортировки с слиянием
# a = [2, 3, 1, 7, 23, 67, 2, 8, 4, 12, 90, 112, 65, 7886, 1234, 31412, 54635, 65673]
# def merge_sort(unsorted_list):
#     if len(unsorted_list) < 2:
#         return unsorted_list
#     # left_index = 0
#     # right_index = len(unsorted_list) - 1
#     medium_index = len(unsorted_list) // 2
#     left_list = merge_sort(unsorted_list[:medium_index])
#     right_list = merge_sort(unsorted_list[medium_index:])
#     return merge(left_list, right_list)
#
# def merge(left_list, right_list):
#     result = []
#     i, j = 0, 0
#     while len(left_list) > i and len(right_list) > j:
#         if left_list[i] < right_list[j]:
#             result.append(left_list[i])
#             # left_list.remove(left_list[i])
#             i += 1
#         else:
#             result.append(right_list[j])
#             # right_list.remove(right_list[j])
#             j += 1
#
#     while len(left_list) > i:
#         result.append(left_list[i])
#         i += 1
#
#     while len(right_list) > j:
#         result.append(right_list[j])
#         j += 1
#
#     return result
#
# print(merge_sort(a))

# класс очередь
# class Queue:
#     def __init__(self, data):
#         self.queue_data = data
#
#     def add(self, element):
#         self.queue_data.append(element)
#
#     def get (self):
#         return self.queue_data.pop(0)
#
# queue = Queue([1, 2 ,3])
# queue.add(7)
#
# print(queue.get())
# print(queue.queue_data)

# class Stack:
#     def __init__(self, data):
#         self.stack_data = data
#
#     def add(self, element):
#         self.stack_data.append(element)
#
#     def get (self):
#         return self.stack_data.pop(-1)
#
#
# stack = Stack([1, 2 ,3])
# stack.add(7)
# print(stack.stack_data)
# print(stack.get())
#
import requests
print(1)

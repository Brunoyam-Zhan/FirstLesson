# class Singleton:
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(). __new__(cls)
#         return cls.instance
#
# s = Singleton()
# # print("Object created", s)
# print(s)
#
# s1 = Singleton()
# print(s1)
#
# s2 = Singleton()
# print(s2)


from abc import abstractmethod, ABC

# class Singleton(ABC):
#     @abstractmethod
#     def func(self):
#         pass
#
#
#     def __new__(cls):
#         if not hasattr(cls, 'instance'):
#             cls.instance = super(). __new__(cls)
#         return cls.instance
#
# s = Singleton()
# # print("Object created", s)
# print(s)
#
# s1 = Singleton()
# print(s1)
#
# s2 = Singleton()
# print(s2)

# a = 8
# b=7

# def here_is_decorator(function):
#     def wrapper():
#         print("I'm in")
#         function()
#         print("I'm out")
#     return  wrapper()
#
#
# @here_is_decorator
# def this_is_decorator():
#     print("Here are we go again")
#     def this_is_second():
#         if a!= b:
#             print("We did it")
#     def this_this_third():
#         print("We did it second time")
#     return this_is_second(), this_this_third()



#
# def here_is_decorator(function):
#     def wrapper(a, b, c):
#         inspire =
#
#
# @here_is_decorator
# def this_is_decorator():
#     print("Here are we go again")
#     def this_is_second():
#         if a!= b:
#             print("We did it")
#     def this_this_third():
#         print("We did it second time")
#     return this_is_second(), this_this_third()




# a = [2, 3, 45, 56, 23, 5]
#
# def Less1():
#     for i in range(len(a)):
#         for j in range(len(a)-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# print(Less1())



# a = [4, 6, 56, 34, 2, 56, 67, 8]
#
# def less_num():
#     for i in range (len(a)):
#         for j in range(len(a)-1):
#             if a[j] > a[j+1]:
#                 a[j], a[j+1] = a[j+1], a[j]
#     return a
#
# print(less_num())














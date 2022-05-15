# class ManagerContext:
#     def __enter__(self):
#         print("Выполнено __enter__")
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("Выполнено __exit__")
#
# with ManagerContext():
#     print("Between")


# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return  factorial(n-1) * n
#
# print (factorial(10))
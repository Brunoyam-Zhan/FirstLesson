
# tuple = (1, 3, 5, 6)
# a = {1, 3, 5, 6}

# list = [1, 3, 5, 6, 1]
# b = set(list)
# print(type(b))

# test_dict = {
#         "test_login": "123456789",
#         "ivan": "r1232153", "oleg": "aasdw4"
#                 ""
#         }
# print(test_dict.values())

# test_dict = {
#         "test_login": "123456789",
#         "ivan": "r1232153", "oleg": "aasdw4"
#                 ""
#         }
# print(list(test_dict.values())[0])

# нужно потыкать
# test_dict = {  "test_login": {"test_login": "123456789",
#                             "ivan": "r1232153", "oleg": "aasdw4"
#                              }
#         "test_login": "123456789",
#         "ivan": "r1232153", "oleg": "aasdw4"
#         }
# print(test_dict.values())
# print(test_dict)



# users = {"admin": "1234"}
# secret_info = "42"
#
# while True:
#     q1 = input("Вход или регистрация? ")
#     if q1 == "Вход":
#         login = input("Введите логин: ")
#         password = input("Введите пароль: ")
#
#         if login in users.keys():
#             if users [login] == password:
#                 print("Успешный вход!")
#                 print(secret_info)
#                 break
#     elif q1 == "Регистрация":
#         login = input("Введите логин: ")
#         password = input("Введите пароль: ")
#         if login in users.keys():
#             print("Логин занят")
#         else:
#             users[login] = password
#             print("Регистрация прошла успешно!")
#     else:
#         print("Данные введены не верно (Нужно Вход/Регистрация)")




#     elif q1 == "Удаление":
#         login = input("Введите логин: ")
#         password = input("Введите пароль: ")
#         if login in users.keys():
#            del users [login]

# del users [login]




# users = {"admin": "1234"}
# secret_info = "42"
#
# def login():
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#
#     if login in users.keys():
#         if users[login] == password:
#             print("Успешный вход!")
#             print(secret_info)
#
# def register():
#     login = input("Введите логин: ")
#     password = input("Введите пароль: ")
#     if login in users.keys():
#         print("Логин занят")
#     else:
#         users[login] = password
#         print("Регистрация прошла успешно!")
#
# def error():
#     print("Данные введены не верно (Нужно Вход/Регистрация)")
#
#
# while True:
#     q1 = input("Вход или регистрация? ")
#     if q1 == "Вход":
#         login()
#         break
#     elif q1 == "Регистрация":
#         register()
#     else:
#         error()












# 1) Аминистратор управляет меню (добавляет пиццу в меню, удаляет пиццу из меню)
# 2) Пользватель делает заказ(выбирает из меню пиццы, автоматически рассчитывается стоимость заказа)

# menu = {
#     'margarite': 400,
#     'pepperone': 600,
# }

import json

# with open('test1.json', "r") as  f:
#     menu = json.load(f)


def load_menu():
    f = open('test1.json', "r")
    menu = json.load(f)
    f.close()
    return menu

def save_menu(menu):
    f = open('test1.json', "w")
    json.dump(menu, f)
    f.close()



def add_pizza(name, price):
    menu = load_menu()
    if name in menu.keys():
        print("Пицца c таким именем уже есть в меню. Придумайте другое название")
    else:
        menu[name] = price

    save_menu(menu)


def remove_pizza(name):
    menu = load_menu()

    if name in menu.keys():
        print("Пицца c таким именем уже есть в меню. Удаляем")
        del menu[name]
    else:
        print("Пицца c таким именем нет  в меню. Удалять нечего")

    save_menu(menu)


def order_pizza():

    menu = load_menu()

    order = []
    cost = 0

    save_menu(menu)

    while True:
        q1 = input("Продолжим? ")
        if q1 == "нет":
            break
        else:
            print("Наше меню: ")
            print(menu)
            pizza_name = input("Какую пиццу заказываем? ")
            if pizza_name in menu.keys():
                order.append(pizza_name)
                cost += menu[pizza_name]
                print("Пицца добавлено в заказ")
                print("Сумма в корзине: {} " .format(cost))

    return  {"order": order, "cost": cost}

if __name__ == "__main__":
    while True:
        q3 = input("Продолжить?")
        if q3 == "да":
            role = input("Выберете вашу роль?")
            if role == "Админ":
                q2 = input("Добавить или удалить?")
                if q2 == "Добавить":
                    name_pizza = input("Введите имя пиццы: ")
                    name_pizza = name_pizza.strip()
                    price_pizza = int(input("Введите стоимость пиццы: " ))
                    add_pizza(name_pizza, price_pizza)
                elif q2 == "remove":
                    name_pizza = input("Введите имя удаляемой пиццы: ")
                    remove_pizza(name_pizza)

            elif role == "Пользователь":
                print(order_pizza())
            else:
                print("Данные введены неверно")
        elif q3 == "нет":
            break
        else:
            print ("Ошибка ввода")



# list_keys = list(menu.keys())
# list_keys_string = ', '.join(list.keys)
# print(list_keys_string)



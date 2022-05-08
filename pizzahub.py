# 1) Аминистратор управляет меню (добавляет пиццу в меню, удаляет пиццу из меню)
# 2) Пользватель делает заказ(выбирает из меню пиццы, автоматически рассчитывается стоимость заказа)

menu = {
    'margarite': 400,
    'pepperone': 600,
}


def add_pizza(name, price):
    if name in menu.keys():
        print("Пицца c таким именем уже есть в меню. Придумайте другое название")
    else:
        menu[name] = price


print("До добавления")
add_pizza('carbonara', 600)
print("После добавления")


def remove_pizza(name):
    if name in menu.keys():
        print("Пицца c таким именем уже есть в меню. Удаляем")
        del menu[name]
    else:
        print("Пицца c таким именем нет  в меню. Удалять нечего")


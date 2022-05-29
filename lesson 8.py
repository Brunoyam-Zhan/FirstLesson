# a = [4, 1, 3, 2, 6, 5]
#
# for j in range(len(a)):
#     for i in range(len(a)-1):
#         if a[i] > a[i+1]:
#             a[i], a[i+1] = a[i+1], a[i]
#
# print(a)

# a = [4, 1, 3, 2, 6, 5]
# b = []
# def FindLessNum(a):
#     less_num = a[0]
#     for i in range(len(a)):
#         if less_num > a[i]:
#             less_num = a[i]
#     return less_num
# while len(a) != 0:
#     v = FindLessNum(a)
#     b.append(v)
#     a.remove(v)
# print(b)



# from bs4 import BeautifulSoup


# import requests
# page = requests.get("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4"
#                     "%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D"
#                     "1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5")
#
# soup = BeautifulSoup(page.text, 'html.parser')
#
# result = soup.find('div', {'class': 'ArchiveTemp'}).find('span', {'class': 't_0'})
#
# print(result.text)
#


# from flask import Flask
# from bs4 import BeautifulSoup
# import requests
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello ():
#     return "<p>Hello world</p> + "<a href= 'http://127.0.0.1:5000/weather'> </a>"
#
# @app.route('/weather')
# def weather ():
#     page = requests.get("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4"
#                     "%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D"
#                     "1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5")
#     soup = BeautifulSoup(page.text, 'html.parser')
#     result = soup.find('div', {'class': 'ArchiveTemp'}).find('span', {'class': 't_0'})  # print(result.text)
#     return "Текущая погода" + result.text
#
#
#
#
# if __name__ == "__main__":
#     app.run()


# from flask import Flask, render_template
# from bs4 import BeautifulSoup
# import requests
#
# app = Flask(__name__)
#
# @app.route('/')
# def hello ():
#     return render_template('index.html')
#     # return "<p>Hello world</p>" + "<a href='http://127.0.0.1:5000/weather'>Weather</a>"
#
# @app.route('/weather')
# def weather ():
#     page = requests.get("https://rp5.ru/%D0%9F%D0%BE%D0%B3%D0%BE%D0%B4"
#                     "%D0%B0_%D0%B2_%D0%A1%D0%B0%D0%BD%D0%BA%D1%82-%D0%9F%D0%B5%D"
#                     "1%82%D0%B5%D1%80%D0%B1%D1%83%D1%80%D0%B3%D0%B5")
#     soup = BeautifulSoup(page.text, 'html.parser')
#     result = soup.find('div', {'class': 'ArchiveTemp'}).find('span', {'class': 't_0'})  # print(result.text)
#     return "<p>Текущая погода:</p>" + result.text
#            # "<a href='http://127.0.0.1:5000/weather1'><p>Перейдите по ссылке<p></a>"
#
# # @app.route('/weather1')
# # def Weather1 ():
# #     return "Теперь вы знаете погоду"
#
#
# if __name__ == "__main__":
#     # app.run(debug=True) Чтобы не перезапускать код
#     app.run(debug=True)



from flask import Flask, render_template, request, abort
import json
from pizzahub import pizzeria

app = Flask(__name__)

@app.route('/')
def hello():
    return "Доброе пожаловать в пиццерию"


@app.route('/pizzeria/menu', methods = ['GET'])
def get_menu():
    menu = pizzeria.load_menu()
    pizza_name = request.args.get("pizza_name")
    if pizza_name:
        pizza_cost = menu
        if pizza_name in menu:
            return json.dumps(({pizza_name: menu[pizza_name]}))
        else:
            abort(404)
    else:
        return json.dumps(menu)




# if __name__ == "__main__":
#     app.run(debug=True)

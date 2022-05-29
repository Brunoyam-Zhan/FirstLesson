from bs4 import BeautifulSoup
import requests

page = requests.get('http://127.0.0.1:5000')
print(menu.json)

# page = requests.get('http://127.0.0.1:5000/pizzeria/menu', params = {"pizza_name": "margarita"})
# print(menu.json)

# if menu.status_code != 404:
#     print(menu.json())
# else:
#     print('Пиццы не существует')

requests.post('http://127.0.0.1:5000/pizzeria/menu', data={"vezuviy": 600})
print(r.status_code)

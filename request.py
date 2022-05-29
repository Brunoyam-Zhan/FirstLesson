from bs4 import BeautifulSoup
import requests

page = requests.get('http://127.0.0.1:5000')
print(menu.json)

# page = requests.get('http://127.0.0.1:5000/pizzeria/menu', params = {"pizza_name": "margarita"})
# print(menu.json)
import requests
import bs4

data = requests.get('https://ipap.ru')

print(data.text)
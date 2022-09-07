import requests
from bs4 import BeautifulSoup

def check():
    url = 'https://alerts.in.ua/'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    print(soup)

check()
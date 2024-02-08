import bs4
import requests

resultado = requests.get('https://www.youtube.com/');

sopa = bs4.BeautifulSoup(resultado.text, 'lxml');

print(sopa.select("title"))
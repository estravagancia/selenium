import requests
import time
from lxml import html


# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
url_a_analizar = input("Pega aquí la dirección de tu web: ")
# url_a_analizar= 'https://estoes.estravagancia.com'

page = requests.get(f'https://googlechrome.github.io/lighthouse/viewer/?psiurl={url_a_analizar}')
print(page.status_code)

tree = html.fromstring(page.content)
time.sleep(10)
print(tree)

performance = tree.xpath('/html/body/text()')
# performance = tree.xpath('/html/body/main/div/div[2]/div[2]/div/div/div/div[2]/a[1]/div[2]/text()')
print(performance)
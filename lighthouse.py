from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver. import
import time


timeout = 30

# driver = webdriver.Firefox()
driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
chrome_options = webdriver.ChromeOptions() 
chrome_options.add_experimental_option("useAutomationExtension", False) 
chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

url_a_analizar= 'https://grupofedola.com/'

driver.get(f'https://googlechrome.github.io/lighthouse/viewer/?psiurl={url_a_analizar}')
try:
    element_present = EC.presence_of_element_located((By.ID, 'lh-log'))
    WebDriverWait(driver, timeout).until(element_present)
    print(f"Página a analizar: {url_a_analizar}")
except:
    print(f"Se ha sobrepasado el tiempo de espera: {timeout}s en {url_a_analizar}")
finally:

    time.sleep(3)
    
    print('Enviada')

    # identificador = driver.find_element(By.ID,'lh-log')
    # print(identificador)
    # page = driver.find_element(By.TAG_NAME,"body")
    # print(page)
    # File screenshotFile = ((TakesScreenshot) driver).getScreenshotAs(OutputType.FILE)
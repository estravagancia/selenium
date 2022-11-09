import pandas as pd
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
espera_corta = 1
espera_larga = 3
timeout=10

driver = webdriver.Firefox()
# driver = webdriver.Chrome(executable_path='driver\chromedriver.exe')
# chrome_options = webdriver.ChromeOptions() 
# chrome_options.add_experimental_option("useAutomationExtension", False) 
# chrome_options.add_experimental_option("excludeSwitches", ["enable-automation"])

df = pd.read_csv('user.csv', '\t' )

for row, datos in df.iterrows():
    sitio = datos["sitio"]
    user  = datos["user"]
    pwd   = datos["pwd"]

    # Open URL
    driver.get(f"https://{sitio}/wp-login.php")
    
    time.sleep(espera_corta)

    user_browser = driver.find_element(By.XPATH,'//*[@id="user_login"]')
    user_browser.send_keys(user)
    
    time.sleep(espera_corta)

    user_pwd =  driver.find_element(By.XPATH,'//*[@id="user_pass"]')
    user_pwd.send_keys(pwd)

    time.sleep(espera_corta)

    user_button =  driver.find_element(By.XPATH,'//*[@id="wp-submit"]')
    user_button.send_keys(Keys.RETURN)

    time.sleep(espera_larga)

    # email confirmation window
    try:
        aviso = driver.find_element(By.CLASS_NAME,'login-action-confirm_admin_email').is_enabled()
        recordar = driver.find_element(By.XPATH,'/html/body/div[1]/form/div/div[2]/a').click()
    except:
        pass

    try:
        element_present = EC.presence_of_element_located((By.ID, 'wpadminbar'))
        WebDriverWait(driver, timeout).until(element_present)
        print(f"Página de administración cargada en: {sitio}")
    except:
        print(f"Se ha sobrepasado el tiempo de espera: {timeout}s en {sitio}")
  
    # plugins
    try:
        updates = driver.find_element(By.ID,'wp-admin-bar-updates').is_enabled()
        
        driver.get(f"https://{sitio}/wp-admin/update-core.php")
        time.sleep(espera_larga)
        
        update_plugins = driver.find_element(By.XPATH,'//*[@id="plugins-select-all"]').click()
        update_plugins_btn = driver.find_element(By.XPATH,'//*[@id="upgrade-plugins"]').click()
        try:
            element_present = EC.presence_of_element_located((By.ID, 'wpbody-content'))
            WebDriverWait(driver, timeout).until(element_present)
            print(f"Actualización de plugins completada en {sitio}")
        except:
            print(f"Se ha sobrepasado el tiempo de espera: {timeout}s")
    except:
        print(f"En {sitio} no hay actualizaciones de plugins disponibles")

    # themes
    try:
        updates = driver.find_element(By.ID,'wp-admin-bar-updates').is_enabled()

        driver.get(f"https://{sitio}/wp-admin/update-core.php")
        time.sleep(espera_larga)
        
        update_themes = driver.find_element(By.XPATH,'//*[@id="themes-select-all"]').click()
        update_themes_btn = driver.find_element(By.XPATH,'//*[@id="upgrade-themes"]').click()
        timeout=10
        try:
            element_present = EC.presence_of_element_located((By.ID, 'wpbody-content'))
            WebDriverWait(driver, timeout).until(element_present)
            print(f"Actualización de temas completada en {sitio}")
            driver.get(f"https://{sitio}/wp-admin/update-core.php")
        except:
            print(f"Se ha sobrepasado el tiempo de espera: {timeout}s")
    except:
        print(f"En {sitio} no hay actualizaciones de temas disponibles")



time.sleep(espera_corta)

ActionChains(driver)\
    .key_down(Keys.CONTROL)\
    .send_keys('w')\
    .perform()
# driver.close()
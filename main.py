import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

service = webdriver.ChromeService(executable_path = 'webdriver//chromedriver.exe')
driver = webdriver.Chrome(service=service)

# driver = webdriver.Chrome('webdriver//chromedriver.exe')

#Abrir formulario


#abrir base de datos
df = pd.read_csv('bd.csv', sep=';',encoding='latin-1')


#recorrer csv
for row, datos in df.iterrows():
 
    driver.get('https://forms.gle/oWXx99e9E7SBtMFt6');
    time.sleep(1)
 
    index = datos['Id']
    nombre = datos['Nombre']
    empresa = datos['Empresa']
    contacto = datos['Contacto']
    
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(index)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(nombre)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(empresa)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[4]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(contacto)
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()


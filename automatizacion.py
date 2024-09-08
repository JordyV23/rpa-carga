import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By
import os

# Credenciales para iniciar sesion
userClaro = ''
passwordClaro = ''

# Ruta donde se descarga el archivo
archivo_descargado = 'C:/User/usuario/Downloads/reporte.xlsx'

# Inicializar arreglo de fechas de reportes
fechasReporte = [
    '06/09/2024'
]

# Cargar el driver
service = webdriver.ChromeService(executable_path = 'webdriver//chromedriver.exe')
driver = webdriver.Chrome(service=service)

# Dirigirse al sitio web de claro
driver.get('https://forms.gle/oWXx99e9E7SBtMFt6')
time.sleep(1)

# Ingresar credenciales
# User
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(userClaro)
# Password
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(passwordClaro)

# Hacer Click en btn de login
driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()


# Recorrer vector de fechas
for fecha in fechasReporte :
    # Hacer click en navbar
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    
    # Setear fecha
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input').send_keys(index)
    
    # Click en boton para Descargar Excel
    driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    
    # Ruta y nombre del archivo renombrado
    archivo_renombrado = f'C:/User/usuario/Downloads/reporte-{fecha}.xlsx'
    
    # Cambiar el nombre del archivo
    os.rename(archivo_descargado, archivo_renombrado)


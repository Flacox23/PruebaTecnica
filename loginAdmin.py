from selenium import webdriver # Traer exploradores
from selenium.webdriver.common.by import By # Elementos del explorador
import time


# Configurar el navegador (Chrome)
driver = webdriver.Chrome()

# Maximizar ventana
driver.maximize_window()

# Abrir la URL
driver.get("https://bioseguridad.godoycordoba.com/Admin")

# Esperar que cargue
time.sleep(2)

# Localizar los campos e ingresar datos 
driver.find_element(By.CSS_SELECTOR, "#TxtUsuario_I").send_keys("bioadmin")
driver.find_element(By.CSS_SELECTOR, "#TxtClave_I").send_keys("B10@dm1n")
driver.find_element(By.CSS_SELECTOR, ".dx-vam").click()

# Esperar respuesta
time.sleep(5)

# Cerrar navegador
driver.quit()


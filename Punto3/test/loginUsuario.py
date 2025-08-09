from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# Ruta absoluta a la carpeta de evidencias
evidencias_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "evidencias"))

# Configurar el navegador (Chrome)
driver = webdriver.Chrome()
driver.maximize_window()

# Abrir la URL
driver.get("https://bioseguridad.godoycordoba.com")

# Esperar que cargue y hacer login
WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#TxtUsuario_I"))).send_keys("testqa@godoycordoba.com")
driver.find_element(By.CSS_SELECTOR, "#TxtClave_I").send_keys("12345")
driver.find_element(By.CSS_SELECTOR, ".dx-vam").click()


# Tomar captura de pantalla del error
driver.save_screenshot(os.path.join(evidencias_path, "login_fallido.png"))

# Cerrar el navegador después de registrar los tres usuarios
time.sleep(20)
driver.quit()
from selenium import webdriver # Traer exploradores
from selenium.webdriver.common.by import By # Elementos del explorador
from selenium.webdriver.common.keys import Keys # Acciones
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains 
import time
import os


# Ruta absoluta a la carpeta de evidencias
evidencias_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "evidencias"))

# Configurar el navegador (Chrome)
driver = webdriver.Chrome()

# Maximizar ventana
driver.maximize_window()

# Abrir la URL
driver.get("https://bioseguridad.godoycordoba.com")

# Espera indicacion
wait = WebDriverWait(driver, 10) 

# Esperar que cargue
time.sleep(2)

# Localizar los campos e ingresar datos incorrectos
driver.find_element(By.CSS_SELECTOR, "#TxtUsuario_I").send_keys("CamiloFalso")
driver.find_element(By.CSS_SELECTOR, "#TxtClave_I").send_keys("1234567")
driver.find_element(By.CSS_SELECTOR, ".dx-vam").click()

# Esperar respuesta
time.sleep(3)

# Tomar captura de pantalla del error
driver.save_screenshot(os.path.join(evidencias_path, "login_fallido.png"))

# Selecciona la opcion registrar
driver.find_element(By.CSS_SELECTOR, ".azulclaro").click()

# Esperar respuesta
time.sleep(2)

# Localizar los campos e ingresar datos
driver.find_element(By.CSS_SELECTOR, "#TxtNombre_I").send_keys("Camilo")
nit = driver.find_element(By.CSS_SELECTOR, "#TxtNit_I")
nit.click()
nit.send_keys("1000467049")

#Selecciona el desplegable
lista = driver.find_element(By.ID, "LstSector_B-1Img")
lista.click()
actions = ActionChains(driver)
actions.move_to_element(lista)
for _ in range(12):  
    actions.send_keys(Keys.DOWN).perform()  # Simula la tecla de flecha hacia abajo
# Finalmente, presiona la tecla Enter
actions.send_keys(Keys.ENTER).perform()

# Localizar los campos e ingresar datos
driver.find_element(By.CSS_SELECTOR, "#TxtTelefono_I").send_keys("3045621042")
driver.find_element(By.CSS_SELECTOR, "#TxtCorreo_I").send_keys("Camilo@hotmail.com")
driver.find_element(By.CSS_SELECTOR, "#TxtClave_I").send_keys("Peque*957283@")
driver.find_element(By.CSS_SELECTOR, "#BtnRegistrar_CD").click()

# Esperar respuesta
time.sleep(5)

# Tomar captura de pantalla de registro
driver.save_screenshot(os.path.join(evidencias_path, "registrado.png"))

# Cerrar navegador
driver.quit()


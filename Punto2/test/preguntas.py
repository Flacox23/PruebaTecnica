from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys # Acciones
import time
import os

# Ruta absoluta a la carpeta de evidencias
evidencias_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "evidencias"))

# Configurar el navegador (Chrome)
driver = webdriver.Chrome()
driver.maximize_window()

# Abrir la URL
driver.get("https://bioseguridad.godoycordoba.com/Admin")

# Esperar que cargue y hacer login
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#TxtUsuario_I"))).send_keys("bioadmin")
driver.find_element(By.CSS_SELECTOR, "#TxtClave_I").send_keys("B10@dm1n")
driver.find_element(By.CSS_SELECTOR, ".dx-vam").click()

# Ir a la sección de preguntas
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "a[href='Pregunta.aspx']"))).click()

# Lista de nombres a registrar
nombres = ["CamiloPreguntas", "PedroPreguntas", "JuanPreguntas"]

# Iterar sobre la lista de nombres para registrar los usuarios
for nombre in nombres:
    # Clic en "Nuevo"
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='ContentPlaceHolder_GridPregunta_DXCBtn0_CD'] span[class='dx-vam']"))).click()

    # Esperar que aparezca el campo para escribir la pregunta
    campo_nombre = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ContentPlaceHolder_GridPregunta_DXEditor4_I"))
    )
    campo_nombre.clear()  # Limpiar el campo antes de escribir la nueva pregunta
    campo_nombre.send_keys(nombre)  # Escribir la pregunta en el campo

    # Esperar que aparezca el campo para escribir la recomendacion
    campo_nombre = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, "#ContentPlaceHolder_GridPregunta_DXEditor5_I"))
    )
    campo_nombre.clear()  # Limpiar el campo antes de escribir la nueva recomendacion
    campo_nombre.send_keys(nombre)  # Escribir la recomendacion en el campo

    #Selecciona el desplegable sector
    lista = driver.find_element(By.ID, "ContentPlaceHolder_GridPregunta_DXEditor1_B-1Img")
    lista.click()
    actions = ActionChains(driver)
    actions.move_to_element(lista)
    for _ in range(4):  
        actions.send_keys(Keys.DOWN).perform()  # Simula la tecla de flecha hacia abajo
    # Finalmente, presiona la tecla Enter
    actions.send_keys(Keys.ENTER).perform()

    time.sleep(10)

    #Selecciona el desplegable subtema
    lista = driver.find_element(By.ID, "ContentPlaceHolder_GridPregunta_DXEditor3_B-1Img")
    lista.click()
    actions = ActionChains(driver)
    actions.move_to_element(lista)
    for _ in range(1):  
        actions.send_keys(Keys.DOWN).perform()  # Simula la tecla de flecha hacia abajo
    # Finalmente, presiona la tecla Enter
    actions.send_keys(Keys.ENTER).perform()

    # Clic en "Actualizar"
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "div[id='ContentPlaceHolder_GridPregunta_DXCBtn1_CD'] span[class='dx-vam']"))
    ).click()

    # Tomar captura de pantalla de cada pregunta
    driver.save_screenshot(os.path.join(evidencias_path, "crearPregunta.png"))

    # Esperar un momento antes de pasar al siguiente nombre
    time.sleep(5)


# Cerrar el navegador después de registrar los tres usuarios
time.sleep(20)
driver.quit()
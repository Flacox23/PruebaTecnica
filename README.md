# PRUEBA TÉCNICA – Automatización de Pruebas Funcionales E2E

## Descripción
Esta prueba tiene como objetivo validar habilidades en **automatización de pruebas funcionales de extremo a extremo (E2E)**, cubriendo:
- Procesos de **login** con usuario incorrecto y registro automatizado.
- Creación de **sectores, temas, subtemas y preguntas** en el módulo de administración.
- Creación de **evaluaciones** y descarga de sus resultados en **PDF**.

El flujo se ejecuta sobre la plataforma real:  
🔗 [https://bioseguridad.godoycordoba.com](https://bioseguridad.godoycordoba.com)

---

## Estructura del Repositorio
PRUEBATECNICA/
│
├── Punto1/
│ ├── test/ # Código fuente de la automatización del punto 1
│ └── evidencias/ # Capturas de pantalla (login, registro)
│
│
├── Punto2/
│ ├── test/ # Código fuente de la automatización del punto 2
│ └── evidencias/ # Capturas (sectores, temas, subtemas, preguntas)
│ 
│
├── Punto3/
│ ├── test/ # Código fuente de la automatización del punto 3
│ ├── evidencias/ # Capturas (evaluaciones creadas)
│ └── resultados/ # PDFs descargados de evaluaciones
│
└── README.md # Este archivo con instrucciones

## Requisitos Previos

- **Lenguaje:** Python 3.10+
- **Framework:** Selenium
- **Navegador:** Google Chrome (última versión)
- **Driver:** ChromeDriver compatible con tu versión de Chrome
- **Librerías Python:**
  ```bash
  pip install selenium

## Ejecucion de la Automatizacion

1. Clonar el repositorio:
    git clone <https://github.com/Flacox23/PruebaTecnica>
    cd PRUEBATECNICA

2. Ubicarte en el punto a ejecutar:
    cd Punto1/test
    cd Punto2/test
    cd Punto3/test

3. Ejecutar el script:
    python loginError.py
    python preguntas.py
    python sectores.py
    python subtema.py
    python temas.py
    python loginUsuario.py

4. Evidencias y resultados:
    Las capturas se guardan en la carpeta /evidencias de cada punto.
    Los PDFs descargados se almacenan en /resultados.






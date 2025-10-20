QA Project Cohorte 33 Jose Perez sprint 8 — Urban.Routes

Automatización de pruebas UI con Selenium WebDriver + Pytest del flujo completo “Pedir un taxi” en Urban.Routes.

Descripción del proyecto

Este repositorio contiene pruebas automatizadas end-to-end de la aplicación web Urban Routes. El set cubre: configurar direcciones, seleccionar tarifa Comfort, registrar número de teléfono (con OTP interceptado), agregar tarjeta de crédito, enviar mensaje al conductor, activar “Manta y pañuelos”, pedir 2 helados y verificar la apertura del modal de búsqueda de taxi.

Tecnologías y técnicas utilizadas

Lenguaje / Librerías

Python 3.11+

Selenium 4.x

Pytest

Navegador

Google Chrome (Selenium Manager gestiona el driver)

Patrones y buenas prácticas

Page Object Model (POM): toda la interacción en pages/Urban_routes_page.py

Setters / Clickers / Readers: set_, click_, get_*

Esperas explícitas: WebDriverWait + expected_conditions

Localizadores estables: preferencia por ID, CSS y XPath relativos

Interceptación de OTP: utils/retrive_code.py usa logs de rendimiento del navegador

Cómo ejecutar las pruebas

Instalar dependencias

pip install -U selenium pytest

Configurar datos en data/data.py

urban_routes_url = 'https://.../containerhub.../?lng=es'

address_from = 'East 2nd Street, 601'

address_to = '1300 1st St'

phone_number = '+1 123 123 12 12'

card_number = '1234 5678 9100'

card_code = '111'

message_for_driver = 'Vamos al partido'

Importante: Actualizar la URL al reiniciar el servidor cada vez que reinicies el servidor/contendedor de TripleTen en: data/data.py → urban_routes_url = "<NUEVA_URL>?lng=es"

Ejecutar Pytest desde la raíz del proyecto

pytest -q tests/Test_urban_routes.py

En PyCharm: clic derecho sobre tests/Test_urban_routes.py → Run 'pytest in Test_urban_routes.py'.

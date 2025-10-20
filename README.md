# 🚖 QA Project – Cohorte 33 | José Pérez | Sprint 8 — Urban.Routes  

## 🧪 Automatización de pruebas UI con Selenium WebDriver + Pytest  
Flujo completo **“Pedir un taxi”** en la aplicación **Urban.Routes**.  

---

## 📄 Descripción del Proyecto  
Este repositorio contiene **pruebas automatizadas end-to-end** de la aplicación web **Urban Routes**.  

El set de pruebas cubre:  
- Configurar direcciones  
- Seleccionar tarifa **Comfort**  
- Registrar número de teléfono (**con OTP interceptado**)  
- Agregar tarjeta de crédito  
- Enviar mensaje al conductor  
- Activar la opción **“Manta y pañuelos”**  
- Pedir **2 helados**  
- Verificar la apertura del **modal de búsqueda de taxi**

---

## ⚙️ Tecnologías y Técnicas Utilizadas  

### 🔹 Lenguaje / Librerías  
- Python 3.11+  
- Selenium 4.x  
- Pytest  

### 🌐 Navegador  
- Google Chrome (Selenium Manager gestiona el driver automáticamente)

---

## 🧱 Patrones y Buenas Prácticas  
- **Page Object Model (POM):** toda la interacción en `pages/Urban_routes_page.py`  
- **Setters / Clickers / Readers:** métodos con prefijos `set_`, `click_`, `get_`  
- **Esperas explícitas:** uso de `WebDriverWait` + `expected_conditions`  
- **Localizadores estables:** preferencia por **ID**, **CSS** y **XPath relativos**  
- **Interceptación de OTP:** `utils/retrieve_code.py` usa los **logs de rendimiento** del navegador  

---

## ▶️ Cómo Ejecutar las Pruebas  

### 📦 Instalar dependencias  
```bash
pip install -U selenium pytest
🧾 Configurar datos en data/data.py
python
Copiar código
urban_routes_url = 'https://.../containerhub.../?lng=es'
address_from = 'East 2nd Street, 601'
address_to = '1300 1st St'
phone_number = '+1 123 123 12 12'
card_number = '1234 5678 9100'
card_code = '111'
message_for_driver = 'Vamos al partido'
⚠️ Importante:
Actualiza la URL cada vez que reinicies el servidor o contenedor de TripleTen:
data/data.py → urban_routes_url = "https://<NUEVA_URL>?lng=es"

💻 Ejecutar Pytest desde la raíz del proyecto
bash
Copiar código
pytest -q tests/Test_urban_routes.py
🧠 En PyCharm
Clic derecho sobre
tests/Test_urban_routes.py → Run 'pytest in Test_urban_routes.py'

pytest -q tests/Test_urban_routes.py

En PyCharm: clic derecho sobre tests/Test_urban_routes.py → Run 'pytest in Test_urban_routes.py'.

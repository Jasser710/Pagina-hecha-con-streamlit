# 🌱 DataGrow - Registro de Productos de Cultivo

**Materia:** Programación Web  
**Participantes:** Jason Barrantes, Jasser Palacios, Junior Ramírez, Melany Ramírez

---

## 🚀 Descripción

DataGrow es una aplicación web construida con **Python + Streamlit + SQLAlchemy + MySQL**, que permite a la empresa ficticia Datagrow registrar y gestionar productos de cultivo.

La aplicación permite:
- Registrar nuevos productos mediante un formulario.
- Guardar los datos en una base de datos MySQL.
- Verificar que los datos se almacenaron correctamente.

---

## 📦 Estructura del proyecto

```
📁 Pagina-hecha-con-streamlit/
 │
 ├── app.py            # App principal (Streamlit)
 ├── database.py       # Configuración de SQLAlchemy + conexión MySQL
 ├── models.py         # Modelo Producto
 ├── requirements.txt  # Dependencias del proyecto
 ├──.gitignore         # Archivo .gitignore
 └── README.md
```

---

## ⚙️ Tecnologías utilizadas

- Python 3.x
- Streamlit
- SQLAlchemy
- MySQL + mysql-connector
- Entorno virtual (recomendado)

---

## 🔑 Configuración previa

1️⃣ **Base de datos MySQL**

- Asegúrate de tener MySQL Server instalado y funcionando.
- Crea la base de datos:
  ```sql
  CREATE DATABASE datagrow;
  ```

2️⃣ **Configura tu conexión**

Abre `database.py` y reemplaza la cadena de conexión:

```py
DATABASE_URL = "mysql+mysqlconnector://root:TU_CONTRASEÑA@localhost/datagrow"
```

➡️ Sustituye **`TU_CONTRASEÑA`** por la contraseña de tu usuario MySQL.

---

## ⚙️ Instalación y ejecución

### ✅ 1️⃣ Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd Pagina-hecha-con-streamlit
```

### ✅ 2️⃣ Crear un entorno virtual

```bash
# En Windows
python -m venv venv
venv\Scripts\activate

# En macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### ✅ 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

**Ejemplo mínimo de `requirements.txt`:**
```
streamlit
sqlalchemy
mysql-connector-python
```

---

## 🚦 4️⃣ Ejecutar la aplicación

Desde la raíz del proyecto, corre:

```bash
streamlit run app.py
```

Esto abrirá la interfaz web de **DataGrow** en tu navegador.  
Ahí podrás registrar productos de cultivo y guardarlos en la base de datos.

---

## ✅ Verifica los registros

Puedes usar MySQL Workbench o consola para revisar los productos guardados:

```sql
USE datagrow;
SELECT * FROM productos;
```

---

## 📝 Notas finales

- Cada vez que se ejecuta `app.py`, SQLAlchemy revisa si la tabla `productos` existe y la crea si es necesario.
- Usa siempre el entorno virtual para evitar conflictos de dependencias.
- Si cambias tu modelo (`models.py`), ejecuta de nuevo `Base.metadata.create_all(bind=engine)` para actualizar la base.

---

🚀 **¡Listo!** Con este proyecto, Datagrow puede registrar y gestionar productos de cultivo de forma sencilla y profesional.

---

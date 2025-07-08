import streamlit as st
from database import SessionLocal, engine, Base
from models import Producto
from datetime import date

# ✅ 1️⃣ Crear tablas si no existen
Base.metadata.create_all(bind=engine)

# ✅ 2️⃣ Título principal
st.title("🌱 DataGrow - Registro de Productos de Cultivo")

# ✅ 3️⃣ Subtítulo o instrucciones
st.write("""
Bienvenido al panel de registro de productos de Datagrow.
Utiliza el formulario para registrar nuevos productos de cultivo.
""")

# ✅ 4️⃣ Formulario Streamlit - versión base
nombre = st.text_input("Nombre del producto")
tipo_cultivo = st.selectbox("Tipo de cultivo", ["Hortaliza", "Grano", "Frutal", "Tubérculo", "Otro"])
fecha_ingreso = st.date_input("Fecha de ingreso", value=date.today())
cantidad_stock = st.number_input("Cantidad en stock", min_value=0, step=1)
precio_unitario = st.number_input("Precio unitario", min_value=0.0, step=0.1, format="%.2f")

# ✅ 5️⃣ Botón para guardar
if st.button("Guardar producto"):
    # Validación básica
    if nombre and cantidad_stock >= 0 and precio_unitario >= 0:
        db = SessionLocal()
        nuevo_producto = Producto(
            nombre=nombre,
            tipo_cultivo=tipo_cultivo,
            fecha_ingreso=fecha_ingreso,
            cantidad_stock=cantidad_stock,
            precio_unitario=precio_unitario
        )
        db.add(nuevo_producto)
        db.commit()
        db.close()
        st.success(f"Producto '{nombre}' guardado correctamente ✅")
    else:
        st.error("Por favor completa todos los campos correctamente.")

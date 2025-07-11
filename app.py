import streamlit as st
from database import SessionLocal, engine, Base
from models import Producto
from datetime import date
import pandas as pd

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

st.header("📊 Productos Registrados")

# Opciones de ordenamiento
sort_by = st.selectbox("Ordenar por", ["Ninguno", "Fecha de Ingreso", "Precio Unitario", "Cantidad en Stock", "Tipo de Cultivo"])
sort_order = st.radio("Orden", ["Ascendente", "Descendente"])

if st.button("Ver Productos"):
    db = SessionLocal()
    productos = db.query(Producto).all()
    db.close()

    if productos:
        # Convertir a DataFrame para fácil manipulación y visualización
        df = pd.DataFrame([p.__dict__ for p in productos])
        df = df.drop(columns=['_sa_instance_state']) # Eliminar columna interna de SQLAlchemy

        # Aplicar ordenamiento
        if sort_by == "Fecha de Ingreso":
            df = df.sort_values(by="fecha_ingreso", ascending=(sort_order == "Ascendente"))
        elif sort_by == "Precio Unitario":
            df = df.sort_values(by="precio_unitario", ascending=(sort_order == "Ascendente"))
        elif sort_by == "Cantidad en Stock":
            df = df.sort_values(by="cantidad_stock", ascending=(sort_order == "Ascendente"))
        elif sort_by == "Tipo de Cultivo":
            df = df.sort_values(by="tipo_cultivo", ascending=(sort_order == "Ascendente"))

        st.dataframe(df)
    else:
        st.info("No hay productos registrados aún.")

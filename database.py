from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 👉 1️⃣ URL de conexión — reemplaza TU_CONTRASEÑA por tu contraseña real de MySQL
DATABASE_URL = "mysql+mysqlconnector://root:jason0808@localhost/datagrow"

# 👉 2️⃣ Crear el engine (motor de conexión)
engine = create_engine(DATABASE_URL)

# 👉 3️⃣ Crear la sesión local — así abres una sesión cada vez que consultas
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# 👉 4️⃣ Declarative Base — de aquí heredan todos tus modelos
Base = declarative_base()

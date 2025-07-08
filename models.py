from sqlalchemy import Column, Integer, String, Date, Float
from database import Base

class Producto(Base):
    __tablename__ = "productos"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    tipo_cultivo = Column(String(50), nullable=False)
    fecha_ingreso = Column(Date, nullable=False)
    cantidad_stock = Column(Integer, nullable=False)
    precio_unitario = Column(Float, nullable=False)

from pydantic import BaseModel
from typing import Optional

class EmpleadoSchema(BaseModel):
    Nombre: str
    Apellido: str
    Telefono: Optional[str] = None
    Direccion: Optional[str] = None
    RFC: Optional[str] = None
    Pago_mes: Optional[float] = None
    contrasena: Optional[str] = None  

class IngredienteSchema(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Cantidad: Optional[int] = None

class PlatilloSchema(BaseModel):
    Nombre: str
    Descripcion: Optional[str] = None
    Precio: Optional[float] = None

class PreparacionSchema(BaseModel):
    Platillos_ID_Platillo: int
    Ingrediente_ID_ingrediente: int

class MesaSchema(BaseModel):
    Capacidad: Optional[int] = None  # ← ahora es int

class ClienteSchema(BaseModel):
    Nombre: str
    Correo: Optional[str] = None
    Telefono: Optional[str] = None
    ID_mesa: Optional[int] = None

class OrdenSchema(BaseModel):
    Tipo_orden: Optional[str] = None
    Total: Optional[float] = None
    Metodo_de_pago: Optional[str] = None
    Cambio: Optional[str] = None
    ID_cliente: int
    fecha: Optional[str] = None

class CompraSchema(BaseModel):
    Id_empleado: int
    Id_orden: int
    Id_platillo: int
    cantidad: Optional[int] = None

class EnSalSchema(BaseModel):
    dinero: float
    tipo: Optional[str] = None
    ID_orden: Optional[int] = None
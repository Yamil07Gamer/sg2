from fastapi import APIRouter, HTTPException
from sg2.schemas.schemas import (
    EmpleadoSchema, IngredienteSchema, PlatilloSchema,
    PreparacionSchema, MesaSchema, ClienteSchema,
    OrdenSchema, CompraSchema, EnSalSchema
)
from sg2.models.controller import (
    EmpleadoModel, IngredienteModel, PlatilloModel,
    PreparacionModel, MesaModel, ClienteModel,
    OrdenModel, CompraModel, EnSalModel, ConsultaModel
)
from sg2.db.database import get_db_connection

router = APIRouter()

# ── EMPLEADO ──────────────────────────────────────────────
@router.post("/empleado/")
def crear_empleado(empleado: EmpleadoSchema):
    id = EmpleadoModel.crear(empleado)
    return {"message": "Empleado creado", "id": id}

@router.get("/empleado/")
def listar_empleados():
    return EmpleadoModel.listar_todos()

@router.get("/empleado/total")
def total_empleados():
    return {"total_empleados": EmpleadoModel.contar_total()}

@router.get("/empleado/{id_empleado}")
def obtener_empleado(id_empleado: int):
    emp = EmpleadoModel.obtener(id_empleado)
    if not emp:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return emp

@router.delete("/empleado/{id_empleado}")
def eliminar_empleado(id_empleado: int):
    EmpleadoModel.eliminar(id_empleado)
    return {"message": "Empleado eliminado"}

# ── INGREDIENTE ───────────────────────────────────────────
@router.post("/ingrediente/")
def crear_ingrediente(ingrediente: IngredienteSchema):
    id = IngredienteModel.crear(ingrediente)
    return {"message": "Ingrediente creado", "id": id}

@router.get("/ingrediente/")
def listar_ingredientes():
    return IngredienteModel.listar_todos()

@router.get("/ingrediente/total")
def total_ingredientes():
    return {"total_ingredientes": IngredienteModel.contar_total()}

@router.get("/ingrediente/{id_ingrediente}")
def obtener_ingrediente(id_ingrediente: int):
    ing = IngredienteModel.obtener(id_ingrediente)
    if not ing:
        raise HTTPException(status_code=404, detail="Ingrediente no encontrado")
    return ing

@router.delete("/ingrediente/{id_ingrediente}")
def eliminar_ingrediente(id_ingrediente: int):
    IngredienteModel.eliminar(id_ingrediente)
    return {"message": "Ingrediente eliminado"}

# ── PLATILLO ──────────────────────────────────────────────
@router.post("/platillo/")
def crear_platillo(platillo: PlatilloSchema):
    id = PlatilloModel.crear(platillo)
    return {"message": "Platillo creado", "id": id}

@router.get("/platillo/")
def listar_platillos():
    return PlatilloModel.listar_todos()

@router.get("/platillo/total")
def total_platillos():
    return {"total_platillos": PlatilloModel.contar_total()}

@router.get("/platillo/{id_platillo}")
def obtener_platillo(id_platillo: int):
    plat = PlatilloModel.obtener(id_platillo)
    if not plat:
        raise HTTPException(status_code=404, detail="Platillo no encontrado")
    return plat

@router.delete("/platillo/{id_platillo}")
def eliminar_platillo(id_platillo: int):
    PlatilloModel.eliminar(id_platillo)
    return {"message": "Platillo eliminado"}

# ── PREPARACION ───────────────────────────────────────────
@router.post("/preparacion/")
def crear_preparacion(preparacion: PreparacionSchema):
    PreparacionModel.crear(preparacion)
    return {"message": "Preparacion creada"}

@router.get("/preparacion/")
def listar_preparaciones():
    return PreparacionModel.listar_todos()

@router.get("/preparacion/{id_platillo}")
def listar_preparacion_por_platillo(id_platillo: int):
    return PreparacionModel.listar_por_platillo(id_platillo)

# ── MESA ──────────────────────────────────────────────────
@router.post("/mesa/")
def crear_mesa(mesa: MesaSchema):
    id = MesaModel.crear(mesa)
    return {"message": "Mesa creada", "id": id}

@router.get("/mesa/")
def listar_mesas():
    return MesaModel.listar_todos()

@router.get("/mesa/total")
def total_mesas():
    return {"total_mesas": MesaModel.contar_total()}

@router.get("/mesa/{id_mesa}")
def obtener_mesa(id_mesa: int):
    mesa = MesaModel.obtener(id_mesa)
    if not mesa:
        raise HTTPException(status_code=404, detail="Mesa no encontrada")
    return mesa

@router.delete("/mesa/{id_mesa}")
def eliminar_mesa(id_mesa: int):
    MesaModel.eliminar(id_mesa)
    return {"message": "Mesa eliminada"}

# ── CLIENTE ───────────────────────────────────────────────
@router.post("/cliente/")
def crear_cliente(cliente: ClienteSchema):
    id = ClienteModel.crear(cliente)
    return {"message": "Cliente creado", "id": id}

@router.get("/cliente/")
def listar_clientes():
    return ClienteModel.listar_todos()

@router.get("/cliente/total")
def total_clientes():
    return {"total_clientes": ClienteModel.contar_total()}

@router.get("/cliente/{id_cliente}")
def obtener_cliente(id_cliente: int):
    cli = ClienteModel.obtener(id_cliente)
    if not cli:
        raise HTTPException(status_code=404, detail="Cliente no encontrado")
    return cli

@router.delete("/cliente/{id_cliente}")
def eliminar_cliente(id_cliente: int):
    ClienteModel.eliminar(id_cliente)
    return {"message": "Cliente eliminado"}

# ── ORDEN ─────────────────────────────────────────────────
@router.post("/orden/")
def crear_orden(orden: OrdenSchema):
    id = OrdenModel.crear(orden)
    return {"message": "Orden creada", "id": id}

@router.get("/orden/")
def listar_ordenes():
    return OrdenModel.listar_todos()

@router.get("/orden/total")
def total_ordenes():
    return {"total_ordenes": OrdenModel.contar_total()}

@router.get("/orden/{id_orden}")
def obtener_orden(id_orden: int):
    orden = OrdenModel.obtener(id_orden)
    if not orden:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return orden

@router.delete("/orden/{id_orden}")
def eliminar_orden(id_orden: int):
    OrdenModel.eliminar(id_orden)
    return {"message": "Orden eliminada"}

# ── COMPRA ────────────────────────────────────────────────
@router.post("/compra/")
def crear_compra(compra: CompraSchema):
    id = CompraModel.crear(compra)
    return {"message": "Compra creada", "id": id}

@router.get("/compra/")
def listar_compras():
    return CompraModel.listar_todos()

@router.get("/compra/total")
def total_compras():
    return {"total_compras": CompraModel.contar_total()}

@router.get("/compra/{id_compra}")
def obtener_compra(id_compra: int):
    compra = CompraModel.obtener(id_compra)
    if not compra:
        raise HTTPException(status_code=404, detail="Compra no encontrada")
    return compra

@router.delete("/compra/{id_compra}")
def eliminar_compra(id_compra: int):
    CompraModel.eliminar(id_compra)
    return {"message": "Compra eliminada"}

@router.post("/ensal/")
def crear_ensal(ensal: EnSalSchema):
    EnSalModel.crear(ensal)
    return {"message": "Registro creado"}

@router.get("/ensal/")
def listar_ensal():
    return EnSalModel.listar_todos()

@router.get("/ensal/total")
def total_ensal():
    return {"total": EnSalModel.contar_total()}
# ── LOGIN ─────────────────────────────────────────────────
from pydantic import BaseModel

class LoginSchema(BaseModel):
    nombre: str
    contrasena: str

@router.post("/login")
def login(data: LoginSchema):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT ID_empleado FROM Empleado WHERE Nombre = %s AND contrasena = %s",
        (data.nombre, data.contrasena)
    )
    emp = cursor.fetchone()
    conn.close()
    if emp:
        return {"ok": True, "id_empleado": emp["ID_empleado"]}
    return {"ok": False}

# ── CONSULTAS MULTITABLA ──────────────────────────────────

@router.get("/consulta/orden/{id_orden}")
def detalle_orden(id_orden: int):
    res = ConsultaModel.detalle_orden(id_orden)
    if not res:
        raise HTTPException(status_code=404, detail="Orden no encontrada")
    return res

@router.get("/consulta/empleado/{id_empleado}/historial")
def historial_empleado(id_empleado: int):
    res = ConsultaModel.historial_empleado(id_empleado)
    if not res:
        raise HTTPException(status_code=404, detail="Sin registros para este empleado")
    return res
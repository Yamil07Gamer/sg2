from sg2.db.database import get_db_connection

# ── EMPLEADO ──────────────────────────────────────────────
class EmpleadoModel:
    @staticmethod
    def crear(empleado):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Empleado 
                   (Nombre, Apellido, Telefono, Direccion, RFC, Pago_mes, contrasena)
                   VALUES (%s, %s, %s, %s, %s, %s, %s)"""
        cursor.execute(query, ( empleado.Nombre, empleado.Apellido,
                               empleado.Telefono, empleado.Direccion, empleado.RFC, empleado.Pago_mes, empleado.contrasena))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Empleado")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener(id_empleado):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Empleado WHERE ID_empleado = %s", (id_empleado,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def eliminar(id_empleado):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Empleado WHERE ID_empleado = %s", (id_empleado,))
        conn.commit()
        conn.close()

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Empleado")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# ── INGREDIENTE ───────────────────────────────────────────
class IngredienteModel:
    @staticmethod
    def crear(ingrediente):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Ingredientes
                   (Nombre, Descripcion, Cantidad)
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (ingrediente.Nombre,
                               ingrediente.Descripcion, ingrediente.Cantidad))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ingredientes")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener(id_ingrediente):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Ingredientes WHERE ID_ingrediente = %s", (id_ingrediente,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def eliminar(id_ingrediente):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Ingredientes WHERE ID_ingrediente = %s", (id_ingrediente,))
        conn.commit()
        conn.close()

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Ingredientes")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# ── PLATILLO ──────────────────────────────────────────────
class PlatilloModel:
    @staticmethod
    def crear(platillo):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Platillos
                   (Nombre, Descripcion, Precio)
                   VALUES (%s, %s, %s)"""
        cursor.execute(query, (platillo.Nombre,
                               platillo.Descripcion, platillo.Precio))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Platillos")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener(id_platillo):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Platillos WHERE ID_platillo = %s", (id_platillo,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def eliminar(id_platillo):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Platillos WHERE ID_platillo = %s", (id_platillo,))
        conn.commit()
        conn.close()

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Platillos")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# ── PREPARACION ───────────────────────────────────────────
class PreparacionModel:
    @staticmethod
    def crear(preparacion):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Preparacion
                   (Platillos_ID_Platillo, Ingrediente_ID_ingrediente)
                   VALUES (%s, %s)"""
        cursor.execute(query, (preparacion.Platillos_ID_Platillo,
                               preparacion.Ingrediente_ID_ingrediente))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Preparacion")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def listar_por_platillo(id_platillo):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""SELECT * FROM Preparacion
                          WHERE Platillos_ID_Platillo = %s""", (id_platillo,))
        res = cursor.fetchall()
        conn.close()
        return res

# ── MESA ──────────────────────────────────────────────────
class MesaModel:
    @staticmethod
    def crear(mesa):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = "INSERT INTO Mesa (Capacidad) VALUES (%s)"
        cursor.execute(query, (mesa.Capacidad,))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Mesa")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener(id_mesa):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Mesa WHERE ID_mesa = %s", (id_mesa,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def eliminar(id_mesa):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Mesa WHERE ID_mesa = %s", (id_mesa,))
        conn.commit()
        conn.close()

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Mesa")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# ── CLIENTE ───────────────────────────────────────────────
class ClienteModel:
    @staticmethod
    def crear(cliente):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Cliente
                   (Nombre, Correo, Telefono, ID_mesa)
                   VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (cliente.Nombre,
                               cliente.Correo, cliente.Telefono, cliente.ID_mesa))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Cliente")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener(id_cliente):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Cliente WHERE ID_cliente = %s", (id_cliente,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def eliminar(id_cliente):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Cliente WHERE ID_cliente = %s", (id_cliente,))
        conn.commit()
        conn.close()

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Cliente")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# ── ORDEN ─────────────────────────────────────────────────
class OrdenModel:
    @staticmethod
    def crear(orden):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Orden
                   (Tipo_orden, Total, Metodo_de_pago, Cambio, ID_cliente, fecha)
                   VALUES (%s, %s, %s, %s, %s, SYSDATE())"""
        cursor.execute(query, (orden.Tipo_orden, orden.Total,
                               orden.Metodo_de_pago, orden.Cambio, orden.ID_cliente))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Orden")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener(id_orden):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Orden WHERE ID_orden = %s", (id_orden,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def eliminar(id_orden):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Orden WHERE ID_orden = %s", (id_orden,))
        conn.commit()
        conn.close()

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Orden")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# ── COMPRA ────────────────────────────────────────────────
class CompraModel:
    @staticmethod
    def crear(compra):
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """INSERT INTO Compra
           (Id_empleado, Id_orden, Id_platillo, cantidad)
           VALUES (%s, %s, %s, %s)"""
        cursor.execute(query, (compra.Id_empleado, compra.Id_orden,
                            compra.Id_platillo, compra.cantidad))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Compra")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def obtener(id_compra):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM Compra WHERE ID_compra = %s", (id_compra,))
        res = cursor.fetchone()
        conn.close()
        return res

    @staticmethod
    def eliminar(id_compra):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Compra WHERE ID_compra = %s", (id_compra,))
        conn.commit()
        conn.close()

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM Compra")
        total = cursor.fetchone()[0]
        conn.close()
        return total

class EnSalModel:
    @staticmethod
    def crear(ensal):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO En_sal (dinero, tipo, ID_orden) VALUES (%s, %s, %s)",
                       (ensal.dinero, ensal.tipo, ensal.ID_orden))
        conn.commit()
        last_id = cursor.lastrowid
        conn.close()
        return last_id

    @staticmethod
    def listar_todos():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM En_sal")
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def contar_total():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM En_sal")
        total = cursor.fetchone()[0]
        conn.close()
        return total

# ── CONSULTAS MULTITABLA ──────────────────────────────────
class ConsultaModel:

    @staticmethod
    def detalle_orden(id_orden):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                o.ID_orden, o.Tipo_orden, o.Total, o.Metodo_de_pago, o.Cambio, o.fecha,
                c.Nombre AS cliente_nombre, c.Correo, c.Telefono,
                p.Nombre AS platillo_nombre, p.Precio,
                co.cantidad
            FROM Orden o
            JOIN Cliente c ON o.ID_cliente = c.ID_cliente
            JOIN Compra co ON co.Id_orden = o.ID_orden
            JOIN Platillos p ON co.Id_platillo = p.ID_platillo
            WHERE o.ID_orden = %s
        """, (id_orden,))
        res = cursor.fetchall()
        conn.close()
        return res

    @staticmethod
    def historial_empleado(id_empleado):
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT
                e.ID_empleado, e.Nombre AS empleado_nombre, e.Apellido,
                co.ID_compra, co.cantidad,
                o.ID_orden, o.Tipo_orden, o.Total, o.fecha,
                p.Nombre AS platillo_nombre
            FROM Compra co
            JOIN Empleado e ON co.Id_empleado = e.ID_empleado
            JOIN Orden o ON co.Id_orden = o.ID_orden
            JOIN Platillos p ON co.Id_platillo = p.ID_platillo
            WHERE e.ID_empleado = %s
            ORDER BY o.fecha DESC, o.ID_orden
        """, (id_empleado,))
        res = cursor.fetchall()
        conn.close()
        return res
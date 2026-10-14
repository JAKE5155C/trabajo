from pydantic import ValidationError

from biblioteca.dominio import repositorios
from biblioteca.dominio.esquemas import ProductoActualizar


async def listar_productos(conn) -> list[dict]:
    return await repositorios.obtener_productos(conn)


async def obtener_producto(conn, producto_id: int) -> dict | None:
    return await repositorios.obtener_producto(conn, producto_id)


def validar_actualizacion_producto(
    nombre: str | None,
    precio: str | None,
    cantidad: str | None,
    descripcion: str | None,
) -> tuple[ProductoActualizar | None, dict[str, str]]:
    errores = {}
    try:
        precio_numero = float(precio) if precio is not None and precio.strip() else None
    except ValueError:
        precio_numero = None
        errores["precio"] = "El precio debe ser un número mayor que cero."

    try:
        cantidad_numero = int(cantidad) if cantidad is not None and cantidad.strip() else None
    except ValueError:
        cantidad_numero = None
        errores["cantidad"] = "La cantidad debe ser un número entero mayor o igual que cero."

    try:
        datos = ProductoActualizar(
            nombre=nombre or "",
            precio=precio_numero,
            cantidad=cantidad_numero,
            descripcion=descripcion,
        )
    except ValidationError as error:
        datos = None
        for detalle in error.errors():
            campo = detalle["loc"][0]
            if campo == "nombre":
                errores[campo] = "El nombre es obligatorio y debe tener entre 1 y 100 caracteres."
            elif campo == "precio":
                errores[campo] = "El precio debe ser un número mayor que cero."
            elif campo == "cantidad":
                errores[campo] = "La cantidad debe ser un número entero mayor o igual que cero."

    return datos, errores


async def guardar_producto(conn, producto_id: int, datos: ProductoActualizar) -> dict | None:
    actualizado = await repositorios.actualizar_producto(
        conn,
        producto_id,
        datos.nombre,
        datos.precio,
        datos.cantidad,
        datos.descripcion,
    )
    if not actualizado:
        return None
    return await repositorios.obtener_producto(conn, producto_id)
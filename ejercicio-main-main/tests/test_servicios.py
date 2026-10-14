import unittest

from biblioteca.dominio.servicios import validar_actualizacion_producto


class ValidarActualizacionProductoTests(unittest.TestCase):
    def test_acepta_datos_validos_y_convierte_tipos(self):
        datos, errores = validar_actualizacion_producto(
            "Teclado",
            "15.75",
            "0",
            None,
        )

        self.assertEqual(errores, {})
        self.assertEqual(datos.nombre, "Teclado")
        self.assertEqual(datos.precio, 15.75)
        self.assertEqual(datos.cantidad, 0)

    def test_rechaza_campos_fuera_de_limites(self):
        datos, errores = validar_actualizacion_producto("", "0", "-1", "")

        self.assertIsNone(datos)
        self.assertEqual(set(errores), {"nombre", "precio", "cantidad"})

    def test_rechaza_valores_no_numericos(self):
        datos, errores = validar_actualizacion_producto(
            "Teclado",
            "abc",
            "2.5",
            None,
        )

        self.assertIsNone(datos)
        self.assertEqual(set(errores), {"precio", "cantidad"})


if __name__ == "__main__":
    unittest.main()
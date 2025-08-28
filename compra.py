from datetime import datetime


class Compra:
    def __init__(self, IDCompra, FechaIngreso, IDEmpleado, NIT, Total):
        self.IDCompra = IDCompra
        self.FechaIngreso = FechaIngreso
        self.IDEmpleado = IDEmpleado
        self.NIT = NIT
        self.Total = Total

    def __str__(self):
        return f"Compra(ID:{self.IDCompra}, Fecha:{self.FechaIngreso}, Empleado:{self.IDEmpleado}, NIT:{self.NIT}, Total:{self.Total})"


class DetalleCompra:
    def __init__(self, IDDetalleCompra, IDVenta, IDProducto, Cantidad, Subtotal, FechaCaducidad):
        self.IDDetalleCompra = IDDetalleCompra
        self.IDVenta = IDVenta
        self.IDProducto = IDProducto
        self.Cantidad = Cantidad
        self.Subtotal = Subtotal
        self.FechaCaducidad = FechaCaducidad

    def __str__(self):
        return f"Detalle(ID:{self.IDDetalleCompra}, Venta:{self.IDVenta}, Prod:{self.IDProducto}, Cantidad:{self.Cantidad}, Subtotal:{self.Subtotal}, Vence:{self.FechaCaducidad})"

class GestorCompras:
    def __init__(self):
        self.compras: dict[int, Compra] = {}
        self.detalles: dict[int, DetalleCompra] = {}
        self.cargar_datos()


    def cargar_datos(self):
        try:
            with open("COMPRAS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    IDCompra, FechaIngreso, IDEmpleado, NIT, Total = linea.strip().split(":")
                    compra = Compra(int(IDCompra), FechaIngreso, int(IDEmpleado), NIT, float(Total))
                    self.compras[compra.IDCompra] = compra
        except FileNotFoundError:
            pass

        try:
            with open("DETALLECOMPRAS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    IDDetalleCompra, IDVenta, IDProducto, Cantidad, Subtotal, FechaCaducidad = linea.strip().split(":")
                    detalle = DetalleCompra(int(IDDetalleCompra), int(IDVenta), int(IDProducto),
                                            int(Cantidad), float(Subtotal), FechaCaducidad)
                    self.detalles[detalle.IDDetalleCompra] = detalle
        except FileNotFoundError:
            pass


    def guardar_datos(self):
        with open("COMPRAS.txt", "w", encoding="utf-8") as archivo:
            for compra in self.compras.values():
                archivo.write(f"{compra.IDCompra}:{compra.FechaIngreso}:{compra.IDEmpleado}:{compra.NIT}:{compra.Total}\n")

        with open("DETALLECOMPRAS.txt", "w", encoding="utf-8") as archivo:
            for detalle in self.detalles.values():
                archivo.write(f"{detalle.IDDetalleCompra}:{detalle.IDVenta}:{detalle.IDProducto}:{detalle.Cantidad}:{detalle.Subtotal}:{detalle.FechaCaducidad}\n")

    def registrar_compra(self, compra: Compra, detalle: DetalleCompra):
        self.compras[compra.IDCompra] = compra
        self.detalles[detalle.IDDetalleCompra] = detalle
        self.guardar_datos()
        print("Compra y detalle registrados correctamente.")

    def mostrar_compras(self):
        print("\n-- LISTA DE COMPRAS --")
        for compra in self.compras.values():
            print(compra)
        print("\n-- DETALLES DE COMPRAS --")
        for detalle in self.detalles.values():
            print(detalle)


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


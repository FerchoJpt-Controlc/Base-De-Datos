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

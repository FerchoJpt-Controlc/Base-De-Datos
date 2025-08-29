from datetime import datetime

class Venta:
    def __init__(self, IDVenta: str, Fecha: str, IDEmpleado: str, NIT: str, Total: float):
        self.IDVenta = IDVenta
        self.Fecha = Fecha if Fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.IDEmpleado = IDEmpleado
        self.NIT = NIT
        self.Total = Total
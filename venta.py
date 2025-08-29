from datetime import datetime

class Venta:
    def __init__(self, IDVenta: str, Fecha: str, IDEmpleado: str, NIT: str, Total: float):
        self.IDVenta = IDVenta
        self.Fecha = Fecha if Fecha else datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.IDEmpleado = IDEmpleado
        self.NIT = NIT
        self.Total = Total


    def __str__(self):

        return f"Venta(ID:{self.IDVenta}, Fecha:{self.Fecha}, Empleado:{self.IDEmpleado}, Cliente:{self.NIT}, Total:{self.Total})"



class GestorVentas:
    def __init__(self):
        self.ventas: dict[str, Venta] = {}
        self.cargar_ventas()

    def cargar_ventas(self):
        try:
            with open("VENTAS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) == 5:
                        IDVenta, Fecha, IDEmpleado, NIT, Total = partes
                        venta = Venta(IDVenta, Fecha, IDEmpleado, NIT, float(Total))
                        self.ventas[IDVenta] = venta
        except FileNotFoundError:
            print("Archivo VENTAS.txt no encontrado, se creara al guardar.")

    def guardar_ventas(self):
        with open("VENTAS.txt", "w", encoding="utf-8") as archivo:
            for venta in self.ventas.values():
                archivo.write(f"{venta.IDVenta}:{venta.Fecha}:{venta.IDEmpleado}:{venta.NIT}:{venta.Total}\n")

    def registrar_venta(self, venta: Venta):
        self.ventas[venta.IDVenta] = venta
        self.guardar_ventas()
        print(f"Venta {venta.IDVenta} registrada correctamente.")

    def mostrar_ventas(self):
        print("\n-- LISTA DE VENTAS --")
        for venta in self.ventas.values():
            print(venta)
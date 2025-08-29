class Proveedor:
    def __init__(self, NIT, Nombre, Direccion, Telefono, Correo, Empresa):
        self.NIT = NIT
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.Empresa = Empresa

    def __str__(self):
        return f"Proveedor(NIT:{self.NIT}, Nombre:{self.Nombre}, Empresa:{self.Empresa})"

class GestorProveedores:
    def __init__(self):
        self.proveedores: dict[str, Proveedor] = {}
        self.cargar_proveedores()

    def cargar_proveedores(self):
        try:
            with open("PROVEEDORES.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) == 6:
                        NIT, Nombre, Direccion, Telefono, Correo, Empresa = partes
                        proveedor = Proveedor(NIT, Nombre, Direccion, Telefono, Correo, Empresa)
                        self.proveedores[NIT] = proveedor
        except FileNotFoundError:
            print("Archivo PROVEEDORES.txt no encontrado, se creará al guardar.")

    def guardar_proveedores(self):
        with open("PROVEEDORES.txt", "w", encoding="utf-8") as archivo:
            for proveedor in self.proveedores.values():
                archivo.write(
                    f"{proveedor.NIT}:{proveedor.Nombre}:{proveedor.Direccion}:{proveedor.Telefono}:{proveedor.Correo}:{proveedor.Empresa}\n")

    def registrar_proveedor(self, proveedor: Proveedor):
        self.proveedores[proveedor.NIT] = proveedor
        self.guardar_proveedores()
        print(f"Proveedor {proveedor.Nombre} registrado correctamente.")

    def mostrar_proveedores(self):
        print("\n-- LISTA DE PROVEEDORES --")
        for proveedor in self.proveedores.values():
            print(proveedor)

class Cliente:
    def __init__(self, NIT: str, Nombre: str, Direccion: str, Telefono: str, Correo: str):
        self.NIT = NIT
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo

    def __str__(self):
        return f"Cliente(NIT:{self.NIT}, Nombre:{self.Nombre}, Dirección:{self.Direccion}, Tel:{self.Telefono}, Correo:{self.Correo})"


class GestorClientes:
    def __init__(self):
        self.clientes: dict[str, Cliente] = {}
        self.cargar_clientes()

    def cargar_clientes(self):
        try:
            with open("CLIENTES.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) == 5:
                        NIT, Nombre, Direccion, Telefono, Correo = partes
                        cliente = Cliente(NIT, Nombre, Direccion, Telefono, Correo)
                        self.clientes[NIT] = cliente
        except FileNotFoundError:
            print("Archivo CLIENTES.txt no encontrado, se creará al guardar.")

    def guardar_clientes(self):
        with open("CLIENTES.txt", "w", encoding="utf-8") as archivo:
            for cliente in self.clientes.values():
                archivo.write(f"{cliente.NIT}:{cliente.Nombre}:{cliente.Direccion}:{cliente.Telefono}:{cliente.Correo}\n")

    def registrar_cliente(self, cliente: Cliente):
        self.clientes[cliente.NIT] = cliente
        self.guardar_clientes()
        print(f"Cliente {cliente.Nombre} registrado correctamente.")

    def mostrar_clientes(self):
        print("\n-- LISTA DE CLIENTES --")
        for cliente in self.clientes.values():
            print(cliente)
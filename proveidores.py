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

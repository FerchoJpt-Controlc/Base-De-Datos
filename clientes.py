class Cliente:
    def __init__(self, NIT: str, Nombre: str, Direccion: str, Telefono: str, Correo: str):
        self.NIT = NIT
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo

    def __str__(self):
        return f"Cliente(NIT:{self.NIT}, Nombre:{self.Nombre}, Dirección:{self.Direccion}, Tel:{self.Telefono}, Correo:{self.Correo})"

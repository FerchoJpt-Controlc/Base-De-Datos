class Empleado:
    def __init__(self, IDEmpleado, Nombre, Direccion, Telefono, Correo, Puesto):
        self.IDEmpleado = IDEmpleado
        self.Nombre = Nombre
        self.Direccion = Direccion
        self.Telefono = Telefono
        self.Correo = Correo
        self.Puesto = Puesto

    def __str__(self):
        return (f"Empleado(ID:{self.IDEmpleado}, Nombre:{self.Nombre}, Dirección:{self.Direccion}, Teléfono:{self.Telefono}, Correo:{self.Correo}, Puesto:{self.Puesto})")

print()


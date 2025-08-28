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




class GestorEmpleados:
    def __init__(self):
        self.empleados: dict[int, Empleado] = {}
        self.cargar_datos()

    def cargar_datos(self):
        try:
            with open("EMPLEADOS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) != 6:
                        continue
                    IDEmpleado, Nombre, Direccion, Telefono, Correo, Puesto = partes
                    empleado = Empleado(int(IDEmpleado), Nombre, Direccion, Telefono, Correo, Puesto)
                    self.empleados[empleado.IDEmpleado] = empleado
            print("Empleados importados desde EMPLEADOS.txt")
        except FileNotFoundError:
            print("No existe el archivo EMPLEADOS.txt, se creará uno nuevo al guardar.")

    def guardar_datos(self):
        with open("EMPLEADOS.txt", "w", encoding="utf-8") as archivo:
            for empleado in self.empleados.values():
                archivo.write(
                    f"{empleado.IDEmpleado}:{empleado.Nombre}:{empleado.Direccion}:{empleado.Telefono}:{empleado.Correo}:{empleado.Puesto}\n")

    def registrar_empleado(self, empleado: Empleado):
        self.empleados[empleado.IDEmpleado] = empleado
        self.guardar_datos()
        print(f"Empleado ID:{empleado.IDEmpleado} registrado correctamente.")

    def mostrar_empleados(self):
        if not self.empleados:
            print("No hay empleados registrados.")
            return
        print("\n-- LISTA DE EMPLEADOS --")
        for empleado in self.empleados.values():
            print(f" - {empleado}")

    def buscar_empleado(self, IDEmpleado: int):
        return self.empleados.get(IDEmpleado, None)






def menu_empleados():
    gestor = GestorEmpleados()

    while True:
        print("\n=== MENÚ DE EMPLEADOS ===")
        print("1. Registrar nuevo empleado")
        print("2. Mostrar empleados")
        print("3. Buscar empleado por ID")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                try:
                    idempleado = int(input("ID Empleado: "))
                    nombre = input("Nombre: ")
                    direccion = input("Dirección: ")
                    telefono = input("Teléfono: ")
                    correo = input("Correo: ")
                    puesto = input("Puesto: ")

                    empleado = Empleado(idempleado, nombre, direccion, telefono, correo, puesto)
                    gestor.registrar_empleado(empleado)

                except ValueError:
                    print("ERROR... Entrada inválida...")

            case "2":
                gestor.mostrar_empleados()

            case "3":
                try:
                    idempleado = int(input("Ingrese ID del empleado a buscar: "))
                    empleado = gestor.buscar_empleado(idempleado)
                    if empleado:
                        print(empleado)
                    else:
                        print("Empleado no encontrado.")
                except ValueError:
                    print("Entrada inválida.")

            case "4":
                print("Saliendo del submenú de empleados...")
                break

            case _:
                print("Opción inválida, intente de nuevo.")



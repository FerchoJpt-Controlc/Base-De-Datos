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

class GestorCompras:
    def __init__(self):
        self.compras: dict[int, Compra] = {}
        self.detalles: dict[int, DetalleCompra] = {}
        self.cargar_datos()


    def cargar_datos(self):
        try:
            with open("COMPRAS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    IDCompra, FechaIngreso, IDEmpleado, NIT, Total = linea.strip().split(":")
                    compra = Compra(int(IDCompra), FechaIngreso, int(IDEmpleado), NIT, float(Total))
                    self.compras[compra.IDCompra] = compra
        except FileNotFoundError:
            pass

        try:
            with open("DETALLECOMPRAS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    partes = linea.strip().split(":")
                    if len(partes) == 9:
                        IDDetalleCompra, IDVenta, IDProducto, NombreProducto, Categoria, IDCategoria, Cantidad, Subtotal, FechaCaducidad = partes
                        detalle = DetalleCompra(int(IDDetalleCompra), int(IDVenta), int(IDProducto),
                                                NombreProducto, Categoria, int(IDCategoria),
                                                int(Cantidad), float(Subtotal), FechaCaducidad)
                        self.detalles[detalle.IDDetalleCompra] = detalle
        except FileNotFoundError:
            pass


    def guardar_datos(self):
        with open("COMPRAS.txt", "w", encoding="utf-8") as archivo:
            for compra in self.compras.values():
                archivo.write(
                    f"{compra.IDCompra}:{compra.FechaIngreso}:{compra.IDEmpleado}:{compra.NIT}:{compra.Total}\n")

        with open("DETALLECOMPRAS.txt", "w", encoding="utf-8") as archivo:
            for detalle in self.detalles.values():
                archivo.write(
                    f"{detalle.IDDetalleCompra}:{detalle.IDVenta}:{detalle.IDProducto}:{detalle.NombreProducto}:{detalle.Categoria}:{detalle.IDCategoria}:{detalle.Cantidad}:{detalle.Subtotal}:{detalle.FechaCaducidad}\n")

    def registrar_compra(self, compra: Compra, detalle: DetalleCompra):
        self.compras[compra.IDCompra] = compra
        self.detalles[detalle.IDDetalleCompra] = detalle


        with open("PRODUCTOS.txt", "a", encoding="utf-8") as archivo:
            archivo.write(
                f"{detalle.IDProducto}:{detalle.NombreProducto}:{detalle.Categoria}:{detalle.IDCategoria}:{detalle.Subtotal / detalle.Cantidad}\n")

        self.guardar_datos()
        print("Compra y detalle registrados correctamente.")


    def mostrar_compras(self):
        print("\n-- DETALLES DE COMPRAS --")
        for detalle in self.detalles.values():
            print(detalle)


    def aumentar_stock(self, IDProducto, cantidad_extra):
        productos = {}


        try:
            with open("PRODUCTOS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    partes = linea.strip().split(":")
                    if len(partes) == 5:
                        idp, nombre, categoria, idcat, precio = partes
                        productos[int(idp)] = [nombre, categoria, int(idcat), float(precio)]
        except FileNotFoundError:
            print("No existe PRODUCTOS.txt")
            return

        if IDProducto in productos:
            print(f"Stock del producto {IDProducto} aumentado en {cantidad_extra}.")

        else:
            print("Producto no encontrado en PRODUCTOS.txt.")


        with open("PRODUCTOS.txt", "w", encoding="utf-8") as archivo:
            for idp, datos in productos.items():
                nombre, categoria, idcat, precio = datos
                archivo.write(f"{idp}:{nombre}:{categoria}:{idcat}:{precio}\n")



def menu_compras():
    gestor = GestorCompras()

    while True:
        print("\n=== MENÚ DE COMPRAS ===")
        print("1. Registrar nueva compra")
        print("2. Mostrar compras y detalles")
        print("3. Aumentar stock de un producto")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        match opcion:
            case "1":
                try:
                    idcompra = input("ID Compra: ")
                    fecha = datetime.now().strftime("%Y-%m-%d")
                    idempleado = int(input("ID Empleado: "))
                    nit = input("NIT DISTRIBUIDORA: ")
                    total = float(input("Total: Q. "))

                    compra = Compra(idcompra, fecha, idempleado, nit, total)

                    iddetalle = input("ID Detalle Compra: ")
                    idventa = input("ID Venta: ")
                    idproducto = int(input("ID Producto: "))
                    nombre_producto = input("Nombre del producto: ")
                    categoria = input("Categoría: ")
                    idcategoria = input("ID Categoría: ")
                    cantidad = int(input("Cantidad: "))
                    subtotal = float(input("Subtotal: "))
                    fechacad = input("Fecha de caducidad (YYYY-MM-DD): ")

                    detalle = DetalleCompra(iddetalle, idventa, idproducto, nombre_producto, categoria, idcategoria,
                                            cantidad, subtotal, fechacad)

                    gestor.registrar_compra(compra, detalle)
                except ValueError:
                    print("Entrada inválida...")

            case "2":
                gestor.mostrar_compras()

            case "3":
                try:
                    idproducto = int(input("ID del producto a aumentar stock: "))
                    cantidad_extra = int(input("Cantidad a agregar: "))
                    gestor.aumentar_stock(idproducto, cantidad_extra)
                except ValueError:
                    print("Entrada inválida...")

            case "4":
                print("Saliendo del submenú de compras...")
                break

            case _:
                print("Opción inválida, intente de nuevo.")
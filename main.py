import compra
import empleados
import proveidores

from abc import ABC, abstractmethod

class I_Producto(ABC):
    @abstractmethod
    def obtener_precio(self):
        pass

class I_Inventario(ABC):
    @abstractmethod
    def aumentar_stock(self, cantidad):
        pass

    @abstractmethod
    def disminuir_stock(self, cantidad):
        pass

class I_Categoria(ABC):
    @abstractmethod
    def obtener_nombre(self):
        pass
#inicio de prueba de adaptacion para guardar los datos en txt

#fin prueba



class Categoria(I_Categoria):
    def __init__(self, IDCategoria, nombre):
        self.IDCategoria = IDCategoria
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre

    def __str__(self):
        return f"Categoria(ID:{self.IDCategoria}, Nombre:{self.nombre})"



class Producto(I_Producto):
    def __init__(self, IDproducto, categoria: Categoria, nombre, precio, stock=0):
        self.IDproducto = IDproducto
        self.categoria = categoria
        self.nombre = nombre
        self.precio = precio
        self.stock = stock



    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return f"{self.nombre} (ID:{self.IDproducto}, Precio: {self.precio}, Cat:{self.categoria.obtener_nombre()}, Stock:{self.stock})"




class Inventario(I_Inventario):
    def __init__(self):
        self.productos: dict[int, Producto] = {}
        self.cargar_productos()

    def cargar_productos(self):
        try:
            with open("PRODUCTOS.txt", "r", encoding="utf-8") as archivo:
                for linea in archivo:
                    linea = linea.strip()
                    if not linea:
                        continue
                    partes = linea.split(":")
                    if len(partes) != 4:

                        continue
                    IDproducto_str, nombre, categoria_nombre, precio_str, stock_str = partes
                    try:
                        IDproducto = int(IDproducto_str)
                        precio = float(precio_str)
                        stock = int(stock_str)
                    except ValueError:
                        continue

                    categoria = Categoria(0, categoria_nombre)
                    producto = Producto(IDproducto, categoria, nombre, precio, stock)
                    self.productos[IDproducto] = producto
            print("Productos importados desde PRODUCTOS.txt")
        except FileNotFoundError:
            print("No existe el archivo PRODUCTOS.txt, se creará uno nuevo al guardar.")

    def guardar_productos(self):
        with open("PRODUCTOS.txt", "w", encoding="utf-8") as archivo:
            for producto in self.productos.values():
                archivo.write(
                    f"{producto.IDproducto}:{producto.nombre}:{producto.categoria.obtener_nombre()}:{producto.precio}:{producto.stock}\n"
                )

    def agregar_producto(self, producto: Producto):
        self.productos[producto.IDproducto] = producto
        self.guardar_productos()
        print(f"Producto ID:{producto.IDproducto} agregado y guardado correctamente.")

    def mostrar_todos(self):
        if not self.productos:
            print("No hay productos registrados.")
            return
        print("\nLista de productos:")
        for producto in self.productos.values():
            print(f" - {producto}")


    def aumentar_stock(self, IDProducto, cantidad):
        if IDProducto in self.productos:
            self.productos[IDProducto].stock += cantidad
            self.guardar_productos()
            print(
                f"Stock del producto {IDProducto} aumentado en {cantidad}. Nuevo stock: {self.productos[IDProducto].stock}")
        else:
            print("Producto no encontrado en inventario.")

    def disminuir_stock(self, IDProducto, cantidad):
        if IDProducto in self.productos:
            if self.productos[IDProducto].stock >= cantidad:
                self.productos[IDProducto].stock -= cantidad
                self.guardar_productos()
                print(
                    f"Stock del producto {IDProducto} disminuido en {cantidad}. Nuevo stock: {self.productos[IDProducto].stock}")
            else:
                print("Stock insuficiente para realizar la operación.")
        else:
            print("Producto no encontrado en inventario.")



class menu:
    inventario = Inventario()

    while True:
        print("\n==M E N U==")
        print("1. Ingresar nuevo producto")
        print("2. Mostrar inventario")
        print("3. Empleados")
        print("4. Compras")
        print("5. Mostrar proveedores")
        print("6. Salir")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                try:
                    idproducto = int(input("ID Producto: "))
                    nombre = input("Nombre del producto: ")
                    precio = float(input("Precio: "))
                    stock = int(input("Cantidad en stock: "))
                    idcategoria = input("ID Categoría (numérico, puede ser 0 si no aplica): ")
                    nombre_categoria = input("Nombre de la categoría: ")


                    categoria = Categoria(idcategoria, nombre_categoria)
                    producto = Producto(idproducto, categoria, nombre, precio, stock)

                    inventario.agregar_producto(producto)

                    print("PRODUCTO REGISTRADO CON ÉXITO")
                except ValueError:
                    print("ERROR... ENTRADA INVÁLIDA...")

            case "2":
                inventario.mostrar_todos()

            case "3":
                empleados.menu_empleados()

            case "4":
                compra.menu_compras()

            case "5":
                proveidores.mostrar_proveedores()

            case "5":
                print("GRACIAS POR USAR EL PROGRAMA...CHAUUU...ASTA LUEGO...POR LA SOMBRITA...")
                break

            case _:
                print("Opcion invalida...intente de nuevo")

menu()
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




class Categoria(I_Categoria):
    def __init__(self, IDCategoria, nombre):
        self.IDCategoria = IDCategoria
        self.nombre = nombre

    def obtener_nombre(self):
        return self.nombre

    def __str__(self):
        return f"Categoria(ID:{self.IDCategoria}, Nombre:{self.nombre})"



class Producto(I_Producto):
    def __init__(self, IDproducto, categoria: Categoria, nombre, precio):
        self.IDproducto = IDproducto
        self.categoria = categoria
        self.nombre = nombre
        self.precio = precio


    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return f"{self.nombre} (ID:{self.IDproducto}, Precio: {self.precio}, Cat:{self.categoria.obtener_nombre()})"




class Inventario(I_Inventario):
    def __init__(self):
        self.productos = {}

    def agregar_producto(self, producto: Producto):
        self.productos[producto.IDproducto] = producto
        print(f"Producto {producto.nombre} agregado al inventario.")

    def mostrar_inventario(self):
        if self.productos:
            print("\n_- INVENTARIO -_")
            for idp, p in self.productos.items():
                print(p)
        else:
            print("El inventario está vacío.")


    def aumentar_stock(self, cantidad):
        pass

    def disminuir_stock(self, cantidad):
        pass



def menu():
    inventario = Inventario()

    while True:
        print("\n==M E N U==")
        print("1. Ingresar nuevo producto")
        print("2. Mostrar inventario")
        print("3. Salir")

        opcion = input("Seleccione una opcion: ")

        match opcion:
            case "1":
                try:
                    idproducto = int(input("ID Producto: "))
                    nombre = input("Nombre del producto: ")
                    precio = float(input("Precio: "))
                    idcategoria = int(input("ID Categoría: "))
                    nombre_categoria = input("Nombre de la categoría: ")

                    categoria = Categoria(idcategoria, nombre_categoria)
                    producto = Producto(idproducto, categoria, nombre, precio)

                    inventario.agregar_producto(producto)

                    print("PRODUCTO REGISTRADO CON EXITO")
                except ValueError:
                    print("ERROR...ENTRADA INVALIDA...")

            case "2":
                inventario.mostrar_inventario()

            case "3":
                print("ADIOS...Saliendo del sistema...")
                break

            case _:
                print("Opcion invalida...intente de nuevo")

menu()
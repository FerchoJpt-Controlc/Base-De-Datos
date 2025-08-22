from abc import ABC, abstractmethod

class I_Producto(ABC):
    @abstractmethod
    def obtener_precio(self) -> float:
        pass

class I_Inventario(ABC):
    @abstractmethod
    def aumentar_stock(self, cantidad: int):
        pass

    @abstractmethod
    def disminuir_stock(self, cantidad: int):
        pass


class Producto(I_Producto):
    def __init__(self, IDproducto, IDcategoria, nombre, precio):
        self.IDproducto = IDproducto
        self.IDcategoria = IDcategoria
        self.nombre = nombre
        self.precio = precio


    def obtener_precio(self):
        return self.precio

    def __str__(self):
        return f"{self.nombre} (ID:{self.IDproducto}, Precio: {self.precio}, Cat:{self.IDcategoria})"




class Inventario(I_Inventario):
    def __init__(self):
        self.productos = {}  # Diccionario para guardar productos {IDproducto: Producto}

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

    # Métodos abstractos requeridos
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
                    nombre = input("Nombre: ")
                    precio = float(input("Precio: "))
                    idcategoria = int(input("ID Categoría: "))

                    produ = Producto(idproducto, idcategoria, nombre, precio)
                    inventario.agregar_producto(produ)

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
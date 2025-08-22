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

def menu():
    inventarios={}

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

                    print("PRODUCTO REGISTRADO CON EXITO")
                except ValueError:
                    print("ERROR...ENTRADA INVALIDA...")

            case "2":
                if inventarios:
                    print("\n_-INVENTARIO-_")

                else:
                    print("NO HAY PRODUCTOS REGISTRADOS")

            case "3":
                print("ADIOS...Saliendo del sistema...")
                break

            case _:
                print("Opcion invalida...intente de nuevo")

menu()
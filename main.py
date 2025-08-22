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


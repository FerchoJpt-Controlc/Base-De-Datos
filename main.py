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
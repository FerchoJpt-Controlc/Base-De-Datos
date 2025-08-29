class DetalleVenta:
    def __init__(self, IDDetalleVenta, IDVenta, IDProducto, Cantidad, Subtotal, Stock):
        self.IDDetalleVenta = IDDetalleVenta
        self.IDVenta = IDVenta
        self.IDProducto = IDProducto
        self.Cantidad = int(Cantidad)
        self.Subtotal = float(Subtotal)
        self.Stock = int(Stock)


from abc import ABC, abstractmethod
from datetime import datetime

# Clase abstracta para representar un Pedido
class Pedido(ABC):
    def __init__(self, cliente, productos):
        self.cliente = cliente
        self.productos = productos
        self.fecha_pedido = datetime.now()

    @abstractmethod
    def generar_factura(self):
        pass

# Clase para representar un Pedido al Contado
class PedidoContado(Pedido):
    def generar_factura(self):
        # Lógica para generar factura en formato PDF
        return f"Generando factura para {self.cliente}"

# Clase para representar un Pedido al Crédito
class PedidoCredito(Pedido):
    def generar_factura(self):
        # Lógica para generar nota de crédito en formato PDF
        return f"Generando nota de crédito para {self.cliente}"

# Factory Method para crear pedidos
class PedidoFactory(ABC):
    @abstractmethod
    def crear_pedido(self, cliente, productos):
        pass

# Factory para crear pedidos al Contado
class PedidoContadoFactory(PedidoFactory):
    def crear_pedido(self, cliente, productos):
        return PedidoContado(cliente, productos)

# Factory para crear pedidos al Crédito
class PedidoCreditoFactory(PedidoFactory):
    def crear_pedido(self, cliente, productos):
        return PedidoCredito(cliente, productos)
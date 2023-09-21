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
        print(f"Generando factura al contado para {self.cliente}")

# Clase para representar un Pedido al Crédito
class PedidoCredito(Pedido):
    def generar_factura(self):
        # Lógica para generar nota de crédito en formato PDF
        print(f"Generando nota de crédito para {self.cliente}")

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

# Aqui en esta seccion se podria generar un ejemplo de uso de este
if __name__ == "__main__":
    cliente = "Cliente Ejemplo"
    productos = ["Pastel de Chocolate", "Pastel de Fresa"]
    
    # Crear un pedido al contado
    factory_contado = PedidoContadoFactory()
    pedido_contado = factory_contado.crear_pedido(cliente, productos)
    pedido_contado.generar_factura()

    # Crear un pedido al crédito
    factory_credito = PedidoCreditoFactory()
    pedido_credito = factory_credito.crear_pedido(cliente, productos)
    pedido_credito.generar_factura()


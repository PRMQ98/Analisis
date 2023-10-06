from abc import ABC, abstractmethod
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import tempfile
from jinja2 import Environment, FileSystemLoader

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
        # Genera el archivo PDF
        pdf_buffer = tempfile.SpooledTemporaryFile()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        c.drawString(100, 750, f"Factura para {self.cliente}")
        c.showPage()
        c.save()
        pdf_buffer.seek(0)

        return pdf_buffer

# Clase para representar un Pedido al Crédito
class PedidoCredito(Pedido):
    def generar_factura(self):
        pdf_buffer = tempfile.SpooledTemporaryFile()
        c = canvas.Canvas(pdf_buffer, pagesize=letter)
        c.drawString(100, 750, f"Nota de crédito para {self.cliente}")
        c.showPage()
        c.save()
        pdf_buffer.seek(0)

        return pdf_buffer

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
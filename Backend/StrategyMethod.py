from abc import ABC, abstractmethod

# Clase base para las estrategias de visualización
class EstrategiaDeVisualizacion(ABC):
    @abstractmethod
    def mostrar_pasteles(self, pasteles):
        pass

# Implementación concreta de una estrategia de visualización en consola
class EstrategiaConsola(EstrategiaDeVisualizacion):
    def mostrar_pasteles(self, pasteles):
        print("Pasteles Disponibles:")
        for pastel in pasteles:
            print(f"- {pastel}")

# Implementación concreta de una estrategia de visualización en una ventana gráfica
class EstrategiaVentana(EstrategiaDeVisualizacion):
    def mostrar_pasteles(self, pasteles):
        # Aquí se puede implementar la visualización en una ventana gráfica
        print("Visualización en una ventana gráfica:")
        for pastel in pasteles:
            print(f"- {pastel}")

# Clase principal que utiliza la estrategia de visualización
class CatalogoDePasteles:
    def __init__(self, estrategia):
        self.estrategia = estrategia
        self.pasteles = []

    def agregar_pastel(self, pastel):
        self.pasteles.append(pastel)

    def mostrar_pasteles(self):
        self.estrategia.mostrar_pasteles(self.pasteles)

# Uso del patrón de estrategia
if __name__ == "__main__":
    # Crear un catálogo con estrategia de visualización en consola
    catalogo_consola = CatalogoDePasteles(EstrategiaConsola())

    catalogo_consola.agregar_pastel("Pastel de Chocolate")
    catalogo_consola.agregar_pastel("Pastel de Fresa")
    catalogo_consola.agregar_pastel("Pastel de Vainilla")

    # Mostrar los pasteles en consola
    catalogo_consola.mostrar_pasteles()

    # Cambiar a una estrategia de visualización en ventana gráfica
    catalogo_ventana = CatalogoDePasteles(EstrategiaVentana())

    catalogo_ventana.agregar_pastel("Pastel de Manzana")
    catalogo_ventana.agregar_pastel("Pastel de Limón")

    # Mostrar los pasteles en una ventana gráfica (simulado)
    catalogo_ventana.mostrar_pasteles()
from abc import ABC, abstractmethod

# Clase base del sujeto observable (CatalogoDePasteles)
class CatalogoDePasteles(ABC):
    def __init__(self):
        self.observadores = []

    def agregar_observador(self, observador):
        self.observadores.append(observador)

    def eliminar_observador(self, observador):
        self.observadores.remove(observador)

    @abstractmethod
    def notificar_observadores(self):
        pass

# Implementación concreta del sujeto observable
class CatalogoDePastelesConcreto(CatalogoDePasteles):
    def __init__(self):
        super().__init__()
        self.pasteles = []

    def agregar_pastel(self, pastel):
        self.pasteles.append(pastel)
        self.notificar_observadores()

    def notificar_observadores(self):
        for observador in self.observadores:
            observador.actualizar(self.pasteles)

# Clase base del observador
class Observador(ABC):
    @abstractmethod
    def actualizar(self, pasteles):
        pass

# Implementación concreta del observador que muestra los pasteles en la consola
class ObservadorDeVisualizacion(Observador):
    def actualizar(self, pasteles):
        print("Pasteles Disponibles:")
        for pastel in pasteles:
            print(f"- {pastel}")

# Uso del patrón de observador
if __name__ == "__main__":
    catalogo = CatalogoDePastelesConcreto()

    observador1 = ObservadorDeVisualizacion()
    catalogo.agregar_observador(observador1)

    catalogo.agregar_pastel("Pastel de Chocolate")
    catalogo.agregar_pastel("Pastel de Fresa")
    catalogo.agregar_pastel("Pastel de Vainilla")
# Clase base del catálogo de pasteles
class CatalogoDePasteles:
    def obtener_pasteles(self):
        pass

# Implementación concreta del catálogo de pasteles
class CatalogoDePastelesConcreto(CatalogoDePasteles):
    def obtener_pasteles(self):
        return ["Pastel de Chocolate", "Pastel de Fresa", "Pastel de Vainilla"]

# Decorador abstracto para agregar funcionalidad de visualización
class DecoradorDeVisualizacion(CatalogoDePasteles):
    def __init__(self, catalogo):
        self.catalogo = catalogo

    def obtener_pasteles(self):
        pasteles = self.catalogo.obtener_pasteles()
        self.mostrar_pasteles(pasteles)
        return pasteles

    def mostrar_pasteles(self, pasteles):
        print("Pasteles Disponibles:")
        for pastel in pasteles:
            print(f"- {pastel}")

# Decorador concreto para resaltar algunos pasteles
class DecoradorDeResaltado(DecoradorDeVisualizacion):
    def obtener_pasteles(self):
        pasteles = super().obtener_pasteles()
        self.resaltar_pasteles(pasteles)
        return pasteles

    def resaltar_pasteles(self, pasteles):
        print("\nPasteles Resaltados:")
        for pastel in pasteles:
            if "Chocolate" in pastel or "Fresa" in pastel:
                print(f"- **{pastel}**")
            else:
                print(f"- {pastel}")

# Uso del patrón de decorador
if __name__ == "__main__":
    catalogo_base = CatalogoDePastelesConcreto()
    catalogo_con_visualizacion = DecoradorDeVisualizacion(catalogo_base)
    catalogo_con_resaltado = DecoradorDeResaltado(catalogo_base)

    print("Catálogo de Pasteles sin Decorador:")
    catalogo_base.obtener_pasteles()

    print("\nCatálogo de Pasteles con Decorador de Visualización:")
    catalogo_con_visualizacion.obtener_pasteles()

    print("\nCatálogo de Pasteles con Decorador de Resaltado:")
    catalogo_con_resaltado.obtener_pasteles()
# Fábrica abstracta para productos de pastelería
class PasteleriaFactory:
    def crear_pastel(self):
        pass
    
    def crear_galleta(self):
        pass

# Fábrica concreta para productos de pastelería de chocolate
class PasteleriaDeChocolateFactory(PasteleriaFactory):
    def crear_pastel(self):
        return PastelDeChocolate()
    
    def crear_galleta(self):
        return GalletaDeChocolate()

# Fábrica concreta para productos de pastelería de vainilla
class PasteleriaDeVainillaFactory(PasteleriaFactory):
    def crear_pastel(self):
        return PastelDeVainilla()
    
    def crear_galleta(self):
        return GalletaDeVainilla()

# Clase base para pasteles
class Pastel:
    def sabor(self):
        pass

# Clase concreta para Pastel de Chocolate
class PastelDeChocolate(Pastel):
    def sabor(self):
        return "Chocolate"

# Clase concreta para Pastel de Vainilla
class PastelDeVainilla(Pastel):
    def sabor(self):
        return "Vainilla"

# Clase base para galletas
class Galleta:
    def sabor(self):
        pass

# Clase concreta para Galleta de Chocolate
class GalletaDeChocolate(Galleta):
    def sabor(self):
        return "Chocolate"

# Clase concreta para Galleta de Vainilla
class GalletaDeVainilla(Galleta):
    def sabor(self):
        return "Vainilla"

# Uso del patrón Abstract Factory
def main():
    # Seleccionamos la fábrica de pastelería de chocolate
    fabrica_chocolate = PasteleriaDeChocolateFactory()
    
    # Creamos un pastel y una galleta de chocolate
    pastel_chocolate = fabrica_chocolate.crear_pastel()
    galleta_chocolate = fabrica_chocolate.crear_galleta()
    
    print(f"Pastel de sabor: {pastel_chocolate.sabor()}")
    print(f"Galleta de sabor: {galleta_chocolate.sabor()}")

if _name_ == "_main_":
    main()
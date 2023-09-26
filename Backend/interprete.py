class BuscadorPasteles:
    def __init__(self):
        self.lista_pasteles = ["pastel de chocolate", "pastel de fresa", "pastel de vainilla", "pastel de fresa frio"]

    def evaluar_expresion(self, expresion, descripcion):
        palabras = descripcion.split()
        operador = None
        resultado = True
        # Iteramos a través de cada palabra en la descripción
        for palabra in palabras:
            if palabra.lower() == "y":
                operador = "and"
            elif palabra.lower() == "o":
                operador = "or"
            else:
                # Comprobar si la palabra actual está presente en la expresión de búsqueda.
                palabra_valida = palabra.lower() in expresion
                if operador == "or":
                    resultado = resultado or palabra_valida
                else:
                    resultado = palabra_valida

        return resultado

    def buscar_pasteles(self):
        while True:
            descripcion = input("¿Qué desea buscar?: ").lower()

            if descripcion == "salir":
                break

            # Crear una lista de pasteles que coinciden con la expresión de búsqueda.
            pasteles_coincidentes = [pastel for pastel in self.lista_pasteles if self.evaluar_expresion(pastel, descripcion)]

            if pasteles_coincidentes:
                print("Se encontraron los siguientes pasteles que coinciden:")
                for pastel in pasteles_coincidentes:
                    print(pastel)
            else:
                print("No se encontraron pasteles que coincidan con la búsqueda.")

if __name__ == "__main__":
    buscador = BuscadorPasteles()
    buscador.buscar_pasteles()
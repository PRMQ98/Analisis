from abc import ABC, abstractmethod
# Estrategia base
class EstrategiaCatalogo:
    def filtrar_pasteles(self, pasteles):
        pass

# Estrategia para pasteles horneados
class EstrategiaHorneado(EstrategiaCatalogo):
    def filtrar_pasteles(self, pasteles):
        return [pastel for pastel in pasteles if pastel['Tipo'] == 'Horneado']

# Estrategia para pasteles fríos
class EstrategiaFrio(EstrategiaCatalogo):
    def filtrar_pasteles(self, pasteles):
        return [pastel for pastel in pasteles if pastel['Tipo'] == 'Frío']

# Estrategia para pasteles de yogurt
class EstrategiaYogurt(EstrategiaCatalogo):
    def filtrar_pasteles(self, pasteles):
        return [pastel for pastel in pasteles if pastel['Tipo'] == 'Yogurt']

# Estrategia para pasteles de queso
class EstrategiaQueso(EstrategiaCatalogo):
    def filtrar_pasteles(self, pasteles):
        return [pastel for pastel in pasteles if pastel['Tipo'] == 'Queso']

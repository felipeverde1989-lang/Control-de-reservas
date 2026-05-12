from abc import ABC, abstractmethod

class EntidadBase(ABC):
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad  # Atributo protegido

    @abstractmethod
    def obtener_detalles(self):
        """Obliga a todas las subclases a describir sus datos."""
        pass
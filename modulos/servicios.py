from abc import ABC, abstractmethod
from .base import EntidadBase

class Servicio(EntidadBase, ABC):
    def __init__(self, id_servicio, nombre, precio_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.precio_base = precio_base

    @abstractmethod
    def calcular_costo(self, **kwargs):
        """Método polimórfico."""
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, horas=1):
        return self.precio_base * horas

    def obtener_detalles(self):
        return f"Servicio: Reserva de Sala - {self.nombre}"

class AlquilerEquipo(Servicio):
    def calcular_costo(self, dias=1):
        return self.precio_base * dias

    def obtener_detalles(self):
        return f"Servicio: Alquiler de Equipo - {self.nombre}"

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, es_urgente=False):
        # Implementación de lógica distinta (Polimorfismo)
        costo = self.precio_base
        if es_urgente:
            costo *= 1.5
        return costo

    def obtener_detalles(self):
        return f"Servicio: Asesoría - {self.nombre}"
import logging
from .excepciones import ReservaInvalidaError

logger = logging.getLogger('SoftwareFJ')

class Reserva:
    def __init__(self, id_reserva, cliente, servicio, duracion):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def procesar(self):
        try:
            print(f"--- Iniciando proceso de reserva {self.id_reserva} ---")
            if self.duracion <= 0:
                raise ValueError("La duración debe ser un número positivo.")
            
            # Cálculo polimórfico
            costo = self.servicio.calcular_costo(horas=self.duracion)
            self.estado = "Confirmada"
            logger.info(f"ÉXITO: Reserva {self.id_reserva} confirmada. Cliente: {self.cliente.nombre}. Total: ${costo}")
            
        except ValueError as e:
            self.estado = "Error en Datos"
            # Encadenamiento de excepciones
            error_msg = f"Error en reserva {self.id_reserva}: {str(e)}"
            logger.error(error_msg)
            raise ReservaInvalidaError(error_msg) from e
            
        except Exception as e:
            self.estado = "Falla Crítica"
            logger.critical(f"Error inesperado en reserva {self.id_reserva}: {str(e)}")
            
        else:
            print(f"Reserva para {self.cliente.nombre} procesada sin errores.")
            
        finally:
            print(f"Estado final de la operación {self.id_reserva}: {self.estado}\n")
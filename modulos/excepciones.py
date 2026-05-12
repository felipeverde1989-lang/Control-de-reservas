class SoftwareFJError(Exception):
    """Clase base para todas las excepciones del sistema."""
    pass

class DatoInvalidoError(SoftwareFJError):
    """Lanzada cuando un dato no cumple con las validaciones (ej. nombre corto)."""
    pass

class ServicioNoDisponibleError(SoftwareFJError):
    """Lanzada cuando un servicio no puede ser procesado."""
    pass

class ReservaInvalidaError(SoftwareFJError):
    """Lanzada para errores específicos en el proceso de reserva."""
    pass
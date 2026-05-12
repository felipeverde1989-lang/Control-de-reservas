from modulos.logger import configurar_logger
from modulos.clientes import Cliente # (Asumiendo que ya tienes tu clase Cliente)
from modulos.servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from modulos.reservas import Reserva
from modulos.excepciones import SoftwareFJError

def ejecutar_sistema():
    configurar_logger()
    
    # 1. Crear instancias de servicios
    sala = ReservaSala(101, "Sala Audiovisual", 50000)
    pc = AlquilerEquipo(202, "Laptop Dell", 30000)
    
    # 2. Lista de clientes y operaciones (Simulación)
    # Debes realizar 10 bloques try/except aquí para cumplir la guía
    try:
        c1 = Cliente(1, "Luis Felipe", "felipe@mail.com")
        
        # OPERACIÓN 1: Válida
        r1 = Reserva("R001", c1, sala, 3)
        r1.procesar()
        
        # OPERACIÓN 2: Inválida (Duración 0 lanzará excepción)
        r2 = Reserva("R002", c1, pc, 0)
        r2.procesar()
        
    except SoftwareFJError as e:
        print(f"Controlado: {e}")
    except Exception as e:
        print(f"Error no esperado: {e}")

if __name__ == "__main__":
    ejecutar_sistema()
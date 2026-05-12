# ========================================================================================================================================================
# Proyecto: Control De Reservas 
# Luis Felipe Montilla Anaya
#Ingenieria De Sistemas
#Programacion 213023A_2201
# ========================================================================================================================================================



from modulos.logger import configurar_logger
from modulos.clientes import Cliente
from modulos.servicios import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from modulos.reservas import Reserva
from modulos.excepciones import SoftwareFJError

def ejecutar_sistema():
    # Inicialización del logger
    logger = configurar_logger()
    print("=== INICIANDO SISTEMA DE GESTIÓN SOFTWARE FJ ===\n")

    # 1. Preparación de datos maestros
    # Servicios disponibles (Polimorfismo)
    sala = ReservaSala(101, "Sala Audiovisual", 50000)
    pc = AlquilerEquipo(202, "Laptop Dell", 30000)
    asesoria = AsesoriaEspecializada(303, "Consultoría Sistemas", 120000)

    # Lista para almacenar operaciones y demostrar persistencia en memoria
    registro_exitoso = []

    # 2. Simulación de 10 operaciones
    # Creamos una lista de diccionarios con casos de prueba (válidos e inválidos)
    operaciones = [
        {"id": "R001", "cliente": ("Luis Felipe", "id1"), "serv": sala, "dur": 3},      # Válida
        {"id": "R002", "cliente": ("Ana Maria", "id2"), "serv": pc, "dur": 0},        # Error: Duración 0
        {"id": "R003", "cliente": ("Pedro S.", "id3"), "serv": asesoria, "dur": 2},    # Válida
        {"id": "R004", "cliente": ("", "id4"), "serv": sala, "dur": 1},               # Error: Nombre vacío (DatoInvalido)
        {"id": "R005", "cliente": ("Carlos V.", "id5"), "serv": pc, "dur": -5},       # Error: Duración negativa
        {"id": "R006", "cliente": ("Marta L.", "id6"), "serv": asesoria, "dur": 4},    # Válida
        {"id": "R007", "cliente": ("Jose D.", "id7"), "serv": sala, "dur": 10},       # Válida
        {"id": "R008", "cliente": ("Lucia H.", "id8"), "serv": pc, "dur": 2},         # Válida
        {"id": "R009", "cliente": ("Error Test", "id9"), "serv": None, "dur": 1},     # Error: Sin servicio
        {"id": "R010", "cliente": ("Final Op", "id10"), "serv": asesoria, "dur": 1},  # Válida
    ]

    for op in operaciones:
        try:
            # Intentamos crear el cliente (aquí puede saltar DatoInvalidoError)
            c = Cliente(op["cliente"][1], op["cliente"][0], "correo@test.com")
            
            # Intentamos crear y procesar la reserva
            if op["serv"] is None:
                raise SoftwareFJError("El servicio no puede ser nulo.")
                
            reserva = Reserva(op["id"], c, op["serv"], op["dur"])
            reserva.procesar()
            
            if reserva.estado == "Confirmada":
                registro_exitoso.append(reserva)

        except SoftwareFJError as e:
            # Captura errores de nuestra lógica y permite que el bucle siga
            print(f"[CONTROLADO] Error en operación {op['id']}: {e}")
        except Exception as e:
            # Captura errores inesperados (como el None) y registra en log
            print(f"[CRÍTICO] Error inesperado en {op['id']}: {e}")
            logger.error(f"Falla crítica: {e}")
        finally:
            print("-" * 40)

    print(f"\n=== SIMULACIÓN FINALIZADA ===")
    print(f"Operaciones exitosas: {len(registro_exitoso)} / {len(operaciones)}")

if __name__ == "__main__":
    ejecutar_sistema()

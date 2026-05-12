from .base import EntidadBase
from .excepciones import DatoInvalidoError

class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, email):
        """
        Constructor de Cliente.
        Llamamos al constructor de la clase abstracta EntidadBase para el ID.
        """
        super().__init__(id_cliente)
        # Usamos los setters para validar los datos desde el inicio
        self.nombre = nombre
        self.email = email

    # --- Encapsulación y Validación para 'nombre' ---
    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, valor):
        if not valor or not isinstance(valor, str) or len(valor.strip()) < 3:
            raise DatoInvalidoError(f"Nombre inválido: '{valor}'. Debe tener al menos 3 caracteres.")
        self.__nombre = valor.strip()

    # --- Encapsulación y Validación para 'email' ---
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, valor):
        if "@" not in valor or "." not in valor:
            raise DatoInvalidoError(f"Email inválido: '{valor}'. Formato incorrecto.")
        self.__email = valor

    # --- Implementación del método abstracto de EntidadBase ---
    def obtener_detalles(self):
        """
        Sobrescritura del método para cumplir con la abstracción.
        """
        return f"CLIENTE ID: {self._id_entidad} | Nombre: {self.__nombre} | Contacto: {self.__email}"

    def __str__(self):
        """Representación amigable en texto."""
        return f"Cliente({self.__nombre})"
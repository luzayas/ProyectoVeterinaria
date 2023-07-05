class Persona:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni

class Macota:
    def __init__(self, nombre, motivo):
        self.nombre = nombre
        self.motivo = motivo

class Cliente(Persona):
    def __init__(self, nombre, dni, contacto):
        Persona.__init__(self, nombre, dni)
        self.mascota = mascota
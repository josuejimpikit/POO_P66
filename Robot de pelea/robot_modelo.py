class Robot:
    def __init__(self, nombre, energia):
        self.nombre = nombre
        self.energia = energia
        self.estado = "Activo"
        self.escudo = 0.3  # 30% de reducción de daño
        self.habilidad_usada = False
        self.danio_recibido = 0
        self.danio_infligido = 0
        self.habilidad = "doble_ataque"  # Cambiar si deseas otras habilidades
        self.efecto_escudo_total = False

    def recibir_danio(self, cantidad):
        if self.estado == "Destruido":
            return
        if self.efecto_escudo_total:
            danio_reducido = 0
            self.efecto_escudo_total = False  # efecto solo una ronda
        else:
            danio_reducido = cantidad * (1 - self.escudo)
        self.energia -= danio_reducido
        self.danio_recibido += danio_reducido
        if self.energia <= 0:
            self.energia = 0
            self.estado = "Destruido"

    def usar_habilidad(self):
        if not self.habilidad_usada and self.estado == "Activo":
            self.habilidad_usada = True
            if self.habilidad == "doble_ataque":
                return "doble_ataque"
            elif self.habilidad == "escudo_total":
                self.efecto_escudo_total = True
                return "escudo_total"
            elif self.habilidad == "regeneracion":
                self.energia += 20
                if self.energia > 100:
                    self.energia = 100
                return "regeneracion"
        return None

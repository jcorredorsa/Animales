class Animal:
    def __init__(self, nombre, edad, especie):
        self.nombre = nombre
        self.edad = edad
        self.especie = especie

    def describir(self):
        return f"{self.nombre} es un {self.especie} de {self.edad} años."
    

class Perro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Perro")

    def hacer_sonido(self):
        return "Guau Guau"


class Gato(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Gato")

    def hacer_sonido(self):
        return "Miau"


class Pajaro(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Pájaro")

    def hacer_sonido(self):
        return "Pío Pío"


class Pez(Animal):
    def __init__(self, nombre, edad):
        super().__init__(nombre, edad, "Pez")

    def hacer_sonido(self):
        return "Blub Blub"
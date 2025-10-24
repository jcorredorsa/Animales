from Model import Animal
from Observable import Observable
class AnimalVM:
    def __init__(self, animal: Animal):
        self.nombre = Observable(animal.nombre)
        self.edad = Observable(animal.edad)
        self.especie = Observable(animal.especie)
        self.sonido = Observable(animal.hacer_sonido())

    def set_nombre(self, nuevo_nombre):
        self.nombre.value = nuevo_nombre

    def set_edad(self, nueva_edad):
        self.edad.value = nueva_edad

    def set_sonido(self, nuevo_sonido):
        self.sonido.value = nuevo_sonido
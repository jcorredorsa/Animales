from AnimalVM import AnimalVM
class AnimalView:
    def __init__(self, animal_vm: AnimalVM):
        self.animal_vm = animal_vm
        self.animal_vm.nombre.subscribe(self._nombre_cambiado)
        self.animal_vm.edad.subscribe(self._edad_cambiada)
        self.animal_vm.sonido.subscribe(self._sonido_cambiado)

    def _nombre_cambiado(self, nuevo_nombre):
        print(f"El nombre del animal cambió a: {nuevo_nombre}")

    def _edad_cambiada(self, nueva_edad):
        print(f"La edad del animal cambió a: {nueva_edad}")

    def _sonido_cambiado(self, nuevo_sonido):
        print(f"El sonido del animal ahora es: {nuevo_sonido}")

    def mostrar_datos(self):
        print("Datos del Animal:")
        print(f"Nombre: {self.animal_vm.nombre.value}")
        print(f"Edad: {self.animal_vm.edad.value}")
        print(f"Especie: {self.animal_vm.especie.value}")
        print(f"Sonido: {self.animal_vm.sonido.value}")

    def actualizar_datos(self):
        opcion = input("¿Quieres cambiar el nombre del animal? (si/no): ")
        if opcion.lower() == "si":
            nuevo_nombre = input("Ingrese el nuevo nombre: ")
            self.animal_vm.set_nombre(nuevo_nombre)

        opcion = input("¿Quieres cambiar la edad del animal? (si/no): ")
        if opcion.lower() == "si":
            nueva_edad = int(input("Ingrese la nueva edad: "))
            self.animal_vm.set_edad(nueva_edad)

        opcion = input("¿Quieres cambiar el sonido del animal? (si/no): ")
        if opcion.lower() == "si":
            nuevo_sonido = input("Ingrese el nuevo sonido: ")
            self.animal_vm.set_sonido(nuevo_sonido)
from Model import  Perro, Gato, Pajaro, Pez
from AnimalVM import AnimalVM
from AnimalView import AnimalView

def main():
    perro = AnimalVM(Perro("Chloe", 7))
    vista_perro = AnimalView(perro)

    vista_perro.mostrar_datos()
    vista_perro.actualizar_datos()  
    vista_perro.mostrar_datos()  

    gato = AnimalVM(Gato("Kira", 3))
    vista_gato = AnimalView(gato)

    vista_gato.mostrar_datos()
    vista_gato.actualizar_datos()
    vista_gato.mostrar_datos()

    pajaro = AnimalVM(Pajaro("Vicente", 1))
    vista_pajaro = AnimalView(pajaro)

    vista_pajaro.mostrar_datos()
    vista_pajaro.actualizar_datos()
    vista_pajaro.mostrar_datos()

    pez = AnimalVM(Pez("Nemo", 2))
    vista_pez = AnimalView(pez)

    vista_pez.mostrar_datos()
    vista_pez.actualizar_datos()
    vista_pez.mostrar_datos()

if __name__ == "__main__":
    main()
    
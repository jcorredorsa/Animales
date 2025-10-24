# Animales en Python

Este proyecto implementa un ejemplo sencillo del patrón MVVM en Python, utilizando un mecanismo de observables para manejar la reactividad de los datos. Este proyecto tiene como objetivo mostrar cómo separar responsabilidades en un programa orientado a objetos y cómo aplicar herencia en clases de animales.

## Estructura del proyecto

- **Observable.py**  
  Contiene la clase `Observable`, que permite suscribirse a cambios en un valor y notifica automáticamente a todos los observadores cuando este cambia.
<img width="542" height="351" alt="image" src="https://github.com/user-attachments/assets/2557587a-9cf9-4fac-acc8-8d329516bb58" />

- **model.py**  
  Define la clase base "Animal" y las subclases Perro, Gato, Pajaro y Pez. Cada subclase hereda de "Animal y redefine el método hacer_sonido.
<img width="725" height="390" alt="image" src="https://github.com/user-attachments/assets/318511c4-1c95-4512-9657-fc5a53be8399" />

- **AnimalVM.py**  
  Define la clase AnimalVM (ViewModel), que envuelve un objeto Animal y expone sus propiedades (nombre, edad, especie, sonido) como observables. Incluye métodos para actualizar los valores.
<img width="559" height="301" alt="image" src="https://github.com/user-attachments/assets/5b924f68-9fb8-408f-8458-22745ed82c7b" />

- **AnimalView.py**  
  Define la clase AnimalView (View), que se suscribe a los observables del ViewModel y reacciona automáticamente a los cambios. También permite mostrar los datos y preguntar al usuario si desea modificarlos.
<img width="625" height="377" alt="image" src="https://github.com/user-attachments/assets/35e13632-f46b-45b1-9f6d-59da7e07cbca" />
<img width="669" height="260" alt="image" src="https://github.com/user-attachments/assets/4a25b39d-cce7-4211-88ef-3e91cd0bd1c1" />

- **main.py**  
  Punto de entrada del programa. Crea instancias de animales, sus ViewModels y Vistas, muestra los datos iniciales y permite al usuario interactuar con ellos.
<img width="720" height="394" alt="image" src="https://github.com/user-attachments/assets/1ef179f0-8cdf-4b46-bc23-5da235b0c2d7" />
<img width="708" height="327" alt="image" src="https://github.com/user-attachments/assets/985265b4-c0cb-4df7-8b79-95efad7cd15a" />

## Funcionamiento

1. El **model** (`Animal y sus subclases) define los datos y comportamientos básicos de los animales.
2. El **ViewModel** (`AnimalVM`) convierte esos datos en propiedades observables y ofrece métodos para modificarlos.
3. La **vista** (`AnimalView`) se suscribe a los observables y reacciona automáticamente cuando cambian, mostrando mensajes en consola.
4. El **usuario** puede decidir si quiere cambiar el nombre, la edad o el sonido de un animal. Al hacerlo, la vista recibe notificaciones y actualiza la salida en tiempo real.

## Ejemplo de uso

Al ejecutar `main.py`, el programa:

1. Muestra los datos iniciales de los animales.
2. Pregunta al usuario si desea cambiar el nombre, la edad o el sonido.
3. Aplica los cambios y muestra los resultados actualizados.

Ejemplo de salida:

<img width="744" height="434" alt="image" src="https://github.com/user-attachments/assets/8c94b6c6-f426-4c37-bf84-43abb7d25d24" />


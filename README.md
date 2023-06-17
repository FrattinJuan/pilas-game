# pilas-game
Game made in pilasengine 1.4.2 using python 2

## Tutorial: Cómo funciona el código del juego "Rock, Paper, Scissors"

En este tutorial, te explicaré cómo funciona el código del juego "Rock, Paper, Scissors" utilizando la biblioteca pilasengine. Este juego consiste en controlar un personaje llamado "rock" (con las flechas del teclado "izquierda" y "derecha") y esquivar los objetos "papel" y "tijera" que caen desde la parte superior de la pantalla.

1. Importar las bibliotecas necesarias:
   El código comienza importando las bibliotecas "random" y "pilasengine". La biblioteca "random" se utiliza para generar valores aleatorios y "pilasengine" es una biblioteca de desarrollo de videojuegos en Python.

2. Definir las clases de los estados:
   El código define una clase base llamada "Estado" que se utiliza para representar el estado del juego en diferentes momentos. Luego, se definen tres clases derivadas de "Estado": "Ingresando", "Moviendo" y "Perdiendo". Estas clases implementan diferentes comportamientos del juego en cada estado.

3. Definir la clase "Rock":
   La clase "Rock" es una subclase de "pilasengine.actores.Actor" y representa al personaje principal del juego. Esta clase inicializa algunas propiedades del personaje, como la imagen, el tamaño y el estado inicial. También define métodos para actualizar el personaje y cambiar su animación. Además, tiene un método "perder" que se llama cuando el personaje es golpeado por un enemigo.

4. Definir las clases "Papel" y "Tijera":
   Estas clases representan los objetos que el personaje principal debe esquivar. Ambas son subclases de "pilasengine.actores.Actor" y definen propiedades como la imagen, el tamaño y el comportamiento de actualización.

5. Iniciar la biblioteca pilasengine:
   Se llama al método "pilasengine.iniciar()" para inicializar la biblioteca pilasengine y crear una ventana de juego.

6. Crear el fondo y los actores del juego:
   Se crea un fondo de nubes y se inicializan los actores principales del juego, como el personaje principal "rock", el puntaje y las listas de objetos "items" y enemigos.

7. Crear objetos "papel" y "tijera":
   Se define una función "crear_item()" que crea un objeto "tijera" y lo agrega a la lista de objetos "items". Esta función se ejecuta cada 2 segundos mediante el uso de la función "pilas.tareas.agregar()".

8. Detectar colisiones con los objetos "papel" y "tijera":
   Se define una función "cuanto_toca_item(v, i)" que se ejecuta cuando el personaje principal colisiona con un objeto "papel" o "tijera". En esta función, se elimina el objeto colisionado, se aumenta el puntaje y se aplican efectos visuales al puntaje.

9. Crear enemigos "papel":
   Se define una función "crear_enemigo()" que crea un objeto "papel" y lo agrega a la lista de enemigos. Esta función se ejecuta cada 3.3 segundos mediante el uso de la función "pilas.tareas.agregar()".

10. Detectar colisiones con los enemigos "papel":
    Se define una función "cuanto_toca_enemigo(rock, enemigo)" que se ejecuta cuando el personaje principal colisiona con un enemigo "papel". En esta función, se llama al método "perder()" del personaje principal para cambiar su estado y se elimina el enemigo.

11. Ejecutar el bucle principal del juego:
    Se llama al método "pilas.ejecutar()" para iniciar el bucle principal del juego y mantenerlo en funcionamiento.

 ### Puedes personalizar y agregar más funcionalidades al juego utilizando la biblioteca pilasengine y modificando el código existente. ¡Diviértete creando tu propio juego!

#Programado por Juan Frattin 14/06/2023
#pilasengine 1.4.2 en python2
# coding: utf-8
import random
import pilasengine

# Definición de la clase Estado
class Estado:

    def __init__(self, rock):
        self.rock = rock
        self.iniciar()

    def iniciar(self):
        pass
        
# Definición de la clase Ingresando, que hereda de Estado
class Ingresando(Estado):

    def iniciar(self):
        self.rock.definir_animacion([3, 4])  # Define la animación del personaje
        self.contador = 0
        self.rock.x = -380
        self.rock.x = [0], 0.5  # Mueve el personaje hacia la posición inicial
        self.rock.y = -150

    def actualizar(self):
        self.contador += 1

        if self.contador > 50:
            self.rock.estado = Moviendo(self.rock)  # Cambia al estado de Moviendo
            
# Definición de la clase Moviendo, que hereda de Estado
class Moviendo(Estado):

    def actualizar(self):
        velocidad = 5

        if pilas.escena.control.derecha:  # Verifica si se presionó la tecla derecha
            self.rock.x += velocidad  # Mueve el personaje hacia la derecha
        elif pilas.escena.control.izquierda:  # Verifica si se presionó la tecla izquierda
            self.rock.x -= velocidad  # Mueve el personaje hacia la izquierda

        if self.rock.x > 210:
            self.rock.x = 210  # Limita el movimiento del personaje a la derecha
        elif self.rock.x < -210:
            self.rock.x = -210  # Limita el movimiento del personaje a la izquierda
            
# Definición de la clase Perdiendo, que hereda de Estado
class Perdiendo(Estado):

    def iniciar(self):
        self.rock.centro = ('centro', 'centro')  # Define el centro del personaje
        self.velocidad = -2

    def actualizar(self):
        self.rock.rotacion += 7  # Rota el personaje
        self.rock.escala -= 0.001  # Reduce la escala del personaje
        self.rock.x -= self.velocidad  # Mueve el personaje horizontalmente
        self.velocidad += 0.2  # Incrementa la velocidad de movimiento
        self.rock.y -= 1  # Mueve el personaje hacia abajo

# Definición de la clase Rock, que hereda de pilasengine.actores.Actor
class Rock(pilasengine.actores.Actor):

    def iniciar(self):        
        self.imagen = 'rock.png'
        self.radio_de_colision = 40
        self.x = 0
        self.escala = 0.04
        self.estado = Ingresando(self)
        self.contador = 0
        
    def definir_animacion(self, cuadros):
        self.paso = 0
        self.contador = 0
        self.cuadros = cuadros

    def actualizar(self):
        self.estado.actualizar()

    def actualizar_animacion(self):
        self.contador += 0.2

        if (self.contador > 1):
            self.contador = 0
            self.paso += 1

            if self.paso >= len(self.cuadros):
                self.paso = 0

    def perder(self):
        self.estado = Perdiendo(self)  # Cambia al estado de Perdiendo
        t = pilas.actores.Texto("Perdiste ! ")
        t.color = 'negro'
        t.escala = 0
        t.escala = [1], 0.5
        
# Definición de la clase Papel, que hereda de pilasengine.actores.Actor
class Papel(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = 'papel.png'
        self.escala = 0.03  
        self.radio_de_colision =30      
        self.arriba = 320
        self.x = random.randint(-210, 210)

    def actualizar(self):
        self.arriba -= 5
        if self.abajo < -320:
            self.eliminar()                    

# Definición de la clase Tijera, que hereda de pilasengine.actores.Actor
class Tijera(pilasengine.actores.Actor):
    def iniciar(self):
        self.imagen = 'tijera.png'
        self.escala = 0.05
        self.rotacion = 180
        self.arriba =320
        self.radio_de_colision = 35
        self.x =random.randint(-210,210)
        
    def actualizar(self):
        self.arriba -=5
        if self.abajo < -320:
            self.eliminar()    
            
pilas = pilasengine.iniciar(capturar_errores=False)

fondo = pilas.fondos.Nubes()
puntos = pilas.actores.Puntaje(x=-290, y=210)
rock = Rock(pilas)
items = []
enemigos = []

def crear_item():
    un_item = Tijera(pilas)
    items.append(un_item)
    return True

pilas.tareas.agregar(2, crear_item)

def cuanto_toca_item(v, i):
    i.eliminar()
    puntos.aumentar(10)
    puntos.escala = 2
    puntos.escala = [1], 0.2
    puntos.rotacion = random.randint(30, 60)
    puntos.rotacion = [0], 0.2

pilas.colisiones.agregar(rock, items, cuanto_toca_item)

def crear_enemigo():
    un_enemigo = Papel(pilas)
    enemigos.append(un_enemigo)
    return True

pilas.tareas.agregar(3.3, crear_enemigo)

def cuanto_toca_enemigo(rock, enemigo):
    rock.perder()
    enemigo.eliminar()
    
pilas.colisiones.agregar(rock, enemigos, cuanto_toca_enemigo)

pilas.ejecutar()

# coding: utf-8
import random
import pilasengine

class Estado:

    def __init__(self, rock):
        self.rock = rock
        self.iniciar()

    def iniciar(self):
        pass
        
class Ingresando(Estado):

    def iniciar(self):
        self.rock.definir_animacion([3, 4])
        self.contador = 0
        self.rock.x = -380
        self.rock.x = [0], 0.5
        self.rock.y = -150

    def actualizar(self):
        self.contador += 1

        if self.contador > 50:
            self.rock.estado = Moviendo(self.rock)
            
            
class Moviendo(Estado):

    def actualizar(self):
        velocidad = 5

        if pilas.escena.control.derecha:
            self.rock.x += velocidad
        elif pilas.escena.control.izquierda:
            self.rock.x -= velocidad

        if self.rock.x > 210:
            self.rock.x = 210
        elif self.rock.x < -210:
            self.rock.x = -210
            
            
class Perdiendo(Estado):

    def iniciar(self):
        self.rock.centro = ('centro', 'centro')
        self.velocidad = -2

    def actualizar(self):
        self.rock.rotacion += 7
        self.rock.escala -= 0.001
        self.rock.x -= self.velocidad
        self.velocidad += 0.2
        self.rock.y -= 1
        
        
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
        self.estado = Perdiendo(self)
        t = pilas.actores.Texto("Perdiste ! ")
        t.color = 'negro'
        t.escala = 0
        t.escala = [1], 0.5
        
        
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
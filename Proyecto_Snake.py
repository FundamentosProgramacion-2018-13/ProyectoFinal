# Jose Luis Mata Lomelí
# A01377205
# Fundamentos de Programación: Grupo 02
# Profesor Roberto Martinez Roman
# Proyecto Final
# Objetivo: Lograr una recreación del juego Snake en Pygame

#Librerias
import pygame
import random


pygame.init()  # Inicia el motor de pygame

#Dimensiones de ventana de trabajo
Ancho = 800
Alto = 600

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)

ventana = pygame.display.set_mode((Ancho, Alto))  # Crear Ventana de trabajo
reloj = pygame.time.Clock()  # Para limitar los fps

fuente = pygame.font.Font(None, 25)


def messageVentana(msg, color):

    texto = fuente.render(msg, True, color)
    ventana.blit(texto, (Ancho//2, Alto//2))


def juego():

    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
    finJuego = False

    # Posicion inicial de la serpiente
    x_serpiente = Ancho // 2
    y_serpiente = Alto // 2

    # Si no queremos que solo avance un paso y se detenga la serpiente ...
    x_movimiento = 0
    y_movimiento = 0

    # aHORA LA MANZANA
    Manzana_X = random.randrange(0, Ancho-15)
    Manzana_Y = random.randrange(0, Alto-15)

    while not termina: # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente


        #Error
        while finJuego == True: #Si el fin de juego es igual a True
            ventana.fill(VERDE)
            messageVentana("Continuar? Y/N", NEGRO) #Poner letrero al usuario si quiere seguir jugando
            pygame.display.update()

            for evento in pygame.event.get(): #Por cada evento dentro del juego

                if evento.type == pygame.KEYDOWN: #Si el tipo del evento fue una tecla

                    if evento.key == pygame.K_n: #Si la tecla oprimida fue la n
                        termina = True  #Terminar programa
                        finJuego = False  #No volver a preguntar si quiere continuar

                    if evento.key == pygame.K_y: #Si la tecla oprimida fue la y
                        juego() #Continuar la funcion del juego

        # Procesa los eventos que recibe
        for evento in pygame.event.get():  # Por cada evento dentro del juego
            # print(evento)   #Imprime eventos dentro de la ventana (como posicion del mouse, salida del juego, acciones del teclado, etc.)

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo

            # Si el evento es una de las flechas del teclado
            if evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_LEFT:  # Si la tecla fue la flecha izquierda...
                    x_movimiento = -10  # Mover a la izquierda la serpiente
                    y_movimiento = 0  # Y para quitar su movimiento en diagonal, cambiamos la otra a 0

                elif evento.key == pygame.K_RIGHT:  # Si la tecla fue la flecha derecha...
                    x_movimiento = 10  # Mover a la derecha la serpiente
                    y_movimiento = 0

                elif evento.key == pygame.K_UP:  # Si la tecla fue la flecha de arriba...
                    y_movimiento = -10  # Mover hacia arriba la serpiente
                    x_movimiento = 0

                elif evento.key == pygame.K_DOWN:  # Si la tecla fue la flecha de abajo...
                    y_movimiento = 10  # Mover hacia abajo la serpiente
                    x_movimiento = 0

        # Si la serpiente se sale de la pantalla
        if x_serpiente >= Ancho or x_serpiente < 0 or y_serpiente >= Alto or y_serpiente < 0:
            termina = True

        # Para no detenerse y sea continuo...
        x_serpiente += x_movimiento
        y_serpiente += y_movimiento

        ventana.fill(VERDE)  # Color del fondo de la ventana

        # Cuerpo de la manzana
        pygame.draw.rect(ventana, ROJO, (Manzana_X, Manzana_Y, 15, 15))

        # Cuerpo de la Serpiente
        pygame.draw.rect(ventana, NEGRO, (x_serpiente, y_serpiente, 10, 10))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(15)  # 15 frames por segundo

    # Despues del ciclo inicial
    pygame.quit()  # Terminar el juego
    quit()
#######################################################################################################################

def main():

    juego()

main()

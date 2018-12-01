# encoding: UTF-8
# Autor: Juan Sebastián Lozano Derbez
# Proyecto Final - Juego Snake

import pygame
from random import randint
from pygame.locals import *

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)  # RGB en el rango [0,255]
AZUL_TEC = (44, 0, 219)
UVA = (193, 31, 183)
BLANCO = (255, 255, 255)

#Estados
menu = 1
jugando = 2

#Lectura de archivo
archivo = open("games.txt", "r")        # Abre el archivo de puntuaciones en modo lectura
numeros = []                            # Crea una lista vacía para poner los valores que están en el archivo
for linea in archivo:
    puntuaciones = linea.split(" ")
    puntuacioness = puntuaciones.sort()
    n1 = int(puntuaciones[4])
    n2 = int(puntuaciones[3])
    n3 = int(puntuaciones[2])           # Agrega los 5 datos del archivo a la lista(convirtiéndolos en enteros primero)
    n4 = int(puntuaciones[1])
    n5 = int(puntuaciones[0])
    numeros.append(n1)
    numeros.append(n2)
    numeros.append(n3)
    numeros.append(n4)
    numeros.append(n5)
minimo = min(numeros)
extring = ' '.join(str(e) for e in numeros)  # Convierte la lista a string


def dibujarPuntosymuerte(puntos,pantalla):      #Se establecen las acciones a tomar cuando el jugador pierde(terminar el juego y texto de puntos(tamaño, posicion y fuente)
    puntuacionn = pygame.font.SysFont('Arial', 60)
    textomuerte = puntuacionn.render('Tu puntuación fue: ' + str(puntos), True, (BLANCO))
    pantalla.blit(textomuerte, (150, 300))
    pygame.display.update()
    pygame.time.delay(1000)

def chocar(x1,x2,y1,y2,z11,z12,z21,z22):   #Se definen las situaciones en las que la serpiente estaria chocando
    if (x1 + z11 > x2) and (x2 + z12 > x1) and (x2 + z12 > x1) and (y1 + z11 > y2) and (y2 + z22 > y1):
        return True
    return False


def dibujar():
    termina = False

    #Imágen del botón del menú
    imgBtnJugar = pygame.image.load("button_jugar.png")

    #Estado del juego
    estado = menu

    #Audio
    pygame.mixer.init()
    morder = pygame.mixer.Sound("morder.wav")
    pygame.mixer.music.load("cancionfondo.mp3")     # Canción 100% original
    pygame.mixer.music.play(80)


    inicX = [390, 390, 390, 390, 390]  # Posicion inicial(despues modificada) de la serpiente
    inicY = [390, 370, 350, 330, 310]

    direccion = 0
    puntuacion = 0
    posComida = (randint(0, 780),
                 randint(0, 580))  # La comida de la serpiente aparece en coordenands aleatorias utilizando dos randints

    pygame.init()

    ventana = pygame.display.set_mode((ANCHO, ALTO))

    #Dibujar serpiente
    serpiente = pygame.Surface((20, 20))
    serpiente.fill(AZUL_TEC)

    #Dibujar comida
    comida = pygame.Surface((20, 20))
    comida.fill(UVA)

    puntuacionTexto = pygame.font.SysFont('Arial', 30)
    reloj = pygame.time.Clock()

    while not termina:
        reloj.tick(20)

        for evento in pygame.event.get():
            if evento.type == QUIT:
                termina = True


            elif evento.type == KEYDOWN:
                if evento.key == K_w and direccion != 0:  # Se establecen los clics de las teclas
                    direccion = 2
                elif evento.key == K_s and direccion != 2:
                    direccion = 0
                elif evento.key == K_a and direccion != 1:
                    direccion = 3
                elif evento.key == K_d and direccion != 3:
                    direccion = 1

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO // 2 - 128
                yb = ALTO // 2 - 50
                anchoB = 256
                altoB = 100
                if xm >= xb and xm <= xb + anchoB and ym >= yb and ym <= yb + altoB:
                    estado = jugando


        if estado == menu:
            # Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgBtnJugar, (ANCHO//2-128, ALTO//2-50))
            highscores = pygame.font.SysFont('Arial', 30)
            decrhighscores = highscores.render('Puntuaciones más altas: ', True, (BLANCO))
            high1 = highscores.render(str(n1), True, (UVA))
            high2 = highscores.render(str(n2), True, (UVA))
            high3 = highscores.render(str(n3), True, (UVA))
            high4 = highscores.render(str(n4), True, (UVA))
            high5 = highscores.render(str(n5), True, (UVA))

            ventana.blit(decrhighscores, (ANCHO//2-128, ALTO//2+100))
            ventana.blit(high1, (ANCHO//2-128, ALTO//2+125))
            ventana.blit(high2, (ANCHO//2-128, ALTO//2+150))
            ventana.blit(high3, (ANCHO//2-128, ALTO//2+175))
            ventana.blit(high4, (ANCHO//2-128, ALTO//2+200))
            ventana.blit(high5, (ANCHO//2-128, ALTO//2+225))

            pygame.display.update()
        elif estado == jugando:

            comollamarlo = len(inicX) - 1

            while comollamarlo >= 2:
                if chocar(inicX[0], inicX[comollamarlo], inicY[0], inicY[comollamarlo], 20, 20, 20, 20):  #
                    dibujarPuntosymuerte(puntuacion, ventana)
                comollamarlo -= 1


            if chocar(inicX[0], posComida[0], inicY[0], posComida[1], 20, 20, 20, 20):  # Se suma a la puntuacion y se da una nueva coordenada a la comida

                morder.play()
                puntuacion += 1
                inicX.append(700)
                inicY.append(700)
                posComida = (randint(0, 780), randint(0, 580))

            if inicX[0] < 0 or inicX[0] > 780 or inicY[0] < 0 or inicY[0] > 580:
                dibujarPuntosymuerte(puntuacion, ventana)  # Si la serpiente toca los bordes, se ejecuta la funcion que da finaliza el juego


                posicion = numeros.index(minimo)
                if puntuacion > minimo:
                    numeros.pop(posicion)               #Después de obtener el menor puntaje de la lista, lo compara con el recién obtenido y si es menor, lo remplaza
                    numeros.append(puntuacion)
                archivo.close()

                wrarchivo = open("games.txt", "w")              # Se abre el archivo en modo w para que se sobreescriba
                estring = ' '.join(str(e) for e in numeros)  # Convierte la lista a string
                wrarchivo.write(estring)                        # Escribe los nuevos valores en el archivo
                wrarchivo.close()

                quit()


            comollamarlo2 = len(inicX) - 1
            while comollamarlo2 >= 1:
                inicX[comollamarlo2] = inicX[comollamarlo2 - 1]
                inicY[comollamarlo2] = inicY[comollamarlo2 - 1]
                comollamarlo2 -= 1

            if direccion == 0:  # Se realiza el movimiento de la serpiente en base a los clics del teclado
                inicY[0] += 20
            elif direccion == 1:
                inicX[0] += 20
            elif direccion == 2:
                inicY[0] -= 20
            elif direccion == 3:
                inicX[0] -= 20

            ventana.fill((NEGRO))
            for comollamarlo in range(0, len(inicX)):
                ventana.blit(serpiente, (inicX[comollamarlo], inicY[comollamarlo]))

            ventana.blit(comida, posComida)
            textomuerte = puntuacionTexto.render("Puntuación: " + str(puntuacion), True, (BLANCO))

            ventana.blit(textomuerte, (630, 10))
            pygame.display.update()


def main():                                                             #funcion main

    dibujar()

main()







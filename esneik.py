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


def dibujarPuntosymuerte(puntos,pantalla):      #Se establecen las acciones a tomar cuando el jugador pierde(terminar el juego y texto de puntos(tamaño, posicion y fuente)
    puntuacionn = pygame.font.SysFont('Arial', 60)
    textomuerte = puntuacionn.render('Tu puntuación fue: ' + str(puntos), True, (BLANCO))
    pantalla.blit(textomuerte, (150, 300))
    pygame.display.update()
    pygame.time.delay(1000)
    quit()

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

    pygame.quit()



def main():                                                             #funcion main

   dibujar()

main()







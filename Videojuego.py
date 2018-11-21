#----------------------
# Zoe Ccaballero Dominguez
#----------------------

#Librerias
import pygame
import time
from random import randint

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
BLANCO =(225,225,225)

#Estados
MENU = 1
JUGAR = 2
INSTRUCCIONES = 3
HIGH_SCORE = 4

#Estados de movimiento
QUIETO = 1
DERECHA= 2
IZQUIERDA = 3
SALTANDO = 4
CAIDA = 5

ENELPISO = True

#Funciones:
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)

def dibujarEnemigos (ventana):
    pass

def moverEnemigos(ventaa):
    pass

def dibujarBalas(ventana):
    pass

def moverBalas(ventana):
    pass

def dibujarMenu(ventana, imgFondoMenu):
    ventana.blit (imgFondoMenu, (0,0))


def verificarColision():
    pass

def dibujarFondos(ventana, fondo1, fondo2, fondo3,fondo4, fondo5, xFondo):
    xf = xFondo
    yf = 0
    ventana.blit(fondo1, (xf,yf))
    ventana.blit(fondo2,( xf + 800, yf))
    ventana.blit(fondo3, (xf + 1600, yf))
    ventana.blit(fondo4, (xf + 2400, yf))
    ventana.blit(fondo5, (xf + 3200, yf))

def dibujarEscena1(ventana,fondo1, bases, xFondo):
    xf = xFondo
    yf = 0
    altoLibros = 56
    ventana.blit(fondo1, (xf, yf))
    ventana.blit(bases, (xf + 300, 540))
    ventana.blit(bases, (xf + 400, 540))
    ventana.blit(bases, (xf + 400, 540 - altoLibros))
    ventana.blit(bases, (xf + 500, 540 - 4*altoLibros))
    ventana.blit(bases, (xf + 600, 540))
    ventana.blit(bases, (xf + 600, 540 - 6 * altoLibros))




def dibujarVidas(ventana, imgVidas):
    ventana.blit(imgVidas, (20, 20))
    ventana.blit(imgVidas, (50, 20))
    ventana.blit(imgVidas, (80, 20))

def dibujarBotones(ventana, imgBotonPausa, imgBotonPlay):
    ventana.blit(imgBotonPausa, (750,20))
    ventana.blit (imgBotonPlay, (700,20))





def dibujar():
    #Inciar pygame
    pygame.init()
    #Crear ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    #Menu
    imgFondoMenu = pygame.image.load("menu.png")
    #Fondos
    imgFondo1 = pygame.image.load("fondo tec 5.png")
    imgFondo2 = pygame.image.load("fondo tec 4.png")
    imgFondo3 = pygame.image.load("fondo tec 3.png")
    imgFondo4 = pygame.image.load("fondo tec 2.png")
    imgFondo5 = pygame.image.load("fondo tec 1.png")

    #Personaje:
    imgPersonajeDerecha = pygame.image.load("borrego1.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonajeDerecha
    spritePersonaje.rect= imgPersonajeDerecha.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO +10
    spritePersonaje.OnGround = True

    #Vidas:
    imgVidas = pygame.image.load("cafe.png")

    #Botones:
    imgBtnPausa = pygame.image.load("botonPausa.png")
    imgBtnPlay = pygame.image.load("botonPlay.png")

    #Bases:
    imgBases = pygame.image.load("libros apilar.png")

    #Contador posición del personaje
    posicionBogo = 0





    estado = MENU
    xFondo = 0
    movimiento = 1


    while not termina:
        #Eventos:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

            elif evento.type == pygame.MOUSEBUTTONUP: #Configuracion del click para cambiar de estados en el menu
                xm, ym = pygame.mouse.get_pos() # y, x del mouse
                if (xm>194 and xm<618 and ym>265 and ym<334) and estado == MENU:
                    estado = JUGAR
                if (xm > 194 and xm < 618 and ym > 351 and ym < 419) and estado == MENU:
                    estado = INSTRUCCIONES
                if (xm>194 and xm<618 and ym>440 and ym<507) and estado == MENU:
                    estado = HIGH_SCORE



            else:
                key = pygame.key.get_pressed()
                if key[pygame.K_RIGHT]:
                    movimiento = 2
                elif key[pygame.K_LEFT]:
                    movimiento = 3
                elif key[pygame.K_UP]:
                    spritePersonaje.rect.bottom -= 10
                    time.sleep(3)
                    spritePersonaje.rect.bottom += 10





                else:
                    movimiento = 1


 


        #Borrar Pantalla
        ventana.fill(BLANCO)
        if estado == MENU:
            #DIBUJAR MENU
            dibujarMenu(ventana, imgFondoMenu)
        if estado == JUGAR:
            #FONDO
            #dibujarFondos(ventana, imgFondo1,imgFondo2,imgFondo3,imgFondo4,imgFondo5, xFondo)
            if posicionBogo <= 16:
                dibujarEscena1(ventana, imgFondo1, imgBases, xFondo)

            #PERSONAJE
            dibujarPersonaje(ventana, spritePersonaje)

            if movimiento == 1:
                spritePersonaje.rect.bottom = spritePersonaje.rect.bottom

            if movimiento == 2:
                if xFondo > -3200:
                    xFondo -= 50
                    spritePersonaje.rect.left += 10
                    posicionBogo += 1

            if movimiento == 3:
                if xFondo < 0:
                    xFondo += 50
                    spritePersonaje.rect.left -= 10
                    posicionBogo -= 1

            if movimiento == 4:
               #copiar lo de onground y self speed y no se que madres odio esto a la verga
                #if ENELPISO == True:
                pass








            #VIDAS
            dibujarVidas(ventana, imgVidas)

            #Botones Pausa/Play:
            dibujarBotones(ventana, imgBtnPausa, imgBtnPlay)









        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()

def main():
    dibujar()


main()
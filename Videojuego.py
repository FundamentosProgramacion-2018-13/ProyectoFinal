#Autor Luis Mario Cervantes Ortiz

import pygame   # Librería de pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0,0,0)
score = 0
x=50
y=425
vel=5

#Estados
MENU=1
JUGANDO= 2

#Estados de Movimiento
QUIETO=1
ARRIBA=2
ABAJO=3
IZQUIERDA=4
DERECHA=5


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana,spritePac):

    ventana.blit(spritePac.image,spritePac.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)


def actualizarEnemigos(listaEnemigos):

    for enemigo in listaEnemigos: #Visita cada enemigo

        enemigo.rect.bottom-=2
        enemigo.rect.left+=0
        enemigo.rect.bottom += 0
        enemigo.rect.right += 2

def dibujarLinea(ventana):
    # Lineas
    pygame.draw.rect(ventana, AZUL, (369, 180, 38, 73), 0)

def dibujarFruta(listaFruta,ventana):
    for fruta in listaFruta:
        ventana.blit(fruta.image,fruta.rect)


def verificarColisiones(listaFruta, spritePac,score):

    while score<=10:
        for k in range(len(listaFruta)-1,-1,-1):
            fruta=listaFruta[k]
            if fruta.rect.colliderect(spritePac):
                score=score+1
                listaFruta.remove(fruta)
                efecto= pygame.mixer.Sound('pacman_chomp.wav')
                efecto.play()


        return score

def colisionF(spritePac,listaEnemigo):

    for k in range(len(listaEnemigo)-1,-1,-1):
        ghost=listaEnemigo[k]
        if ghost.rect.colliderect(spritePac):
            pygame.quit()






def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Personaje
    pac=pygame.image.load("pacman.gif").convert()
    spritePac=pygame.sprite.Sprite()
    spritePac.image=pac
    spritePac.rect=pac.get_rect()
    spritePac.rect.left=380      # Se queda a la izquerda
    spritePac.rect.bottom = 275 + spritePac.rect.height//2 # Se queda en la mitad
    movimiento= QUIETO

    #fruta
    fruta=pygame.image.load("bola.gif").convert()
    listaFruta=[]
    for k in range(3):
        spriteFruta=pygame.sprite.Sprite()
        spriteFruta.image=fruta
        spriteFruta.rect=fruta.get_rect()
        spriteFruta.rect.left=randint(10,780)
        spriteFruta.rect.bottom=randint(10,580)
        listaFruta.append(spriteFruta)


    #Estado Del juego
    estado= MENU   #Inicial


    #ImagenesMenu
    imgBotonJugar=pygame.image.load("button_play.png")

    #Imagenes Fondo


    #Enemigos
    listaEnemigos=[] #Lista vacia d enemigos
    ghost= pygame.image.load("ghost1.gif").convert()
    for k in range(1):
        spriteGhost=pygame.sprite.Sprite()
        spriteGhost.image=ghost
        spriteGhost.rect=ghost.get_rect()
        spriteGhost.rect.left=380   #Se genera entre 800 y 400 ( en la izquierda)
        spriteGhost.rect.bottom =415 + spriteGhost.rect.height//2       # se genera entre 0 y 600
        listaEnemigos.append(spriteGhost)

        # Tiempo
        timer = 0  # acumulador de tiempo
        # audio
        pygame.mixer.init()
        efecto = pygame.mixer.Sound('pacman_chomp.wav')
        pygame.mixer.music.load("pacman_beginning.wav")
        pygame.mixer.music.play(-1)
        #Texto
        fuente = pygame.font.SysFont("monospace", 54)


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type==pygame.KEYDOWN:
                if evento.key==pygame.K_UP:
                    movimiento= ARRIBA

                elif evento.key==pygame.K_DOWN:
                    movimiento=ABAJO

                elif evento.key==pygame.K_LEFT:
                    movimiento=IZQUIERDA

                elif evento.key==pygame.K_RIGHT:
                    movimiento=DERECHA


            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm,ym = pygame.mouse.get_pos()
                xb =ANCHO//2-128
                yb=ALTO//2-50
                anchoB=256
                altoB=100
                if xm >= xb and xm <= xb + anchoB and ym>= yb and ym <= yb+altoB:
                    estado=JUGANDO


        #Prguntar Estado del juego
        if estado==MENU:
            #Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgBotonJugar,(ALTO/2-40,ANCHO/2-160))
        elif estado==JUGANDO:
            #Actualizar objetos
            actualizarEnemigos(listaEnemigos)
            verificarColisiones(listaFruta,spritePac,score)
            colisionF(spritePac,listaEnemigos)

            #MoverPersonaje
            if movimiento==ARRIBA:
                spritePac.rect.bottom-=vel
            elif movimiento==ABAJO:
                spritePac.rect.bottom+=vel
            elif movimiento==IZQUIERDA:
                spritePac.rect.left -=vel
            elif movimiento==DERECHA:
                spritePac.rect.right +=vel




            #Colision paredes


            # Borrar pantalla
            ventana.fill(NEGRO)





            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana,spritePac)
            dibujarEnemigos (ventana,listaEnemigos)
            dibujarLinea(ventana)
            dibujarFruta(listaFruta,ventana)

            texto = fuente.render("Puntuacion:%2i" % puntos, True, ROJO)
            ventana.blit(texto, (0, 10))

            #Dibujar texto




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)

        reloj.tick(30)  # 40 fps
        puntos=verificarColisiones(listaFruta,spritePac,score)

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
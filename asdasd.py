# Autor: Luis Humberto Burgueño Paz
# Videojuego

"""Dudas:
Balas de los Enemigos cada cierto tiempo
Archivo con puntajes
Colisiones asteroide"""


import pygame   # Librería de pygame
from random import randint
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# Estados
MENU = 1
JUGANDO = 2
COMOJUGAR = 3
SCOREBOARD = 4

# Estados de Movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
DERECHA = 4
IZQUIERDA = 5

#

def dibujarPersonaje(ventana, spriteNaveJugador):
   ventana.blit(spriteNaveJugador.image, spriteNaveJugador.rect)


def dibujarEnemigos(ventana, listaEnemigos):
   for enemigo in listaEnemigos:
       ventana.blit(enemigo.image, enemigo.rect)


def actualizarEnemigos(listaEnemigos, angulo):
   for enemigo in listaEnemigos: # Visita cada enemigo
       d = 5*math.sin(math.radians(angulo))
       enemigo.rect.bottom += int(d)




def dibujarBalas(ventana, listaBalasAliadas):
   for bala in listaBalasAliadas:
       ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalasAliadas):
   for bala in listaBalasAliadas:
       bala.rect.left += 30


def verificarColisiones(listaBalasAliadas, listaEnemigos):
   if len(listaEnemigos) == 0:
       generarEnemigos(listaEnemigos)
   # recorre las listas al revés
   for k in range(len(listaBalasAliadas)-1, -1, -1):
       bala = listaBalasAliadas[k]
       for e in range(len(listaEnemigos)-1, -1, -1):
           enemigo = listaEnemigos[e]
           # bala vs enemigo
           xb = bala.rect.left
           yb = bala.rect.bottom
           xe, ye, anchoe, altoe = enemigo.rect
           if xb>=xe and xb <= xe + anchoe and yb >= ye and yb <= ye + altoe:
               listaEnemigos.remove(enemigo)   # Borra de la lista
               listaBalasAliadas.remove(bala)
               break
           elif xb>ANCHO:
               listaBalasAliadas.remove(bala)
               break



def actualizarAsteroides(listaAsteroides):
    for asteroide in listaAsteroides:
        asteroide.rect.left -= 8
    if asteroide.rect.left <= -ANCHO:
        asteroide.rect.left = ANCHO + 100
        asteroide.rect.bottom = randint(0, ALTO)



def dibujarAsteroides(ventana, listaAsteroides):
    for asteroide in listaAsteroides:
        ventana.blit(asteroide.image, asteroide.rect)


def generarEnemigos(listaEnemigos):
    imgEnemigo = pygame.image.load("naveEnemiga.png")
    for k in range(15):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(2*ANCHO // 3, ANCHO)
        spriteEnemigo.rect.bottom = randint(3*ALTO//8, 6*ALTO//8)
        listaEnemigos.append(spriteEnemigo)


def verificarChoqueAsteroide(spriteNaveJugador, listaAsteroides):
    xNJ, yNJ, anchoNJ, altoNJ = spriteNaveJugador.rect
    xA, yA, anchoA, altoA = listaAsteroides[0].rect
    if xNJ>=xA and xNJ<=xA+anchoA and yNJ<=yA and yNJ>=yA-altoA:
        listaAsteroides[0].rect.left = 2*ANCHO
        print("hit")
        yA = randint(0, ALTO)


def dibujar():
   # Inicializa el motor de pygame
   pygame.init()
   # Crea una ventana de ANCHO x ALTO
   ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
   reloj = pygame.time.Clock()  # Para limitar los fps
   termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


   # Personaje Principal
   imgNaveJugador = pygame.image.load("naveJugador.png")
   spriteNaveJugador = pygame.sprite.Sprite()  # Sprite vacío
   spriteNaveJugador.image = imgNaveJugador
   spriteNaveJugador.rect = imgNaveJugador.get_rect()
   spriteNaveJugador.rect.left = 0
   spriteNaveJugador.rect.bottom = ALTO // 2 + spriteNaveJugador.rect.height // 2

   movimiento = QUIETO

   # Enemigos
   listaEnemigos = [] # Lista vacía de enemigos


   # Balas
   imgBalaAliada = pygame.image.load("balaAliada.png")
   listaBalasAliadas = []
   imgBalaEnemiga = pygame.image.load("balaEnemiga.png")
   listaBalasEnemigas = []

   # Asteroides
   listaAsteroides = []
   imgAsteroide = pygame.image.load("asteroides.png")
   for k in range(1):
       spriteAsteroide = pygame.sprite.Sprite()
       spriteAsteroide.image = imgAsteroide
       spriteAsteroide.rect = imgAsteroide.get_rect()
       spriteAsteroide.rect.left = ANCHO
       spriteAsteroide.rect.bottom = randint(0, ALTO)
       listaAsteroides.append(spriteAsteroide)

   # Estado del Juego
   estado = MENU   # Inicial

   # Imágenes para el menú
   imgBtnJugar = pygame.image.load("btnJugar.png")
   xBtnJ, yBtnJ, anchoBtnJ, altoBtnJ = imgBtnJugar.get_rect() # Dimensiones botón
   imgBtnComoJugar = pygame.image.load("btnComoJugar.png")
   xBtnCJ, yBtnCJ, anchoBtnCJ, altoBtnCJ = imgBtnComoJugar.get_rect()  # Dimensiones botón
   imgBtnScoreboard = pygame.image.load("btnScoreboard.png")
   xBtnS, yBtnS, anchoBtnS, altoBtnS = imgBtnScoreboard.get_rect()  # Dimensiones botón
   imgBtnRegresar = pygame.image.load("btnRegresar.png")
   xBtnR, yBtnR, anchoBtnR, altoBtnR = imgBtnRegresar.get_rect()  # Dimensiones botón
   imgLogoJuego = pygame.image.load("logoJuego.png")
   xL, yL, anchoL, altoL = imgLogoJuego.get_rect()  # Dimensiones Logo

   # Imágenes para el juego
   imgFondo = pygame.image.load("fondoJuego.jpg")
   xFondo = 0
   imgComoJugar = pygame.image.load("comoJugar.png")

   # Ángulo
   alfa = 0

   # Tiempo
   timer = 0
   timerBalas = 0

   # Audio
   pygame.mixer.init()
   disparo = pygame.mixer.Sound("shoot.wav")
   pygame.mixer.music.load("musicaFondo.wav")
   pygame.mixer.music.play(-1)

   # Vida
   escudo = 100
   vida = 50



   while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
       # Procesa los eventos que recibe
       for evento in pygame.event.get():
           if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
               termina = True      # Queremos terminar el ciclo
           elif evento.type == pygame.KEYDOWN:
               if evento.key == pygame.K_UP:
                   movimiento = ARRIBA
               elif evento.key == pygame.K_DOWN:
                   movimiento = ABAJO
               elif evento.key == pygame.K_RIGHT:
                   movimiento = DERECHA
               elif evento.key == pygame.K_LEFT:
                   movimiento = IZQUIERDA
               elif evento.key == pygame.K_SPACE: #disparo
                   spriteBalaAliada = pygame.sprite.Sprite()
                   spriteBalaAliada.image = imgBalaAliada
                   spriteBalaAliada.rect = imgBalaAliada.get_rect()
                   spriteBalaAliada.rect.left = spriteNaveJugador.rect.width + spriteNaveJugador.rect.left
                   spriteBalaAliada.rect.bottom = spriteNaveJugador.rect.bottom - spriteNaveJugador.rect.height//2
                   listaBalasAliadas.append(spriteBalaAliada)
                   disparo.play()

       # Pregunta en qué estado está el juego
       if estado == MENU:
           # Borrar pantalla
           ventana.fill(NEGRO)
           ventana.blit(imgFondo, (xFondo, 0))
           ventana.blit(imgFondo, (xFondo + 1067, 0))  # 1067 Ancho de la Imagen
           xFondo -= 1
           if xFondo <= -1067:
               xFondo = 0
           ventana.blit(imgBtnJugar, (ANCHO//2-anchoBtnJ//2, ALTO//2-altoBtnJ//2))
           ventana.blit(imgBtnComoJugar, (ANCHO//2 -anchoBtnCJ//2, ALTO//2 + 25 + altoBtnCJ))    # Dejar pixeles de separación
           ventana.blit(imgBtnScoreboard, (ANCHO//2 - anchoBtnS//2, ALTO//2 + 50 + altoBtnCJ + altoBtnS))
           ventana.blit(imgLogoJuego, (ANCHO//2-anchoL//2, ALTO//2-altoL - 50))
           for evento in pygame.event.get():
               if evento.type == pygame.MOUSEBUTTONDOWN:
                   xm, ym = pygame.mouse.get_pos()
                   xbtnJ = ANCHO // 2 - anchoBtnJ // 2
                   yBtnJ = ALTO // 2 - altoBtnJ // 2
                   xBtnCJ = ANCHO // 2 - anchoBtnCJ // 2
                   yBtnCJ = ALTO // 2 + 25 + altoBtnCJ
                   xbtnS = ANCHO // 2 - anchoBtnS // 2
                   yBtnS = ALTO // 2 + 50 + altoBtnCJ + altoBtnS
                   if xm >= xbtnJ and xm <= xbtnJ + anchoBtnJ and ym >= yBtnJ and ym <= yBtnJ + altoBtnJ:
                       estado = JUGANDO
                   if xm >= xBtnCJ and xm <= xBtnCJ + anchoBtnCJ and ym >= yBtnCJ and ym <= yBtnCJ + altoBtnCJ:
                       estado = COMOJUGAR
                   if xm >= xbtnS and xm <= xbtnS + anchoBtnS and ym >= yBtnS and ym <= yBtnS + altoBtnS:
                       estado = SCOREBOARD
       elif estado == COMOJUGAR:
           ventana.fill(BLANCO)
           ventana.blit(imgComoJugar, (0, 0))
           ventana.blit(imgBtnRegresar, (ANCHO-((3*anchoBtnR)//2), ALTO-2*altoBtnR))
           for evento in pygame.event.get():
               if evento.type == pygame.MOUSEBUTTONDOWN:
                   xm, ym = pygame.mouse.get_pos()
                   xbtnR = ANCHO-(3*anchoBtnR)//2
                   yBtnR = ALTO-2*altoBtnR
                   if xm >= xbtnR and xm <= xbtnR + anchoBtnR and ym >= yBtnR and ym <= yBtnR + altoBtnR:
                       estado = MENU
       elif estado == SCOREBOARD:
           ventana.fill(ROJO)
           ventana.blit(imgBtnRegresar, (ANCHO - ((3 * anchoBtnR) // 2), ALTO - 2 * altoBtnR))
           for evento in pygame.event.get():
               if evento.type == pygame.MOUSEBUTTONDOWN:
                   xm, ym = pygame.mouse.get_pos()
                   xbtnR = ANCHO - (3 * anchoBtnR) // 2
                   yBtnR = ALTO - 2 * altoBtnR
                   if xm >= xbtnR and xm <= xbtnR + anchoBtnR and ym >= yBtnR and ym <= yBtnR + altoBtnR:
                       estado = MENU
       elif estado == JUGANDO:
           # Actualizar objetos
           actualizarEnemigos(listaEnemigos, alfa)
           alfa += 2
           actualizarBalas(listaBalasAliadas)
           actualizarAsteroides(listaAsteroides)
           verificarColisiones(listaBalasAliadas, listaEnemigos)
           verificarChoqueAsteroide(spriteNaveJugador, listaAsteroides)
           # Mover personaje
           if movimiento==ARRIBA:
               spriteNaveJugador.rect.bottom -= 4
           elif movimiento==ABAJO:
               spriteNaveJugador.rect.bottom += 4
           elif movimiento==DERECHA:
               spriteNaveJugador.rect.left += 4
           elif movimiento==IZQUIERDA:
               spriteNaveJugador.rect.left -= 4

           # Borrar pantalla
           ventana.fill(BLANCO)
           ventana.blit(imgFondo, (xFondo, 0))
           ventana.blit(imgFondo, (xFondo+1067, 0))    # 1067 Ancho de la Imagen
           xFondo-=1
           if xFondo<=-1067:
               xFondo=0


           dibujarPersonaje(ventana, spriteNaveJugador)
           dibujarEnemigos(ventana, listaEnemigos)
           dibujarBalas(ventana, listaBalasAliadas)
           dibujarAsteroides(ventana, listaAsteroides)
           timer += 1/60
           timerBalas += 1/60

       pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
       reloj.tick(60)  # 60 fps

   # Después del ciclo principal
   pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
   dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
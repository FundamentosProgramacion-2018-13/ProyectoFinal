# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla
import math

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
NEGRO = (0, 0, 0)

#VIDAS = 3
# Estados
MENU = 1
JUGANDO = 2
PERDEDOR = 3


# Estados de movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
AVANZAR = 4




# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePlanta):
    ventana.blit(spritePlanta.image, spritePlanta.rect)


def dibujarRocas(ventana, listaRocas, spriteRoca):
    for roca in listaRocas:
        ventana.blit(roca.image, roca.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def actualizarRocas(listaRocas):
    for roca in listaRocas:
        roca.rect.left -= 20


def actualizarEnemigos(listaEnemigos, angulo):
    for enemigo in listaEnemigos:   # VISITA cada enemigo
        #enemigo.rect.left -= 1
        d = 10*math.sin(math.radians(angulo))
        enemigo.rect.bottom += int(d)


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 30

#def moverPrincesa(spritePlanta):
    global PrincesaA, Princesa
#

def verificarColisionesRoca(listaRocas,spritePlanta):
    VIDAS = 1
    for k in range(len(listaRocas)-1,-1,-1):
        roca = listaRocas[k]
        borrarRoca = False
         #personaje= spritePlanta[n]
        xb = roca.rect.left
        yb = roca.rect.bottom
        xr, yr, anchor, altor, = spritePlanta.rect
        if xb >= xr and xb <= xr + anchor and yb >= yr and yb <= yr + altor:
            VIDAS -= 1
            borrarRoca = True
        if yb > ALTO:
            borrarRoca = True
            break
    if borrarRoca:
        listaRocas.remove(roca)
        return VIDAS
        if VIDAS <= 1:
            spritePlanta.remove








def verificarColisiones(listaBalas, listaEnemigos):
    # recorre las listas al revés
    for k in range(len(listaBalas)-1,-1,-1):
        bala = listaBalas[k]
        borrarBala = False
        for e in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, anchoe, altoe = enemigo.rect
            if xb>=xe and xb<=xe+anchoe and yb>=ye and yb<=ye+altoe:
                listaEnemigos.remove(enemigo)   # borra de la lista
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # personaje principal
    imgPlanta = pygame.image.load("PrincesaC.png")
    spritePlanta = pygame.sprite.Sprite()  # sprite vacío
    spritePlanta.image = imgPlanta
    spritePlanta.rect = imgPlanta.get_rect()
    spritePlanta.rect.left = 0
    spritePlanta.rect.bottom =(ALTO//16 + spritePlanta.rect.height//16)*13
    movimiento = QUIETO

    listaRocas = []  # Lista vacía de enemigos
    imgRoca = pygame.image.load("Rock.png")
    for k in range(50):
        spriteRoca = pygame.sprite.Sprite()  # sprite vacío
        spriteRoca.image = imgRoca
        spriteRoca.rect = imgRoca.get_rect()
        spriteRoca.rect.left = ANCHO*(k+1)
        spriteRoca.rect.bottom = (ALTO // 32 + spriteRoca.rect.height // 32) * 29
        listaRocas.append(spriteRoca)
        #movimiento = AVANZAR



    # Enemigos
    listaEnemigos = []  # Lista vacía de enemigos
    imgEnemigo = pygame.image.load("DragonA.png")
    for k in range(1):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = (ALTO//32 + spritePlanta.rect.height//32)*29
        spriteEnemigo.rect.bottom = (ALTO//32 + spritePlanta.rect.height//32)*17
        listaEnemigos.append(spriteEnemigo)


 


    # Balas
    imgBala = pygame.image.load("bolaFuego.png")
    listaBalas = []

    # Estado del juego
    estado = MENU       # Inicial

    # Imágenes para el menú
    imgBtnJugar = pygame.image.load("btnJugar.png")

    # Imágenes para el juego
    imgFondo = pygame.image.load("FondoAldeaP.png")
    xFondo = 0

    # TIEMPO
    timer = 0   # acumulador de tiempo

    # Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("Slainte - Kesh Jig Leitrim Fancy.wmv.mp3")
    pygame.mixer.music.play(-1)

    # TEXTO
    fuente = pygame.font.SysFont("monospace", 54)
    alfa = 0

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:

                    #if spritePlanta.rect.bottom>= 300: #or spritePlanta.rect.bottom<=0:
                    movimiento = ARRIBA


                   #spritePlanta.rect.bottom -= 30
                   #movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    #if spritePlanta.rect.bottom<=0:
                    movimiento = ABAJO
                    #spritePlanta.rect.bottom += 30
                    #spritePlanta.rect.bottom += 30 # más es para abajo

                elif evento.key == pygame.K_z:  # Disparo
                     efecto.play()
                     spriteBala = pygame.sprite.Sprite()
                     spriteBala.image = imgBala
                     spriteBala.rect = imgBala.get_rect()
                     spriteBala.rect.left = spriteEnemigo.rect.width
                     spriteBala.rect.bottom = spriteEnemigo.rect.bottom - spriteEnemigo.rect.height//2
                     listaBalas.append(spriteBala)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO//2 - 128
                yb = ALTO//2 - 50
                anchoB = 256
                altoB = 100
                if xm>=xb and xm<=xb+anchoB and ym>=yb and ym<=yb+altoB:
                    estado = JUGANDO

        # Pregunta en qué estado está el juego
        if estado==MENU:
            # Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgBtnJugar, (ANCHO//2-128, ALTO//2-50))
        elif estado == JUGANDO:
            # Actualizar objetos
            actualizarEnemigos(listaEnemigos, alfa)
            alfa += 5
            actualizarRocas(listaRocas)

            actualizarBalas(listaBalas)
            verificarColisiones(listaBalas, listaEnemigos)
            verificarColisionesRoca(listaRocas,spritePlanta)




            # Disparar?????
            if timer >= 2:
                timer = 0
                efecto.play()
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePlanta.rect.width
                spriteBala.rect.bottom = spritePlanta.rect.bottom - spritePlanta.rect.height // 2
                listaBalas.append(spriteBala)

            # Mover personaje
            if movimiento==ARRIBA:
                spritePlanta.rect.bottom -= 5
                if spritePlanta.rect.bottom<=460:
                    spritePlanta.rect.bottom += 5
            elif movimiento==ABAJO:
                spritePlanta.rect.bottom += 5
                if spritePlanta.rect.bottom>= 550:
                    spritePlanta.rect.bottom -= 5
            elif movimiento == AVANZAR:
                spriteRoca.rect.left -= 4

            # Borrar pantalla
            ventana.fill(VERDE_BANDERA)
            ventana.blit(imgFondo, (xFondo,0))
            ventana.blit(imgFondo, (xFondo+1067,0))     # 1067 Ancho de la imagen
            xFondo -= 18
            if xFondo<=-1067:
                xFondo = 0

            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana, spritePlanta)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)
            dibujarRocas(ventana, listaRocas, spriteRoca)
            # Dibujar texto
            texto = fuente.render("Tiempo: %.3f"%timer, 1, ROJO)
            ventana.blit(texto, (150, 50))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/11

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
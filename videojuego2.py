# encoding: UTF-8
# Autor: Silvia Ferman
# VIDEOJUEGO

import pygame
from random import randint
import time


# DIMENSIONES PANTALLA:
ANCHO = 800
ALTO = 600

# COLORES_
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
MORADO = (74, 35, 90)
ROSA = (255, 93, 133)

# ESTADOS_
MENU = 1
JUGANDO = 2
REGLAS = 3
RANK = 4

# ESTADOS DE MOVIMIENTO
QUIETO = 1
ABAJO = 2
ARRIBA = 3
ATRAS = 4
ADELANTE = 5


# Estructura básica de un programa que usa pygame para dibujar
def dibujarSuricata(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)

def dibujarRoca(ventana, spriteRoca):
    ventana.blit(spriteRoca.image, spriteRoca.rect)

def dibujarCactus(ventana, listaEnemigos):
    # VISITAR/ACCEDER DIRECTAMENTE a cada elemento
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def moverCactus(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 2


def dibujarMisiles(ventana, listaMisil):
    for bala in listaMisil:
        ventana.blit(bala.image, bala.rect)


def moverMisiles(listaMisil):
    for bala in listaMisil:
        bala.rect.left += 10


def dibujarMenu(ventana, imgButtonPlay, imgButtonReglas, imgButtonRank):
    ventana.blit(imgButtonPlay, (ANCHO // 2 - 128 , ALTO // 3 - 128))
    ventana.blit(imgButtonReglas, (ANCHO // 2 - 128, ALTO // 3 + 25))
    ventana.blit(imgButtonRank, (ANCHO // 2 - 128, ALTO // 3 + 175))

def dibujarGameOver(ventana, imgGameOver):
    ventanaJuego = ventana
    imagenPerdio = imgGameOver
    ventanaJuego.blit(imagenPerdio, (0,0))
    pygame.display.update()
    time.sleep(5)
    dibujar()

def verificarBoom(listaEnemigos, listaMisil, puntos):
    for k in range(len(listaMisil)-1, -1, -1):
        misil= listaMisil[k]
        for e in range(len(listaEnemigos)-1, -1, -1):              # Recorrer con INDICES
            cactus = listaEnemigos[e]
            # bala vs enemigo
            xb = misil.rect.left
            yb = misil.rect.bottom
            xe, ye, ae, alte = cactus.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte :
                # hit
                listaEnemigos.remove(cactus)
                listaMisil.remove(misil)
                puntos += 1
                break

def verificarGameOver(ventana, spriteRoca, listaMisil, imgGameOver):
    for k in range(len(listaMisil)-1, -1, -1):
        misil = listaMisil[k]
        xmisil = misil.rect.left
        ymisil = misil.rect.bottom
        xroca, yroca, aroca, altroca = spriteRoca.rect
        if xmisil >= xroca and xmisil <= xroca + aroca and ymisil >= yroca and ymisil <= yroca + altroca :
            # Game Over --> pantalla
            dibujarGameOver(ventana, imgGameOver)

def dibujar():
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # ROCA
    x = ANCHO
    imgRoca = pygame.image.load("roca.png")
    spriteRoca = pygame.sprite.Sprite()
    spriteRoca.image = imgRoca
    spriteRoca.rect = imgRoca.get_rect()
    spriteRoca.rect.left = x
    x += 140 + randint(0, 55)
    spriteRoca.rect.bottom = ALTO - 25

    # PERSONAJE
    imgPersonaje = pygame.image.load("suricata.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO

    # ENEMIGOS
    x = ANCHO
    listaEnemigos = []
    imgEnemigo = pygame.image.load("cactus.png")
    imgEnemigoUno = pygame.image.load("Cactus2A.png")
    imgEnemigoDos = pygame.image.load("Cactus3A.png")
    for k in range(50):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigoUno = pygame.sprite.Sprite()
        spriteEnemigoDos = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigoUno.image = imgEnemigoUno
        spriteEnemigoDos.image = imgEnemigoDos
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigoUno.rect = imgEnemigoUno.get_rect()
        spriteEnemigoDos.rect = imgEnemigoDos.get_rect()
        spriteEnemigo.rect.left = x
        x += 140 + randint(0, 50)
        spriteEnemigoUno.rect.left = x
        x += 140 + randint(0, 35)
        spriteEnemigoDos.rect.left = x
        x += 140 + randint(0, 75)
        spriteEnemigo.rect.bottom = ALTO
        spriteEnemigoUno.rect.bottom = ALTO - 10
        spriteEnemigoDos.rect.bottom = ALTO - 10
        listaEnemigos.append(spriteEnemigo)
        listaEnemigos.append(spriteEnemigoUno)
        listaEnemigos.append(spriteEnemigoDos)

    # PROYECTILES / BALAS
    listaMisil = []
    imgMisil = pygame.image.load("misil.png")

    # MENU
    imgButtonPlay = pygame.image.load("buttonPlay.png")
    imgButtonReglas = pygame.image.load("buttonReglas.png")
    imgButtonRank = pygame.image.load("buttonRanking.png")
    imgRegresar = pygame.image.load("buttonRegresar.png")
    imgGameOver = pygame.image.load("Game Over.png")

    # IMAGENES
    imgFondo = pygame.image.load("desierto.JPG")
    imgReglas = pygame.image.load("reglas.jpg")
    imgRank = pygame.image.load("ranking.jpg")

    estado = MENU

    moviendo = QUIETO

    xFondo = 0

    puntos = 0

    # TIEMPOS
    timer = 0       # Acumulador de tiempo

    # TEXTO
    fuente = pygame.font.SysFont("monospace", 25)

    # AUDIO
    pygame.mixer.init()
    pygame.mixer.music.load("BACKGROUND.mp3")   # archivos largos (mp3)
    pygame.mixer.music.play(-1)

    efecto = pygame.mixer.Sound("shoot.wav")     # archivos cortos

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    #spritePersonaje.rect.bottom -= 5    #  Velocidad mov. arriba
                    moviendo = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    #spritePersonaje.rect.bottom += 5    # Velocidad mov. abajo
                    moviendo = ABAJO
                elif evento.key == pygame.K_LEFT:
                    moviendo = ATRAS
                elif evento.key == pygame.K_RIGHT:
                    moviendo = ADELANTE
                elif evento.key == pygame.K_SPACE:
                    # Crear una bala
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgMisil
                    spriteBala.rect = imgMisil.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width - 120
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom - 100
                    listaMisil.append(spriteBala)
                    # SONIDO Boom
                    efecto.play()
            elif evento.type == pygame.KEYUP:
                moviendo = QUIETO
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()         # dupla: se regresan DOS variables
                print(xm, " , ", ym)
                # Preguntar si solto el mouse dentro del boton (BOTON JUGAR)
                xb = ANCHO // 2 - 128
                yb = ALTO // 3 - 128
                if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                    estado = JUGANDO
                # Preguntar si solto el mouse dentro del boton (BOTON REGLAS)
                xb = ANCHO // 2 - 128
                yb = ALTO // 3 + 25
                if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                    estado = REGLAS
                # Preguntar si solto el mouse dentro del boton (BOTON RANK)
                xb = ANCHO // 2 - 128
                yb = ALTO // 3 + 178
                if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                    estado = RANK

        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == JUGANDO:
            # TIEMPOS
            if timer >= 2:
                timer = 0
                # Enemigos
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigoUno = pygame.sprite.Sprite()
                spriteEnemigoDos = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigoUno.image = imgEnemigoUno
                spriteEnemigoDos.image = imgEnemigoDos
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigoUno.rect = imgEnemigoUno.get_rect()
                spriteEnemigoDos.rect = imgEnemigoDos.get_rect()
                spriteEnemigo.rect.left = x
                x += 140 + randint(0, 50)
                spriteEnemigoUno.rect.left = x
                x += 140 + randint(0, 35)
                spriteEnemigoDos.rect.left = x
                x += 140 + randint(0, 75)
                spriteEnemigo.rect.bottom = ALTO
                spriteEnemigoUno.rect.bottom = ALTO - 10
                spriteEnemigoDos.rect.bottom = ALTO - 10
                listaEnemigos.append(spriteEnemigo)
                listaEnemigos.append(spriteEnemigoUno)
                listaEnemigos.append(spriteEnemigoDos)

            # Actualizar ENEMIGOS / BALAS
            # MOVER Personaje
            if moviendo == ARRIBA:
                spritePersonaje.rect.bottom -= 15        # se mueve solo ARRIBA
            elif moviendo == ABAJO:
                spritePersonaje.rect.bottom += 15        # se mueve solo ABAJO
            elif moviendo == ATRAS:
                spritePersonaje.rect.left -= 5
            elif moviendo == ADELANTE:
                spritePersonaje.rect.left += 5
            moverCactus(listaEnemigos)
            moverMisiles(listaMisil)
            verificarBoom(listaEnemigos, listaMisil, puntos)
            verificarGameOver(ventana, spriteRoca, listaMisil, imgGameOver)


            # Dibujar, aquí haces todos los trazos que requieras
            ventana.blit(imgFondo, (xFondo, 0))
            ventana.blit(imgFondo, (xFondo + ANCHO, 0))
            xFondo -= 1
            if xFondo == -ANCHO:
                xFondo = 0
            dibujarSuricata(ventana, spritePersonaje)
            dibujarRoca(ventana, spriteRoca)
            dibujarCactus(ventana, listaEnemigos)
            dibujarMisiles(ventana, listaMisil)
        elif estado == MENU:
            # Dibujar MENU
            dibujarMenu(ventana, imgButtonPlay, imgButtonReglas, imgButtonRank)
        elif estado == REGLAS:
            ventana.blit(imgReglas, (0,0))
        elif estado == RANK:
            ventana.blit(imgRank, (0,0))

        # TEXTO PANTALLA
        texto = fuente.render("PUNTOS = %d" % puntos, 1, NEGRO)
        ventana.blit(texto, (ANCHO // 2 - 370, 25))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/40

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal
def main():
    dibujar()


# Llama a la función principal
main()

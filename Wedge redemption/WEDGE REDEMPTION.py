# encoding: UTF-8
# Autor: Alek Fernando Howland Aguilar, A01747765
# Descripción: Proyecto final videojuego

import pygame  # Librería de pygame
from random import randint
import time

# Dimensiones de la pantalla

ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
COLORPERDISTE = (152,152,152)

# Estados

MENU = 1
JUGANDO = 2
CREDITOS = 3
PUNTAJES = 4
GANASTE = 5
PERDISTE = 6
SCORES = 7


def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.bottom += 7


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.bottom -= 13


def verificarColision(listaEnemigos, listaBalas):
    for k in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[k]
        for e in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[e]
            # Si bala le da al enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect

            if xb >= xe and xb < xe + ae - 50 and yb >= ye and yb <= ye + alte and yb > 0:
                # Le pego !!!
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                return True




def dibujarMenu(ventana, imgBtnJugar, imgFondoMenu, boton2, boton3):
    ventana.blit(imgFondoMenu, (0, 0))
    ventana.blit(imgBtnJugar, (ANCHO // 2 - 100, 370))
    ventana.blit(boton2, (ANCHO // 2 - 100, 400))
    ventana.blit(boton3, (ANCHO // 2 - 100, 430))


def dibujarGanaste(ventana, imgFondoGanaste, boton4):
    ventana.blit(imgFondoGanaste, (0, 0))
    ventana.blit(boton4, (ANCHO // 2 - 190, 145))


def dibujarPerdiste(ventana, imgFondoPerdiste, boton4):
    ventana.blit(imgFondoPerdiste, (0, 0))
    ventana.blit(boton4, (ANCHO // 2 - 190, 145))


def dibujarCreditos(ventana, imgFondoCreditos):
    ventana.blit(imgFondoCreditos, (0, 0))


def moverFondo(ventana, spriteFondoMovido):
    ventana.blit(spriteFondoMovido.image, spriteFondoMovido.rect)
    yf = spriteFondoMovido.rect.bottom - ALTO * 2
    spriteFondoMovido.rect.bottom += 30
    ventana.blit(spriteFondoMovido.image, (0, yf))
    if spriteFondoMovido.rect.bottom == ALTO * 2:
        spriteFondoMovido.rect.bottom = 0 + ALTO


def dibujarScores(ventana, imgFondoScores):
    ventana.blit(imgFondoScores, (0, 0))


def detectarColisionHeroe(listaEnemigos, spritePersonaje):
    for e in range(len(listaEnemigos)-1,-1,-1):
        enemigo = listaEnemigos[e]
        xe = enemigo.rect.left
        ye = enemigo.rect.bottom
        xh, yh, ah, alth = spritePersonaje.rect
        if xe >= xh  and xe < xh + ah -50 and ye >= yh and ye <= yh + alth:
            return True


def obtenerScores(score):
    scores = open("scores.txt", "r")
    lista = scores.read().split("\n")
    lista2 = []
    for n in lista:
        if n != "":
            lista2.append(n)
    if score > 0:
        lista2.append(score)
        lista2.sort()
    scores.close()
    return lista2



def dibujar():
    # Inicializar el motor de pygame
    pygame.init()
    pygame.display.set_caption("Wedge Redemption")
    icon = pygame.image.load("XWING.png")
    pygame.display.set_icon(icon)
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()  # Inicia los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje

    imgPersonaje = pygame.image.load("XWING.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = ANCHO // 2 - 23
    spritePersonaje.rect.bottom = ALTO // 2 + 337

    # Proyectiles

    listaBalas = []
    imgBala = pygame.image.load("BALA.png")

    # Fondo

    imgFondo = pygame.image.load("FONDO.png")
    imgFondoMovida = pygame.image.load("VELOCIDAD.png")
    spriteFondoMovido = pygame.sprite.Sprite
    spriteFondoMovido.image = imgFondoMovida
    spriteFondoMovido.rect = imgFondoMovida.get_rect()
    spriteFondoMovido.left = 0
    spriteFondoMovido.bottom = ALTO

    # Menu

    imgBtnJugar = pygame.image.load("BOTON 1.png")
    imgFondoMenu = pygame.image.load("MENU.png")
    imgFondoGanaste = pygame.image.load("WIN.png")
    imgFondoPerdiste = pygame.image.load("LOST.png")
    imgFondoCreditos = pygame.image.load("CREDS.png")
    imgFondoScores = pygame.image.load("SCORES.png")
    boton2 = pygame.image.load("BOTON 2.png")
    boton3 = pygame.image.load("BOTON 3.png")
    boton4 = pygame.image.load("ESC.png")

    # ----------------------------------
    estado = MENU
    # -----------------------------------

    # Enemigos

    listaEnemigos = []
    imgEnemigo = pygame.image.load("TIE.png")

    # Musica

    pygame.mixer.set_num_channels(10)
    if estado == MENU:
        pygame.mixer.music.load("INTRO.mp3")
        pygame.mixer.music.set_volume(1.0)
        pygame.mixer.music.play(-1)
    elif estado == JUGANDO:
        pygame.mixer.music.load("FLYYY.mp3")
        pygame.mixer.music.play(-1)
        disparoLaser1 = pygame.mixer.Sound("LASERXWING.wav")
        explo = pygame.mixer.Sound("EXPLO.wav")
    elif estado == GANASTE:
        pygame.mixer.music.load("THRONER.mp3")
        pygame.mixer.music.play(-1)
    elif estado == PERDISTE:
        pygame.mixer.music.load("LOST.mp3")
        pygame.mixer.music.play(-1)
    elif estado == CREDITOS:
        pygame.mixer.music.load("CREDS.mp3")
        pygame.mixer.music.play(-1)
    elif estado == SCORES:
        pygame.mixer.music.load("FORCEH.mp3")
        pygame.mixer.music.play(-1)

    # Generar enemigos

    for n in range(4):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(250, 500)
        spriteEnemigo.rect.bottom = randint(0, 100)
        listaEnemigos.append(spriteEnemigo)

    #Timepo
    timer = 0

    #Socre
    score = 0

    #Texto
    fuente = pygame.font.SysFont("cursedtimerulil", 30)
    fuente2 = pygame.font.SysFont("cursedtimerulil", 64)
    fuente3 = pygame.font.SysFont("aurebesh", 28)
    fuente4 = pygame.font.SysFont("cursedtimerulil", 44)


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False
        # , el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    if spritePersonaje.rect.left < 540:
                        spritePersonaje.rect.left += 13
                elif evento.key == pygame.K_LEFT:
                    if spritePersonaje.rect.left > 183:
                        spritePersonaje.rect.left -= 13
                elif evento.key == pygame.K_ESCAPE:
                    estado = MENU
                    pygame.mixer.music.load("INTRO.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play(-1)

        # Borrar pantalla

        ventana.fill(NEGRO)

        if estado == JUGANDO:
            tiempo = int(time.perf_counter())
            #---------------------------------
            if timer >= 2:
                timer = 0
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(250, 500)
                spriteEnemigo.rect.bottom = randint(0, 100)
                listaEnemigos.append(spriteEnemigo)
                #------------------------------------
                disparoLaser1.play()
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.left + 49
                spriteBala.rect.bottom = spritePersonaje.rect.bottom - 125
                listaBalas.append(spriteBala)

                spriteBala1 = pygame.sprite.Sprite()
                spriteBala1.image = imgBala
                spriteBala1.rect = imgBala.get_rect()
                spriteBala1.rect.left = spritePersonaje.rect.left - 23
                spriteBala1.rect.bottom = spritePersonaje.rect.bottom - 125
                listaBalas.append(spriteBala1)


            # -------------------------------------------
            a = verificarColision(listaEnemigos, listaBalas)
            if a == True:
                explo.play()
                score += 50
            else:
                pass
            # -------------------------------------------
            ventana.blit(imgFondo, (0, 0))
            texto = fuente.render(str(score), 1, BLANCO)
            ventana.blit(texto, (23,120))
            textoTiempo = fuente3.render(str(tiempo), 1, BLANCO)
            ventana.blit(textoTiempo,(47,235))
            #----------------------------------------
            moverFondo(ventana, spriteFondoMovido)
            # --------------------------------------
            dibujarPersonaje(ventana, spritePersonaje)
            # --------------------------------------------
            dibujarEnemigos(ventana, listaEnemigos)
            moverEnemigos(listaEnemigos)
            # --------------------------------------------
            dibujarBalas(ventana, listaBalas)
            moverBalas(listaBalas)
            # --------------------------------------------
            b = detectarColisionHeroe(listaEnemigos, spritePersonaje)
            if b == True:
                estado = PERDISTE
                pygame.mixer.music.load("LOST.mp3")
                pygame.mixer.music.play(-1)


            if tiempo > 76.015284398:
                estado = GANASTE
                pygame.mixer.music.load("THRONER.mp3")
                pygame.mixer.music.play(-1)




        elif estado == MENU:
            dibujarMenu(ventana, imgBtnJugar, imgFondoMenu, boton2, boton3)
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()


                xb = ANCHO // 2 - 100
                yb = 370
                if xm >= xb +10 and xm < xb + 175 and ym > yb and ym < yb + 30:
                    estado = JUGANDO
                    pygame.mixer.music.load("FLYYY.mp3")
                    pygame.mixer.music.play(-1)
                    disparoLaser1 = pygame.mixer.Sound("LASERXWING.wav")
                    explo = pygame.mixer.Sound("EXPLO.wav")
                #-----------------------------------------------------
                xb1 = ANCHO // 2 - 100
                yb1 = 400
                if xm >= xb1 + 10 and xm < xb1 + 175 and ym > yb1 + 15  and ym < yb1 +30:
                    estado = SCORES
                    pygame.mixer.music.load("FORCEH.mp3")
                    pygame.mixer.music.play(-1)
                #--------------------------------------------
                xb2 = ANCHO // 2 - 100
                yb2 = 430
                if xm >= xb2 + 23 and xm < xb2 + 160 and ym > yb2 + 15 and ym < yb2 + 30:
                    estado = CREDITOS
                    pygame.mixer.music.load("CREDS.mp3")
                    pygame.mixer.music.play(-1)
                #-----------------------------------------------
        elif estado == GANASTE:
            dibujarGanaste(ventana, imgFondoGanaste, boton4)
            texto = fuente2.render(str(score), 1, ROJO)
            ventana.blit(texto, (ALTO // 2 + 13, ANCHO // 2))
        elif estado == PERDISTE:
            dibujarPerdiste(ventana, imgFondoPerdiste, boton4)
            texto = fuente2.render(str(score), 1, COLORPERDISTE)
            ventana.blit(texto, (ALTO // 2 + 13, ANCHO // 2))
        elif estado == CREDITOS:
            dibujarCreditos(ventana, imgFondoCreditos)
        elif estado == SCORES:
            dibujarScores(ventana, imgFondoScores)
            a = obtenerScores(score)
            texto = fuente4.render(str(a[0]), 1, BLANCO)
            ventana.blit(texto, (ALTO // 2 + 50, 160))
            texto2 = fuente4.render(str(a[1]), 1, BLANCO)
            ventana.blit(texto2, (ALTO // 2 + 50, 260))
            texto3 = fuente4.render(str(a[2]), 1, BLANCO)
            ventana.blit(texto3, (ALTO // 2 + 50, 360))


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(20)
        timer += 1/20


    # Después del ciclo principal
    pygame.quit()  # termina pygame


def main():
    dibujar()


main()

# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame   # Librería de pygame
from random import randint
import time

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)# nada de rojo, ni verde, solo azul
NARANJA = (255,165,0)

# Estados
MENU = 1
JUGANDO = 2
PERDISTE = 3


#Estados de movimiento
QUIETO = 1
ABAJO = 2
ARRIBA = 3




# BETA
def mostrarReloj(ventana, listaSegundos):
    segundos = sum(listaSegundos)
    font = pygame.font.SysFont("Silom", 50)
    text = font.render(str(segundos), 1, BLANCO)
    ventana.blit(text, (672,530))
    for k in ((listaSegundos)):
        k += 1
        tiempo = sum(k)
        listaSegundos.append(str(tiempo))



# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje (ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    #VISITAR a cada elemento #for (variable) in (lista)
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def dibujarEnemigosII(ventana, listaEnemigosII):
    for enemigoR in listaEnemigosII:
        ventana.blit(enemigoR.image, enemigoR.rect)


def moverEnemigos(listaEnemigos, listaEnemigosII):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 25
        if enemigo.rect.left < -100:
            enemigo.rect.left = (randint(800, 1200))
    for k in range(len(listaEnemigosII)-1, -1, -1):
        enemigo = listaEnemigosII[k]
        enemigo.rect.left -= 5
        if enemigo.rect.left < -100:
            enemigo.rect.left = (randint(800, 1200))


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 40


def dibujarVidas(ventana, listaVidas):
    imgVida = pygame.image.load("VIDA.png")
    for n in listaVidas:
        spriteVida = pygame.sprite.Sprite
        spriteVida.image = imgVida
        spriteVida.rect = imgVida.get_rect()
        ventana.blit(imgVida, (n, 546))



def eliminarVida(listaVidas):
    for k in range(len(listaVidas)):
        if k == 0:
            vida = listaVidas[k]
            listaVidas.remove(vida)


def dibujarMenu(ventana, imgBtnJugar, titulo, instrucciones):
    ventana.blit(titulo, (ANCHO//2-150, randint(ALTO//2-220, ALTO//2-215)))
    ventana.blit(imgBtnJugar, (ANCHO//2-128, ALTO//2+120))
    ventana.blit(instrucciones, (ANCHO//2+160, 0))


def dibujarFin(ventana, imgBtnRegresar, imgFondoP):
    ventana.blit(imgFondoP, (ANCHO//2-150, randint(ALTO//2-220, ALTO//2-215)))
    ventana.blit(imgBtnRegresar, (ANCHO//2-128, ALTO//2+120))


def finalizarJuego(ventana, listaVidas, imgBtnRegresar, imgFondoP):
    if len(listaVidas) == 0:
        dibujarFin(ventana, imgBtnRegresar, imgFondoP)
        # Preguntar si soltó el mouse dentro del botón
        xm, ym = pygame.mouse.get_pos()
        xb = ANCHO // 2 - 128
        yb = ALTO // 2 + 120
        if xm >= xb and xm <= xb + 236 and ym >= yb and ym <= yb + 100:
            estado = JUGANDO


def definirPuntaje(ventana, count):
    puntos = sum(count)
    if puntos < 0:
        puntos = 0
    font = pygame.font.SysFont("Silom", 50)
    text = font.render(str(puntos), 1, BLANCO)
    ventana.blit(text, (450,490))


def dibujarScore(ventana, listaPuntos):
    totalPuntos = str(sum(listaPuntos))
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    text = font.render(totalPuntos, 1, ROJO)
    ventana.blit(text, (ANCHO//2+25, ALTO//2-50))
    puntos = "Score:"
    pygame.font.init()
    font = pygame.font.Font(None, 40)
    textPuntaje = font.render(puntos, 1, BLANCO)
    ventana.blit(textPuntaje, (ANCHO//2-80, ALTO//2-50))

    antes = open("puntajes.txt", "r")
    linea = antes.readline()
    puntajePasado = linea
    pygame.font.init()
    fontHS = pygame.font.Font(None, 40)
    textHS = fontHS.render(puntajePasado, 1, ROJO)
    ventana.blit(textHS, (ANCHO//2+50, ALTO//2+50))
    puntajeMayor = "HighScore:"
    pygame.font.init()
    font1 = pygame.font.Font(None, 40)
    textHS1 = font1.render(puntajeMayor, 1, BLANCO )
    ventana.blit(textHS1, (ANCHO//2-120, ALTO//2+50))
    pygame.display.flip()

# BETA
def verificarColisionPersonaje(ventana, spritePersonaje, listaVidas, listaEnemigos, listaEnemigosII, listaPuntos):
    dibujarVidas(ventana, listaVidas)
    for e in range(len(listaEnemigos)-1,-1,-1):
        enemigo = listaEnemigos[e]
        xb = spritePersonaje.rect.left
        yb = spritePersonaje.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            enemigo.rect.left = (randint(800, 1200))
            listaPuntos.append(-50)

    for e in range(len(listaEnemigosII)-1,-1,-1):
        enemigo = listaEnemigosII[e]
        xb = spritePersonaje.rect.left
        yb = spritePersonaje.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            enemigo.rect.left = (randint(800, 1200))
            listaPuntos.append(-100)
            eliminarVida(listaVidas)



def verificarColision(ventana, listaBalas, listaEnemigosII, listaEnemigos, listaPuntos, listaVidas):
    dibujarVidas(ventana, listaVidas)
    definirPuntaje(ventana, listaPuntos)
    for k in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        # AUTOS
        for e in range(len(listaEnemigosII)-1, -1, -1):
            enemigo = listaEnemigosII[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb>=xe and xb<=xe+ae and yb>=ye and yb<=ye + alte:
                # Le pegó
                enemigo.rect.left = (randint(800,1200))
                listaBalas.remove(bala)
                listaPuntos.append(50)


        for e in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[e]
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                enemigo.rect.left = (randint(800, 1200))
                listaPuntos.append(-100)
                eliminarVida(listaVidas)

    return listaPuntos



def moverFondo(ventana, imgFondo, tablero):
    for columna in range(1):
        a = float(randint(ALTO-126,ALTO-125))
        ventana.blit(imgFondo, (0, 0))
        ventana.blit(tablero, (0, a))



def moverFondoII(ventana, imgFondoII, xFondoII):
    for columna in range(6):
        x = (800*columna) - xFondoII
        while not x > - 800:
             x = x + 1600
        ventana.blit(imgFondoII, (x,218))



def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje
    imgPersonaje = pygame.image.load("AUTO B.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO//2 + spritePersonaje.rect.height//2


    # Enemigos
    a = int(randint(0,3))
    listaEnemigos = []
    imgEnemigo = pygame.image.load("Bomba.png")
    for k in range(a):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(ANCHO//2, ANCHO)
        spriteEnemigo.rect.bottom = randint(300, 470)
        listaEnemigos.append(spriteEnemigo)


    b = int(randint(3,8))
    listaEnemigosII = []
    imgEnemigoR = pygame.image.load("AUTO ROJO.png")
    for k in range(b):
        spriteEnemigoR = pygame.sprite.Sprite()
        spriteEnemigoR.image = imgEnemigoR
        spriteEnemigoR.rect = imgEnemigoR.get_rect()
        spriteEnemigoR.rect.left = randint(ANCHO // 2, ANCHO)
        spriteEnemigoR.rect.bottom = randint(310, 467)
        listaEnemigosII.append(spriteEnemigoR)


    # Proyectiles/balas
    listaBalas = []
    imgBala = pygame.image.load("BALA.png")
    listaPuntos = []
    listaSegundos = []
    listaVidas = [380, 440, 500]


    # Audio
    efecto = pygame.mixer.Sound("shoot.wav")


    # Menú
    imgBtnJugar = pygame.image.load("BTN INICIAR.png")
    titulo = pygame.image.load("TITULO.png")
    instrucciones = pygame.image.load("Instrucciones.png")
    estado = MENU


    # Perdiste
    imgBtnRegresar = pygame.image.load("VolverJuego.png")
    imgFondoP = pygame.image.load("Perdiste.png")

    # Audio
    # pygame.mixer.init()
    # pygame.mixer.Sound('DISPARO.mp3')

    imgFondo = pygame.image.load("FONDO .png")
    imgFondoII = pygame.image.load("PISTA.png")
    tablero = pygame.image.load("Tablero.png")
    moviendo = QUIETO
    xFondoII = 0
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente)
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    #spritePersonaje.rect.bottom -= 5
                    moviendo = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    moviendo = ABAJO
                elif evento.key == pygame.K_z:
                    #Crear una bala
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalas.append(spriteBala)
                    efecto.play()
            elif evento.type == pygame.KEYUP:
                moviendo == QUIETO
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm, ",", ym)
                # Preguntar si soltó el mouse dentro del botón
                xb = ANCHO//2 - 128
                yb = ALTO//2 + 120
                if xm>=xb and xm<=xb+236 and ym>=yb and ym<=yb+100:
                    estado = JUGANDO
                    pygame.mixer.music.load("musicaFondo.mp3")
                    pygame.mixer.music.play(-1)



        # Borrar pantalla
        ventana.fill(NARANJA)

        if estado == JUGANDO:
            #Actualizar enemigos
            if moviendo == ARRIBA:
                spritePersonaje.rect.bottom -= 6
                if spritePersonaje.rect.bottom <= 300:
                    spritePersonaje.rect.bottom += 8
            elif moviendo == ABAJO:
                spritePersonaje.rect.bottom += 6
                if spritePersonaje.rect.bottom >= 467:
                    spritePersonaje.rect.bottom -= 8
            moverEnemigos(listaEnemigos, listaEnemigosII)
            moverBalas(listaBalas)
            verificarColision(ventana, listaBalas, listaEnemigosII, listaEnemigos, listaPuntos, listaVidas)
            xFondoII += 25

            # Dibujar, aquí haces todos los trazos que requieras
            ventana.blit(imgFondo, (0,0))
            dibujarVidas(ventana, listaVidas)
            moverFondo(ventana, imgFondo, tablero)
            moverFondoII(ventana, imgFondoII, xFondoII)
            verificarColision(ventana, listaBalas, listaEnemigosII, listaEnemigos, listaPuntos, listaVidas)
            # verificarColisionPersonaje(ventana, listaEnemigos, listaEnemigosII, listaVidas, listaPuntos, spritePersonaje)
            mostrarReloj(ventana, listaSegundos)
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarEnemigosII(ventana, listaEnemigosII)
            dibujarBalas(ventana, listaBalas)
            if len(listaVidas) == 0:
                dibujarFin(ventana, imgBtnRegresar, imgFondoP)
                dibujarScore(ventana, listaPuntos)
                puntajePasado = open("puntajes.txt", "r")
                linea = puntajePasado.readline()
                puntaje = int(linea)
                total = sum(listaPuntos)
                if puntaje < total:
                    puntos = open("puntajes.txt", "w")
                    puntos.write("%d" % total)
                    puntos.close()
                puntajePasado.close()
                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                        termina = True
                        # Preguntar si soltó el mouse dentro del botón
                    if evento.type == pygame.MOUSEBUTTONUP:
                        xm, ym = pygame.mouse.get_pos()
                        xb = ANCHO // 2 - 128
                        yb = ALTO // 2 + 120
                        if xm >= xb and xm <= xb + 236 and ym >= yb and ym <= yb + 100:
                            dibujar()
                            estado = JUGANDO


        elif estado == MENU:
            # Dibujar Menú
            dibujarMenu(ventana, imgBtnJugar, titulo, instrucciones)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
    reloj.tick(40)  # 40 fps
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
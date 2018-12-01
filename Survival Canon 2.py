#Alberto Contreras Torres
#Survival Canon

import pygame   # Librería de pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE = (51, 255, 51)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0,0,0)
AZUL_CLARO = (0,255,255)
AMARILLO = (251,255,0)



#Estados
MENU = 1
JUGANDO = 2
GAMEOVER = 3
INSTRUCCIONES = 4

#Estados de movimiento
QUIETO = 1
ABAJO = 2
ARRIBA = 3

#PUNTOS
puntos = 0

#VIDAS
vidas = 3


def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)
# Estructura básica de un programa que usa pygame para dibujar
def dibujarEnemigos(ventana, listaEnemigos):
    #Visitar a cada elemento
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarEnemigosA(ventana, listaEnemigosA):
    for enemigo in listaEnemigosA:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarEnemigosArriba(ventana, listaEnemigosArriba):
    for enemigo in listaEnemigosArriba:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarEnemigosIzquierda(ventana, listaEnemigosIzquierda):
    for enemigo in listaEnemigosIzquierda:
        ventana.blit(enemigo.image, enemigo.rect)

'-------------------------------------------------------------------------------------------------------------------'

def dibujarEnemigoXDerecha(ventana, listaEnemigoXDerecha):
    for enemigo in listaEnemigoXDerecha:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarEnemigoXIzquierda(ventana, listaEnemigoXIzquierda):
    for enemigo in listaEnemigoXIzquierda:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarEnemigoXAbajo(ventana, listaEnemigoXAbajo):
    for enemigo in listaEnemigoXAbajo:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarEnemigoXArriba(ventana, listaEnemigoXArriba):
    for enemigo in listaEnemigoXArriba:
        ventana.blit(enemigo.image, enemigo.rect)

def moverEnemigoXDerecha(listaEnemigoXDerecha):
    for enemigo in listaEnemigoXDerecha:
        enemigo.rect.left -= 7

def moverEnemigoXIzquierda(listaEnemigosXIzquierda):
    for enemigo in listaEnemigosXIzquierda:
        enemigo.rect.left += 7

def moverEnemigoXAbajo(listaEnemigoXAbajo):
    for enemigo in listaEnemigoXAbajo:
        enemigo.rect.bottom -= 7

def moverEnemigoXArriba(listaEnemigoXArriba):
    for enemigo in listaEnemigoXArriba:
        enemigo.rect.bottom += 7

def verificarColisionXDerecha(listaEnemigoXDerecha, listaBalas):
    global puntos
    for k in range (len(listaBalas)-1,-1,-1):
        bala=listaBalas[k]
        for e in range (len(listaEnemigoXDerecha)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigoXDerecha[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos+= 1
                # Le pegó!!!!
                listaEnemigoXDerecha.remove(enemigo)
                listaBalas.remove(bala)
                break

def verificarColisionXIzquierda(listaEnemigoXIzquierda, listaBalasIzquierda):
    global puntos
    for k in range (len(listaBalasIzquierda)-1,-1,-1):
        bala=listaBalasIzquierda[k]
        for e in range (len(listaEnemigoXIzquierda)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigoXIzquierda[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos+= 1
                # Le pegó!!!!
                listaEnemigoXIzquierda.remove(enemigo)
                listaBalasIzquierda.remove(bala)
                break

def verificarColisionXAbajo(listaEnemigoXAbajo, listaBalasAbajo):
    global puntos
    for k in range (len(listaBalasAbajo)-1,-1,-1):
        bala=listaBalasAbajo[k]
        for e in range (len(listaEnemigoXAbajo)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigoXAbajo[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos+= 1
                # Le pegó!!!!
                listaEnemigoXAbajo.remove(enemigo)
                listaBalasAbajo.remove(bala)
                break

def verificarColisionXArriba(listaEnemigoXArriba, listaBalasArriba):
    global puntos
    for k in range (len(listaBalasArriba)-1,-1,-1):
        bala=listaBalasArriba[k]
        for e in range (len(listaEnemigoXArriba)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigoXArriba[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos+= 1
                # Le pegó!!!!
                listaEnemigoXArriba.remove(enemigo)
                listaBalasArriba.remove(bala)
                break

def verificarDañoXDerecha(spritePersonaje, listaEnemigoXDerecha):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigoXDerecha)-1,-1,-1):
        enemigo = listaEnemigoXDerecha[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigoXDerecha.remove(enemigo)
            break

def verificarDañoXIzquierda(spritePersonaje, listaEnemigoXIzquierda):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigoXIzquierda)-1,-1,-1):
        enemigo = listaEnemigoXIzquierda[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigoXIzquierda.remove(enemigo)
            break

def verificarDañoXArriba(spritePersonaje, listaEnemigoXArriba):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigoXArriba)-1,-1,-1):
        enemigo = listaEnemigoXArriba[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigoXArriba.remove(enemigo)
            break

def verificarDañoXAbajo(spritePersonaje, listaEnemigoXAbajo):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigoXAbajo)-1,-1,-1):
        enemigo = listaEnemigoXAbajo[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigoXAbajo.remove(enemigo)
            break
'---------------------------------------------------------------------------------------------------------------------'

def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 3

def moverEnemigosIzquierda(listaEnemigosIzquierda):
    for enemigo in listaEnemigosIzquierda:
        enemigo.rect.left += 3
        #enemigo.rect.bottom += 1


def moverEnemigosA(listaEnemigosA):
    for enemigo in listaEnemigosA:
        enemigo.rect.bottom -= 3

def moverEnemigosArriba(listaEnemigosArriba):
    for enemigo in listaEnemigosArriba:
        enemigo.rect.bottom += 3

#-----------------------------------------------------------------------------------------------------------------------------------------BALAS-----------------------------------------------
def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

def dibujarBalasIzquierda(ventana, listaBalasIzquierda):
    for bala in listaBalasIzquierda:
        ventana.blit(bala.image, bala.rect)

def dibujarBalasAbajo(ventana, listaBalasAbajo):
    for bala in listaBalasAbajo:
        ventana.blit(bala.image, bala.rect)

def dibujarBalasArriba(ventana, listaBalasArriba):
    for bala in listaBalasArriba:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 2

def moverBalasIzquierda(listaBalasIzquierda):
    for bala in listaBalasIzquierda:
        bala.rect.left -= 2

def moverBalasAbajo(listaBalasAbajo):
    for bala in listaBalasAbajo:
        bala.rect.bottom += 2

def moverBalasArriba(listaBalasArriba):
    for bala in listaBalasArriba:
        bala.rect.bottom -= 2

def dibujarMenu(ventana, imgBtnJugar):
    ventana.blit(imgBtnJugar, (ANCHO//2-128, ALTO//3))

def dibujarIns(ventana, imgBtnIns):
    ventana.blit(imgBtnIns, (550, 500))

def dibujarJugar(ventana, imgBtnJugar2):
    ventana.blit(imgBtnJugar2, (650,100))


def verificarColision(listaEnemigos, listaBalas):
    global puntos
    for k in range (len(listaBalas)-1,-1,-1):
        bala=listaBalas[k]
        for e in range (len(listaEnemigos)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigos[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos+= 1
                # Le pegó!!!!
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                break

def verificarColisionIzquierda(listaEnemigosIzquierda, listaBalasIzquierda):
    global puntos
    for k in range (len(listaBalasIzquierda)-1,-1,-1):
        bala=listaBalasIzquierda[k]
        for e in range (len(listaEnemigosIzquierda)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigosIzquierda[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos += 1
                # Le pegó!!!!
                listaEnemigosIzquierda.remove(enemigo)
                listaBalasIzquierda.remove(bala)
                break


def verificarColisionAbajo(listaEnemigosA, listaBalasAbajo):
    global puntos
    for k in range (len(listaBalasAbajo)-1,-1,-1):
        bala=listaBalasAbajo[k]
        for e in range (len(listaEnemigosA)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigosA[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos += 1
                # Le pegó!!!!
                listaEnemigosA.remove(enemigo)
                listaBalasAbajo.remove(bala)
                break


def verificarColisionArriba(listaEnemigosArriba, listaBalasArriba):
    global puntos
    for k in range (len(listaBalasArriba)-1,-1,-1):
        bala=listaBalasArriba[k]
        for e in range (len(listaEnemigosArriba)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigosArriba[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                puntos += 1
                # Le pegó!!!!
                listaEnemigosArriba.remove(enemigo)
                listaBalasArriba.remove(bala)
                break

def verificarDaño(spritePersonaje, listaEnemigos):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigos)-1,-1,-1):
        enemigo = listaEnemigos[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigos.remove(enemigo)
            break

def verificarDañoAbajo(spritePersonaje, listaEnemigosA):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigosA)-1,-1,-1):
        enemigo = listaEnemigosA[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigosA.remove(enemigo)
            break

def verificarDañoIzquierda(spritePersonaje, listaEnemigosIzquierda):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigosIzquierda)-1,-1,-1):
        enemigo = listaEnemigosIzquierda[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigosIzquierda.remove(enemigo)
            break


def verificarDañoArriba(spritePersonaje, listaEnemigosArriba):
    global vidas
    canon = spritePersonaje
    for e in range(len(listaEnemigosArriba)-1,-1,-1):
        enemigo = listaEnemigosArriba[e]
        xb = canon.rect.left
        yb = canon.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
            vidas -= 1
            # Le pegó!!!!
            listaEnemigosArriba.remove(enemigo)
            break


def GuardarPuntos():
    global puntos
    entrada = open("puntuacion.txt", "r")

    linea = entrada.readline()
    puntosPasados = int(linea)
    if puntosPasados < puntos:
        salida = open("puntuacion.txt", "w")
        salida.write("%s"%(puntos))
        salida.close()
    entrada.close()






def dibujarBoton(ventana, imgBoton):
    ventana.blit(imgBoton,(300, 450))

def borrarEnemigos(listaEnemigos, listaEnemigosA, listaEnemigosArriba, listaEnemigosIzquierda, listaEnemigoXDerecha, listaEnemigoXIzquierda, listaEnemigoXArriba, listaEnemigoXAbajo):
    for enemigo in listaEnemigosIzquierda:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 800 and enemigo.rect.left >= -100 and enemigo.rect.left <= 800:
            listaEnemigosIzquierda.remove(enemigo)
            break

    for enemigo in listaEnemigos:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 800 and enemigo.rect.left >= -100 and enemigo.rect.left <= 800:
            listaEnemigos.remove(enemigo)
            break

    for enemigo in listaEnemigosA:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 800 and enemigo.rect.left >= -100 and enemigo.rect.left <= 800:
            listaEnemigosA.remove(enemigo)
            break

    for enemigo in listaEnemigosArriba:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 800 and enemigo.rect.left >= -100 and enemigo.rect.left <= 800:
            listaEnemigosArriba.remove(enemigo)
            break

    for enemigo in listaEnemigoXDerecha:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 800 and enemigo.rect.left >= -100 and enemigo.rect.left <= 800:
            listaEnemigoXDerecha.remove(enemigo)
            break

    for enemigo in listaEnemigoXIzquierda:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 800 and enemigo.rect.left >= -100 and enemigo.rect.left <= 800:
            listaEnemigoXIzquierda.remove(enemigo)
            break

    for enemigo in listaEnemigoXArriba:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 800 and enemigo.rect.left >= -100 and enemigo.rect.left <= 800:
            listaEnemigoXArriba.remove(enemigo)
            break

    for enemigo in listaEnemigoXAbajo:
        if enemigo.rect.bottom >= -100 and enemigo.rect.bottom <= 850 and enemigo.rect.left >= -100 and enemigo.rect.left >= 350:
            listaEnemigoXAbajo.remove(enemigo)
            break


def borrarBalas(listaBalas, listaBalasIzquierda, listaBalasAbajo, listaBalasArriba):
    for bala in listaBalasIzquierda:
        if bala.rect.bottom >= -800 and bala.rect.bottom <= 800 and bala.rect.left >= -800 and bala.rect.left <= 800:
            listaBalasIzquierda.remove(bala)
            break

    for bala in listaBalas:
        if bala.rect.bottom >= -800 and bala.rect.bottom <= 800 and bala.rect.left >= -800 and bala.rect.left <= 800:
            listaBalas.remove(bala)
            break

    for bala in listaBalasAbajo:
        if bala.rect.bottom >= -800 and bala.rect.bottom <= 800 and bala.rect.left >= -800 and bala.rect.left <= 800:
            listaBalasAbajo.remove(bala)
            break

    for bala in listaBalasArriba:
        if bala.rect.bottom >= -800 and bala.rect.bottom <= 800 and bala.rect.left >= -800 and bala.rect.left <= 800:
            listaBalasArriba.remove(bala)
            break

def desplegarHighscore(ventana, fuente):
    entrada = open("puntuacion.txt", "r")

    linea = entrada.readline()
    puntaje = int(linea)
    highScore = fuente.render("HIGHSCORE %d" % puntaje, 1 , AMARILLO)
    ventana.blit(highScore, (0,500))
    entrada.close()





def dibujar():
    global vidas
    global puntos
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #--------------------------------------------------------------------------------------------------------------------------------------------Personaje
    imgPersonaje = pygame.image.load("canon.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect= imgPersonaje.get_rect()
    spritePersonaje.rect.left = 360
    spritePersonaje.rect.bottom = ALTO//2 + spritePersonaje.rect.height//2

    #-----------------------------------------------------------------------------------------------------------------------------------------------Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("ghost-blue.png")
    imgEnemigoX = pygame.image.load("ghost-red.png")

    listaEnemigosA = []

    listaEnemigosArriba = []

    listaEnemigosIzquierda = []

    listaEnemigoXDerecha = []
    listaEnemigoXIzquierda = []
    listaEnemigoXArriba = []
    listaEnemigoXAbajo = []


    #---------------------------------------------------------------------------------------------------------------------------------------------------Proyectiles/balas
    listaBalas = []
    listaBalasIzquierda = []
    listaBalasAbajo = []
    listaBalasArriba = []
    imgBala = pygame.image.load("flame.png")

    #--------------------------------------------------------------------------------------------------------------------------------------------------Menú
    imgBtnJugar = pygame.image.load("button_iniciar-juego (3).png")
    imgBtnIns = pygame.image.load("botoninstrucciones.png")
    imgBtnJugar2 = pygame.image.load("botonjugar2.png")
    imgFondo = pygame.image.load("fondo2.jpg")
    imgFondoM = pygame.image.load("fondomenu.jpg")
    imgGameOver = pygame.image.load("gameover.png")
    imgBoton = pygame.image.load("menu.png")
    imgIns = pygame.image.load("instrucciones.jpg")

    estado = MENU


    xf = 0

    #TIEMPO
    timer = 0   #Acumulador de tiempo


    #TEXTO
    fuente = pygame.font.SysFont("monospace", 64)

    #AUDIO
    pygame.mixer.init()
    pygame.mixer.music.load("adamas-8bit.mp3")
    pygame.mixer.music.play(-1)     #-1 para infinito y 1 para momentaneo


    efecto = pygame.mixer.Sound("shoot.wav")


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_d:
                    #Crear una bala
                    efecto.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalas.append(spriteBala)
            #elif evento.type == pygame.KEYDOWN:
                elif evento.key == pygame.K_a:
                    efecto.play()
                    spriteBalaIzquierda = pygame.sprite.Sprite()
                    spriteBalaIzquierda.image = imgBala
                    spriteBalaIzquierda.rect = imgBala.get_rect()
                    spriteBalaIzquierda.rect.left = spritePersonaje.rect.left - spritePersonaje.rect.width
                    spriteBalaIzquierda.rect.bottom = spritePersonaje.rect.bottom
                    listaBalasIzquierda.append(spriteBalaIzquierda)
                elif evento.key == pygame.K_s:
                    efecto.play()
                    spriteBalaAbajo = pygame.sprite.Sprite()
                    spriteBalaAbajo.image = imgBala
                    spriteBalaAbajo.rect = imgBala.get_rect()
                    spriteBalaAbajo.rect.left = spritePersonaje.rect.left
                    spriteBalaAbajo.rect.bottom = spritePersonaje.rect.bottom + spritePersonaje.rect.width
                    listaBalasAbajo.append(spriteBalaAbajo)
                elif evento.key == pygame.K_w:
                    efecto.play()
                    spriteBalaArriba = pygame.sprite.Sprite()
                    spriteBalaArriba.image = imgBala
                    spriteBalaArriba.rect = imgBala.get_rect()
                    spriteBalaArriba.rect.left = spritePersonaje.rect.left
                    spriteBalaArriba.rect.bottom = spritePersonaje.rect.bottom - spritePersonaje.rect.width
                    listaBalasArriba.append(spriteBalaArriba)



            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm,",",ym)
                #Preguntar si soltó el mouse dentro del botón
                xb = ANCHO//2-128
                yb= ALTO//3
                if xm >= 271 and ym >= 202 and xm <= 524 and ym <= 296:
                    estado = JUGANDO

                elif xm >=302 and ym >= 452 and xm <= 493 and ym <= 518:
                    estado = MENU

                elif xm >= 550 and ym >= 502 and xm <= 721 and ym <= 538:
                    estado = INSTRUCCIONES

                elif xm >= 651 and ym >= 100 and xm <= 732 and ym <= 137:
                    estado = JUGANDO





        # Borrar pantalla
        ventana.fill(NEGRO)

        if estado == JUGANDO:


            #TIEMPO
            if timer >= 2:  #>Tiene que llegar a 2
                timer = 0   #Vuelve a ser cero
            #Actualizar enemigos
            # Mover PERSONAJE


                #----------------------------------------------------------------------------------------- CREA ENEMIGO DESPUÉS DE PANATALLA
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(800,2000)  # AREA DONDE SE GENERAN
                spriteEnemigo.rect.bottom = 350
                listaEnemigos.append(spriteEnemigo)

                spriteEnemigoIzquierda = pygame.sprite.Sprite()
                spriteEnemigoIzquierda.image = imgEnemigo
                spriteEnemigoIzquierda.rect = imgEnemigo.get_rect()
                spriteEnemigoIzquierda.rect.left = randint(-1000,0) # AREA DONDE SE GENERAN
                spriteEnemigoIzquierda.rect.bottom = 350
                listaEnemigosIzquierda.append(spriteEnemigoIzquierda)

                spriteEnemigoA = pygame.sprite.Sprite()
                spriteEnemigoA.image = imgEnemigo
                spriteEnemigoA.rect = imgEnemigo.get_rect()
                spriteEnemigoA.rect.left = 350  # AREA DONDE SE GENERAN
                spriteEnemigoA.rect.bottom = randint(850, 1000)
                listaEnemigosA.append(spriteEnemigoA)

                spriteEnemigoArriba = pygame.sprite.Sprite()
                spriteEnemigoArriba.image = imgEnemigo
                spriteEnemigoArriba.rect = imgEnemigo.get_rect()
                spriteEnemigoArriba.rect.left = 350  # AREA DONDE SE GENERAN
                spriteEnemigoArriba.rect.bottom = randint (-1000, 0)
                listaEnemigosArriba.append(spriteEnemigoArriba)

                for k in range(3):
                    spriteEnemigoXDerecha = pygame.sprite.Sprite()
                    spriteEnemigoXDerecha.image = imgEnemigoX
                    spriteEnemigoXDerecha.rect = imgEnemigo.get_rect()
                    spriteEnemigoXDerecha.rect.left = 900  # AREA DONDE SE GENERAN
                    spriteEnemigoXDerecha.rect.bottom = 350
                    listaEnemigoXDerecha.append(spriteEnemigoXDerecha)

                for k in range(3):
                    spriteEnemigoXIzquierda = pygame.sprite.Sprite()
                    spriteEnemigoXIzquierda.image = imgEnemigoX
                    spriteEnemigoXIzquierda.rect = imgEnemigo.get_rect()
                    spriteEnemigoXIzquierda.rect.left = -200  # AREA DONDE SE GENERAN
                    spriteEnemigoXIzquierda.rect.bottom = 350
                    listaEnemigoXIzquierda.append(spriteEnemigoXIzquierda)

                for k in range(3):
                    spriteEnemigoXArriba = pygame.sprite.Sprite()
                    spriteEnemigoXArriba.image = imgEnemigoX
                    spriteEnemigoXArriba.rect = imgEnemigo.get_rect()
                    spriteEnemigoXArriba.rect.left = 350  # AREA DONDE SE GENERAN
                    spriteEnemigoXArriba.rect.bottom = -100
                    listaEnemigoXArriba.append(spriteEnemigoXArriba)

                for k in range(3):
                    spriteEnemigoXAbajo = pygame.sprite.Sprite()
                    spriteEnemigoXAbajo.image = imgEnemigoX
                    spriteEnemigoXAbajo.rect = imgEnemigo.get_rect()
                    spriteEnemigoXAbajo.rect.left = 350  # AREA DONDE SE GENERAN
                    spriteEnemigoXAbajo.rect.bottom = 850
                    listaEnemigoXAbajo.append(spriteEnemigoXAbajo)

            elif vidas == 0:
                estado = GAMEOVER



            # Dibujar, aquí haces todos los trazos que requieras
            ventana.blit(imgFondo, (xf,0))
            #xf -= 1         Avanza pantalla
            #---------------------------------------------PERSONAJE-------------------------------------
            dibujarPersonaje(ventana, spritePersonaje)
            #---------------------------------------------ENEMIGOS--------------------------------------
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarEnemigosA(ventana, listaEnemigosA)
            dibujarEnemigosArriba(ventana, listaEnemigosArriba)
            dibujarEnemigosIzquierda(ventana, listaEnemigosIzquierda)
            dibujarEnemigoXDerecha(ventana, listaEnemigoXDerecha)
            dibujarEnemigoXIzquierda(ventana, listaEnemigoXIzquierda)
            dibujarEnemigoXArriba(ventana, listaEnemigoXArriba)
            dibujarEnemigoXAbajo(ventana, listaEnemigoXAbajo)
            moverEnemigos(listaEnemigos)
            moverEnemigosA(listaEnemigosA)
            moverEnemigosIzquierda(listaEnemigosIzquierda)
            moverEnemigosArriba(listaEnemigosArriba)
            moverEnemigoXDerecha(listaEnemigoXDerecha)
            moverEnemigoXIzquierda(listaEnemigoXIzquierda)
            moverEnemigoXAbajo(listaEnemigoXAbajo)
            moverEnemigoXArriba(listaEnemigoXArriba)
            #----------------------------------------------BALAS-----------------------------------------
            moverBalas(listaBalas)
            moverBalasIzquierda(listaBalasIzquierda)
            moverBalasAbajo(listaBalasAbajo)
            moverBalasArriba(listaBalasArriba)
            dibujarBalas(ventana, listaBalas)
            dibujarBalasIzquierda(ventana, listaBalasIzquierda)
            dibujarBalasAbajo(ventana, listaBalasAbajo)
            dibujarBalasArriba(ventana, listaBalasArriba)
            verificarColision(listaEnemigos, listaBalas)
            verificarColisionIzquierda(listaEnemigosIzquierda, listaBalasIzquierda)
            verificarColisionAbajo(listaEnemigosA, listaBalasAbajo)
            verificarColisionArriba(listaEnemigosArriba, listaBalasArriba)
            verificarColisionXDerecha(listaEnemigoXDerecha, listaBalas)
            verificarColisionXIzquierda(listaEnemigoXIzquierda, listaBalasIzquierda)
            verificarColisionXArriba(listaEnemigoXArriba,listaBalasArriba)
            verificarColisionXAbajo(listaEnemigoXAbajo,listaBalasAbajo)
            #------------------------------------------------DAÑO-----------------------------------------
            verificarDaño(spritePersonaje,listaEnemigos)
            verificarDañoAbajo(spritePersonaje,listaEnemigosA)
            verificarDañoArriba(spritePersonaje,listaEnemigosArriba)
            verificarDañoIzquierda(spritePersonaje,listaEnemigosIzquierda)
            verificarDañoXDerecha(spritePersonaje,listaEnemigoXDerecha)
            verificarDañoXIzquierda(spritePersonaje,listaEnemigoXIzquierda)
            verificarDañoXArriba(spritePersonaje,listaEnemigoXArriba)
            verificarDañoXAbajo(spritePersonaje,listaEnemigoXAbajo)
            GuardarPuntos()
            texto = fuente.render("PUNTOS %d" % puntos, 1, ROJO)
            ventana.blit(texto, (ANCHO // 2 - 400, 0))
            vida = fuente.render("VIDAS %d" % vidas, 1, AZUL_CLARO)
            ventana.blit(vida, (ANCHO // 2, 0))
            desplegarHighscore(ventana, fuente)





        elif estado == MENU:
            vidas = 3
            puntos = 0

            #Dibujar menú
            ventana.blit(imgFondoM, (xf, 0))
            dibujarMenu(ventana, imgBtnJugar)
            dibujarIns(ventana, imgBtnIns)
            desplegarHighscore(ventana, fuente)
            borrarEnemigos(listaEnemigos, listaEnemigosA, listaEnemigosArriba, listaEnemigosIzquierda, listaEnemigoXDerecha, listaEnemigoXIzquierda, listaEnemigoXArriba, listaEnemigoXAbajo)
            borrarBalas(listaBalas, listaBalasIzquierda, listaBalasAbajo, listaBalasArriba)
            #desplegarHighscore(ventana, fuente)
            # Texto en la pantalla
            titulo = fuente.render("SURVIVAL CANON", 1, VERDE)
            ventana.blit(titulo,(120, 50))

        elif estado == INSTRUCCIONES:
            ventana.blit(imgIns,(xf, 0))
            dibujarJugar(ventana, imgBtnJugar2)
            borrarEnemigos(listaEnemigos, listaEnemigosA, listaEnemigosArriba, listaEnemigosIzquierda, listaEnemigoXDerecha, listaEnemigoXIzquierda, listaEnemigoXArriba, listaEnemigoXAbajo)
            borrarBalas(listaBalas, listaBalasIzquierda, listaBalasAbajo, listaBalasArriba)




        elif estado == GAMEOVER:
            ventana.blit(imgGameOver, (xf, 0))
            dibujarBoton(ventana, imgBoton)
            texto = fuente.render("PUNTOS %d" % puntos, 1, ROJO)
            ventana.blit(texto, (ANCHO // 2 - 400, 0))
            desplegarHighscore(ventana, fuente)







        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/20

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
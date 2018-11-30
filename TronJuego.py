# encoding: UTF-8
# Autor: David Isaí Lóez Jaimes     A01748363
# Juego de Tron que conforme vayas avanzando de nivel, va aumentando la dificultad, si no logras el nivel, pierdes, pero si completas todos, ganas. Tus puntos que lograste en el intento se guardan en un archivo de texto.

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

# Estados
MENU = 1
JUGANDO = 2
FIN = 3
FIN2 = 4
FIN3 = 8
TERMINA = 5
INTENTO = 6
NIVELFINAL = 7

# Contador de puntos
puntos = []

# Estados de movimineto
QUIETO = 1
ARRIBA = 2
ABAJO = 3
DERECHA = 4
IZQUIERDA = 5

# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePlanta):
    ventana.blit(spritePlanta.image, spritePlanta.rect)

def dibujarEnemigos2(ventana, listaEnemigos2):
    for enemigo2 in listaEnemigos2:
        ventana.blit(enemigo2.image, enemigo2.rect)


def actualizarEnemigos2(listaEnemigos2):
    for enemigo in listaEnemigos2:  # Vista cada enemigo2
        enemigo.rect.left -= 2
        enemigo.rect.bottom -= randint(0, 10)
        enemigo.rect.bottom += randint(0, 10)



def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def acttualizarEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:  # Vista cada enemigo
        enemigo.rect.left -= 1
        enemigo.rect.bottom -= randint(0, 10)
        enemigo.rect.bottom += randint(0, 10)


def dibujarEnemigos3(ventana, listaEnemigos3):
    for enemigo2 in listaEnemigos3:
        ventana.blit(enemigo2.image, enemigo2.rect)


def actualizarEnemigos3(listaEnemigos3):
    for enemigo in listaEnemigos3:  # Vista cada enemigo2
        enemigo.rect.left -= 3
        enemigo.rect.bottom -= randint(0, 10)
        enemigo.rect.bottom += randint(0, 10)


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listaBalas):
    for balas in listaBalas:
        balas.rect.left += 30


def verificarColisiones(listaBalas, listaEnemigos, puntos):
    # recorre las listas al revés
    for k in range(len(listaBalas)-1,-1,-1):
        bala = listaBalas[k]
        borrarBala = False
        for e in range(len(listaEnemigos)-1, -1, -1):
            enemigo = listaEnemigos[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, anchoe, altoe = enemigo.rect
            if xb >= xe and xb <= xe+anchoe and yb >= ye and yb <= ye+altoe:
                listaEnemigos.remove(enemigo) # Borra de la lista
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)
            puntos.append(1)






def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje principal
    imgPlanta = pygame.image.load("motoTron.png")
    spritePlanta = pygame.sprite.Sprite()  # sprite vacío
    spritePlanta.image = imgPlanta
    spritePlanta.rect = imgPlanta.get_rect()
    spritePlanta.rect.left = 0
    spritePlanta.rect.bottom = ALTO//2 + spritePlanta.rect.height//2

    movimiento = QUIETO

    # Enemigos
    listaEnemigos = []  # Lista vacía de enemigos
    imgEnemigo = pygame.image.load("motoTron2.png")
    for k in range(25):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(ANCHO//2, ANCHO)
        spriteEnemigo.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteEnemigo)

    # Enemigos 2
    listaEnemigos2 = []  # Lista vacía de enemigos2
    imgEnemigo2 = pygame.image.load("naves.png")
    for ka in range(35):
        spriteEnemigo2 = pygame.sprite.Sprite()
        spriteEnemigo2.image = imgEnemigo2
        spriteEnemigo2.rect = imgEnemigo2.get_rect()
        spriteEnemigo2.rect.left = randint(ANCHO//2, ANCHO)
        spriteEnemigo2.rect.bottom = randint(0, ALTO)
        listaEnemigos2.append(spriteEnemigo2)

    # Enemigos 3
    listaEnemigos3 = []  # Lista vacía de enemigos2
    imgEnemigo3 = pygame.image.load("nave3.png")
    for kb in range(20):
        spriteEnemigo3 = pygame.sprite.Sprite()
        spriteEnemigo3.image = imgEnemigo3
        spriteEnemigo3.rect = imgEnemigo3.get_rect()
        spriteEnemigo3.rect.left = randint(ANCHO // 2, ANCHO)
        spriteEnemigo3.rect.bottom = randint(0, ALTO)
        listaEnemigos3.append(spriteEnemigo3)

    # Balas
    imgBala = pygame.image.load("disco.png")
    listaBalas = []

    # Estado del juego
    estado = MENU       # Estado inicial

    # Imágenes para el menú
    imgbtnJugar = pygame.image.load("button_jugar.png")
    imgbtn1 = pygame.image.load("boton1.png")
    imgbtn2 = pygame.image.load("boton2.png")
    imgbtnFinal = pygame.image.load("botonFinal.png")

    # Imagenes para el juego
    imgFondo = pygame.image.load("Fondo.jpg")
    xFondo = 0

    # Imagen del final
    imgFINAL = pygame.image.load("FINAL.jpg")

    # Tiempo
    timer = 0   #" Acumulador de tiempo"

    # Imagen del Menu
    imgMenu = pygame.image.load("Menu.jpg")

    # Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)   # -1 Para que se repita infinito

    # Texto
    fuente = pygame.font.SysFont("monospace", 54)


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    #spritePlanta.rect.bottom -= 5
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    #spritePlanta.rect.bottom += 5
                    movimiento = ABAJO
                elif evento.key == pygame.K_RIGHT:
                    #spritePlanta.rect.left += 5
                    movimiento = DERECHA
                elif evento.key == pygame.K_LEFT:
                    #spritePlanta.rect.left -= 5
                    movimiento = IZQUIERDA
                elif evento.key == pygame.K_SPACE:   # Disparo
                    efecto.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePlanta.rect.width + spritePlanta.rect.left
                    spriteBala.rect.bottom = spritePlanta.rect.bottom + spritePlanta.rect.height//8
                    listaBalas.append(spriteBala)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO//2 - 128
                yb = ALTO//2 - 50
                anchoB = 256
                altoB = 100
                if xm>=xb and xm<=xb+anchoB and ym>=yb and ym<=yb+altoB:
                    estado = JUGANDO

        # Pregunta en qué estado esta el juego
        if estado == MENU:
            # Borrar pantalla
            ventana.blit(imgMenu, (0,0))
            ventana.blit(imgbtnJugar, (ANCHO//2-128, ALTO//2-50))
            ventana.blit(imgbtn1, (ANCHO//2-171, ALTO//2+70))
            ventana.blit(imgbtn2, (ANCHO//2-171, ALTO//2+130))
            ventana.blit(imgbtnFinal, (ANCHO//2-189, ALTO//2+190))
        elif estado == JUGANDO:
            # Actualizar objetos
            acttualizarEnemigos(listaEnemigos)
            actualizarBalas(listaBalas)
            verificarColisiones(listaBalas, listaEnemigos, puntos)
            # Disparar?????



            # Mover personaje
            if movimiento == ARRIBA:
                spritePlanta.rect.bottom-=5
            elif movimiento == ABAJO:
                spritePlanta.rect.bottom+=5
            elif movimiento == DERECHA:
                spritePlanta.rect.left+=5
            elif movimiento == IZQUIERDA:
                spritePlanta.rect.left-=5


            # Borrar pantalla
            ventana.fill(VERDE_BANDERA)
            ventana.blit(imgFondo, (xFondo,0))
            ventana.blit(imgFondo, (xFondo+800,0))    # 800 es el Ancho de la imagen
            xFondo -= 1
            if xFondo<=-800:
                xFondo = 0

            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana, spritePlanta)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)
            # Dibujar texto
            texto = fuente.render("%.3f" %timer, 1, BLANCO)
            ventana.blit(texto, (0,ALTO-54))
            textoPuntos = fuente.render("Puntos: %d" % (sum(puntos)), 1, BLANCO)
            ventana.blit(textoPuntos, (0,0))
            if sum(puntos) == 20 and timer <= 50:
                estado = FIN
            elif timer > 50 and sum(puntos) < 20:
                estado = INTENTO

        elif estado == INTENTO:
            ventana.fill(NEGRO)
            texto2 = fuente.render("Game Over tus puntos: %d" % (sum(puntos)), 1, BLANCO)
            ventana.blit(texto2, (0, ALTO // 2))
            salida = open("marcadores.txt","w",encoding="UTF-8")
            salida.write("Tu puntuación: %d puntos" % (sum(puntos)))
            salida.close()
            if timer == 70:
                estado = MENU
                timer = 0

        elif estado == FIN:
            ventana.fill(NEGRO)
            texto2 = fuente.render("Haz completado el nivel 1 en %.3f!!" % timer, 1, BLANCO)
            ventana.blit(texto2, (0, ALTO//2))
            if timer >= 55:
                estado = FIN2

        elif estado == FIN2:
            # Actualizar objetos
            actualizarEnemigos2(listaEnemigos2)
            actualizarBalas(listaBalas)
            verificarColisiones(listaBalas, listaEnemigos2, puntos)
            # Disparar?????

            # Mover personaje
            if movimiento == ARRIBA:
                spritePlanta.rect.bottom -= 5
            elif movimiento == ABAJO:
                spritePlanta.rect.bottom += 5
            elif movimiento == DERECHA:
                spritePlanta.rect.left += 5
            elif movimiento == IZQUIERDA:
                spritePlanta.rect.left -= 5

            # Borrar pantalla
            ventana.fill(VERDE_BANDERA)
            ventana.blit(imgFondo, (xFondo, 0))
            ventana.blit(imgFondo, (xFondo + 800, 0))  # 800 es el Ancho de la imagen
            xFondo -= 1
            if xFondo <= -800:
                xFondo = 0

            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana, spritePlanta)
            dibujarEnemigos2(ventana, listaEnemigos2)
            dibujarBalas(ventana, listaBalas)
            # Dibujar texto
            texto = fuente.render("%.3f" % timer, 1, BLANCO)
            ventana.blit(texto, (0, ALTO - 54))
            textoPuntos = fuente.render("Puntos: %d" % (sum(puntos)), 1, BLANCO)
            ventana.blit(textoPuntos, (0, 0))
            if timer <= 80 and sum(puntos) == 50:
                estado = FIN3
            elif timer > 80 and sum(puntos) < 50:
                estado = INTENTO

        elif estado == FIN3:
            ventana.fill(NEGRO)
            texto2 = fuente.render("Haz completado el nivel 2!!", 1, BLANCO)
            ventana.blit(texto2, (0, ALTO // 2))
            if timer >= 87:
                estado = NIVELFINAL


        elif estado == NIVELFINAL:
            # Actualizar objetos
            actualizarEnemigos3(listaEnemigos3)
            actualizarBalas(listaBalas)
            verificarColisiones(listaBalas, listaEnemigos3, puntos)
            # Disparar?????

            # Mover personaje
            if movimiento == ARRIBA:
                spritePlanta.rect.bottom -= 5
            elif movimiento == ABAJO:
                spritePlanta.rect.bottom += 5
            elif movimiento == DERECHA:
                spritePlanta.rect.left += 5
            elif movimiento == IZQUIERDA:
                spritePlanta.rect.left -= 5

            # Borrar pantalla
            ventana.fill(VERDE_BANDERA)
            ventana.blit(imgFondo, (xFondo, 0))
            ventana.blit(imgFondo, (xFondo + 800, 0))  # 800 es el Ancho de la imagen
            xFondo -= 1
            if xFondo <= -800:
                xFondo = 0

            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana, spritePlanta)
            dibujarEnemigos3(ventana, listaEnemigos3)
            dibujarBalas(ventana, listaBalas)
            # Dibujar texto
            texto = fuente.render("%.3f" % timer, 1, BLANCO)
            ventana.blit(texto, (0, ALTO - 54))
            textoPuntos = fuente.render("Puntos: %d" % (sum(puntos)), 1, BLANCO)
            ventana.blit(textoPuntos, (0, 0))
            if timer <= 97 and sum(puntos) == 65:
                estado = TERMINA
            elif timer > 97 and sum(puntos) < 65:
                estado = INTENTO


        elif estado == TERMINA:
            ventana.blit(imgFINAL, (0,0))
            texto2 = fuente.render("Felicidades!! %d Puntos" % (sum(puntos)), 1, BLANCO)
            salida = open("marcadores.txt", "w", encoding="UTF-8")
            salida.write("Tu puntuación: %d puntos" % (sum(puntos)))
            salida.close()
            ventana.blit(texto2, (0, ALTO // 2))


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/10


    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()

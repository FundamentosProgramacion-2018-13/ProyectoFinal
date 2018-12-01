# Autor: Juan Carlos Flores García, A01376511. Grupo 4.

# Descripción: Videojuego de disparos ambientado en el espacio y basado en la serie Star Trwk.


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
GAMEOVER = 3

# Estados de movimiento
QUIETO = 1
ABAJO = 2
ARRIBA = 3
IZQUIERDA = 4
DERECHA = 5


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    # VISITAR a cada elemento
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 5


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 20


def dibujarMenu(ventana, imgBtnJugar, imgLogo):
    ventana.blit(imgBtnJugar, (ANCHO//2-72.5, ALTO-200))
    ventana.blit(imgLogo, (ANCHO//2-280, ALTO//4))


def verificarColision(listaEnemigos, listaBalas):
    for k in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        for e in range(len(listaEnemigos)-1, -1, -1):   # Recorrer con INDICES
            enemigo = listaEnemigos[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                # Le pegó
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                break


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje
    imgPersonaje = pygame.image.load("Enterprise.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO // 2 + spritePersonaje.rect.height // 2

    # Enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("Klingon.png")
    for k in range(10):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
        spriteEnemigo.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteEnemigo)

    # Proyectiles/balas
    listaBalas = []
    imgBala = pygame.image.load("Phaser-1.png")

    # Menu
    imgBtnJugar = pygame.image.load("button_start.png")
    imgLogo = pygame.image.load("Logo.png")

    # Puntos
    timer = 0

    # Fondo
    imgFondo = pygame.image.load("Fondo.jpg")

    estado = MENU

    moviendo = QUIETO

    # Tiempo
    timer = 0  # Acumulador de tiempo

    # Texto
    fuente = pygame.font.SysFont("monospace", 30)

    # Audio
    pygame.mixer.init()
    pygame.mixer.music.load("STTOS.mp3")
    pygame.mixer.music.play(-1)
    efecto = pygame.mixer.Sound("shoot.wav")


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    # spritePersonaje.rect.bottom -= 5
                    moviendo = ARRIBA

                elif evento.key == pygame.K_DOWN:
                    # spritePersonaje.rect.bottom += 5
                    moviendo = ABAJO

                elif evento.key == pygame.K_LEFT:
                    moviendo = IZQUIERDA

                elif evento.key == pygame.K_RIGHT:
                    moviendo = DERECHA

                elif evento.key == pygame.K_z:
                    # Crear una bala
                    efecto.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalas.append(spriteBala)
                    # ENEMIGO
                    spriteEnemigo = pygame.sprite.Sprite()
                    spriteEnemigo.image = imgEnemigo
                    spriteEnemigo.rect = imgEnemigo.get_rect()
                    spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
                    spriteEnemigo.rect.bottom = randint(0, ALTO)
                    listaEnemigos.append(spriteEnemigo)
            elif evento.type == pygame.KEYUP:
                moviendo = QUIETO

            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm, ",", ym)
                # Preguntar si soltó el mouse dentro del botón
                xb = ANCHO//2-72.5
                yb = ALTO - 200
                if xm > xb and xm <= xb+145 and ym >= yb and ym <= yb+56:
                    pygame.mixer.stop()
                    estado = JUGANDO
                    pygame.mixer.init()
                    pygame.mixer.music.load("Beyond.mp3")
                    pygame.mixer.music.play(-1)


        # Borrar pantalla
        ventana.fill(NEGRO)


        if estado == JUGANDO:

            if moviendo == ARRIBA:
                spritePersonaje.rect.bottom -= 5
            elif moviendo == ABAJO:
                spritePersonaje.rect.bottom += 5
            elif moviendo == IZQUIERDA:
                spritePersonaje.rect.left -= 5
            elif moviendo == DERECHA:
                spritePersonaje.rect.right += 5

            # Tiempo
            if timer <= 2:
                timer = 0
                # Crear una bala
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                spriteBala.rect.bottom = spritePersonaje.rect.bottom
                listaBalas.append(spriteBala)
            # Actualizar enemigos
            moverEnemigos(listaEnemigos)
            moverBalas(listaBalas)
            verificarColision(listaEnemigos, listaBalas)

            # Dibujar, aquí haces todos los trazos que requieras
            # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
            # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
            ventana.blit(imgFondo, (0, 0))
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)

        elif estado == MENU:
            # Dibujar menu
            dibujarMenu(ventana, imgBtnJugar, imgLogo)
           

            # Música del menu


            # Texto en la pantalla
            # texto = fuente.render("Valor de xFondo %d" % xFondo, 1, BLANCO)
            # ventana.blit(texto, (ANCHO // 2 - 100, 50))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(60)  # 40 fps
        timer += 1/20
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamada a la función principal
main()


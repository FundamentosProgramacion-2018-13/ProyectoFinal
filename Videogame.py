# Autor: Ivan Honc Ayón
# Descripción: Shooter 2D que consiste en defender una base. Desarrollado en pygame.


import time
import pygame  # Librería de pygame
from random import randint


# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

# Estado
MENU = 1
JUGANDO = 2
CONTROLES = 3

# Movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
DERECHA = 4
IZQUIERDA = 5

# Vida
VIDA = 5000


# Función que dibuja al personaje del jugador.
def dibujarPersonaje(ventana, spritePlanta):
    ventana.blit(spritePlanta.image, spritePlanta.rect)


# Función para dibujar todos los Elites de la lista que recibe.
def dibujarElites(ventana, listaElites):
    for enemigo in listaElites:
        ventana.blit(enemigo.image, enemigo.rect)


# Función para dibujar todos los Grunts de la lista que recibe.
def dibujarGrunts(ventana, listaGrunts):
    for enemigo in listaGrunts:
        ventana.blit(enemigo.image, enemigo.rect)


# Función que actualiza a los Elites de la lista que recibe.
def actualizarElites(listaElites):
    for enemigo in listaElites:
        enemigo.rect.left -= 1


# Función para dibujar las balas del jugador.
def dibujarBullet(ventana, listaBullet, contRecarga, sonidoRecarga):
    for bullet in listaBullet:
        if contRecarga == 0:
            sonidoRecarga.play()
        if contRecarga > 0:
            ventana.blit(bullet.image, bullet.rect)


# Función para dibujar las balas de los enemigos.
def dibujarPlasma(ventana, listaPlasma, sonidoPlasma):
    for plasma in listaPlasma:
        # sonidoPlasma.play()
        ventana.blit(plasma.image, plasma.rect)


# Función para dibujar actualizar las balas del jugador.
def actualizarBullet(listaBullet):
    for bullet in listaBullet:
        bullet.rect.right += 8


# Función para actualizar las balas del enemigo.
def actualizarPlasma(listaPlasma):
    for plasma in listaPlasma:
        plasma.rect.right -= 5


# Función para verificar que las balas le den a los enemigos.
def verificarColisiones(listaBullet, listaElites, listaGrunts):
    for k in range(len(listaBullet) - 1, -1, -1):
        bullet = listaBullet[k]
        borrarBullet = False
        for Elites in range(len(listaElites) - 1, -1, -1):
            enemigo = listaElites[Elites]

            xBullet = bullet.rect.left
            yBullet = bullet.rect.bottom
            xCordElite, yCordElite, anchoEnemigo, altoEnemigo = enemigo.rect

            if xCordElite <= xBullet <= xCordElite + anchoEnemigo and yCordElite <= yBullet <= yCordElite + altoEnemigo:
                listaElites.remove(enemigo)
                borrarBullet = True
                break
        for Grunts in range(len(listaGrunts) - 1, -1, -1):
            enemigo2 = listaGrunts[Grunts]

            xBullet = bullet.rect.left
            yBullet = bullet.rect.bottom
            xCordGrunt, yCordGrunt, anchoGrunt, altoGrunt = enemigo2.rect
            if xCordGrunt <= xBullet <= xCordGrunt + anchoGrunt and yCordGrunt <= yBullet <= yCordGrunt + altoGrunt:
                listaGrunts.remove(enemigo2)
                borrarBullet = True
                break
        if borrarBullet:
            listaBullet.remove(bullet)


# Función para verificar que las balas de los enemigos le den al jugador.
def verificarDanoPlasma(listaPlasma, spriteCarter):
    for k in range(len(listaPlasma) - 1, -1, -1):
        plasma = listaPlasma[k]
        borrarPlasma = False
        xPlasma = plasma.rect.left
        yPlasma = plasma.rect.bottom
        xCordCarter, yCordCarter, anchoPersonaje, altoPersonaje = spriteCarter.rect
        if xCordCarter + anchoPersonaje >= xPlasma >= xCordCarter and yCordCarter <= yPlasma <= yCordCarter + altoPersonaje:
            global VIDA
            VIDA -= 250
            borrarPlasma = True
        if borrarPlasma:
            listaPlasma.remove(plasma)


# Función para verificar que los enemigos lleguen a la base.
def verificarAtaques(listaElites):
    for Elites in range(len(listaElites)-1, -1, -1):
        enemigo = listaElites[Elites]
        xCordElite, yCordElite, anchoEnemigo, altoEnemigo = enemigo.rect
        if xCordElite <= -70:
            listaElites.remove(enemigo)
            global VIDA
            VIDA -= 500


# Función encargada de dibujar el juego.
def dibujar():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    # Personaje principal.
    imgCarter = pygame.image.load("Carter.png")
    spriteCarter = pygame.sprite.Sprite()
    spriteCarter.image = imgCarter
    spriteCarter.rect = imgCarter.get_rect()
    spriteCarter.rect.left = ANCHO // 5 + spriteCarter.rect.height // 2
    spriteCarter.rect.bottom = ALTO // 2 + spriteCarter.rect.height // 2
    movimiento = QUIETO

    # Enemigos Elite.
    listaElites = []
    imgElite = pygame.image.load("Elite.png")
    for k in range(20):
        spriteElite = pygame.sprite.Sprite()
        spriteElite.image = imgElite
        spriteElite.rect = imgElite.get_rect()
        spriteElite.rect.left = randint(ANCHO // 2, ANCHO)
        spriteElite.rect.bottom = randint(120, ALTO-5)
        listaElites.append(spriteElite)

    # Enemigos Grunt.
    listaGrunts = []  # Lista vacía de Grunts.
    imgGrunt = pygame.image.load("Grunt.png")
    for gg in range(3):
        spriteGrunt = pygame.sprite.Sprite()
        spriteGrunt.image = imgGrunt
        spriteGrunt.rect = imgGrunt.get_rect()
        spriteGrunt.rect.left = randint((ANCHO // 2) + 70, ANCHO-70)
        spriteGrunt.rect.bottom = randint(100, ALTO-20)
        listaGrunts.append(spriteGrunt)

    # Municiones.
    imgBullet = pygame.image.load("Bullet.png")
    listaBullet = []
    contRecargar = 30
    imgPlasma = pygame.image.load("Plasma.png")
    listaPlasma = []

    # Estado inicial: Comienza con el menú.
    estado = MENU

    # Multimedia del menú.
    imgBtnJugar = pygame.image.load("Jugar.png")
    imgBtnRegresar = pygame.image.load("Regresar.png")
    imgBtnControles = pygame.image.load("Controles.png")

    # Fondo del juego.
    imgFondo = pygame.image.load("Background.jpg")
    ubicacionFondo = 0

    # Audio.
    pygame.mixer.init()
    sonidoDisparo = pygame.mixer.Sound("Shooting.ogg")
    sonidoRecarga = pygame.mixer.Sound("Reload.ogg")
    sonidoPlasma = pygame.mixer.Sound("Plasma.ogg")
    pygame.mixer.music.load("Halo.mp3")
    pygame.mixer.music.play(-1)

    # Tiempos.
    tiempoVida = 0
    tiempoDisparo = 0
    tiempoUniversal = 0
    tiempoGrunt = 0

    # Fuente de texto del juego.
    fuenteTexto1 = pygame.font.SysFont("monospace", 20)
    fuenteTexto2 = pygame.font.SysFont("monospace", 40)
    fuenteTexto3 = pygame.font.SysFont("monospace", 30)

    # Ciclo principal que refresca los frames del juego.
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    movimiento = ABAJO
                elif evento.key == pygame.K_LEFT:
                    movimiento = IZQUIERDA
                elif evento.key == pygame.K_RIGHT:
                    movimiento = DERECHA
                elif evento.key == pygame.K_SPACE:
                    contRecargar -= 1
                    sonidoDisparo.play()
                    spriteBullet = pygame.sprite.Sprite()
                    spriteBullet.image = imgBullet
                    spriteBullet.rect = imgBullet.get_rect()
                    spriteBullet.rect.left = spriteCarter.rect.left + spriteCarter.rect.width
                    spriteBullet.rect.bottom = spriteCarter.rect.bottom - spriteCarter.rect.height // 2 - 30
                    listaBullet.append(spriteBullet)

            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    movimiento = QUIETO
                elif evento.key == pygame.K_DOWN:
                    movimiento = QUIETO
                elif evento.key == pygame.K_LEFT:
                    movimiento = QUIETO
                elif evento.key == pygame.K_RIGHT:
                    movimiento = QUIETO

            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO // 2 - 127
                yb = ALTO // 2 - 150
                xb2 = ANCHO // 2 - 127
                yb2 = ALTO // 2
                xb3 = ANCHO // 2 - 127
                yb3 = ALTO // 2 + 100
                anchoBoton = 258
                altoBoton = 100
                if xb <= xm <= xb + anchoBoton and yb <= ym <= yb + altoBoton:
                    estado = JUGANDO
                elif xb2 <= xm <= xb2 + anchoBoton and yb2 <= ym <= yb2 + altoBoton:
                    estado = CONTROLES
                elif xb3 <= xm <= xb3 + anchoBoton and yb3 <= ym <= yb3 + altoBoton:
                    estado = MENU

        if estado == MENU:
            ventana.fill(ROJO)
            ventana.blit(imgBtnJugar, (ANCHO // 2 - 100, ALTO // 2 - 150))
            ventana.blit(imgBtnControles, (ANCHO // 2 - 130, ALTO // 2))

        elif estado == CONTROLES:
            ventana.fill(NEGRO)
            controles1 = fuenteTexto1.render("Instrucciones", 1, BLANCO)
            controles2 = fuenteTexto1.render("Flechas para mover.", 1, BLANCO)
            controles3 = fuenteTexto1.render("Espacio para disparar.", 1, BLANCO)
            controles4 = fuenteTexto1.render("Espacio x4 cuando ya no hay balas para recargar.", 1, BLANCO)
            controles5 = fuenteTexto1.render("Los Elite hacen 500 de daño cuando llegan a la base", 1, BLANCO)
            controles6 = fuenteTexto1.render("Los Grunts hacen 250 de daño si le dan al jugador.", 1, BLANCO)
            ventana.blit(controles1, (300, 100))
            ventana.blit(controles2, (100, 150))
            ventana.blit(controles3, (100, 200))
            ventana.blit(controles4, (100, 250))
            ventana.blit(controles5, (100, 300))
            ventana.blit(controles6, (100, 350))
            ventana.blit(imgBtnRegresar, (ANCHO // 2 - 100, ALTO // 2 + 100))

        elif estado == JUGANDO:
            actualizarElites(listaElites)
            actualizarBullet(listaBullet)
            actualizarPlasma(listaPlasma)
            verificarColisiones(listaBullet, listaElites, listaGrunts)
            verificarDanoPlasma(listaPlasma, spriteCarter)
            verificarAtaques(listaElites)

            # Reaparición de enemigos:
            if tiempoVida >= 10:
                tiempoVida = 0
                for kk in range(30):
                    spriteElite = pygame.sprite.Sprite()
                    spriteElite.image = imgElite
                    spriteElite.rect = imgElite.get_rect()
                    spriteElite.rect.left = randint(ANCHO // 2, ANCHO)
                    spriteElite.rect.bottom = randint(100, ALTO-5)
                    listaElites.append(spriteElite)

            if tiempoGrunt >= 5:
                tiempoGrunt = 0
                for ggg in range(2):
                    spriteGrunt = pygame.sprite.Sprite()
                    spriteGrunt.image = imgGrunt
                    spriteGrunt.rect = imgGrunt.get_rect()
                    spriteGrunt.rect.left = randint((ANCHO // 2) + 70, ANCHO - 70)
                    spriteGrunt.rect.bottom = randint(100, ALTO - 20)
                    listaGrunts.append(spriteGrunt)

            if len(listaGrunts) > 0:
                if tiempoDisparo >= 3:
                    tiempoDisparo = 0
                    # sonidoPlasma.play()
                    for Grunts in range(len(listaGrunts)-1, -1, -1):
                        enemigo = listaGrunts[Grunts]
                        spritePlasma = pygame.sprite.Sprite()
                        spritePlasma.image = imgPlasma
                        spritePlasma.rect = imgPlasma.get_rect()
                        spritePlasma.rect.left = enemigo.rect.left
                        spritePlasma.rect.bottom = enemigo.rect.bottom - enemigo.rect.height // 2 + 10
                        listaPlasma.append(spritePlasma)

            # Movimiento del personaje jugable.
            if movimiento == ARRIBA:
                spriteCarter.rect.bottom -= 5
            elif movimiento == ABAJO:
                spriteCarter.rect.bottom += 5
            elif movimiento == DERECHA:
                spriteCarter.rect.left += 5
            elif movimiento == IZQUIERDA:
                spriteCarter.rect.left -= 5


            ventana.fill(NEGRO)
            ventana.blit(imgFondo, (ubicacionFondo, 0))
            ventana.blit(imgFondo, (ubicacionFondo + 1024, 0))
            ubicacionFondo -= 5
            if ubicacionFondo <= -1024:
                ubicacionFondo = 0

            dibujarPersonaje(ventana, spriteCarter)
            dibujarElites(ventana, listaElites)
            dibujarBullet(ventana, listaBullet, contRecargar, sonidoRecarga)
            dibujarGrunts(ventana, listaGrunts)
            dibujarPlasma(ventana, listaPlasma, sonidoPlasma)

            # Dibujar texto
            texto = fuenteTexto1.render('Tiempo: %.3f' % tiempoUniversal, 1, NEGRO)
            if contRecargar <= -4:
                contRecargar = 30
            if contRecargar >= 0:
                textoBalas = fuenteTexto1.render("Municiones: %i" % contRecargar, 1, ROJO)
            textoVida = fuenteTexto2.render("Vida: %i" % VIDA, 1, ROJO)
            ventana.blit(texto, (200, 30))
            ventana.blit(textoBalas, (200, 50))
            ventana.blit(textoVida, (200, 80))
            if VIDA <= 0:
                textoFinal = fuenteTexto3.render("¡¡¡HAS PERDIDO!!! Duraste: %.3f segundos" % tiempoUniversal, 1, ROJO)
                ventana.blit(textoFinal, (20, 200))
                salida = open("Puntaje.txt", "w")
                salida.write("Tiempo más alto al que se ha llegado: %.3f segundos" % tiempoUniversal)
                salida.close()
                termina = True

        pygame.display.flip()
        reloj.tick(40)  # 40 fps
        tiempoVida += 1 / 40
        tiempoDisparo += 1 / 40
        tiempoGrunt += 1 / 40
        tiempoUniversal += 1/40

    # Después del ciclo principal
    time.sleep(7)
    pygame.quit()


# Función principal que manda llamar a la funció de dibujo.
def main():
    dibujar()


main()

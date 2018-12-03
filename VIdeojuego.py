# Autor: Ithan Alexis Perez Sanchez
# Matricula: A01377717
# Descripcion: Proyecto Videojuego

# El codigo empieza después de esta linea

import pygame
import random

puntos = 0
restantes = 0
restantes2 = 0

# Colores

Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Verde = (0, 255, 0)
Turquesa = (0, 133, 104)

# Dimensiones de la pantalla

Ancho = 800
Alto = 600

# Estados

Menu = 1
Jugar = 2
Puntuaje = 3

# Estados de movimiento

Quieto = 1
Derecha = 2
Izquierda = 3
Findejuego = 4
Ganaste = 5


def dibujarPersonaje(ventana, spriteNave):
    ventana.blit(spriteNave.image, spriteNave.rect)


def dibujarEnemigo(ventana, listaEnemigos):
    for Enemigo in listaEnemigos:
        ventana.blit(Enemigo.image, Enemigo.rect)


def actualizarEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.bottom += 2

        if enemigo.rect.bottom <= 1000:
            pass
        else:
            break
        xe, ye, anchoe, altoe = enemigo.rect
        if ye + altoe <= 0:
            return True



def dibujarAmmo(ventana, listaAmmo):
    for Ammo in listaAmmo:
        ventana.blit(Ammo.image, Ammo.rect)


def actualizarAmmo(listaAmmo):
    for Ammo in listaAmmo:
        Ammo.rect.bottom -= 15


def verificarColisiones(listaAmmo, listaEnemigos):
    global restantes
    global restantes2
    global puntos
    SUN = False
    for k in range(len(listaAmmo) - 1, -1, -1):
        bala = listaAmmo[k]
        for e in range(len(listaEnemigos) - 1, -1, -1):
            enemigo = listaEnemigos[e]
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, anchoe, altoe = enemigo.rect
            if xe <= xb <= xe + anchoe and ye >= yb >= ye - altoe:
                listaEnemigos.remove(enemigo)
                puntos += 10
                restantes -= 1
                restantes2 = 0
                SUN = True
                break
        if SUN:
            listaAmmo.remove(bala)
            return True


def Puntuacion():
    puntuaje = open("Puntuacion.txt", "r+")
    lista = []
    listas = puntuaje.readlines()
    for linea in listas:
        lista.append(int(linea.replace("\n", " ")))
    puntuaje.close()
    return lista


def losmejores():
    mejores = Puntuacion()

    mejores.append(puntos)
    mejores.sort(reverse=True)

    salida = open("Los_mejores_5.txt", "w")
    for puesto in range(0, 6):
        salida.write(str(mejores[puesto]) + "\n")
    salida.close()


def dibujar():
    global restantes
    global restantes2
    pygame.init()
    ventana = pygame.display.set_mode((Ancho, Alto))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje Principal
    imgNave = pygame.image.load("Nave.png")
    spriteNave = pygame.sprite.Sprite()
    spriteNave.image = imgNave
    spriteNave.rect = imgNave.get_rect()
    spriteNave.rect.left = Ancho // 2 - spriteNave.rect.width // 2
    spriteNave.rect.bottom = Alto - spriteNave.rect.height + 40

    movimiento = Quieto

    # Enemigos

    listaEnemigos = []
    imgEnemigo = pygame.image.load("Enemy.png")
    for k in range(20):
        spriteEnemy = pygame.sprite.Sprite()
        spriteEnemy.image = imgEnemigo
        spriteEnemy.rect = imgEnemigo.get_rect()
        spriteEnemy.rect.left = random.randrange(0, Ancho - spriteEnemy.rect.width - 10)
        spriteEnemy.rect.bottom = 0 - spriteEnemy.rect.height - 40
        listaEnemigos.append(spriteEnemy)

    restantes = len(listaEnemigos)

    # Munición
    imgAmmo = pygame.image.load("Sun.png")
    listaAmmo = []

    # Estado del juego
    estado = Menu

    # Imagenes para el menu
    imgBtJugar = pygame.image.load("button_jugar.png")
    imgBtPuntuaje = pygame.image.load("button_puntuaje.png")

    # Imagenes para la puntuacion
    imgBtPosicion = pygame.image.load("button_posicion.png")
    imgBtPuntos = pygame.image.load("button_puntos.png")

    # Imagenes para el juego
    imgFondo = pygame.image.load("Espacio.jpg")
    yFondo = 0

    # Fuentes
    Fuente = pygame.font.SysFont("comicsansms", 30)

    # Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("SUN.mp3")
    pygame.mixer.music.play()

    # Tiempo
    timer = 0

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_RIGHT:
                    movimiento = Derecha
                if evento.key == pygame.K_LEFT:
                    movimiento = Izquierda
                if evento.key == pygame.K_SPACE:
                    efecto.play()
                    spriteAmmo = pygame.sprite.Sprite()
                    spriteAmmo.image = imgAmmo
                    spriteAmmo.rect = imgAmmo.get_rect()
                    spriteAmmo.rect.left = spriteNave.rect.left + 20
                    spriteAmmo.rect.bottom = spriteNave.rect.top
                    listaAmmo.append(spriteAmmo)

            if evento.type == pygame.KEYUP:
                movimiento = Quieto

            if evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xm2, ym2 = pygame.mouse.get_pos()
                xm3, ym3 = pygame.mouse.get_pos()
                xb3 = 600
                yb3 = Alto // 2 - 40
                xb2 = Ancho // 2 - 80
                yb2 = Alto // 2 + 40
                xb = Ancho // 2 - 80
                yb = Alto // 2 - 40
                anchoB = 160
                altoB = 80
                anchoC = 200
                altoC = 160
                altoD = 80
                anchoD = 160

                if xb <= xm <= xb + anchoB and yb <= ym <= yb + altoB:
                    estado = Jugar
                if xb2 <= xm2 <= xb2 + anchoC and yb2 <= ym2 <= yb2 + altoC:
                    estado = Puntuaje
                if xb3 <= xm3 <= xb3 + anchoD and yb3 <= ym3 <= yb3 + altoD:
                    estado = Jugar

        # Pregunta en que estado está el juego
        if estado == Menu:
            ventana.fill(Negro)
            texto4 = Fuente.render("Galaxy Wars", 0, Blanco)
            ventana.blit(texto4, (Ancho // 2 - 80, Alto - 450))
            ventana.blit(imgBtJugar, (Ancho // 2 - 80, Alto // 2 - 40))
            ventana.blit(imgBtPuntuaje, (Ancho // 2 - 80, Alto // 2 + 40))
        elif estado == Puntuaje:
            ventana.fill(Negro)
            ventana.blit(imgBtPosicion, (0, 0))
            ventana.blit(imgBtPuntos, (200, 0))
            ventana.blit(imgBtJugar, (600, Alto // 2 - 40))
        elif estado == Jugar:

            # Actualizar objetos
            actualizarAmmo(listaAmmo)
            actualizarEnemigos(listaEnemigos)
            verificarColisiones(listaAmmo, listaEnemigos)

            # Movimiento
            if movimiento == Derecha and spriteNave.rect.left < 750:
                spriteNave.rect.left += 10
            elif movimiento == Izquierda and spriteNave.rect.left > 0:
                spriteNave.rect.left -= 10


            # Borrar pantalla

            ventana.fill(Negro)
            ventana.blit(imgFondo, (-100, yFondo))
            ventana.blit(imgFondo, (-100, yFondo - 1080))
            yFondo += 5
            if yFondo >= 1080:
                yFondo = 1

            # Dibujar, aqui haces todos los trazos que haremos
            dibujarPersonaje(ventana, spriteNave)
            dibujarAmmo(ventana, listaAmmo)
            dibujarEnemigo(ventana, listaEnemigos)

            # Puntuacion()

            # Mostrar texto
            texto = Fuente.render("Tiempo: %.2f" % timer, 0, Blanco)
            ventana.blit(texto, (Alto, Ancho - 700))
            texto2 = Fuente.render("Puntuación: %.2f" % puntos, 0, Blanco)
            ventana.blit(texto2, (Alto - 600, Ancho - 700))

            if restantes == 0:
                estado = Ganaste

            if restantes == 1:
                estado = Findejuego

        if estado == Ganaste:
            texto4 = Fuente.render("Ganaste", 0, Blanco)
            ventana.blit(texto4, (Alto // 2, Ancho // 2))
        else:
            if estado == Findejuego:
                texto3 = Fuente.render("Game Over", 0, Blanco)
                ventana.blit(texto3, (Ancho // 2, Alto // 2))

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        timer += 1 / 30
        reloj.tick(120)  # 120 fps

        # Después del ciclo principal

    pygame.quit()  # termina pygame


def main():
    dibujar()


main()

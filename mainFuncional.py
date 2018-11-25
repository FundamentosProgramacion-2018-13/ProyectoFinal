# encoding: UTF-8
# Autor: Diego Palmerín Bonada, A01747290
# Descripción: Main

import pygame
import random
from timeit import default_timer as timer

pygame.init()
pygame.mixer.init(44100, 16, 4, 8192)

settingstxt = open("settings.txt", "r+")
record = float(settingstxt.readlines()[len(settingstxt.readlines())-1])

# Colores
BLANCO = (249, 249, 249)
ROJO = (210, 77, 76)
AZUL = (9, 44, 116)
NARANJA = (253, 107, 53)
NEGRO = (40, 40, 40)

# Imágenes
imgJugador = pygame.image.load("Jugador.png")
imgCocheAzul = pygame.image.load("CocheAzul.png")
imgCocheRojo = pygame.image.load("CocheRojo.png")
imgCocheNegro = pygame.image.load("CocheNegro.png")
imgCocheAmarillo = pygame.image.load("CocheAmarillo.png")
imgCoches = [imgCocheAmarillo, imgCocheAzul, imgCocheNegro, imgCocheRojo]
imgFondoJuego = pygame.image.load("FondoJuego.png")
imgFondoMain = pygame.image.load("FondoMain.png")
imgArbol = pygame.image.load("Arbol.png")
imgIcono = pygame.image.load("Icono.png")
imgGracias = pygame.image.load("Gracias.gif")

# Sonidos
cancionFondo = pygame.mixer.Sound('Cancion.wav')
MotorSFX = pygame.mixer.Sound('EngineStart.wav')
crashSFX = pygame.mixer.Sound('Crash.wav')
cornetaSFX = pygame.mixer.Sound('Corneta.wav')
skidSFX = pygame.mixer.Sound('Skid.wav')

Ancho = 800
Alto = 600

win = pygame.display.set_mode((Ancho, Alto))

reloj = pygame.time.Clock()

pygame.display.set_caption("Periferico Simulator 2018")
pygame.display.set_icon(imgIcono)

# Alineaciones
posicionarx: int = Ancho // 4
posicionary: int = Alto // 4

# Texto
pygame.font.init()
myfont = pygame.font.SysFont('Helvetica', 25, True, True)

# Elementos
botones = []
coches = []
extras = []
jugador = (Ancho//2, Alto-posicionary - 50, imgJugador)

# Variables internas
score = 0.
startTime = 0
menuActual = 0
musica = False

dibujado = False


# Coches
def crearCoches():
    global posicionarx
    coches.append(((280 + 135 * random.randint(0, 2)), -250, imgCoches[random.randint(0, len(imgCoches)-1)]))


def dibujarCoches():
    global coches, jugador
    for coche in coches:
        x, y, imgCoche = coche
        if y >= 0:
            win.blit(imgCoche, (x, y))

    xp_, yp_, imgp_ = jugador
    win.blit(imgp_, (xp_, yp_))


# Botones
def crearBoton(x: int, y: int, w: int, h: int, text: str, color: tuple, funcion: int):
    botones.append((x, y, w, h, text, color, funcion))


def reproducirSonido(sonidoFX):
    global musica
    if musica:
        pygame.mixer.Sound.play(sonidoFX)


"""
0 = x
1 = y
2 = w
3 = h
4 = text
5 = color
6 = funcion
"""


def dibujarBotones():
    global botones

    for boton_ in botones:
        x, y, w, h, text, color, funcion = boton_
        pygame.draw.rect(win, color, (x, y, w, h))
        textsurface = myfont.render(text, 1, BLANCO)
        win.blit(textsurface, (x + w // 2 - len(text)/1.2 * 5, y + h // 3))


def llamarFuncion(fun: int):
    global menuActual, dibujado, musica, startTime, run
    reproducirSonido(cornetaSFX)

    # Juego
    if fun == 0:
        dibujado = False
        botones.clear()
        startTime = timer()
        menuActual = 1
        reproducirSonido(MotorSFX)

    # Salir
    if fun == 1:
        global run
        run = False

    # Creditos
    if fun == 2:
        dibujado = False
        botones.clear()
        menuActual = 2

    # Puntuaciones
    if fun == 3:
        dibujado = False
        botones.clear()
        menuActual = 0

    # Sonido
    if fun == 4:
        if not musica:
            musica = True
            reproducirSonido(cancionFondo)
        else:
            musica = False


# Lineas de la calle
def crearLineas():
    extras.append((370, 0, 0))
    extras.append((500, 0, 0))


def crearArboles():
    extras.append((625, 0, 1))


def dibujarExtras():
    global extras
    for dibujaEsto in extras:
        xextra, yextra, tipoExtra = dibujaEsto
        if tipoExtra == 0:
            pygame.draw.rect(win, BLANCO, (xextra, yextra, 7, 80))
        if tipoExtra == 1:
            win.blit(imgArbol, (xextra, yextra))


# Menus
def mainMenu():
    global dibujado
    if not dibujado:
        win.fill(NEGRO)
        botones.clear()
        crearBoton(posicionarx // 2 * 7, posicionary - 50, posicionarx // 2, posicionary // 2, "Musik", NEGRO, 4)
        crearBoton(posicionarx, posicionary - 50, posicionarx * 2, posicionary // 2, "Jugar", NARANJA, 0)
        crearBoton(posicionarx, posicionary * 2 - 50, posicionarx * 2, posicionary // 2, "Creditos", AZUL, 2)
        crearBoton(posicionarx, posicionary * 3 - 50, posicionarx * 2, posicionary // 2, "Salir", ROJO, 1)
        dibujado = True


contadorJuego = 0


def iniciarJuego():
    global reloj, score, contadorJuego, startTime

    if contadorJuego % 12 == 0:
        crearLineas()

    if contadorJuego % 20 == 0:
        crearArboles()

    if contadorJuego % 40 == 0:
        crearCoches()

    if contadorJuego == 60:
        contadorJuego = 0

    contadorJuego += 1
    currentTime = timer()
    score = currentTime-startTime


def mostrarCreditos():
    global dibujado
    if not dibujado:
        botones.clear()
        crearBoton(posicionarx, posicionary//2, posicionarx * 2, posicionary // 2, "Juego por", AZUL, -1)
        crearBoton(posicionarx, posicionary, posicionarx * 2, posicionary // 2, "Diego Palmerin", AZUL, -1)
        crearBoton(posicionarx, posicionary // 2 * 3, posicionarx * 2, posicionary // 2, "A01747290", AZUL, -1)
        crearBoton(posicionarx // 2 * 3, posicionary // 2 * 4, posicionarx, posicionary // 2, "Menu Principal", ROJO, 3)
        dibujado = True


def mostrarPuntuaciones():
    global dibujado, score, record
    if not dibujado:
        reproducirSonido(crashSFX)
        if score > record:
            record = score
            settingstxt.write("%.2f" % score+"\n")
        botones.clear()
        crearBoton(posicionarx // 2 * 7, posicionary - 50, posicionarx // 2, posicionary // 2, "Musik", NEGRO, 4)
        crearBoton(posicionarx, posicionary//2, posicionarx * 2, posicionary // 2, "Uksi, Chochaste", NARANJA, -1)
        crearBoton(posicionarx, posicionary, posicionarx * 2, posicionary // 2, "Record: %.2f s" % record, NEGRO, -1)
        crearBoton(posicionarx, posicionary + posicionary // 2, posicionarx * 2, posicionary // 2, "Puntuación: ", AZUL, -1)
        crearBoton(posicionarx, posicionary // 2 * 4, posicionarx * 2, posicionary // 2, "%.2f s" % score, AZUL, -1)
        crearBoton(posicionarx, posicionary // 2 * 5, posicionarx * 2, posicionary // 2, "Volver a Jugar", NARANJA, 0)
        crearBoton(posicionarx // 2 * 3, posicionary // 2 * 6, posicionarx, posicionary // 2, "Menu Principal", ROJO, 3)
        dibujado = True


def mainDibujar():
    win.fill(NEGRO)
    if menuActual == 1:
        win.blit(imgFondoJuego, (0, 0))
        dibujarExtras()
        dibujarCoches()
        scoreText = myfont.render("%.2f s" % score, 1, BLANCO)
        scoreTag = myfont.render("Puntaje:", 1, BLANCO)
        pygame.draw.rect(win, AZUL, (20, 20, 100, 60))
        win.blit(scoreText, (20 + 4 * 2, 50))
        win.blit(scoreTag, (20 + 4 * 2, 30))
    elif menuActual == 2:
        win.blit(imgFondoMain, (0, 0))
        win.blit(imgGracias, (Ancho//2 - 230, 350))
    else:
        win.blit(imgFondoMain, (0, 0))
    dibujarBotones()

    pygame.display.update()


run = True
reproducirSonido(cancionFondo)

while run:
    reloj.tick(60)

    if menuActual == 0:
        mainMenu()

    if menuActual == 1:
        iniciarJuego()
        for n in range(len(coches)-1, -1, -1):
            x, y, img = coches[n]
            xp, yp, imgp = jugador
            y += 10

            if (xp < 238) or (xp+75 > 670):
                menuActual = 3
                jugador = (Ancho // 2, yp, imgp)
                coches.clear()
                extras.clear()
                break

            if ((Alto - posicionary <= y <= Alto) or (Alto - posicionary <= y + 150 <= Alto)) and (
                    (xp <= x <= (xp + 75)) or (xp <= x + 65 <= (xp + 75))):
                menuActual = 3
                jugador = (Ancho // 2, yp, imgp)
                coches.clear()
                extras.clear()
                break
            else:
                if y > Alto:
                    coches.remove(coches[n])
                    break
                else:
                    coches[n] = (x, y, img)

        for n in range(len(extras) - 1, -1, -1):
            xextra, yextra, tipoExtra = extras[n]
            yextra += 30
            if yextra > Alto:
                extras.pop(n)
            else:
                extras[n] = (xextra, yextra, tipoExtra)

    if menuActual == 2:
        mostrarCreditos()

    if menuActual == 3:
        mostrarPuntuaciones()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            for boton in botones:
                posx, posy = pos
                x, y, w, h, text, color, funcion = boton
                if x <= posx <= (x + w) and y <= posy <= (y + h):
                    llamarFuncion(funcion)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_ESCAPE]:
        llamarFuncion(1)

    if keys[pygame.K_LEFT] and menuActual == 1:
        xp, yp, imgp = jugador
        if xp - 20 > 0:
            reproducirSonido(skidSFX)
            xp -= 15
        jugador = (xp, yp, imgp)

    if keys[pygame.K_RIGHT] and menuActual == 1:
        xp, yp, imgp = jugador
        reproducirSonido(skidSFX)
        if xp + 95 < Ancho:
            xp += 15
        jugador = (xp, yp, imgp)

    if keys[pygame.K_SPACE] and menuActual == 3:
        llamarFuncion(0)

    mainDibujar()
settingstxt.close()
pygame.mixer.quit()
pygame.quit()

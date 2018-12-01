# El anibals


import pygame
import math
from random import randint as random
import os


ANCHO = 800
ALTO = 600
# Colores
NEGRO= (0,0,0)
BLANCO = (248, 248, 248)
VERDE = (27, 94, 32)
ROJO = (248, 30, 30)
AZUL = (38, 38, 248)
MENU=1
JUGANDO=2
# Archivo Highscore
archivo = open("record.txt", "r+")
record = int(archivo.readlines()[len(archivo.readlines())-1])
fondo=pygame.image.load("menu.png")
# Inicializa el motor de pygame
pygame.init()



# Crea una ventana de ANCHO x ALTO
ventana = pygame.display.set_mode((ANCHO, ALTO))
reloj = pygame.time.Clock()
termina = False
# Texto
pygame.font.init()
fuente = pygame.font.SysFont("Helvetica", 40)

#PERSONAJE PRINCIPAL
PersonajePrincipal = (400, 300)

pygame.mixer.init()
pygame.mixer.music.load("kevin-macleod-scheming-weasel-faster-version.mp3")
pygame.mixer.music.play(-1)  # -1 para reproducción infninita

#CAÑON
Canon = ((400, 300), 0)

#CARGAR BALA
listaBala = []

#ENEMIGOS
listaEnemigos = []
vertices = 32
r = 400
d = ANCHO // 2
Puntos = []
for n in range(1, vertices + 1):
    Puntos.append((d + (r * math.cos(n)), d + (r * math.sin(n))))

score = 0


def dibujarPersonaje():
    global PersonajePrincipal
    pos = PersonajePrincipal
    pygame.draw.circle(ventana, ROJO, pos, 60)


def moverCanon():
    global Canon
    xm, ym = pygame.mouse.get_pos()

    if xm != ANCHO // 2:
        xm -= ANCHO // 2
    else:
        xm = 0
    if ym != ALTO // 2:
        ym = ALTO // 2 - ym
    else:
        ym = 0

    angulo = math.atan2(ym, xm)

    corX = int(math.sin((angulo + math.radians(90))) * 60) + ANCHO // 2
    corY = int((math.cos(angulo + math.radians(90))) * 60) + ALTO // 2

    Canon = ((corX, corY), angulo)


def dibujarCanon():
    global Canon
    pos, ang = Canon
    pygame.draw.circle(ventana, ROJO, pos, 15)


def crearBala():
    global Canon
    pos, ang = Canon
    x, y = pos[0], pos[1]
    listaBala.append(((x, y), ang))


def dibujarBala():
    for bala_ in listaBala:
        pos, ang = bala_
        x, y = pos
        pygame.draw.circle(ventana, AZUL, (int(x), int(y)), 10)


def moverBala():
    global listaEnemigos
    for n in range(len(listaBala)-1, -1, -1):
        pos, ang = listaBala[n]
        x, y = pos

        x += 20 * math.sin(ang + math.radians(90))
        y += 20 * math.cos(ang + math.radians(90))
        if x > ANCHO or x < 0 or y < 0 or y > ALTO:
            listaBala.pop(n)
            return
        pos = (x, y)

        for enemigo in listaEnemigos:
            xe, ye = enemigo

            if (x < xe < x + 30 and y < ye < y + 30) or (x < xe + 30 < x + 30 and y < ye + 30 < y + 30):
                global score
                listaBala.pop(n)
                listaEnemigos.remove(enemigo)
                score += 1
                return
        listaBala[n] = (pos, ang)


def crearEnemigo():
    listaEnemigos.append((Puntos[random(0, vertices - 1)]))


def moverEnemigos():
    for n in range(0, len(listaEnemigos) - 1):
        pos = listaEnemigos[n]
        x, y = pos

        x -= (x - ANCHO // 2)//40
        y -= (y - ALTO // 2)//40

        if 360 < x < 440 and 270 < y < 330:
            global score, contador, record
            if score > record:
                record = score
                archivo.write("\n" + str(score))
            score = 0
            contador = 0
            listaEnemigos.clear()
            listaBala.clear()

            return

        listaEnemigos[n] = (x, y)


def dibujarEnemigos():
    for enemigo in listaEnemigos:
        pos = enemigo
        x, y = pos
        pygame.draw.circle(ventana, VERDE, (int(x), int(y)), 20)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
        # Borrar pantalla

        pygame.display.update()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)


contador = 0
selector=0
entrada=open("record.txt","r")
listaTop=[]
for linea in entrada:  # LEE TODAS LAS LINEAS DEL ARCHIVO
    listaTop.append(linea[0])
entrada.close()


while not termina:
    reloj.tick(40)  # 40 fps
    estado=MENU

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
            termina = True  # Queremos terminar el ciclo

        elif evento.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            pos = [pos[0], pos[1]]
            pos[0] -= ANCHO // 2
            pos[1] = ALTO // 2 - pos[1]
            crearBala()
    if evento.type == pygame.KEYDOWN:
        selector += 1
    print(selector)
    if selector != 0:
        estado = JUGANDO


    if  estado == MENU:
        for linea in archivo:  # LEE TODAS LAS LINEAS DEL ARCHIVO
            listaTop.append(linea)

        # Borrar pantalla
        ventana.blit(fondo,(0, 0))
        puntajetxt = fuente.render(str(listaTop[len(listaTop)-1]), True, NEGRO)
        ventana.blit(puntajetxt, (720, 90))
        print(listaTop)


    elif estado == JUGANDO:
        ventana.fill(BLANCO)
        dibujarPersonaje()
        moverCanon()
        dibujarCanon()
        moverBala()
        dibujarBala()
        moverEnemigos()
        dibujarEnemigos()
        scoretxt = fuente.render(str(score), True, ROJO)
        ventana.blit(scoretxt, (30, 30))
        recordtxt = fuente.render(str(record), True, ROJO)
        ventana.blit(recordtxt, (30, 80))

    contador += 1

    if contador % 20 == 0:
        contador = 0
        crearEnemigo()

    dibujar()

archivo.close()
pygame.quit()
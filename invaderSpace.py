# encoding: UTF-8
# Luis Jonathan Rosas Ramos
# Relizar juego "Space Invaders"

import pygame
from random import randint
ANCHO = 800
ALTO = 600
# Colores a utilziar
NEGRO = (0,0,0)
BLANCO = (255,255,255)
ROJO = (255,0,0)

# Estados del juego
MENU = 1
JUGANDO = 2
SCORE = 3

# Estados de movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
ADELANTE = 4
ATRAS = 5


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)

def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarRocas(ventana, listaRoca):
    for roca in listaRoca:
        ventana.blit(roca.image, roca.rect)

def actualizarEnemigos(listaEnemigos):
    pass

def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

def actualizarBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 30

def actualizarRocas(listaRoca):
    for roca in listaRoca:
        roca.rect.left -= 3

def verificarColisiones(listaBalas, listaEnemigos,PUNTOS):
    acumulador = 0
    # recorre las listas al revés
    for k in range(len(listaBalas)-1,-1,-1):
        bala = listaBalas[k]
        borrarBala = False
        for e in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, anchoe, altoe = enemigo.rect
            if xb>=xe and xb<=xe+anchoe and yb>=ye and yb<=ye+altoe:
                listaEnemigos.remove(enemigo)   # borra de la lista
                borrarBala = True
                break
        if borrarBala:
            listaBalas.remove(bala)
            acumulador = acumulador + 10
    return PUNTOS + acumulador

def verficarColisionesRocas(spritePersonaje,listaRoca,Vidas):
    acumulador = 0
    # recorre las listas al revés
    for k in range(len(listaRoca) - 1, -1, -1):
        roca = listaRoca[k]
        xb = roca.rect.left
        yb = roca.rect.bottom
        xe,ye,anchoe,altoe = spritePersonaje.rect
        if xb >= xe and xb <= xe + anchoe and yb >= ye and yb <= ye + altoe:
            listaRoca.remove(roca)  # borra de la lista
            acumulador = acumulador - 1
            break
    return Vidas + acumulador


def guardarScore(nombreJugador,PUNTOS):
    salida = open("Jugadores.txt","a")
    acumulador = 0
    for i in range(PUNTOS):
        acumulador = acumulador + 10
        if acumulador >= PUNTOS:
            salida.write("%s,%d\n"%(nombreJugador,PUNTOS))
    salida.close()

def obtenerMejor(archivo):
    entrada = open(archivo,"r")
    acumulador = 0
    for linea in entrada:
        dato = linea.split(",")
        puntos = int(dato[1])
        acumulador = acumulador + puntos
        if acumulador <= puntos:
            acumulador = puntos
    return acumulador



def correrJuego():
    nombreJugador = input("¿Cual es tu nombre: ")
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # personaje principal
    imgPersonaje = pygame.image.load("PersonajeDos.png")
    spritePersonaje = pygame.sprite.Sprite()  # sprite vacío
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO // 2 + spritePersonaje.rect.height // 2
    movimiento = QUIETO
    if spritePersonaje.rect.bottom == 50:
        movimiento = ABAJO
    elif spritePersonaje.rect.bottom == 550:
        movimiento = ARRIBA

    # Enemigos
    listaEnemigos = []  # Lista vacía de enemigos
    imgEnemigo = pygame.image.load("PersonajeTres.png")
    for k in range(20):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(ANCHO//2, ANCHO-50)
        spriteEnemigo.rect.bottom = randint(200, ALTO-80)
        listaEnemigos.append(spriteEnemigo)

    # Balas
    imgBala = pygame.image.load("bala.png")
    listaBalas = []

    # Cosas a esquivar
    imgRoca = pygame.image.load("roca.jpg")
    listaRoca =[]

    # Estado del juego
    estado = MENU       # Inicial

    # Imágenes para el menú
    imgBtnJugar = pygame.image.load("button_entrar.png")
    imgBtnScore = pygame.image.load("button_laderboard.png")
    imgBtnRegresar = pygame.image.load("button_regresar.png")

    # Imágenes para el juego
    imgFondo = pygame.image.load("mundo.jpg")
    xFondo = 0
    imgLlaves =pygame.image.load("LLAVES.png")
    imgPersonajes = pygame.image.load("personajes.png")

    # TIEMPO
    timer = 0   # acumulador de tiempo

    # TEXTO
    fuente = pygame.font.SysFont("monospace", 20)
    fuenteGrande = pygame.font.SysFont("monospace",54)

    # Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)

    # TEXTO
    fuente = pygame.font.SysFont("monospace", 24)

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    movimiento = ABAJO
                elif evento.key == pygame.K_RIGHT:
                    movimiento = ADELANTE
                elif evento.key == pygame.K_LEFT:
                    movimiento = ATRAS
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO//2 - 100
                yb = ALTO//2 - 50
                xs = ANCHO//2 + 200
                ys = ALTO//2 + 150
                xr = ANCHO//2 - 380
                yr = ALTO//2 - 250
                anchoB = 163
                altoB = 72
                anchoS = 182
                altoS = 41
                anchoR = 165
                altoR = 52
                if xm>=xb and xm<=xb+anchoB and ym>=yb and ym<=yb+altoB:
                    estado = JUGANDO
                if xm>=xs and xm<=xs+anchoS and ym>=ys and ym<=ys+altoS:
                    estado = SCORE
                if xm>=xr and xm<=xr+anchoR and ym>=yr and ym<=yr+altoR:
                    estado = MENU


        # Pregunta en qué estado está el juego
        if estado==MENU:
            # Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgBtnScore, (ANCHO//2 + 200, ALTO//2 + 150))
            ventana.blit(imgBtnJugar, (ANCHO//2 - 100, ALTO//2 - 50))
            ventana.blit(imgPersonajes,(0,0))
            Vidas = 3
            PUNTOS = 0

        if estado == SCORE:
            ventana.fill(NEGRO)
            ventana.blit(imgBtnRegresar,(ANCHO//2 - 380, ALTO//2 - 250))
            ventana.blit(imgLlaves,(ANCHO//2-300,ALTO//2-100))
            textoGrande = fuenteGrande.render("SCORE", 1, ROJO)
            ventana.blit(textoGrande, (100, 150))
            entrada = open("Top5.txt", "r")
            for linea in entrada:
                datos = linea.split(",")
                persona = datos[0]
                textoTop5 = fuente.render("%s         ,................ 000"%(persona),1,ROJO)
                x = 350
                for i in range(0,5):
                    ventana.blit(textoTop5,(100,x))
                    x += 50
            entrada.close()

        elif estado == JUGANDO:
            if timer >= 3:
                timer = 0
                spriteRoca = pygame.sprite.Sprite()
                spriteRoca.image = imgRoca
                spriteRoca.rect = imgRoca.get_rect()
                spriteRoca.rect.left = randint(ANCHO // 2, ANCHO - 50)
                spriteRoca.rect.bottom = randint(200, ALTO - 80)
                listaRoca.append(spriteRoca)
                efecto.play()
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.width
                spriteBala.rect.bottom = spritePersonaje.rect.bottom - spritePersonaje.rect.height // 2
                listaBalas.append(spriteBala)
            if listaEnemigos == []:
                imgEnemigo = pygame.image.load("PersonajeTres.png")
                for k in range(20):
                    spriteEnemigo = pygame.sprite.Sprite()
                    spriteEnemigo.image = imgEnemigo
                    spriteEnemigo.rect = imgEnemigo.get_rect()
                    spriteEnemigo.rect.left = randint(ANCHO // 2, ANCHO - 50)
                    spriteEnemigo.rect.bottom = randint(200, ALTO - 80)
                    listaEnemigos.append(spriteEnemigo)

            # Actualizar enemigos
            actualizarBalas(listaBalas)
            actualizarEnemigos(listaEnemigos)
            actualizarRocas(listaRoca)
            guardarScore(nombreJugador, PUNTOS)
            PUNTOS = verificarColisiones(listaBalas, listaEnemigos,PUNTOS)
            Vidas = verficarColisionesRocas(spritePersonaje,listaRoca,Vidas)
            if Vidas == 0:
                estado = SCORE

            # Mover personaje
            if movimiento == ARRIBA:
                spritePersonaje.rect.bottom -= 2
                if spritePersonaje.rect.bottom <= 170:
                    spritePersonaje.rect.left = 0
                    spritePersonaje.rect.bottom = 565
            elif movimiento == ABAJO:
                spritePersonaje.rect.bottom += 2
                if spritePersonaje.rect.bottom >= 565:
                    spritePersonaje.rect.left = 0
                    spritePersonaje.rect.bottom = 170
            elif movimiento == ADELANTE:
                spritePersonaje.rect.left += 2
                if spritePersonaje.rect.left >= 180:
                    spritePersonaje.rect.left = 0
            elif movimiento == ATRAS:
                spritePersonaje.rect.left -= 2
                if spritePersonaje.rect.left <= 0:
                    spritePersonaje.rect.left = 180

            # Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgFondo, (xFondo,100))

            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)
            dibujarRocas(ventana, listaRoca)

            pygame.draw.line(ventana, BLANCO, (250,100), (250,546),5)
            pygame.draw.line(ventana, BLANCO, (0, 100), (0, 546), 5)
            pygame.draw.line(ventana, BLANCO, (0, 100), (800, 100), 5)
            pygame.draw.line(ventana, BLANCO, (0, 546), (800, 546), 5)
            pygame.draw.line(ventana, BLANCO, (800, 100), (800, 546), 5)

            # Dibujar texto
            textoPuntos = fuente.render("Puntos: %.0f"%PUNTOS,1,ROJO)
            ventana.blit(textoPuntos,(300,100))
            textoVida = fuente.render("Vidas: %.f"%Vidas,1,ROJO)
            ventana.blit(textoVida,(500,100))


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/11

    # Después del ciclo principal
    pygame.quit()  # termina pygame

def main():
    correrJuego()

main()
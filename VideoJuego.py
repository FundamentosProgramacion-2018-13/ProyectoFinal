#Autor Claudio Mayoral Garcia
#Descripcion: Es un videojuego para entretenerse

import pygame
from random import randint
import math

#Pantalla
ANCHO = 800
ALTO = 600

#Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)

#Estado del menú
MENU = 1
JUGANDO = 2
PERDISTE = 3

#Movimiento
QUIETO = 1
ABAJO = 2
ARRIBA = 3


def dibujarScore(ventana, listaPuntaje):
    a = str(sum(listaPuntaje))
    pygame.font.init()
    fuente = pygame.font.Font(None, 100)
    texto = fuente.render(a, 1, (255, 255, 255), )
    ventana.blit(texto, (320, 350))

    score = "Score:"
    pygame.font.init()
    fuente = pygame.font.Font(None, 100)
    textoScore = fuente.render(score, 1, (255, 255, 255), )
    ventana.blit(textoScore, (80, 350))

    antes = open("puntajes.txt", "r")
    linea = antes.readline()
    b = linea
    pygame.font.init()
    fuente1 = pygame.font.Font(None, 100)
    texto1 = fuente1.render(b, 1, (255, 255, 255), )
    ventana.blit(texto1, (460, 480))

    highScore = "HighScore:"
    pygame.font.init()
    fuente = pygame.font.Font(None, 100)
    textoHighScore = fuente.render(highScore, 1, (255, 255, 255), )
    ventana.blit(textoHighScore, (80, 480))
    pygame.display.flip()


def dibujarMarcador(ventana, listaPuntaje):
    a = str(sum(listaPuntaje))
    pygame.font.init()
    fuente = pygame.font.Font(None, 50)
    texto = fuente.render(a, 1, (0, 0, 0), )
    ventana.blit(texto, (0, 0))
    pygame.display.flip()

#Dibuja el Menu
def dibujarMenu(ventana, imgBtnJugar):
    ventana.blit(imgBtnJugar, (0, 50))


def dibujarPerdiste(ventana, fondoPerdiste):
    ventana.blit(fondoPerdiste, (0,0))


#Dibuja el sprite de las balas
def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


#Dibuja el sprite del personaje
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


#Dibuja el sprite de Tauros
def dibujarTauros(ventana, listaTauros):
    for enemigo in listaTauros:
        ventana.blit(enemigo.image, enemigo.rect)


#Dibuja el sprite de Magikarp
def dibujarMagikarp(ventana, listaMagikarp):
    for magikarp in listaMagikarp:
        ventana.blit(magikarp.image, magikarp.rect)


#Dibuja el sprite de miltank
def dibujarMiltank(ventana, listaMiltank):
    for miltank in listaMiltank:
        ventana.blit(miltank.image, miltank.rect)


def dibujarPoder(ventana, listaPoder):
    for poder in listaPoder:
        ventana.blit(poder.image, poder.rect)

def dibujarProyectil(ventana, listaProyectil):
    for proyectil in listaProyectil:
        ventana.blit(proyectil.image, proyectil.rect)


def moverProyectil(listaProyectil):
    for proyectil in listaProyectil:
        proyectil.rect.left += 10

#Mueve el sprite de Tauros
def moverTauros(listaTauros):
    for enemigo in listaTauros:
        enemigo.rect.left -= 2


#Mueve el sprite de Magikarp
def moverMagikarp(listaMagikarp):
    for magikarp in listaMagikarp:
        magikarp.rect.left -= 10


#Mueve el sprite de Paracaidas
def moverParacaidas(listaParacaidas):
    for paracaidas in listaParacaidas:
        paracaidas.rect.bottom += 10


#Mueve el sprite de Pidgey
def moverPidgey(listaPidgey, contador):
    mover = math.sin(contador)
    x = mover*2
    for pidgey in listaPidgey:
        pidgey.rect.left -= 3
        pidgey.rect.bottom -= x



#Mueve el sprite de las balas
def moverBalas(listaBalas):
    for balas in listaBalas:
        balas.rect.left += 15


#Verifica si algun magikarp se paso de cierta coordenada para eliminarlo
def verificarMagikarp(listaMagikarp):
    for magikarp in range(len(listaMagikarp)-1, -1, -1):
        enemigo = listaMagikarp[magikarp]
        if enemigo.rect.left <= -50:
            # Le pegó
            listaMagikarp.remove(enemigo)
            break

def verificarBala(listaBalas):
    for bala in range(len(listaBalas)-1, -1, -1):
        enemigo = listaBalas[bala]
        if enemigo.rect.left >= ANCHO+50:
            # Le pegó
            listaBalas.remove(enemigo)
            break


def dibujarPidgey(ventana, listaPidgey):
    for pidgey in listaPidgey:
        ventana.blit(pidgey.image, pidgey.rect)


def dibujarParacaidas(ventana, listaParacaidas):
    for paracaidas in listaParacaidas:
        ventana.blit(paracaidas.image, paracaidas.rect)


#Verifica si la bala choco con algun pidgey
def verificarColisionPidgey(listaPidgey, listaBalas, listaPuntos, listaPuntaje):
    for k in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[k]
        for e in range(len(listaPidgey)-1, -1, -1):
            enemigo = listaPidgey[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            altoe = enemigo.rect.height
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
                # Le pegó
                listaPidgey.remove(enemigo)
                listaBalas.remove(bala)
                listaPuntos.append(10)
                listaPuntaje.append(1)

                break

#Verifica si el proyectil choco con algun pidgey
def verificarColisionPidgeyProyectil(listaPidgey, listaProyectil, listaPuntos, listaPuntaje):
    for k in range(len(listaProyectil) - 1, -1, -1):
        bala = listaProyectil[k]
        for e in range(len(listaPidgey)-1, -1, -1):
            enemigo = listaPidgey[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            altoe = enemigo.rect.height
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
                # Le pegó
                listaPidgey.remove(enemigo)
                listaPuntos.append(10)
                listaPuntaje.append(1)

                break


#Verifica si el pidgey salio de la pantalla para eliminarlo
def verificarPidgey(listaPidgey, listaPuntos):
    for pidgey in range(len(listaPidgey)-1, -1, -1):
        enemigo = listaPidgey[pidgey]
        if enemigo.rect.left <= -70:
            # Callo
            listaPidgey.remove(enemigo)
            listaPuntos.append(0)
            break


#verifica si tauros salio de la pantalla para eliminarlo
def verificarTauros(listaTauros, listaMiltank):
    for k in range(len(listaMiltank) -1, -1, -1):
        bala = listaMiltank[k]
        for e in range(len(listaTauros)-1, -1, -1):
            enemigo = listaTauros[e]
            # bala vs enemigo
            if enemigo.rect.left <= 0:
                # Le pegó
                listaTauros.remove(enemigo)
                listaMiltank.remove(bala)
                break


#verifica si algun paracaidas salio de la pantalla para eliminarlo
def verificarParacaidas(listaParacaidas):
    for paracaidas in range(len(listaParacaidas)-1, -1, -1):
        enemigo = listaParacaidas[paracaidas]
        if enemigo.rect.bottom >= ALTO+110:
            # Callo
            listaParacaidas.remove(enemigo)
            break


#Verifica si algun magikarp chocó con alguna bala
def verificarColisionMagikarp(listaMagikarp, listaBalas, listaPuntos, listaPuntaje):
    for k in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[k]
        for e in range(len(listaMagikarp)-1, -1, -1):
            enemigo = listaMagikarp[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            altoe = enemigo.rect.height
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
                # Le pegó
                listaMagikarp.remove(enemigo)
                listaBalas.remove(bala)
                listaPuntos.append(5)
                listaPuntaje.append(1)
                break


#Verifica si el proyectil choco con algun Magikarp
def verificarColisionMagikarpProyectil(listaMagikarp, listaProyectil, listaPuntos, listaPuntaje):
    for k in range(len(listaProyectil) - 1, -1, -1):
        bala = listaProyectil[k]
        for e in range(len(listaMagikarp)-1, -1, -1):
            enemigo = listaMagikarp[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            altoe = enemigo.rect.height
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
                # Le pegó
                listaMagikarp.remove(enemigo)
                listaPuntos.append(10)
                listaPuntaje.append(1)

                break


#Verifica si algun Tauros choco con alguna bala
def verificarColisionTauros(listaTauros, listaBalas, listaPuntos, listaPuntaje):
    for k in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[k]
        for e in range(len(listaTauros)-1, -1, -1):
            enemigo = listaTauros[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            altoe = enemigo.rect.height
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
                # Le pegó
                listaTauros.remove(enemigo)
                listaBalas.remove(bala)
                listaPuntos.append(2)
                listaPuntaje.append(1)
                break

#Verifica si el proyectil choco con algun Tauros
def verificarColisionTaurosProyectil(listaTauros, listaProyectil, listaPuntos, listaPuntaje):
    for k in range(len(listaProyectil) - 1, -1, -1):
        bala = listaProyectil[k]
        for e in range(len(listaTauros)-1, -1, -1):
            enemigo = listaTauros[e]
            # bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            altoe = enemigo.rect.height
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
                # Le pegó
                listaTauros.remove(enemigo)
                listaPuntos.append(10)
                listaPuntaje.append(1)
                break


#Verifica si mataste a algun paracaidas
def verificarMuerte(listaParacaidas, listaBalas, listaMiltank):
    for a in range(len(listaMiltank)-1, -1, -1):
        miltank = listaMiltank[a]
        for k in range(len(listaBalas) - 1, -1, -1):
            bala = listaBalas[k]
            for e in range(len(listaParacaidas)-1, -1, -1):
                enemigo = listaParacaidas[e]
                # bala vs enemigo
                xb = bala.rect.left
                yb = bala.rect.bottom
                xe, ye, ae, alte = enemigo.rect
                altoe = enemigo.rect.height
                if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
                    # Le pegó
                    listaParacaidas.remove(enemigo)
                    listaBalas.remove(bala)
                    listaMiltank.remove(miltank)
                    break


def usarSuper(listaPuntos, listaPoder, imgPoder):
    y = 100
    z = 0
    if sum(listaPuntos) >= y:
        spritePoder = pygame.sprite.Sprite()
        spritePoder.image = imgPoder
        spritePoder.rect = imgPoder.get_rect()
        spritePoder.rect.left = z
        spritePoder.rect.bottom = 100
        listaPoder.append(spritePoder)
        listaPuntos.append(-100)



#Funcion que dibuja el juego
def dibujar():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    # Personaje
    imgPersonaje = pygame.image.load('personajeMontura.png')
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO//2 + spritePersonaje.rect.height//2


    #Puntos
    listaPuntos = []


    #Puntaje
    listaPuntaje = []


    #Fondo
    fondo = pygame.image.load("Fondo1.jpg")


    #Perdiste
    fondoPerdiste = pygame.image.load("fondoPerdiste.png")


    # Magikarp
    listaMagikarp = []
    imgMagikarp = pygame.image.load("Magikarp.png")
    for x in range(2):
        spriteMagikarp = pygame.sprite.Sprite()
        spriteMagikarp.image = imgMagikarp
        spriteMagikarp.rect = imgMagikarp.get_rect()
        spriteMagikarp.rect.left = randint(ANCHO + 50, ANCHO + 450)
        spriteMagikarp.rect.bottom = randint(450, ALTO - 120)
        listaMagikarp.append(spriteMagikarp)


    # Pidgey
    listaPidgey = []
    imgPidgey = pygame.image.load("pidgey2.png")
    for x in range(12):
        spritePidgey = pygame.sprite.Sprite()
        spritePidgey.image = imgPidgey
        spritePidgey.rect = imgPidgey.get_rect()
        spritePidgey.rect.left = randint(ANCHO + 80, ANCHO + 600)
        spritePidgey.rect.bottom = randint(100, ALTO - 170)
        listaPidgey.append(spritePidgey)


    # Tauros
    listaTauros = []
    imgTauros = pygame.image.load("Tauros.png")
    for k in range(5):
        spriteTauros = pygame.sprite.Sprite()
        spriteTauros.image = imgTauros
        spriteTauros.rect = imgTauros.get_rect()
        spriteTauros.rect.left = randint(ANCHO + 50, ANCHO + 450)
        spriteTauros.rect.bottom = randint(480, ALTO - 10)
        listaTauros.append(spriteTauros)


    # Paracaídas
    listaParacaidas = []
    imgParacaidas = pygame.image.load("paracaidasJames.png")
    for k in range(3):
        spriteParacaidas = pygame.sprite.Sprite()
        spriteParacaidas.image = imgParacaidas
        spriteParacaidas.rect = imgParacaidas.get_rect()
        spriteParacaidas.rect.left = randint(100, ANCHO)
        spriteParacaidas.rect.bottom = randint(-200, -100)
        listaParacaidas.append(spriteParacaidas)


    #Miltank
    listaMiltank = []
    imgMiltank = pygame.image.load("Miltank.png")
    spriteMiltank = pygame.sprite.Sprite()
    spriteMiltank.image = imgMiltank
    spriteMiltank.rect = imgMiltank.get_rect()
    spriteMiltank.rect.left = ANCHO-50
    spriteMiltank.rect.bottom = 50
    listaMiltank.append(spriteMiltank)
    spriteMiltank = pygame.sprite.Sprite()
    spriteMiltank.image = imgMiltank
    spriteMiltank.rect = imgMiltank.get_rect()
    spriteMiltank.rect.left = ANCHO-100
    spriteMiltank.rect.bottom = 50
    listaMiltank.append(spriteMiltank)
    spriteMiltank = pygame.sprite.Sprite()
    spriteMiltank.image = imgMiltank
    spriteMiltank.rect = imgMiltank.get_rect()
    spriteMiltank.rect.left = ANCHO-150
    spriteMiltank.rect.bottom = 50
    listaMiltank.append(spriteMiltank)

    #Poder
    listaPoder = []
    imgPoder = pygame.image.load("poder.png")

    #Sonido Choque
    efecto = pygame.mixer.Sound("pokebala.wav")
    efectoDisparo = pygame.mixer.Sound("choque.wav")
    fuego = pygame.mixer.Sound("fuego.wav")

    contador = 0


    #Proyectil
    listaProyectil = []
    imgProyectil = pygame.image.load("proyectil.png")

    #Balas
    listaBalas = []
    imgBala = pygame.image.load("def.png")

    #Estado del juego
    estado = MENU

    #Menu
    imgBtnJugar = pygame.image.load("menuinicio.jpg")

    #Estado del Personaje
    moviendo = QUIETO
    pygame.mixer.init()
    if estado == MENU:
        pygame.mixer.music.load("music.ogg")
        pygame.mixer.music.play(-1)

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True


            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    moviendo = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    moviendo = ABAJO


                if evento.key == pygame.K_z:
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom-25
                    listaBalas.append(spriteBala)
                    if estado == JUGANDO:
                        efecto.play()

                elif evento.key == pygame.K_x:
                    if len(listaPoder) != 0:
                        fuego.play()
                        spriteProyectil = pygame.sprite.Sprite()
                        spriteProyectil.image = imgProyectil
                        spriteProyectil.rect = imgProyectil.get_rect()
                        spriteProyectil.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                        spriteProyectil.rect.bottom = spritePersonaje.rect.bottom-25
                        listaProyectil.append(spriteProyectil)
                        listaPoder = []


                elif evento.key == pygame.K_SPACE:
                    if estado == MENU or estado == PERDISTE:
                        estado = JUGANDO
                        pygame.mixer.music.load("musicajugando.mp3")
                        pygame.mixer.music.play(-1)
                        listaPuntaje = []
                        listaBalas = []
        contador = (contador + 1/10)
        ventana.fill(NEGRO)
        if estado == JUGANDO:
            ventana.blit(fondo, (0,0))
            dibujarPersonaje(ventana, spritePersonaje)
            if moviendo == ARRIBA:
                spritePersonaje.rect.bottom -= 5
                if spritePersonaje.rect.bottom <= 75:
                    moviendo = QUIETO
            elif moviendo == ABAJO:
                spritePersonaje.rect.bottom += 5
                if spritePersonaje.rect.bottom >= 580:
                    moviendo = QUIETO
            dibujarPoder(ventana, listaPoder)
            usarSuper(listaPuntos, listaPoder, imgPoder)
            dibujarProyectil(ventana, listaProyectil)

            dibujarMagikarp(ventana, listaMagikarp)
            moverMagikarp(listaMagikarp)
            dibujarTauros(ventana, listaTauros)
            moverTauros(listaTauros)
            dibujarPidgey(ventana, listaPidgey)
            moverPidgey(listaPidgey, contador)
            dibujarParacaidas(ventana, listaParacaidas)
            moverParacaidas(listaParacaidas)
            dibujarMiltank(ventana, listaMiltank)
            dibujarBalas(ventana, listaBalas)
            moverBalas(listaBalas)
            moverProyectil(listaProyectil)
            verificarColisionTauros(listaTauros, listaBalas, listaPuntos, listaPuntaje)
            verificarColisionMagikarp(listaMagikarp, listaBalas, listaPuntos, listaPuntaje)
            verificarColisionPidgey(listaPidgey, listaBalas, listaPuntos, listaPuntaje)
            verificarPidgey(listaPidgey, listaPuntos)
            verificarMagikarp(listaMagikarp)
            verificarParacaidas(listaParacaidas)
            verificarMuerte(listaBalas, listaParacaidas, listaMiltank)
            verificarTauros(listaTauros, listaMiltank)
            verificarBala(listaBalas)
            dibujarMarcador(ventana, listaPuntaje)
            verificarColisionPidgeyProyectil(listaPidgey, listaProyectil, listaPuntos, listaPuntaje)
            verificarColisionMagikarpProyectil(listaMagikarp, listaProyectil, listaPuntos, listaPuntaje)
            verificarColisionTaurosProyectil(listaTauros, listaProyectil, listaPuntos, listaPuntaje)


            if len(listaPidgey) != 12:
                efectoDisparo.play()
                spritePidgey = pygame.sprite.Sprite()
                spritePidgey.image = imgPidgey
                spritePidgey.rect = imgPidgey.get_rect()
                spritePidgey.rect.left = randint(ANCHO + 100, ANCHO + 300)
                spritePidgey.rect.bottom = randint(200, ALTO - 70)
                listaPidgey.append(spritePidgey)
            if len(listaMagikarp) != 2:
                efectoDisparo.play()
                spriteMagikarp = pygame.sprite.Sprite()
                spriteMagikarp.image = imgMagikarp
                spriteMagikarp.rect = imgMagikarp.get_rect()
                spriteMagikarp.rect.left = randint(ANCHO // 2, ANCHO)
                spriteMagikarp.rect.bottom = randint(450, ALTO - 120)
                listaMagikarp.append(spriteMagikarp)
            if len(listaTauros) != 5:
                efectoDisparo.play()
                spriteTauros = pygame.sprite.Sprite()
                spriteTauros.image = imgTauros
                spriteTauros.rect = imgTauros.get_rect()
                spriteTauros.rect.left = randint(ANCHO, ANCHO+200)
                spriteTauros.rect.bottom = randint(480, ALTO - 10)
                listaTauros.append(spriteTauros)
            if len(listaParacaidas) != 3:
                efectoDisparo.play()
                spriteParacaidas = pygame.sprite.Sprite()
                spriteParacaidas.image = imgParacaidas
                spriteParacaidas.rect = imgParacaidas.get_rect()
                spriteParacaidas.rect.left = randint(100, ANCHO-200)
                spriteParacaidas.rect.bottom = randint(0-400, 20-100)
                listaParacaidas.append(spriteParacaidas)


            #Cuando Pierdes
            if len(listaMiltank) == 0:
                pygame.mixer.music.load("cancionPerdiste.mp3")
                pygame.mixer.music.play(-1)
                estado = PERDISTE
                listaProyectil = []
                listaPuntos = []
                #Balas
                listaBalas = []
                #Poder
                listaPoder = []
                # Miltank
                listaMiltank = []
                imgMiltank = pygame.image.load("Miltank.png")
                spriteMiltank = pygame.sprite.Sprite()
                spriteMiltank.image = imgMiltank
                spriteMiltank.rect = imgMiltank.get_rect()
                spriteMiltank.rect.left = ANCHO - 50
                spriteMiltank.rect.bottom = 50
                listaMiltank.append(spriteMiltank)
                spriteMiltank = pygame.sprite.Sprite()
                spriteMiltank.image = imgMiltank
                spriteMiltank.rect = imgMiltank.get_rect()
                spriteMiltank.rect.left = ANCHO - 100
                spriteMiltank.rect.bottom = 50
                listaMiltank.append(spriteMiltank)
                spriteMiltank = pygame.sprite.Sprite()
                spriteMiltank.image = imgMiltank
                spriteMiltank.rect = imgMiltank.get_rect()
                spriteMiltank.rect.left = ANCHO - 150
                spriteMiltank.rect.bottom = 50
                listaMiltank.append(spriteMiltank)

                # Magikarp
                listaMagikarp = []
                imgMagikarp = pygame.image.load("Magikarp.png")
                for x in range(2):
                    spriteMagikarp = pygame.sprite.Sprite()
                    spriteMagikarp.image = imgMagikarp
                    spriteMagikarp.rect = imgMagikarp.get_rect()
                    spriteMagikarp.rect.left = randint(ANCHO + 50, ANCHO + 450)
                    spriteMagikarp.rect.bottom = randint(450, ALTO - 120)
                    listaMagikarp.append(spriteMagikarp)

                # Pidgey
                listaPidgey = []
                imgPidgey = pygame.image.load("pidgey2.png")
                for x in range(12):
                    spritePidgey = pygame.sprite.Sprite()
                    spritePidgey.image = imgPidgey
                    spritePidgey.rect = imgPidgey.get_rect()
                    spritePidgey.rect.left = randint(ANCHO+100, ANCHO + 600)
                    spritePidgey.rect.bottom = randint(100, ALTO - 170)
                    listaPidgey.append(spritePidgey)

                # Tauros
                listaTauros = []
                imgTauros = pygame.image.load("Tauros.png")
                for k in range(5):
                    spriteTauros = pygame.sprite.Sprite()
                    spriteTauros.image = imgTauros
                    spriteTauros.rect = imgTauros.get_rect()
                    spriteTauros.rect.left = randint(ANCHO+50, ANCHO+650)
                    spriteTauros.rect.bottom = randint(480, ALTO - 10)
                    listaTauros.append(spriteTauros)

                # Paracaídas
                listaParacaidas = []
                imgParacaidas = pygame.image.load("paracaidasJames.png")
                for k in range(3):
                    spriteParacaidas = pygame.sprite.Sprite()
                    spriteParacaidas.image = imgParacaidas
                    spriteParacaidas.rect = imgParacaidas.get_rect()
                    spriteParacaidas.rect.left = randint(100, ANCHO)
                    spriteParacaidas.rect.bottom = randint(-200, -100)
                    listaParacaidas.append(spriteParacaidas)

                #Posicion del personaje
                spritePersonaje.rect.bottom = ALTO // 2 + spritePersonaje.rect.height // 2
                moviendo = QUIETO


        if estado == MENU:
            dibujarMenu(ventana, imgBtnJugar)

        if estado == PERDISTE:
            dibujarPerdiste(ventana, fondoPerdiste)
            dibujarScore(ventana, listaPuntaje)

            antes = open("puntajes.txt", "r")

            linea = antes.readline()
            puntaje = int(linea)
            total = sum(listaPuntaje)
            if puntaje < total:
                puntos = open("puntajes.txt", "w")
                puntos.write("%d" % total)
                puntos.close()
            antes.close()

        pygame.display.flip()
        reloj.tick(30)

    pygame.quit()
def main():
    dibujar()

main()
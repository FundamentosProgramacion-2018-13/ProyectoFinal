#Autor: Michelle Sánchez Guerrero
#Descripción: Aliens vs Astronauts

import pygame
import random

#Dimensiones
ANCHO = 800
ALTO = 600

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)

#Estados
MENU = 1
INSTRUCTIVO = 2
NIVELES = 3
NIVEL1 = 4
NIVEL2 = 5
INFINITO = 6
PERDER = 7
GANAR = 8

#Coordenadas slots
slotsX = [65, 175.5, 286, 396.5, 507]
coordenadas = [[216, 344 , 472], [344, 472, 216], [472, 216, 344], [216, 472, 344], [344, 216, 472], [472, 344, 216]]
coordAstronautas = coordenadas[random.randint(0,5)]
slotsY = [216, 344, 472]


#Función que dibuja el menu
def dibujarMenu(ventana, menu, boton, highscore):
    ventana.blit(menu, (0,0))
    ventana.blit(boton, (ANCHO//2-146.5, ALTO//2-30))
    ventana.blit(highscore, (315, 485))


#Función que dibuja el instructivo
def dibujarInstructivo(ventana, instructivo, botonAdv, botonInf):
    ventana.blit(instructivo, (0,0))
    ventana.blit(botonAdv, (30, 50))
    ventana.blit(botonInf, (545, 375))


#Función que dibuja la pantalla de selección de niveles
def dibujarNiveles(ventana, niveles, boton1, boton2, botonBack, proximamente):
    ventana.blit(niveles, (0,0))
    ventana.blit(boton1, (220, 280))
    ventana.blit(boton2, (450, 280))
    ventana.blit(botonBack, (680, 480))
    ventana.blit(proximamente, (415, 375))


#Función que dibuja la pantalla de que perdiste la partida
def dibujarPartidaPerdida(ventana, perdida, boton, texto):
    ventana.blit(perdida, (0,0))
    ventana.blit(boton, (475, 460))
    ventana.blit(texto, (500, 390))


#Función que dibuja la pantalla de que ganaste
def dibujarPartidaGanada(ventana, ganar, boton):
    ventana.blit(ganar, (0, 0))
    ventana.blit(boton, (485, 465))


#Función que dibuja todos los elementos del nivel 1 (también se usa para el modo infinito)
def dibujarNivel1(ventana, jugando, slot, btnAl1):
    ventana.blit(jugando, (0,0))
    #Slots (1 al 5, Primera columna)
    ventana.blit(slot, (slotsX[0], slotsY[0])) #Slot 1. Primera columna
    ventana.blit(slot, (slotsX[1], slotsY[0]))
    ventana.blit(slot, (slotsX[2], slotsY[0]))
    ventana.blit(slot, (slotsX[3], slotsY[0]))
    ventana.blit(slot, (slotsX[4], slotsY[0]))
    #Slots (6 al 10, Segunda columna)
    ventana.blit(slot, (slotsX[0], slotsY[1])) #Slot 6. Segunda columna
    ventana.blit(slot, (slotsX[1], slotsY[1]))
    ventana.blit(slot, (slotsX[2], slotsY[1]))
    ventana.blit(slot, (slotsX[3], slotsY[1]))
    ventana.blit(slot, (slotsX[4], slotsY[1]))
    #Slots (11 al 15, Tercera columna)
    ventana.blit(slot, (slotsX[0], slotsY[2])) #Slot 11. Tercera columna
    ventana.blit(slot, (slotsX[1], slotsY[2]))
    ventana.blit(slot, (slotsX[2], slotsY[2]))
    ventana.blit(slot, (slotsX[3], slotsY[2]))
    ventana.blit(slot, (slotsX[4], slotsY[2]))
    #Botones
    ventana.blit(btnAl1, (151, 42)) #Alien1


#Función que dibuja el alien
def dibujarAlien(ventana, imgAlien, x, y):
    spriteAlien = pygame.sprite.Sprite()
    spriteAlien.image =imgAlien
    spriteAlien.rect = imgAlien.get_rect()
    spriteAlien.rect.left = x
    spriteAlien.rect.bottom = y
    ventana.blit(spriteAlien.image, spriteAlien.rect)


#Función que crea el sprite del astronauta
def crearAstronauta(imgNaut, x, y):
    spriteNaut = pygame.sprite.Sprite()
    spriteNaut.image = imgNaut
    spriteNaut.rect = imgNaut.get_rect()
    spriteNaut.rect.left = x
    spriteNaut.rect.bottom = y

    return spriteNaut


#Función que dibuja el astronauta
def dibujarAstronauta(ventana, listaAstronautas):
    for naut in listaAstronautas:
        ventana.blit(naut.image, naut.rect)


#Función que actualiza la lista de astronautas
def actualizarAstronautas(listaAstronautas):
    for naut in listaAstronautas:
        naut.rect.left -= 0.05


#Función que crea el sprite de la bala
def crearBala(imgBala, x, y):
    spriteBala = pygame.sprite.Sprite()
    spriteBala.image = imgBala
    spriteBala.rect = imgBala.get_rect()
    spriteBala.rect.left = x
    spriteBala.rect.bottom = y

    return spriteBala


#Función que dibuja las balas
def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


#Función que actualiza la lista de las balas
def actualizarBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 10


#Función que verifica si hubo una colision, elimina al astronauta y a la bala
def verificarColisiones(listaBalas, listaAstronautas, listaRestantes):
    #recorre las listas al revés
    for k in range(len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        borrarBala = False

        for a in range(len(listaAstronautas)-1, -1, -1):
            naut = listaAstronautas[a]

            #Bala vs Naut
            xBala = bala.rect.left
            yBala = bala.rect.bottom
            xA, yA, anchoA, altoA = naut.rect

            if xBala >= xA and xBala <= xA + anchoA and yBala <= yA+100 and yBala >= yA:
                listaAstronautas.remove(naut)
                listaRestantes.pop()
                borrarBala = True
                break

        if borrarBala:
            listaBalas.remove(bala)


#Función que verifica si hubo una colision, elimina al astronauta y a la bala. Añade el puntaje
def verificarColisionesInfinito(listaBalas, listaAstronautas, listaHighscore):
    # recorre las listas al revés
    for k in range(len(listaBalas) - 1, -1, -1):
        bala = listaBalas[k]
        borrarBala = False

        for a in range(len(listaAstronautas) - 1, -1, -1):
            naut = listaAstronautas[a]

            # Bala vs Naut
            xBala = bala.rect.left
            yBala = bala.rect.bottom
            xA, yA, anchoA, altoA = naut.rect

            if xBala >= xA and xBala <= xA + anchoA and yBala <= yA + 100 and yBala >= yA:
                listaAstronautas.remove(naut)
                listaHighscore.append(1)
                borrarBala = True

                break

        if borrarBala:
            listaBalas.remove(bala)


#Función que verifica si el astronauta ya cruzó la linea
def verificarSiPierde(listaAstronautas):
    for a in range(0, len(listaAstronautas), 1):
        naut = listaAstronautas[a]

        xA, yA, anchoA, altoA = naut.rect

        if xA == 45:
            return True

        return False


#Función que reproduce la música
def ponerMusica(cancion):
    pygame.mixer.init()
    pygame.mixer.music.load(cancion)
    pygame.mixer.music.play(-1)


#Función que dibuja el juego
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Imágenes
    menu = pygame.image.load("menu.png")
    instructivo = pygame.image.load("instructivo.png")
    niveles = pygame.image.load("niveles.png")
    jugando = pygame.image.load("jugando.png")
    perdida = pygame.image.load("perder.png")
    ganar = pygame.image.load("ganar.png")

    btnJugar = pygame.image.load("boton jugar.png")
    btnlvl1 = pygame.image.load("boton nivel1.png")
    btnlvl2 = pygame.image.load("boton nivel2.png")
    btnAlien100 = pygame.image.load("botonal100.png")
    btnAventura = pygame.image.load("modav.png")
    btnInfinito = pygame.image.load("modinf.png")
    slot = pygame.image.load("slot.png")
    btnMenu = pygame.image.load("botonmenu.png")
    btnSigNivel = pygame.image.load("botonsignivel.png")
    btnBack = pygame.image.load("btnback.png")
    proximamente = pygame.image.load("proximamente.png")
    highscore = pygame.image.load("hgh.png")

    imgAlien100 = pygame.image.load("alien100.png")
    imgNaut1 = pygame.image.load("naut1.png")
    imgNautFW = pygame.image.load("nautfw.png")
    bala100 = pygame.image.load("balaAmarilla.png")

    listaImgsNauts = [imgNaut1, imgNautFW]

    #Lista balas para cada slot
    listaBalas1 = []
    listaBalas2 = []
    listaBalas3 = []
    listaBalas4 = []
    listaBalas5 = []
    listaBalas6 = []
    listaBalas7 = []
    listaBalas8 = []
    listaBalas9 = []
    listaBalas10 = []
    listaBalas11 = []
    listaBalas12 = []
    listaBalas13 = []
    listaBalas14 = []
    listaBalas15 = []

    #Astronautas
    listaAstronautas = []

    #Aliens - Slots
    alienSlot1 = 0
    alienSlot2 = 0
    alienSlot3 = 0
    alienSlot4 = 0
    alienSlot5 = 0
    alienSlot6 = 0
    alienSlot7 = 0
    alienSlot8 = 0
    alienSlot9 = 0
    alienSlot10 = 0
    alienSlot11 = 0
    alienSlot12 = 0
    alienSlot13 = 0
    alienSlot14 = 0
    alienSlot15 = 0

    #Medidas y
    alienY = 102
    difAlienX = 12

    #Elixir
    elixir = 500

    #Tiempo
    timerBala1 = 0
    timerBala2 = 0
    timerBala3 = 0
    timerBala4 = 0
    timerBala5 = 0
    timerBala6 = 0
    timerBala7 = 0
    timerBala8 = 0
    timerBala9 = 0
    timerBala10 = 0
    timerBala11 = 0
    timerBala12 = 0
    timerBala13 = 0
    timerBala14 = 0
    timerBala15 = 0

    timerAstronauta1 = 0
    timerAstronauta2 = 0
    timerAstronauta3 = 0

    timerGeneral = 0

    tiempoBala = 16

    #Texto
    fuenteNivel = pygame.font.SysFont("comicsansms", 20)
    fuenteModo = pygame.font.SysFont("comincansms", 15)
    fuenteHS = pygame.font.SysFont("comicsansms", 30)
    fuenteScore = pygame.font.SysFont("comicsansms", 55)

    #Contadores
    puntajeHighscore = []

    contadorColumna1= 0
    contadorColumna2 = 0
    contadorColumna3 = 0

    restantesLvl1 = list(range(0,24))

    #Definir el estado
    estado = MENU

    botonAlienON = 0

    #Audio
    musicaJugar = "jugar.mp3"
    musicaIntro = "intro.mp3"
    pistola = pygame.mixer.Sound("ray.wav")
    blop = pygame.mixer.Sound("beep.wav")

    ponerMusica(musicaIntro)

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.MOUSEBUTTONUP: #Tipo de evento, en este caso cuando se oprime una tecla
                if estado == MENU:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnJugar = ANCHO//2-146.5
                    yBtnJugar = ALTO//2-30
                    anchoBtnJugar = 293
                    altoBtnJugar = 103

                    if xm >= xBtnJugar and xm <= xBtnJugar + anchoBtnJugar and ym >= yBtnJugar and ym <= yBtnJugar + altoBtnJugar:
                        estado = INSTRUCTIVO

                elif estado == INSTRUCTIVO:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnAv = 30
                    yBtnAv = 50
                    anchoBtnAv = 233
                    altoBtnAv = 201

                    xBtnInf = 545
                    yBtnInf = 375
                    anchoBtnInf = 232
                    altoBtnInf = 203

                    if xm >= xBtnAv and xm <= xBtnAv + anchoBtnAv and ym >= yBtnAv and ym <= yBtnAv + altoBtnAv:
                        estado = NIVELES

                    if xm >= xBtnInf and xm <= xBtnInf + anchoBtnInf and ym >= yBtnInf and ym <= yBtnInf + altoBtnInf:
                        estado = INFINITO
                        ponerMusica(musicaJugar)

                elif estado == NIVELES:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnLvl1 = 220
                    yBtnLvl1 = 280
                    anchoBtnLvl1 = 141
                    altoBtnLvl1 = 134

                    xBtnBck = 680
                    yBtnBck = 480
                    anchoBtnBck = 103
                    altoBtnBck = 103

                    if xm >= xBtnLvl1 and xm <= xBtnLvl1 + anchoBtnLvl1 and ym >= yBtnLvl1 and ym <= yBtnLvl1 + altoBtnLvl1:
                        estado = NIVEL1
                        ponerMusica(musicaJugar)

                    if xm >= xBtnBck and xm <= xBtnBck + anchoBtnBck and ym >= yBtnBck and ym <= yBtnBck + altoBtnBck:
                        estado = INSTRUCTIVO

                elif estado == INFINITO:
                    dibujarNivel1(ventana, jugando, slot, btnAlien100)
                    xm, ym = pygame.mouse.get_pos()
                    xBtnAlien = 150
                    yBtnAlien = 41
                    anchoBtnAlien = 83
                    altoBtnAlien = 92

                    if xm >= xBtnAlien and xm <= xBtnAlien + anchoBtnAlien and ym >= yBtnAlien and ym <= yBtnAlien + altoBtnAlien and elixir >= 100:
                        botonAlienON = 1

                elif estado == NIVEL1:
                    dibujarNivel1(ventana, jugando, slot, btnAlien100)
                    xm, ym = pygame.mouse.get_pos()
                    xBtnAlien = 150
                    yBtnAlien = 41
                    anchoBtnAlien = 83
                    altoBtnAlien = 92

                    if xm >= xBtnAlien and xm <= xBtnAlien + anchoBtnAlien and ym >= yBtnAlien and ym <= yBtnAlien + altoBtnAlien and elixir >= 100:
                        botonAlienON = 1

                elif estado == PERDER:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnMn = 475
                    yBtnMn = 460
                    anchoBtnMn = 276
                    altoBtnMn = 107

                    if xm >= xBtnMn and xm <= xBtnMn + anchoBtnMn and ym >= yBtnMn and ym <= yBtnMn + altoBtnMn:
                        estado = MENU
                        ponerMusica(musicaIntro)

                elif estado == GANAR:
                    xm, ym = pygame.mouse.get_pos()
                    xBtnSN = 485
                    yBtnSN = 465
                    anchoBtnSN = 278
                    altoBtnSN = 108

                    if xm >= xBtnSN and xm <= xBtnSN + anchoBtnSN and ym >= yBtnSN and ym <= yBtnSN + altoBtnSN:
                        estado = NIVELES
                        ponerMusica(musicaIntro)

                if botonAlienON == 1:
                    xm, ym = pygame.mouse.get_pos()

                    anchoSlot = 103
                    altoSlot = 103

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot and alienSlot1 == 0: #1 slot
                        elixir -= 100
                        alienSlot1 = 1
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot and alienSlot2 == 0: #2 slot
                        elixir -= 100
                        alienSlot2 = 1
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot and alienSlot3 == 0: #3 slot
                        elixir -= 100
                        alienSlot3 = 1
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot and alienSlot4 == 0: #4 slot
                        elixir -= 100
                        alienSlot4 = 1
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[0] and ym <= slotsY[0] + altoSlot and alienSlot5 == 0:  #5 slot
                        elixir -= 100
                        alienSlot5 = 1
                        botonAlienON = 0

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot and alienSlot6 == 0:  #6 slot
                        elixir -= 100
                        alienSlot6 = 1
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot and alienSlot7 == 0:  #7 slot
                        elixir -= 100
                        alienSlot7 = 1
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot and alienSlot8 == 0: #8 slot
                        elixir -= 100
                        alienSlot8 = 1
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot and alienSlot9 == 0:  #9 slot
                        elixir -= 100
                        alienSlot9 = 1
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[1] and ym <= slotsY[1] + altoSlot and alienSlot10 == 0:  #10 slot
                        elixir -= 100
                        alienSlot10 = 1
                        botonAlienON = 0

                    if xm >= slotsX[0] and xm <= slotsX[0] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot and alienSlot11 == 0:  #11 slot
                        elixir -= 100
                        alienSlot11 = 1
                        botonAlienON = 0

                    if xm >= slotsX[1] and xm <= slotsX[1] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot and alienSlot12 == 0: #12 slot
                        elixir -= 100
                        alienSlot12 = 1
                        botonAlienON = 0

                    if xm >= slotsX[2] and xm <= slotsX[2] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot and alienSlot13 == 0:  #13 slot
                        elixir -= 100
                        alienSlot13 = 1
                        botonAlienON = 0

                    if xm >= slotsX[3] and xm <= slotsX[3] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot and alienSlot14 == 0:  #14 slot
                        elixir -= 100
                        alienSlot14 = 1
                        botonAlienON = 0

                    if xm >= slotsX[4] and xm <= slotsX[4] + anchoSlot and ym >= slotsY[2] and ym <= slotsY[2] + altoSlot and alienSlot15 == 0:  #15 slot
                        elixir -= 100
                        alienSlot15 = 1
                        botonAlienON = 0


        #Preguntar en qué estado está el juego
        if estado == MENU:
            dibujarMenu(ventana, menu, btnJugar, highscore)

            puntajeMax = open("highscore", "r")

            for puntaje in puntajeMax:
                score = puntaje

            puntajeMax.close()

            imprimirHighscore = fuenteHS.render("%d" % int(score), 1, NEGRO)
            imprimirModo = fuenteModo.render("MODO INFINITO", 2, NEGRO)
            ventana.blit(imprimirHighscore, (375, 530))
            ventana.blit(imprimirModo, (350, 530))

        if estado == INSTRUCTIVO:
            dibujarInstructivo(ventana, instructivo, btnAventura, btnInfinito)
            listaAstronautas = []
            puntajeHighscore = []
            elixir = 300
            restantesLvl1 = list(range(0, 24))
            listaBalas1 = []
            listaBalas2 = []
            listaBalas3 = []
            listaBalas4 = []
            listaBalas5 = []
            listaBalas6 = []
            listaBalas7 = []
            listaBalas8 = []
            listaBalas9 = []
            listaBalas10 = []
            listaBalas11 = []
            listaBalas12 = []
            listaBalas13 = []
            listaBalas14 = []
            listaBalas15 = []
            alienSlot1 = 0
            alienSlot2 = 0
            alienSlot3 = 0
            alienSlot4 = 0
            alienSlot5 = 0
            alienSlot6 = 0
            alienSlot7 = 0
            alienSlot8 = 0
            alienSlot9 = 0
            alienSlot10 = 0
            alienSlot11 = 0
            alienSlot12 = 0
            alienSlot13 = 0
            alienSlot14 = 0
            alienSlot15 = 0
            timerAstronauta1 = 0
            timerAstronauta2 = 0
            timerAstronauta3 = 0
            timerGeneral = 0
            contadorColumna1 = 0
            contadorColumna2 = 0
            contadorColumna3 = 0
            botonAlienON = 0

        if estado == NIVELES:
            dibujarNiveles(ventana, niveles, btnlvl1, btnlvl2, btnBack, proximamente)
            listaAstronautas = []
            puntajeHighscore = []
            restantesLvl1 = list(range(0, 24))
            listaBalas1 = []
            listaBalas2 = []
            listaBalas3 = []
            listaBalas4 = []
            listaBalas5 = []
            listaBalas6 = []
            listaBalas7 = []
            listaBalas8 = []
            listaBalas9 = []
            listaBalas10 = []
            listaBalas11 = []
            listaBalas12 = []
            listaBalas13 = []
            listaBalas14 = []
            listaBalas15 = []
            alienSlot1 = 0
            alienSlot2 = 0
            alienSlot3 = 0
            alienSlot4 = 0
            alienSlot5 = 0
            alienSlot6 = 0
            alienSlot7 = 0
            alienSlot8 = 0
            alienSlot9 = 0
            alienSlot10 = 0
            alienSlot11 = 0
            alienSlot12 = 0
            alienSlot13 = 0
            alienSlot14 = 0
            alienSlot15 = 0
            timerAstronauta1 = 0
            timerAstronauta2 = 0
            timerAstronauta3 = 0
            contadorColumna1 = 0
            contadorColumna2 = 0
            contadorColumna3 = 0
            botonAlienON = 0
            elixir = 500

        if estado == NIVEL1:
            dibujarNivel1(ventana, jugando, slot, btnAlien100)
            textoElixir = fuenteNivel.render(("%d") % elixir, 1, BLANCO)
            textoNivel1 = fuenteNivel.render("Nivel 1", 1, BLANCO)
            ventana.blit(textoElixir, (65, 103))
            ventana.blit(textoNivel1, (630, 40))

            if timerAstronauta1 >= random.randint(5,20):
                timerAstronauta1 = 0
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, coordAstronautas[0]+100)
                listaAstronautas.append(spriteAstronauta)
                contadorColumna1 += 1
                if contadorColumna1 >= 8:
                    timerAstronauta1 = -1000

            if timerAstronauta2 >= random.randint(6,25):
                timerAstronauta2 = 0
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, coordAstronautas[1]+100)
                listaAstronautas.append(spriteAstronauta)
                contadorColumna2 += 1
                if contadorColumna2 >= 7:
                    timerAstronauta2 = -1000

            if timerAstronauta3 >= random.randint(4,30):
                timerAstronauta3 = 0
                spriteAstronauta = crearAstronauta(imgNaut1, ANCHO, coordAstronautas[2]+100)
                listaAstronautas.append(spriteAstronauta)
                contadorColumna3 += 1
                if contadorColumna3 >= 9:
                    timerAstronauta3 = -1000

            if alienSlot1 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[0] + alienY)

                if timerBala1 >= 14 and timerBala1 <14.1:
                    pistola.play()
                if timerBala1 >= 17:

                    timerBala1 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[0] + 77)
                    listaBalas1.append(spriteBala)

                actualizarBalas(listaBalas1)
                dibujarBalas(ventana, listaBalas1)
                verificarColisiones(listaBalas1, listaAstronautas, restantesLvl1)

            if alienSlot2 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[0] + alienY)

                if timerBala2 >= 14 and timerBala2 <14.1:
                    pistola.play()
                if timerBala2 >= 17:
                    timerBala2 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[0] + 77)
                    listaBalas2.append(spriteBala)

                actualizarBalas(listaBalas2)
                dibujarBalas(ventana, listaBalas2)
                verificarColisiones(listaBalas2, listaAstronautas, restantesLvl1)

            if alienSlot3 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[0] + alienY)

                if timerBala3 >= 14 and timerBala3 <14.1:
                    pistola.play()
                if timerBala3 >= 15:
                    pistola.play()
                if timerBala3 >= 17:
                    timerBala3 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[0] + 77)
                    listaBalas3.append(spriteBala)

                actualizarBalas(listaBalas3)
                dibujarBalas(ventana, listaBalas3)
                verificarColisiones(listaBalas3, listaAstronautas, restantesLvl1, impacto)

            if alienSlot4 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[0] + alienY)

                if timerBala4 >= 14 and timerBala4 <14.1:
                    pistola.play()
                if timerBala4 >= 17:
                    timerBala4 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[0] + 77)
                    listaBalas4.append(spriteBala)

                actualizarBalas(listaBalas4)
                dibujarBalas(ventana, listaBalas4)
                verificarColisiones(listaBalas4, listaAstronautas, restantesLvl1)

            if alienSlot5 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[0] + alienY)

                if timerBala5 >= 14 and timerBala5 <14.1:
                    pistola.play()
                if timerBala5 >= 17:
                    timerBala5 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[0] + 77)
                    listaBalas5.append(spriteBala)

                actualizarBalas(listaBalas5)
                dibujarBalas(ventana, listaBalas5)
                verificarColisiones(listaBalas5, listaAstronautas, restantesLvl1)

            if alienSlot6 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[1] + alienY)

                if timerBala6 >= 14 and timerBala6 <14.1:
                    pistola.play()
                if timerBala6 >= 17:
                    timerBala6 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[1] + 77)
                    listaBalas6.append(spriteBala)

                actualizarBalas(listaBalas6)
                dibujarBalas(ventana, listaBalas6)
                verificarColisiones(listaBalas6, listaAstronautas, restantesLvl1)

            if alienSlot7 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[1] + alienY)

                if timerBala7 >= 14 and timerBala7 <14.1:
                    pistola.play()
                if timerBala7 >= 17:
                    timerBala7 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[1] + 77)
                    listaBalas7.append(spriteBala)

                actualizarBalas(listaBalas7)
                dibujarBalas(ventana, listaBalas7)
                verificarColisiones(listaBalas7, listaAstronautas, restantesLvl1)

            if alienSlot8 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[1] + alienY)

                if timerBala8 >= 14 and timerBala8 <14.1:
                    pistola.play()
                if timerBala8 >= 17:
                    timerBala8 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[1] + 77)
                    listaBalas8.append(spriteBala)

                actualizarBalas(listaBalas8)
                dibujarBalas(ventana, listaBalas8)
                verificarColisiones(listaBalas8, listaAstronautas, restantesLvl1)

            if alienSlot9 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[1] + alienY)

                if timerBala9 >= 14 and timerBala9 <14.1:
                    pistola.play()
                if timerBala9 >= 17:
                    timerBala9 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[1] + 77)
                    listaBalas9.append(spriteBala)

                actualizarBalas(listaBalas9)
                dibujarBalas(ventana, listaBalas9)
                verificarColisiones(listaBalas9, listaAstronautas, restantesLvl1)

            if alienSlot10 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[1] + alienY)

                if timerBala10 >= 14 and timerBala10 <14.1:
                    pistola.play()
                if timerBala10 >= 17:
                    timerBala10 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[1] + 77)
                    listaBalas10.append(spriteBala)

                actualizarBalas(listaBalas10)
                dibujarBalas(ventana, listaBalas10)
                verificarColisiones(listaBalas10, listaAstronautas, restantesLvl1)

            if alienSlot11 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[2] + alienY)

                if timerBala11 >= 14 and timerBala11 <14.1:
                    pistola.play()
                if timerBala11 >= 17:
                    timerBala11 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[2] + 77)
                    listaBalas11.append(spriteBala)

                actualizarBalas(listaBalas11)
                dibujarBalas(ventana, listaBalas11)
                verificarColisiones(listaBalas11, listaAstronautas, restantesLvl1)

            if alienSlot12 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[2] + alienY)

                if timerBala12 >= 14 and timerBala12 <14.1:
                    pistola.play()
                if timerBala12 >= 17:
                    timerBala12 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[2] + 77)
                    listaBalas12.append(spriteBala)

                actualizarBalas(listaBalas12)
                dibujarBalas(ventana, listaBalas12)
                verificarColisiones(listaBalas12, listaAstronautas, restantesLvl1)

            if alienSlot13 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[2] + alienY)

                if timerBala13 >= 14 and timerBala13 <14.1:
                    pistola.play()
                if timerBala13 >= 17:
                    timerBala13 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[2] + 77)
                    listaBalas13.append(spriteBala)

                actualizarBalas(listaBalas13)
                dibujarBalas(ventana, listaBalas13)
                verificarColisiones(listaBalas13, listaAstronautas, restantesLvl1)

            if alienSlot14 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[2] + alienY)

                if timerBala14 >= 14 and timerBala14 <14.1:
                    pistola.play()
                if timerBala14 >= 17:
                    timerBala14 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[2] + 77)
                    listaBalas14.append(spriteBala)

                actualizarBalas(listaBalas14)
                dibujarBalas(ventana, listaBalas14)
                verificarColisiones(listaBalas14, listaAstronautas, restantesLvl1)

            if alienSlot15 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[2] + alienY)

                if timerBala15 >= 14 and timerBala15 <14.1:
                    pistola.play()
                if timerBala15 >= 17:
                    timerBala15 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[2] + 77)
                    listaBalas15.append(spriteBala)

                actualizarBalas(listaBalas15)
                dibujarBalas(ventana, listaBalas15)
                verificarColisiones(listaBalas15, listaAstronautas, restantesLvl1)

            actualizarAstronautas(listaAstronautas)
            dibujarAstronauta(ventana, listaAstronautas)

            if verificarSiPierde(listaAstronautas):
                estado = PERDER
                imprimirScore = fuenteScore.render("", 1, BLANCO)

            if len(restantesLvl1) == 0:
                estado = GANAR

        if estado == INFINITO:
            dibujarNivel1(ventana, jugando, slot, btnAlien100)
            textoScore = fuenteHS.render("SCORE: %d" % len(puntajeHighscore), 1, BLANCO)
            textoModoInfinito = fuenteNivel.render("MODO INFINITO", 1, BLANCO)
            textoElixir = fuenteNivel.render(("%d") % elixir, 1, BLANCO)
            ventana.blit(textoScore, (615, 75))
            ventana.blit(textoElixir, (65, 103))
            ventana.blit(textoModoInfinito, (615, 40))

            if timerGeneral >= 50:
                elixir += 100
                blop.play()
                timerGeneral = 0

            if timerAstronauta1 >= random.randint(5,65):
                timerAstronauta1 = 0
                spriteAstronauta = crearAstronauta(listaImgsNauts[random.randint(0,1)], ANCHO, coordAstronautas[0] + 100)
                listaAstronautas.append(spriteAstronauta)

            if timerAstronauta2 >= random.randint(5,65):
                timerAstronauta2 = 0
                spriteAstronauta = crearAstronauta(listaImgsNauts[random.randint(0,1)], ANCHO, coordAstronautas[1] + 100)
                listaAstronautas.append(spriteAstronauta)

            if timerAstronauta3 >= random.randint(5,65):
                timerAstronauta3 = 0
                spriteAstronauta = crearAstronauta(listaImgsNauts[random.randint(0,1)], ANCHO, coordAstronautas[2] + 100)
                listaAstronautas.append(spriteAstronauta)

            if alienSlot1 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[0] + alienY)

                if timerBala1 >= tiempoBala - 3 and timerBala1 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala1 >= tiempoBala:
                    timerBala1 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[0] + 77)
                    listaBalas1.append(spriteBala)

                actualizarBalas(listaBalas1)
                dibujarBalas(ventana, listaBalas1)
                verificarColisionesInfinito(listaBalas1, listaAstronautas, puntajeHighscore)

            if alienSlot2 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[0] + alienY)

                if timerBala2 >= tiempoBala - 3 and timerBala2 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala2 >= tiempoBala:
                    timerBala2 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[0] + 77)
                    listaBalas2.append(spriteBala)

                actualizarBalas(listaBalas2)
                dibujarBalas(ventana, listaBalas2)
                verificarColisionesInfinito(listaBalas2, listaAstronautas, puntajeHighscore)

            if alienSlot3 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[0] + alienY)

                if timerBala3 >= tiempoBala - 3 and timerBala3 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala3 >= tiempoBala:
                    timerBala3 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[0] + 77)
                    listaBalas3.append(spriteBala)

                actualizarBalas(listaBalas3)
                dibujarBalas(ventana, listaBalas3)
                verificarColisionesInfinito(listaBalas3, listaAstronautas, puntajeHighscore)

            if alienSlot4 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[0] + alienY)

                if timerBala4 >= tiempoBala - 3 and timerBala4 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala4 >= tiempoBala:
                    timerBala4 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[0] + 77)
                    listaBalas4.append(spriteBala)

                actualizarBalas(listaBalas4)
                dibujarBalas(ventana, listaBalas4)
                verificarColisionesInfinito(listaBalas4, listaAstronautas, puntajeHighscore)

            if alienSlot5 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[0] + alienY)

                if timerBala5 >= tiempoBala - 3 and timerBala5 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala5 >= tiempoBala:
                    timerBala5 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[0] + 77)
                    listaBalas5.append(spriteBala)

                actualizarBalas(listaBalas5)
                dibujarBalas(ventana, listaBalas5)
                verificarColisionesInfinito(listaBalas5, listaAstronautas, puntajeHighscore)

            if alienSlot6 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[1] + alienY)

                if timerBala6 >= tiempoBala - 3 and timerBala6 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala6 >= tiempoBala:
                    timerBala6 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[1] + 77)
                    listaBalas6.append(spriteBala)

                actualizarBalas(listaBalas6)
                dibujarBalas(ventana, listaBalas6)
                verificarColisionesInfinito(listaBalas6, listaAstronautas, puntajeHighscore)

            if alienSlot7 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[1] + alienY)

                if timerBala7 >= tiempoBala - 3 and timerBala7 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala7 >= tiempoBala:
                    timerBala7 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[1] + 77)
                    listaBalas7.append(spriteBala)

                actualizarBalas(listaBalas7)
                dibujarBalas(ventana, listaBalas7)
                verificarColisionesInfinito(listaBalas7, listaAstronautas, puntajeHighscore)

            if alienSlot8 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[1] + alienY)

                if timerBala8 >= tiempoBala - 3 and timerBala8 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala8 >= tiempoBala:
                    timerBala8 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[1] + 77)
                    listaBalas8.append(spriteBala)

                actualizarBalas(listaBalas8)
                dibujarBalas(ventana, listaBalas8)
                verificarColisionesInfinito(listaBalas8, listaAstronautas, puntajeHighscore)

            if alienSlot9 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[1] + alienY)

                if timerBala9 >= tiempoBala - 3 and timerBala9 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala9 >= tiempoBala:
                    timerBala9 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[1] + 77)
                    listaBalas9.append(spriteBala)

                actualizarBalas(listaBalas9)
                dibujarBalas(ventana, listaBalas9)
                verificarColisionesInfinito(listaBalas9, listaAstronautas, puntajeHighscore)

            if alienSlot10 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[1] + alienY)

                if timerBala10 >= tiempoBala - 3 and timerBala10 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala10 >= tiempoBala:
                    timerBala10 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[1] + 77)
                    listaBalas10.append(spriteBala)

                actualizarBalas(listaBalas10)
                dibujarBalas(ventana, listaBalas10)
                verificarColisionesInfinito(listaBalas10, listaAstronautas, puntajeHighscore)

            if alienSlot11 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[0] + difAlienX, slotsY[2] + alienY)

                if timerBala11 >= tiempoBala - 3 and timerBala11 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala11 >= tiempoBala:
                    timerBala11 = 0
                    spriteBala = crearBala(bala100, slotsX[0] + 43, slotsY[2] + 77)
                    listaBalas11.append(spriteBala)

                actualizarBalas(listaBalas11)
                dibujarBalas(ventana, listaBalas11)
                verificarColisionesInfinito(listaBalas11, listaAstronautas, puntajeHighscore)

            if alienSlot12 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[1] + difAlienX, slotsY[2] + alienY)

                if timerBala12 >= tiempoBala - 3 and timerBala12 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala12 >= tiempoBala:
                    timerBala12 = 0
                    spriteBala = crearBala(bala100, slotsX[1] + 43, slotsY[2] + 77)
                    listaBalas12.append(spriteBala)

                actualizarBalas(listaBalas12)
                dibujarBalas(ventana, listaBalas12)
                verificarColisionesInfinito(listaBalas12, listaAstronautas, puntajeHighscore)

            if alienSlot13 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[2] + difAlienX, slotsY[2] + alienY)

                if timerBala13 >= tiempoBala - 3 and timerBala13 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala13 >= tiempoBala:
                    timerBala13 = 0
                    spriteBala = crearBala(bala100, slotsX[2] + 43, slotsY[2] + 77)
                    listaBalas13.append(spriteBala)

                actualizarBalas(listaBalas13)
                dibujarBalas(ventana, listaBalas13)
                verificarColisionesInfinito(listaBalas13, listaAstronautas, puntajeHighscore)

            if alienSlot14 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[3] + difAlienX, slotsY[2] + alienY)

                if timerBala14 >= tiempoBala - 3 and timerBala14 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala14 >= tiempoBala:
                    timerBala14 = 0
                    spriteBala = crearBala(bala100, slotsX[3] + 43, slotsY[2] + 77)
                    listaBalas14.append(spriteBala)

                actualizarBalas(listaBalas14)
                dibujarBalas(ventana, listaBalas14)
                verificarColisionesInfinito(listaBalas14, listaAstronautas, puntajeHighscore)

            if alienSlot15 == 1:
                dibujarAlien(ventana, imgAlien100, slotsX[4] + difAlienX, slotsY[2] + alienY)

                if timerBala15 >= tiempoBala - 3 and timerBala15 < tiempoBala - 2.9:
                    pistola.play()
                if timerBala15 >= tiempoBala:
                    timerBala15 = 0
                    spriteBala = crearBala(bala100, slotsX[4] + 43, slotsY[2] + 77)
                    listaBalas15.append(spriteBala)

                actualizarBalas(listaBalas15)
                dibujarBalas(ventana, listaBalas15)
                verificarColisionesInfinito(listaBalas15, listaAstronautas, puntajeHighscore)

            actualizarAstronautas(listaAstronautas)
            dibujarAstronauta(ventana, listaAstronautas)

            if verificarSiPierde(listaAstronautas):
                estado = PERDER

                puntajeAnterior = open("highscore", "r")

                for puntaje in puntajeAnterior:
                    score = int(puntaje)

                puntajeAnterior.close()

                puntajeMax = open("highscore", "w")

                if score < len(puntajeHighscore):
                    puntajeMax.write(str(len(puntajeHighscore)))
                else:
                    puntajeMax.write(str(score))
                puntajeMax.close()

                imprimirScore = fuenteScore.render("Score: %d" % len(puntajeHighscore), 1, BLANCO)

        if estado == GANAR:
            dibujarPartidaGanada(ventana, ganar, btnSigNivel)

        if estado == PERDER:
            dibujarPartidaPerdida(ventana, perdida, btnMenu, imprimirScore)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

        timerBala1 += 1/10
        timerBala2 += 1 / 10
        timerBala3 += 1 / 10
        timerBala4 += 1 / 10
        timerBala5 += 1 / 10
        timerBala6 += 1 / 10
        timerBala7 += 1 / 10
        timerBala8 += 1 / 10
        timerBala9 += 1 / 10
        timerBala10 += 1 / 10
        timerBala11 += 1 / 10
        timerBala12 += 1 / 10
        timerBala13 += 1 / 10
        timerBala14 += 1 / 10
        timerBala15 += 1 / 10

        timerAstronauta1 += 1/10
        timerAstronauta2 += 1 / 10
        timerAstronauta3 += 1 / 10

        timerGeneral += 1/10

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Función principal
def main():
    dibujar()


#Llamar a la función principal
main()
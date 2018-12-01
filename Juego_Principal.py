# Rubén Villalpando Bremont
# Proyecto final de fundamentos de programación, Juego

import pygame, random

# Dimensiones de la pantalla
ALTO = 600
ANCHO = 800

# colores
NEGRO = (0, 0, 0)
VERDE = (20, 210, 50)
ROJO = (200, 32, 50)
BLANCO = (255, 255, 255)

# Estados de juego y niveles
MENU = 0
INSTRUCCIONES = 1
PUNTUACIONES = 2
JUGANDO1 = 3
JUGANDO2 = 4
JUGANDO3 = 5


# Estados del personaje principal
SALTO = 0
ABAJO = 1
QUIETO = 2
DERECHA = 3
IZQUIERDA = 4


def dibujarNivelTres(ventana, spritePersonaje, listaParedes3, diccionarioEnemigoVidas3, listaFlechasD,
                            listaFlechasI, listaFlechasEnD, listaFlechasEnI):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)
    for pared in listaParedes3:
        ventana.blit(pared.image, pared.rect)
    for enemigo in diccionarioEnemigoVidas3:
        ventana.blit(enemigo.image, enemigo.rect)
    for flecha in listaFlechasD:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasI:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasEnI:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasEnD:
        ventana.blit(flecha.image, flecha.rect)


# Funcion que checa si el personaje agarró a la flecha mejorada
def checarPersonajeObtuvoFlechaMejorada(spritePersonaje, listaFlechasPorAgarrar):
    xP, yP, anP, altP = spritePersonaje.rect
    xF, yF, anF, altF = listaFlechasPorAgarrar[0].rect
    xDentroFlecha = xF <= xP + anP <= xF + anF or xF <= xP <= xF + anF
    yDentroFlecha = yF <= yP + altP <= yF + altF or yF <= yP <= yF + altF
    if xDentroFlecha and yDentroFlecha:
        listaFlechasPorAgarrar.remove(listaFlechasPorAgarrar[0])
        return 10, 25, True, 2
    else:
        return 7, 9, False, 1


def crearListaPuntuaciones():
    archivo = open("puntuaciones_altas.txt", "r", encoding="UTF-8")
    puntuaciones = []
    for linea in archivo:
        datos = linea.split()
        puntuaciones.append(datos[1])
    puntuaciones = [int(x) for x in puntuaciones]
    archivo.close()
    return puntuaciones


def escribirPuntuacionesNuevoArchivo(listaPuntuaciones):
    archivo = open("Puntuaciones_altas.txt", "w", encoding="UTF-8")
    listaPuntuaciones.sort(reverse=True)
    if len(listaPuntuaciones) > 10:
        listaPuntuaciones.pop()
    for x in range(1, len(listaPuntuaciones) + 1):
        stringArchivo = str(x) + " " + str(listaPuntuaciones[x-1]) + "\n"
        archivo.write(stringArchivo)
    archivo.close()

# Función para dibujar todos los elementos del primer nivel
def dibujarNivelUno(ventana, spritePersonaje, listaParedes, diccionarioEnemigos,
                    listaFlechasD, listaFlechasI, listaFlechasEnI, listaFlechasEnD, spritePuerta):
    ventana.blit(spritePuerta.image, spritePuerta.rect)
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)
    for enemigo in diccionarioEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
    for flecha in listaFlechasI:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasD:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasEnI:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasEnD:
        ventana.blit(flecha.image, flecha.rect)
    for pared in listaParedes:
        ventana.blit(pared.image, pared.rect)



# Función para dibujar todos los elementos del srgundo nivel
def dibujarNivelDos(ventana, spritePersonaje, listaParedes, diccionarioEnemigos, listaFlechasD,
                            listaFlechasI, listaFlechasEnD, listaFlechasEnI, spritePuerta, listaFlechasPorAgarrar):
    ventana.blit(spritePuerta.image, spritePuerta.rect)
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)
    for flecha in listaFlechasPorAgarrar:
        ventana.blit(flecha.image, flecha.rect)
    for pared in listaParedes:
        ventana.blit(pared.image, pared.rect)
    for enemigo in diccionarioEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
    for flecha in listaFlechasD:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasI:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasEnD:
        ventana.blit(flecha.image, flecha.rect)
    for flecha in listaFlechasEnI:
        ventana.blit(flecha.image, flecha.rect)



# Función que dibuja al menú
def dibujarMenu(ventana, imgBtnJugar, listaParedes, imgBtnInstrucciones, imgPuntuacionesAltas):
    ventana.blit(imgBtnJugar, (ANCHO // 2 - 100, ALTO // 4))
    ventana.blit(imgBtnInstrucciones, (ANCHO//2-100, ALTO//4 + 100))
    ventana.blit(imgPuntuacionesAltas, (ANCHO//2 -100, ALTO//4 + 200))
    for pared in listaParedes:
        ventana.blit(pared.image, pared.rect)

# Dibuja las instrucciones del juego
def dibujarInstrucciones(ventana, imgInstrucciones):
    ventana.blit(imgInstrucciones, (0, 0))


# Dibuja las puntuaciones más altas
def dibujarPuntuaciones(ventana, tipoDeLetra2):
    archivo = open("puntuaciones_altas.txt", "r", encoding="UTF-8")
    puntuaciones = []
    for linea in archivo:
        datos = linea.split()
        puntuaciones.append(datos[1])
    titulo = tipoDeLetra2.render("PUNTUACIONES MÁS ALTAS", False, BLANCO)
    ventana.blit(titulo, (ANCHO//2-150, 0))
    for x in range(1, len(puntuaciones)+1):
        puntos = puntuaciones[x-1]
        stringPuntos = str(x) + ".................." + puntos
        puntuacionesEnPantalla = tipoDeLetra2.render(stringPuntos, False, BLANCO)
        ventana.blit(puntuacionesEnPantalla, (50, x*55))


def checarPersonajeEnPiso(listaParedes, spritePersonaje): # Función que checa si el personaje ya cayó al piso
    xP, yP, anP, altP = spritePersonaje.rect
    for pared in listaParedes:
        xPar, yPar, anPar, altPar = pared.rect
        xPersonajeDentroDePared = xPar < xP + 1 < xPar + anPar or xPar < xP + anP < xPar + anPar
        yPersonajeChocoConPared = yPar <= yP + altP <= yPar+altPar
        if xPersonajeDentroDePared and yPersonajeChocoConPared: # Checar si coincide que cayó en el piso
            return True
    return False


def checarPersonajePared(listaParedes, spritePersonaje): # Checa los choques contra las paredes
    xP, yP, anP, altP = spritePersonaje.rect
    for pared in listaParedes:
        xPar, yPar, anPar, altPar = pared.rect
        yPersonajeDentroDePared = yPar < yP+altP-1 <= yPar + altPar or yPar <= yP <= yPar + altPar-1
        if xPar+anPar == xP and yPersonajeDentroDePared: # Checar si choco por la derecha.
            return False, True
        elif xPar == xP + anP and yPersonajeDentroDePared: # Checar si choco por la izquierda
            return True, False
    return False, False


# Checa si el personaje chocó con el techo
def checarPersonajeChocoConTecho(listaParedes, spritePersonaje, contadorSalto):
    xP, yP, anP, altP = spritePersonaje.rect
    for pared in listaParedes:
        xPar, yPar, anPar, altPar = pared.rect
        xPersonajeDentroDePared = xPar < xP + 1 < xPar + anPar or xPar < xP + anP < xPar + anPar
        chocoConElTecho = yPar+altPar >= yP >= yPar
        if xPersonajeDentroDePared and chocoConElTecho:
            return 1000
    return contadorSalto


def dibujarVidas(ventana, spritePersonaje, vidaPersonaje, diccionarioEnemigos): # Dibuja las vidas de los enemigos y el personaje Principal
    pygame.draw.rect(ventana, ROJO, [spritePersonaje.rect.left-20, spritePersonaje.rect.bottom - 80, 100, 10])
    pygame.draw.rect(ventana, VERDE, [spritePersonaje.rect.left - 20, spritePersonaje.rect.bottom - 80, vidaPersonaje, 10])
    for enemigo in diccionarioEnemigos:
        vidaEnemigo = diccionarioEnemigos[enemigo]
        pygame.draw.rect(ventana, ROJO, [enemigo.rect.left - 20, enemigo.rect.bottom - 80, 100, 10])
        pygame.draw.rect(ventana, VERDE, [enemigo.rect.left - 20, enemigo.rect.bottom - 80, vidaEnemigo, 10])


def dibujarVidas3(ventana, spritePersonaje, vidaPersonaje, diccionarioEnemigos): # Dibuja las vidas de los enemigos y el personaje Principal
    pygame.draw.rect(ventana, ROJO, [spritePersonaje.rect.left-20, spritePersonaje.rect.bottom - 80, 100, 10])
    pygame.draw.rect(ventana, VERDE, [spritePersonaje.rect.left - 20, spritePersonaje.rect.bottom - 80, vidaPersonaje, 10])
    for enemigo in diccionarioEnemigos:
        vidaEnemigo = diccionarioEnemigos[enemigo]
        pygame.draw.rect(ventana, ROJO, [enemigo.rect.left - 20, enemigo.rect.bottom - 80, 100, 10])
        pygame.draw.rect(ventana, VERDE, [enemigo.rect.left - 20, enemigo.rect.bottom - 80, vidaEnemigo//5, 10])


# Checa colisiones entre las flechas y cualquier personaje
def checarFlechasPersonajes(listaFlechasD, listaFlechasI, listaFlechasEnD, listaFlechasEnI,
                            diccionarioEnemigos, spritePersonaje, vidaPersonaje, ataquePersonaje, puntos):
    xP, yP, anP, altP = spritePersonaje.rect
    for f in range(len(listaFlechasEnI)-1, -1, -1):
        flecha = listaFlechasEnI[f]
        xf, yf, anf, altf = flecha.rect
        if xf + anf <= 0:
            listaFlechasEnI.remove(flecha)
        if xP<= xf <= xP + anP and (yP <= yf <= yP + altP or yP <= yf + altf <= yP + altP): # si el personaje le da una flecha
            listaFlechasEnI.remove(flecha)
            vidaPersonaje -= 10
            puntos[0] -= 10
    for f in range(len(listaFlechasI)-1, -1, -1):
        flecha = listaFlechasI[f]
        xf, yf, anf, altf = flecha.rect
        if xf + anf <= 0:
            listaFlechasI.remove(flecha)
        for enemigo in diccionarioEnemigos:
            xe, ye, ane, alte = enemigo.rect
            if xe <= xf <= xe + ane and (ye <= yf <= ye + alte or ye <= yf + altf <= ye + alte): # Checa si las flechas chocaron con algún enemigo, quita la flecha y le baja vida al enemigo
                listaFlechasI.remove(flecha)
                diccionarioEnemigos[enemigo] -= ataquePersonaje
                vidaEnemigo = diccionarioEnemigos[enemigo]
                puntos[0] += 15
                if vidaEnemigo <= 0:
                    del diccionarioEnemigos[enemigo]
                    puntos[0] += 50
                    return vidaPersonaje
    for f in range(len(listaFlechasEnD)-1, -1, -1): # Checa choques entre las flechas de los enemigos y el personaje
        flecha = listaFlechasEnD[f]
        xf, yf, anf, altf = flecha.rect
        if xf > ANCHO:
            listaFlechasEnD.remove(flecha)
        if xP + anP >= xf + anf >= xP and (yP <= yf <= yP + altP or yP <= yf + altf <= yP + altP):
            listaFlechasEnD.remove(flecha)
            vidaPersonaje -= 10
            puntos[0] -= 10
    for f in range(len(listaFlechasD)-1, -1, -1): # Checa choques entre enemigos y flechas del personaje
        flecha = listaFlechasD[f]
        xf, yf, anf, altf = flecha.rect
        if xf > ANCHO:
            listaFlechasD.remove(flecha)
        for enemigo in diccionarioEnemigos:
            xe, ye, ane, alte = enemigo.rect
            if xe + ane >= xf + anf >= xe and (ye <= yf <= ye + alte or ye <= yf + altf <= ye + alte):
                listaFlechasD.remove(flecha)
                diccionarioEnemigos[enemigo] -= ataquePersonaje
                vidaEnemigo = diccionarioEnemigos[enemigo]
                puntos[0] += 15
                if vidaEnemigo <= 0:
                    del diccionarioEnemigos[enemigo]
                    puntos[0] += 50
                    return vidaPersonaje
    return vidaPersonaje


# Esta función hace que el personaje cambie de dirección hacia el personaje
def checarSiEnemigoVioPersonaje(diccionarioEnemigosDirecciones, spritePersonaje):
    xP, yP, anP, altP = spritePersonaje.rect
    for enemigo in diccionarioEnemigosDirecciones:
        xE, yE, anE, altE = enemigo.rect
        if xP < xE and yE <= yP + altP-1 <= yE + altE:
            diccionarioEnemigosDirecciones[enemigo] = IZQUIERDA
        elif xP > xE and yE <= yP + altP-1 <= yE + altE:
            diccionarioEnemigosDirecciones[enemigo] = DERECHA


# Quita las flechas cuando chocan con alguna pared
def checarColisionesFlechasParedes(listaFlechasEnD, listaFlechasEnI, listaParedes, listaFlechasI, listaFlechasD):
    for p in range(len(listaParedes)-1, -1, -1):
        pared = listaParedes[p]
        xP, yP, anP, altP = pared.rect
        for f in range(len(listaFlechasD)-1, -1, -1):
            flecha = listaFlechasD[f]
            xF, yF, anF, altF = flecha.rect
            if xP <= xF + anF <= xP + anP and (yP <= yF <= yP + altP or yP <= yF + altF <= yP + altP):
                listaFlechasD.remove(flecha)
        for f in range(len(listaFlechasI)-1, -1, -1):
            flecha = listaFlechasI[f]
            xF, yF, anF, altF = flecha.rect
            if xP + anP >= xF >= xP and (yP <= yF <= yP + altP or yP <= yF + altF <= yP + altP):
                listaFlechasI.remove(flecha)
        for f in range(len(listaFlechasEnD)-1, -1, -1):
            flecha = listaFlechasEnD[f]
            xF, yF, anF, altF = flecha.rect
            if xP <= xF + anF <= xP + anP and (yP <= yF <= yP + altP or yP <= yF + altF <= yP + altP):
                listaFlechasEnD.remove(flecha)
        for f in range(len(listaFlechasEnI)-1, -1, -1):
            flecha = listaFlechasEnI[f]
            xF, yF, anF, altF = flecha.rect
            if xP + anP >= xF >= xP and (yP <= yF <= yP + altP or yP <= yF + altF <= yP + altP):
                listaFlechasEnI.remove(flecha)

def personajeChocoEnemigo(spritePersonaje, diccionarioEnemigosVidas, vidaPersonaje, puntos, ESTADO): # checa si chocan el personaje y los enemigos, lo manda al principio del nivel
    xP, yP, anP, altP = spritePersonaje.rect
    for enemigo in diccionarioEnemigosVidas:
        xE, yE, anE, altE = enemigo.rect
        xDentroEnemigo = xE <= xP + anP <= xE + anE or xE <= xP <= xE + anE
        yDentroEnemigo = yE <= yP + altP <= yE + altE or yE <= yP <= yE + altE
        if xDentroEnemigo and yDentroEnemigo:
            vidaPersonaje-=20
            diccionarioEnemigosVidas[enemigo] -= 20
            if ESTADO == JUGANDO1:
                spritePersonaje.rect.left = 0
                spritePersonaje.rect.bottom = ALTO//2 + spritePersonaje.rect.height//2
            elif ESTADO == JUGANDO2:
                spritePersonaje.rect.left = 0
                spritePersonaje.rect.bottom = ALTO-50
            elif ESTADO == JUGANDO3:
                spritePersonaje.rect.left = 0
                spritePersonaje.rect.bottom = 100
            puntos[0] -= 20
            if diccionarioEnemigosVidas[enemigo] <= 0:
                del diccionarioEnemigosVidas[enemigo]
                puntos[0] += 50
                return vidaPersonaje
    return vidaPersonaje


# Función que checa si puede avanzar al siguiente nivel
def checarPersonajePuerta(spritePuerta, spritePersonaje):
    xPer, yPer, anPer, altPer = spritePersonaje.rect
    xP, yP, anP, altP = spritePuerta.rect
    xDentroPuerta = xP <= xPer + anPer <= xP + anP or xP <= xPer <= xP + anP
    yDentroPuerta = yP <= yPer + altPer <= yP + altP or yP <= yPer <= yP + altP
    if xDentroPuerta and yDentroPuerta:
        personajeChocoConPuerta = True
    else:
        personajeChocoConPuerta = False
    return personajeChocoConPuerta

def correrJuego(listaPuntuaciones): # Aquí ocurre el juego principal
    pygame.init()

    # Aquí se cargan los tipos de letras
    pygame.font.init()
    tipoDeLetra = pygame.font.SysFont('georgia', 60, True)
    tipoDeLetra2 = pygame.font.SysFont('bahnschrift', 24, True)
    gameOver = tipoDeLetra.render('Game Over', False, BLANCO)
    escMenu = tipoDeLetra2.render("'ESC' para volver al menu principal", False, BLANCO)
    victory = tipoDeLetra.render("VICTORIA!!!", False, BLANCO)

    # Sonidos del juego
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.01)
    sonidoFlecha = pygame.mixer.Sound("sonidoFlecha.ogg")
    sonidoFlecha.set_volume(1.0)


    # Crear la ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    # Seccion de los sprites (0,0) abajo izquierda

    # Personaje principal
    imgPersonajeD = pygame.image.load("personajePrincipal.png") # personaje viendo a la derecha
    imgPersonajeI = pygame.image.load("personajePrincipal2.png") # personaje viendo a la izquierda
    imgPersonajeMuerto = pygame.image.load("personajePrincipalMuerto.png") # Personaje acostado indicando que ya se murió
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonajeD
    spritePersonaje.rect = imgPersonajeD.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO//2 + spritePersonaje.rect.height//2

    # Flechas que lanza el personaje principa
    imgFlechaD = pygame.image.load("flecha.png")
    imgFlechaI = pygame.image.load("flecha2.png")
    imgFlechaDoradaD = pygame.image.load("flecha3.png")
    imgFlechaDoradaI = pygame.image.load("flecha4.png")
    listaFlechasD = []
    listaFlechasI = []

    # Flechas de los enemigos
    listaFlechasEnI = [] # Flechas enemigas que van a la izquierda
    listaFlechasEnD = [] # Flechas enemigas que van a la derecha

    # Menu
    imgPared = pygame.image.load("pared.jpg")
    listaParedesMenu = []
    for x in range(0, ANCHO+1, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = 50
        listaParedesMenu.append(spritePared)
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = ALTO
        listaParedesMenu.append(spritePared)
    for y in range(50, ALTO-49, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = 0
        spritePared.rect.bottom = y
        listaParedesMenu.append(spritePared)
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = ANCHO-50
        spritePared.rect.bottom = y
        listaParedesMenu.append(spritePared)


    # Nivel 1

    # Puerta por la que sale el personaje para el siguiente nivel
    imgPuertaCerrada = pygame.image.load("puertaCerrada.png")
    imgPuertaAbierta = pygame.image.load("puertaAbierta.png")

    spritePuerta = pygame.sprite.Sprite()
    spritePuerta.rect = imgPuertaCerrada.get_rect()
    spritePuerta.image = imgPuertaCerrada
    spritePuerta.rect.left = ANCHO-50
    spritePuerta.rect.bottom = ALTO-50

    # Paredes de los niveles
    listaParedes1 = []
    for x in range(0, ANCHO - 50 + 1, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = 50
        listaParedes1.append(spritePared)
    for x in range(0, ANCHO - 50 +1, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = ALTO
        listaParedes1.append(spritePared)
    for x in range(50, ALTO - 50 + 1, 50):
        if 250<= x <= 350:
            spritePared = pygame.sprite.Sprite()
            spritePared.image = imgPared
            spritePared.rect = imgPared.get_rect()
            spritePared.rect.left = -50
            spritePared.rect.bottom = x
            listaParedes1.append(spritePared)
        else:
            spritePared = pygame.sprite.Sprite()
            spritePared.image = imgPared
            spritePared.rect = imgPared.get_rect()
            spritePared.rect.left = 0
            spritePared.rect.bottom = x
            listaParedes1.append(spritePared)
    for y in range(50, ALTO-100+1, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = ANCHO-50
        spritePared.rect.bottom = y
        listaParedes1.append(spritePared)
    for x in range (300, 451, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = ALTO-100
        listaParedes1.append(spritePared)

    # Enemigos
    diccionarioEnemigosVidas1 = {}
    diccionarioEnemigosDirecciones1 = {}
    imgEnemigoI = pygame.image.load("enemigo.png") # Enemigo viendo hacia la izquierda
    imgEnemigoD = pygame.image.load("enemigo2.png") # Enemigo viendo hacia la derecha
    spriteEnemigo = pygame.sprite.Sprite()
    spriteEnemigo.image = imgEnemigoD
    spriteEnemigo.rect = imgEnemigoI.get_rect()
    spriteEnemigo.rect.bottom = ALTO - 50
    spriteEnemigo.rect.left = 600
    diccionarioEnemigosVidas1[spriteEnemigo] = 100
    diccionarioEnemigosDirecciones1[spriteEnemigo] = DERECHA



    # Nivel 2

    listaParedes2 = []
    for x in range(0, ANCHO+1, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = ALTO
        listaParedes2.append(spritePared)
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = 50
        listaParedes2.append(spritePared)
        if 550 >= x >= 200:
            spritePared = pygame.sprite.Sprite()
            spritePared.image = imgPared
            spritePared.rect = imgPared.get_rect()
            spritePared.rect.left = x
            spritePared.rect.bottom = 150
            listaParedes2.append(spritePared)
            spritePared = pygame.sprite.Sprite()
            spritePared.image = imgPared
            spritePared.rect = imgPared.get_rect()
            spritePared.rect.left = x
            spritePared.rect.bottom = 300
            listaParedes2.append(spritePared)
            spritePared = pygame.sprite.Sprite()
            spritePared.image = imgPared
            spritePared.rect = imgPared.get_rect()
            spritePared.rect.left = x
            spritePared.rect.bottom = 450
            listaParedes2.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = 16
    spritePared.rect.bottom = 200
    listaParedes2.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = ANCHO-100
    spritePared.rect.bottom = 250
    listaParedes2.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = 50
    spritePared.rect.bottom = 500
    listaParedes2.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = ANCHO-100
    spritePared.rect.bottom = 500
    listaParedes2.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = 50
    spritePared.rect.bottom = 350
    listaParedes2.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = ANCHO - 100
    spritePared.rect.bottom = 350
    listaParedes2.append(spritePared)
    for y in range(50, ALTO + 1 - 50, 50):
        if y <550:
            spritePared = pygame.sprite.Sprite()
            spritePared.image = imgPared
            spritePared.rect = imgPared.get_rect()
            spritePared.rect.left = 0
            spritePared.rect.bottom = y
            listaParedes2.append(spritePared)
        if y == 100:
            continue
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = ANCHO-50
        spritePared.rect.bottom = y
        listaParedes2.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = -50
    spritePared.rect.bottom = 550
    listaParedes2.append(spritePared)

    # Enemigos
    diccionarioEnemigosVidas2 = {}
    diccionarioEnemigosDirecciones2 = {}
    spriteEnemigo1 = pygame.sprite.Sprite()
    spriteEnemigo1.image = imgEnemigoD
    spriteEnemigo1.rect = imgEnemigoI.get_rect()
    spriteEnemigo1.rect.left = ANCHO-250
    spriteEnemigo1.rect.bottom = ALTO-50
    diccionarioEnemigosVidas2[spriteEnemigo1] = 100
    diccionarioEnemigosDirecciones2[spriteEnemigo1] = IZQUIERDA
    spriteEnemigo2 = pygame.sprite.Sprite()
    spriteEnemigo2.image = imgEnemigoD
    spriteEnemigo2.rect = imgEnemigoI.get_rect()
    spriteEnemigo2.rect.left = 200
    spriteEnemigo2.rect.bottom = 400
    diccionarioEnemigosVidas2[spriteEnemigo2] = 100
    diccionarioEnemigosDirecciones2[spriteEnemigo2] = DERECHA
    spriteEnemigo3 = pygame.sprite.Sprite()
    spriteEnemigo3.image = imgEnemigoD
    spriteEnemigo3.rect = imgEnemigoI.get_rect()
    spriteEnemigo3.rect.left = ANCHO-250
    spriteEnemigo3.rect.bottom = 250
    diccionarioEnemigosVidas2[spriteEnemigo3] = 100
    diccionarioEnemigosDirecciones2[spriteEnemigo3] = DERECHA

    # Flecha que agarras para mejorar el daño y frecuencia de disparo de tu personaje
    listaFlechaporAgarrar = []
    spriteFlechaMejorarPersonaje = pygame.sprite.Sprite()
    spriteFlechaMejorarPersonaje.image = imgFlechaDoradaD
    spriteFlechaMejorarPersonaje.rect = imgFlechaDoradaD.get_rect()
    spriteFlechaMejorarPersonaje.rect.bottom = 70
    spriteFlechaMejorarPersonaje.rect.left = 40
    listaFlechaporAgarrar.append(spriteFlechaMejorarPersonaje)

    # Nivel 3

    #Paredes
    listaParedes3 = []
    for x in range(0, ANCHO+1, 50):
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = 50
        listaParedes3.append(spritePared)
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = x
        spritePared.rect.bottom = ALTO
        listaParedes3.append(spritePared)
    for y in range(0, ALTO+1, 50):
        if y == 100:
            pass
        else:
            spritePared = pygame.sprite.Sprite()
            spritePared.image = imgPared
            spritePared.rect = imgPared.get_rect()
            spritePared.rect.left = 0
            spritePared.rect.bottom = y
            listaParedes3.append(spritePared)
        spritePared = pygame.sprite.Sprite()
        spritePared.image = imgPared
        spritePared.rect = imgPared.get_rect()
        spritePared.rect.left = ANCHO-50
        spritePared.rect.bottom = y
        listaParedes3.append(spritePared)
    spritePared = pygame.sprite.Sprite()
    spritePared.image = imgPared
    spritePared.rect = imgPared.get_rect()
    spritePared.rect.left = ANCHO//2
    spritePared.rect.bottom = ALTO - 100
    listaParedes3.append(spritePared)

    # Enemigo nivel 3
    imgBossD = pygame.image.load("enemigo3.png")
    imgBossI = pygame.image.load("enemigo4.png")
    diccionarioEnemigoVidas3 = {}
    diccionarioEnemigoDirecciones3 = {}
    spriteEnemigo4 = pygame.sprite.Sprite()
    spriteEnemigo4.image = imgBossD
    spriteEnemigo4.rect = imgEnemigoI.get_rect()
    spriteEnemigo4.rect.bottom = ALTO-50
    spriteEnemigo4.rect.left = ANCHO//2
    diccionarioEnemigoVidas3[spriteEnemigo4] = 500
    diccionarioEnemigoDirecciones3[spriteEnemigo4] = DERECHA


    # Botones del menu principal
    imgBtnJugar = pygame.image.load("jugarBtn.png")
    imgBtnInstrucciones = pygame.image.load("instruccionesBtn.png")
    imgBtnPuntuacionesAltas = pygame.image.load("puntuacionesAltasBtn.png")

    # Instrucciones
    imgInstrucciones = pygame.image.load("Instrucciones.png")

    # Las variables que estan predeterminadas
    ESTADO = MENU
    movimientoPersonajeY = ABAJO
    puedeSaltar = False
    contadorSalto = 0
    personajeChocoDerecha, personajeChocoIzquierda = False, False
    vidaPersonaje = 100
    movimientoEnemigo = DERECHA
    contadorDisparosEnemigos = 0
    juegoSigue = True
    flechasQuePuedeDisparar = 1
    minAtaque = 7
    maxAtaque = 9
    personajeChocoPuerta = False
    yaEscribioLasPuntuaciones = False
    puntos = [0]
    flechaEstaMejorada = False

    # loop principal del juego
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_w and puedeSaltar:
                    contadorSalto = 0
                    movimientoPersonajeY = SALTO
                    puedeSaltar = False
                if evento.key == pygame.K_DOWN and len(listaFlechasD) + len(listaFlechasI) < flechasQuePuedeDisparar:
                    if spritePersonaje.image == imgPersonajeD:
                        spriteFlecha = pygame.sprite.Sprite()
                        spriteFlecha.rect = imgFlechaD.get_rect()
                        spriteFlecha.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                        spriteFlecha.rect.bottom = spritePersonaje.rect.bottom - 20
                        listaFlechasD.append(spriteFlecha)
                        if flechaEstaMejorada:
                            spriteFlecha.image = imgFlechaDoradaD
                        else:
                            spriteFlecha.image = imgFlechaD
                        sonidoFlecha.play()
                    elif spritePersonaje.image == imgPersonajeI:
                        spriteFlecha = pygame.sprite.Sprite()
                        spriteFlecha.rect = imgFlechaI.get_rect()
                        spriteFlecha.rect.left = spritePersonaje.rect.left
                        spriteFlecha.rect.bottom = spritePersonaje.rect.bottom - 20
                        listaFlechasI.append(spriteFlecha)
                        if flechaEstaMejorada:
                            spriteFlecha.image = imgFlechaDoradaI
                        else:
                            spriteFlecha.image = imgFlechaI
                        sonidoFlecha.play()
                if evento.key == pygame.K_LEFT:
                    spritePersonaje.image = imgPersonajeI
                elif evento.key == pygame.K_RIGHT:
                    spritePersonaje.image = imgPersonajeD
                if evento.key == pygame.K_ESCAPE and not juegoSigue: # regresa al menu principal y regresa los valores del nivel 1 a los predeterminados
                    correrJuego(listaPuntuaciones)

            elif evento.type == pygame.MOUSEBUTTONUP and ESTADO == MENU:
                xm, ym = pygame.mouse.get_pos()
                xbj, ybj = ANCHO // 2 - 100, ALTO // 4 + 50
                xbi, ybi = ANCHO // 2 - 100, ALTO //4 + 150
                xbp, ybp = ANCHO // 2 - 100, ALTO //4 + 250
                if xbj <= xm <= xbj + 200 and ybj >= ym >= ybj - 50:
                    ESTADO = JUGANDO1
                elif xbi <= xm <= xbi + 200 and ybi >= ym >= ybi - 50:
                    ESTADO = INSTRUCCIONES
                elif xbp <= xm <= xbp + 200 and ybp >= ym >= ybp - 50:
                    ESTADO = PUNTUACIONES
        # Función get_pressed() regresa true si esa tecla está siendo presionada
        if pygame.key.get_pressed()[pygame.K_d] and not pygame.key.get_pressed()[pygame.K_a] \
                and not personajeChocoIzquierda and not personajeChocoPuerta:
            movimientoPersonajeX = DERECHA
        elif pygame.key.get_pressed()[pygame.K_a] and not pygame.key.get_pressed()[pygame.K_d]\
                and not personajeChocoDerecha:
            movimientoPersonajeX = IZQUIERDA
        else:
            movimientoPersonajeX = QUIETO
        ventana.fill(NEGRO)

        # NIVEL 1
        if ESTADO == JUGANDO1:
            # Mueve a los sprites
            if juegoSigue:
                # Personaje Principal
                if movimientoPersonajeY == SALTO:
                    spritePersonaje.rect.bottom -= 3
                    if contadorSalto >= 110:
                        movimientoPersonajeY = ABAJO
                    else:
                        contadorSalto += 3
                elif movimientoPersonajeY == ABAJO:
                    if not puedeSaltar:
                        spritePersonaje.rect.bottom += 3
                if movimientoPersonajeX == DERECHA:
                    spritePersonaje.rect.left += 2
                elif movimientoPersonajeX == IZQUIERDA:
                    spritePersonaje.rect.left -= 2

                # Mueve a las flechas disparadas por el personajePrincipal y los enemigos
                for flecha in listaFlechasD:
                    flecha.rect.left += 5
                for flecha in listaFlechasI:
                    flecha.rect.left -= 5
                for flecha in listaFlechasEnD:
                    flecha.rect.left += 5
                for flecha in listaFlechasEnI:
                    flecha.rect.left -= 5

                # Mueve al enemigo del primer nivel
                if movimientoEnemigo == DERECHA:
                    spriteEnemigo.rect.left += 1
                    spriteEnemigo.image = imgEnemigoD
                elif movimientoEnemigo == IZQUIERDA:
                    spriteEnemigo.rect.left -= 1
                    spriteEnemigo.image = imgEnemigoI

                # Obtiene el daño del personaje
                ataquePersonaje = random.randint(minAtaque, maxAtaque)

                # Checa las colisiones
                vidaPersonaje = personajeChocoEnemigo(spritePersonaje, diccionarioEnemigosVidas1, vidaPersonaje, puntos,
                                                      ESTADO)
                puedeSaltar = checarPersonajeEnPiso(listaParedes1, spritePersonaje)
                contadorSalto = checarPersonajeChocoConTecho(listaParedes1, spritePersonaje, contadorSalto)
                personajeChocoIzquierda, personajeChocoDerecha = checarPersonajePared(listaParedes1, spritePersonaje)
                checarColisionesFlechasParedes(listaFlechasEnD, listaFlechasEnI, listaParedes1, listaFlechasI,
                                               listaFlechasD)
                vidaPersonaje = checarFlechasPersonajes(listaFlechasD, listaFlechasI, listaFlechasEnD, listaFlechasEnI,
                                                        diccionarioEnemigosVidas1, spritePersonaje, vidaPersonaje,
                                                        ataquePersonaje, puntos)
                # La función de arriba regresa la vida del personaje si es que sufrió daño y modifica las vidas de los enemigos a través de un diccionario


            # Cambia la dirección del enemigo del primer nivel

                # Función para cambiar al enemigo en dirección del personaje
                checarSiEnemigoVioPersonaje(diccionarioEnemigosDirecciones1, spritePersonaje)

                xe, ye, ane, alte = spriteEnemigo.rect
                if xe + ane >= ANCHO-50:
                    diccionarioEnemigosDirecciones1[spriteEnemigo] = IZQUIERDA
                elif xe <= 50:
                    diccionarioEnemigosDirecciones1[spriteEnemigo] = DERECHA

                # Checa si el enemigo vio al personaje principal y lo persigue

                movimientoEnemigo = diccionarioEnemigosDirecciones1[spriteEnemigo]

                # Hacer que los enemigos disparen
                if contadorDisparosEnemigos >= 1.3 and diccionarioEnemigosVidas1:
                    contadorDisparosEnemigos = 0
                    if spriteEnemigo.image == imgEnemigoI:
                        spriteFlechaI = pygame.sprite.Sprite()
                        spriteFlechaI.image = imgFlechaI
                        spriteFlechaI.rect = imgFlechaI.get_rect()
                        spriteFlechaI.rect.bottom = spriteEnemigo.rect.bottom - spriteEnemigo.rect.height//3
                        spriteFlechaI.rect.left = spriteEnemigo.rect.left - spriteFlechaI.rect.width
                        listaFlechasEnI.append(spriteFlechaI)
                        sonidoFlecha.play()
                    elif spriteEnemigo.image == imgEnemigoD:
                        spriteFlechaD = pygame.sprite.Sprite()
                        spriteFlechaD.image = imgFlechaD
                        spriteFlechaD.rect = imgFlechaD.get_rect()
                        spriteFlechaD.rect.bottom = spriteEnemigo.rect.bottom - spriteEnemigo.rect.height//3
                        spriteFlechaD.rect.left = spriteEnemigo.rect.left + spriteEnemigo.rect.width
                        listaFlechasEnD.append(spriteFlechaD)
                        sonidoFlecha.play()
                if diccionarioEnemigosVidas1:
                    contadorDisparosEnemigos += 1/80

            if not diccionarioEnemigosVidas1:
                spritePuerta.image = imgPuertaAbierta

            #Checa si el personaje se salio Por la puerta, sólo se deja de mover al chocar por la puerta si está cerrada
            if spritePuerta.image == imgPuertaCerrada:
                personajeChocoPuerta = checarPersonajePuerta(spritePuerta, spritePersonaje)
            elif spritePuerta.image == imgPuertaAbierta:
                personajeChocoPuerta = False

            # Dibuja a los sprites en las nuevas coordenadas
            dibujarNivelUno(ventana, spritePersonaje, listaParedes1, diccionarioEnemigosVidas1, listaFlechasD,
                            listaFlechasI, listaFlechasEnI, listaFlechasEnD, spritePuerta)

            # Dibuja las barras de vida de los personajes en la pantalla
            dibujarVidas(ventana, spritePersonaje, vidaPersonaje, diccionarioEnemigosVidas1)

            # checar si el personaje no ha muerto
            if vidaPersonaje <= 0:
                spritePersonaje.image = imgPersonajeMuerto
                juegoSigue = False
                ventana.blit(gameOver, (ANCHO // 2 - 150, ALTO // 3))
                ventana.blit(escMenu, (ANCHO // 2 - 200, (ALTO // 3) + 100))
                if not yaEscribioLasPuntuaciones:
                    yaEscribioLasPuntuaciones = True
                    listaPuntuaciones.append(puntos[0])
                    escribirPuntuacionesNuevoArchivo(listaPuntuaciones)

            # Checar si ya completó el primer nivel
            if spritePersonaje.rect.left > ANCHO:
                ESTADO = JUGANDO2
                spritePersonaje.rect.left = 0
                spritePersonaje.rect.bottom = ALTO-50
                puntos[0] += 100
                contadorDisparosEnemigos = 0
                spritePuerta.image = imgPuertaCerrada
                spritePuerta.rect.bottom = 100


            # Mostrar los puntos en la pantalla
            puntuacion = tipoDeLetra2.render(str(puntos[0]), False, BLANCO)
            ventana.blit(puntuacion, (120, 60))

        # NIVEL 2
        elif ESTADO == JUGANDO2:
            # Mueve a los sprites
            if juegoSigue:
                # Personaje Principal
                if movimientoPersonajeY == SALTO:
                    spritePersonaje.rect.bottom -= 3
                    if contadorSalto >= 110:
                        movimientoPersonajeY = ABAJO
                    else:
                        contadorSalto += 3
                elif movimientoPersonajeY == ABAJO:
                    if not puedeSaltar:
                        spritePersonaje.rect.bottom += 3
                if movimientoPersonajeX == DERECHA:
                    spritePersonaje.rect.left += 2
                elif movimientoPersonajeX == IZQUIERDA:
                    spritePersonaje.rect.left -= 2

                # Mueve a las flechas disparadas por el personajePrincipal y los enemigos
                for flecha in listaFlechasD:
                    flecha.rect.left += 5
                for flecha in listaFlechasI:
                    flecha.rect.left -= 5
                for flecha in listaFlechasEnD:
                    flecha.rect.left += 5
                for flecha in listaFlechasEnI:
                    flecha.rect.left -= 5

                # Obtiene el daño del personaje
                ataquePersonaje = random.randint(minAtaque, maxAtaque)

                # Colisiones
                vidaPersonaje = personajeChocoEnemigo(spritePersonaje, diccionarioEnemigosVidas2, vidaPersonaje, puntos,
                                                      ESTADO)
                puedeSaltar = checarPersonajeEnPiso(listaParedes2, spritePersonaje)
                contadorSalto = checarPersonajeChocoConTecho(listaParedes2, spritePersonaje, contadorSalto)
                personajeChocoIzquierda, personajeChocoDerecha = checarPersonajePared(listaParedes2, spritePersonaje)
                checarColisionesFlechasParedes(listaFlechasEnD, listaFlechasEnI, listaParedes2, listaFlechasI,
                                               listaFlechasD)
                vidaPersonaje = checarFlechasPersonajes(listaFlechasD, listaFlechasI, listaFlechasEnD, listaFlechasEnI,
                                                        diccionarioEnemigosVidas2, spritePersonaje, vidaPersonaje,
                                                        ataquePersonaje, puntos)
                # Checa si agarró a la flecha dorada
                if not flechaEstaMejorada:
                    minAtaque, maxAtaque, flechaEstaMejorada, flechasQuePuedeDisparar = \
                        checarPersonajeObtuvoFlechaMejorada(spritePersonaje, listaFlechaporAgarrar)

            # Cambia la dirección del enemigo del primer nivel

                # Función para cambiar al enemigo en dirección del personaje
                checarSiEnemigoVioPersonaje(diccionarioEnemigosDirecciones2, spritePersonaje)

                for spriteEnemigo in diccionarioEnemigosDirecciones2: # Cambia las direcciones de los sprites
                    # Mueve al enemigo del primer nivel
                    if diccionarioEnemigosDirecciones2[spriteEnemigo] == DERECHA:
                        spriteEnemigo.rect.left += 1
                        spriteEnemigo.image = imgEnemigoD
                    elif diccionarioEnemigosDirecciones2[spriteEnemigo] == IZQUIERDA:
                        spriteEnemigo.rect.left -= 1
                        spriteEnemigo.image = imgEnemigoI

                    xe, ye, ane, alte = spriteEnemigo.rect
                    if xe + ane >= ANCHO - 200:
                        diccionarioEnemigosDirecciones2[spriteEnemigo] = IZQUIERDA
                    elif xe <= 200:
                        diccionarioEnemigosDirecciones2[spriteEnemigo] = DERECHA

                if contadorDisparosEnemigos % 75 == 0 and diccionarioEnemigosVidas2:
                    for spriteEnemigo in diccionarioEnemigosVidas2:
                    # Hacer que los enemigos disparen
                        if spriteEnemigo.image == imgEnemigoI:
                            spriteFlechaI = pygame.sprite.Sprite()
                            spriteFlechaI.image = imgFlechaI
                            spriteFlechaI.rect = imgFlechaI.get_rect()
                            spriteFlechaI.rect.bottom = spriteEnemigo.rect.bottom - spriteEnemigo.rect.height // 3
                            spriteFlechaI.rect.left = spriteEnemigo.rect.left - spriteFlechaI.rect.width
                            listaFlechasEnI.append(spriteFlechaI)
                        elif spriteEnemigo.image == imgEnemigoD:
                            spriteFlechaD = pygame.sprite.Sprite()
                            spriteFlechaD.image = imgFlechaD
                            spriteFlechaD.rect = imgFlechaD.get_rect()
                            spriteFlechaD.rect.bottom = spriteEnemigo.rect.bottom - spriteEnemigo.rect.height // 3
                            spriteFlechaD.rect.left = spriteEnemigo.rect.left + spriteEnemigo.rect.width
                            listaFlechasEnD.append(spriteFlechaD)
                if diccionarioEnemigosVidas2:
                    contadorDisparosEnemigos += 1

            if not diccionarioEnemigosVidas2:
                spritePuerta.image = imgPuertaAbierta

            #Checa si el personaje se salio Por la puerta, sólo se deja de mover al chocar por la puerta si está cerrada
            if spritePuerta.image == imgPuertaCerrada:
                personajeChocoPuerta = checarPersonajePuerta(spritePuerta, spritePersonaje)
            elif spritePuerta.image == imgPuertaAbierta:
                personajeChocoPuerta = False

            # Dibuja todos los componentes del nivel 2
            dibujarNivelDos(ventana, spritePersonaje, listaParedes2, diccionarioEnemigosVidas2, listaFlechasD,
                            listaFlechasI, listaFlechasEnD, listaFlechasEnI, spritePuerta, listaFlechaporAgarrar)
            dibujarVidas(ventana, spritePersonaje, vidaPersonaje, diccionarioEnemigosVidas2)

            # checar si el personaje no ha muerto si sí congela a los personajes y registra la puntuación
            if vidaPersonaje <= 0:
                spritePersonaje.image = imgPersonajeMuerto
                juegoSigue = False
                ventana.blit(gameOver, (ANCHO // 2 - 150, ALTO // 3))
                ventana.blit(escMenu, (ANCHO // 2 - 200, (ALTO // 3) + 100))
                if not yaEscribioLasPuntuaciones:
                    yaEscribioLasPuntuaciones = True
                    listaPuntuaciones.append(puntos[0])
                    escribirPuntuacionesNuevoArchivo(listaPuntuaciones)

            if spritePersonaje.rect.left > ANCHO:
                ESTADO = JUGANDO3
                spritePersonaje.rect.left = 0
                spritePersonaje.rect.bottom = 100



            # Mostrar los puntos en la pantalla
            puntuacion = tipoDeLetra2.render(str(puntos[0]), False, BLANCO)
            ventana.blit(puntuacion, (120, 60))

        elif ESTADO == JUGANDO3:
            # Mueve a los sprites
            if juegoSigue:
                # Personaje Principal
                if movimientoPersonajeY == SALTO:
                    spritePersonaje.rect.bottom -= 3
                    if contadorSalto >= 110:
                        movimientoPersonajeY = ABAJO
                    else:
                        contadorSalto += 3
                elif movimientoPersonajeY == ABAJO:
                    if not puedeSaltar:
                        spritePersonaje.rect.bottom += 3
                if movimientoPersonajeX == DERECHA:
                    spritePersonaje.rect.left += 2
                elif movimientoPersonajeX == IZQUIERDA:
                    spritePersonaje.rect.left -= 2

                # Mueve a las flechas disparadas por el personajePrincipal y los enemigos
                for flecha in listaFlechasD:
                    flecha.rect.left += 5
                for flecha in listaFlechasI:
                    flecha.rect.left -= 5
                for flecha in listaFlechasEnD:
                    flecha.rect.left += 5
                for flecha in listaFlechasEnI:
                    flecha.rect.left -= 5

                # Obtiene el daño del personaje
                ataquePersonaje = random.randint(minAtaque, maxAtaque)

                # Colisiones
                vidaPersonaje = personajeChocoEnemigo(spritePersonaje, diccionarioEnemigoVidas3, vidaPersonaje, puntos,
                                                      ESTADO)
                puedeSaltar = checarPersonajeEnPiso(listaParedes3, spritePersonaje)
                contadorSalto = checarPersonajeChocoConTecho(listaParedes3, spritePersonaje, contadorSalto)
                personajeChocoIzquierda, personajeChocoDerecha = checarPersonajePared(listaParedes3, spritePersonaje)
                checarColisionesFlechasParedes(listaFlechasEnD, listaFlechasEnI, listaParedes3, listaFlechasI,
                                               listaFlechasD)
                vidaPersonaje = checarFlechasPersonajes(listaFlechasD, listaFlechasI, listaFlechasEnD, listaFlechasEnI,
                                                        diccionarioEnemigoVidas3, spritePersonaje, vidaPersonaje,
                                                        ataquePersonaje, puntos)

                # Cambia la dirección del enemigo del Tercer nivel

                # Función para cambiar al enemigo en dirección del personaje
                checarSiEnemigoVioPersonaje(diccionarioEnemigoDirecciones3, spritePersonaje)

                for spriteEnemigo in diccionarioEnemigoDirecciones3:  # Cambia las direcciones de los sprites
                    # Mueve al enemigo del primer nivel
                    if diccionarioEnemigoDirecciones3[spriteEnemigo] == DERECHA:
                        spriteEnemigo.rect.left += 1
                        spriteEnemigo.image = imgBossD
                    elif diccionarioEnemigoDirecciones3[spriteEnemigo] == IZQUIERDA:
                        spriteEnemigo.rect.left -= 1
                        spriteEnemigo.image = imgBossI

                    xe, ye, ane, alte = spriteEnemigo.rect
                    if xe + ane >= ANCHO - 60:
                        diccionarioEnemigoDirecciones3[spriteEnemigo] = IZQUIERDA
                    elif xe <= 60:
                        diccionarioEnemigoDirecciones3[spriteEnemigo] = DERECHA

                if contadorDisparosEnemigos % 80 == 0 and diccionarioEnemigoVidas3:
                    for spriteEnemigo in diccionarioEnemigoVidas3:
                        # Hacer que los enemigos disparen
                        if spriteEnemigo.image == imgBossI:
                            spriteFlechaI = pygame.sprite.Sprite()
                            spriteFlechaI.image = imgFlechaI
                            spriteFlechaI.rect = imgFlechaI.get_rect()
                            spriteFlechaI.rect.bottom = spriteEnemigo.rect.bottom - spriteEnemigo.rect.height // 3
                            spriteFlechaI.rect.left = spriteEnemigo.rect.left - spriteFlechaI.rect.width
                            listaFlechasEnI.append(spriteFlechaI)
                            sonidoFlecha.play()
                        elif spriteEnemigo.image == imgBossD:
                            spriteFlechaD = pygame.sprite.Sprite()
                            spriteFlechaD.image = imgFlechaD
                            spriteFlechaD.rect = imgFlechaD.get_rect()
                            spriteFlechaD.rect.bottom = spriteEnemigo.rect.bottom - spriteEnemigo.rect.height // 3
                            spriteFlechaD.rect.left = spriteEnemigo.rect.left + spriteEnemigo.rect.width
                            listaFlechasEnD.append(spriteFlechaD)
                            sonidoFlecha.play()
                if diccionarioEnemigoVidas3:
                    contadorDisparosEnemigos += 1

            if not diccionarioEnemigoVidas3:
                juegoSigue = False
                ventana.blit(victory , (ANCHO // 2 - 150, ALTO // 3))
                ventana.blit(escMenu, (ANCHO // 2 - 200, (ALTO // 3) + 100))
                puntos[0] += 3000
                if not yaEscribioLasPuntuaciones:
                    yaEscribioLasPuntuaciones = True
                    listaPuntuaciones.append(puntos[0])
                    escribirPuntuacionesNuevoArchivo(listaPuntuaciones)

            # Checa si el personaje se salio Por la puerta, sólo se deja de mover al chocar por la puerta si está cerrada
            if spritePuerta.image == imgPuertaCerrada:
                personajeChocoPuerta = checarPersonajePuerta(spritePuerta, spritePersonaje)
            elif spritePuerta.image == imgPuertaAbierta:
                personajeChocoPuerta = False

            # Dibuja todos los componentes del nivel 3
            dibujarNivelTres(ventana, spritePersonaje, listaParedes3, diccionarioEnemigoVidas3, listaFlechasD,
                            listaFlechasI, listaFlechasEnD, listaFlechasEnI)
            dibujarVidas3(ventana, spritePersonaje, vidaPersonaje, diccionarioEnemigoVidas3)

            # checar si el personaje no ha muerto si sí congela a los personajes y registra la puntuación
            if vidaPersonaje <= 0:
                spritePersonaje.image = imgPersonajeMuerto
                juegoSigue = False
                ventana.blit(gameOver, (ANCHO // 2 - 150, ALTO // 3))
                ventana.blit(escMenu, (ANCHO // 2 - 200, (ALTO // 3) + 100))
                if not yaEscribioLasPuntuaciones:
                    yaEscribioLasPuntuaciones = True
                    listaPuntuaciones.append(puntos[0])
                    escribirPuntuacionesNuevoArchivo(listaPuntuaciones)

            if spritePersonaje.rect.left > ANCHO:
                ESTADO = JUGANDO3

            # Mostrar los puntos en la pantalla
            puntuacion = tipoDeLetra2.render(str(puntos[0]), False, BLANCO)
            ventana.blit(puntuacion, (120, 60))


        elif ESTADO == MENU:
            # puntos del juego en el que se está jugando
            dibujarMenu(ventana, imgBtnJugar,   listaParedesMenu, imgBtnInstrucciones, imgBtnPuntuacionesAltas)


        elif ESTADO == INSTRUCCIONES:
            juegoSigue = False # Esto es para que funcione la tecla escape para regresar al menu principal
            dibujarInstrucciones(ventana, imgInstrucciones)


        elif ESTADO == PUNTUACIONES:
            juegoSigue = False # Esto es para que funcione la tecla escape para regresar al menu principal
            dibujarPuntuaciones(ventana, tipoDeLetra2)
            ventana.blit(escMenu, (300, 550))


        pygame.display.flip()
        reloj.tick(80) # 80 frames per second

    pygame.quit()


def main():
    listaPuntuaciones = crearListaPuntuaciones()
    correrJuego(listaPuntuaciones)


main()
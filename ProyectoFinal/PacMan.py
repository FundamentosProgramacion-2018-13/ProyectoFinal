import pygame  # Librería de pygame
from random import randrange

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (6, 10, 147)
NEGRO = (0, 0, 0)

# Estados de movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
IZQUIERDA = 4
DERECHA = 5

puntaje = -100


def dibujarMapa(ventana, listaCajas):
    # Bordes
    pygame.draw.line(ventana, AZUL, (75, 100), (75, ALTO // 2), 2)
    pygame.draw.line(ventana, AZUL, (75, ALTO // 2 + 50), (75, ALTO - 50), 2)

    pygame.draw.line(ventana, AZUL, (75, 100), (ANCHO - 75, 100), 2)

    pygame.draw.line(ventana, AZUL, (ANCHO - 75, 100), (ANCHO - 75, ALTO // 2), 2)
    pygame.draw.line(ventana, AZUL, (ANCHO - 75, ALTO - 50), (ANCHO - 75, ALTO // 2 + 50), 2)

    pygame.draw.line(ventana, AZUL, (75, ALTO - 50), (ANCHO - 75, ALTO - 50), 2)

    pygame.draw.line(ventana, AZUL, (0, ALTO // 2), (75, ALTO // 2), 2)
    pygame.draw.line(ventana, AZUL, (0, ALTO // 2 + 50), (75, ALTO // 2 + 50), 2)

    pygame.draw.line(ventana, AZUL, (ANCHO - 75, ALTO // 2), (ANCHO, ALTO // 2), 2)
    pygame.draw.line(ventana, AZUL, (ANCHO - 75, ALTO // 2 + 50), (ANCHO, ALTO // 2 + 50), 2)

    #Cajas
    for caja in listaCajas:
        ventana.blit(caja.image, caja.rect)

def dibujarVidas(ventana, listaVidas):
    for vida in listaVidas:
        ventana.blit(vida.image, vida.rect)

def dibujarPacMan(ventana, spritePacman):
    ventana.blit(spritePacman.image, spritePacman.rect)

def dibujarFantasma1(ventana, spriteFantasma1):
    ventana.blit(spriteFantasma1.image, spriteFantasma1.rect)

def dibujarFantasma2(ventana, spriteFantasma2):
    ventana.blit(spriteFantasma2.image, spriteFantasma2.rect)

def dibujarFantasma3(ventana, spriteFantasma3):
    ventana.blit(spriteFantasma3.image, spriteFantasma3.rect)

def dibujarPuntos(ventana, listaPuntos, listaCajas):
    for punto in listaPuntos:
        xP = punto.rect.left
        yP = punto.rect.bottom
        for caja in listaCajas:
            xC = caja.rect.left
            yC = caja.rect.bottom
            if xP >xC and xP<xC+50 and yP >yC-50 and yP <yC:
                listaPuntos.remove(punto)
        if xP >375 and xP<425 and yP>300 and yP<350:
            listaPuntos.remove(punto)

    for punto in listaPuntos:
        ventana.blit(punto.image, punto.rect)

def actualizarPuntos(listaPuntos, spritePacman):
    for punto in listaPuntos:
        xPunto = punto.rect.left+7.5
        yPunto = punto.rect.bottom-7.5
        xPM = spritePacman.rect.left
        yPM = spritePacman.rect.bottom
        anchoPM = spritePacman.rect.width
        altoPM = spritePacman.rect.height
        if xPunto>xPM and xPunto<xPM+anchoPM and yPunto>yPM-altoPM and yPunto<yPM:
            listaPuntos.remove(punto)
            global puntaje
            puntaje += 100

def verificarParedArriba(spritePacman, listaCajas):
    yArribaPM = spritePacman.rect.bottom - spritePacman.rect.height -4
    xPM = spritePacman.rect.left
    anchoPM = spritePacman.rect.width
    for caja in listaCajas:
        xCaja = caja.rect.left
        yCaja = caja.rect.bottom
        anchoCaja = caja.rect.width
        altoCaja = caja.rect.height
        if yArribaPM > yCaja-6 and yArribaPM < yCaja and (xPM < xCaja + anchoCaja and xPM > xCaja - anchoPM):
            return True
    if yArribaPM <= 104:
        return True
    return False

def verificarParedAbajo(spritePacman, listaCajas):
    yAbajoPM = spritePacman.rect.bottom
    xPM = spritePacman.rect.left
    anchoPM = spritePacman.rect.width
    for caja in listaCajas:
        xCaja = caja.rect.left
        yCaja = caja.rect.bottom-caja.rect.height
        anchoCaja= caja.rect.width
        altoCaja = caja.rect.height
        if yAbajoPM > yCaja-6 and yAbajoPM<yCaja and (xPM>xCaja-anchoPM-2 and xPM < xCaja+anchoCaja ):
            return True
    if yAbajoPM >= 546:
        return True
    return False

def verificarParedIzquierda(spritePacman, listaCajas):
    xPM = spritePacman.rect.left
    yPM = spritePacman.rect.bottom
    altoPM = spritePacman.rect.height
    for caja in listaCajas:
        xCaja = caja.rect.left
        yCaja = caja.rect.bottom
        altoCaja = caja.rect.height
        anchoCaja = caja.rect.width
        if xPM > xCaja+anchoCaja and xPM < xCaja+anchoCaja+6 and yPM > yCaja - altoCaja and yPM < yCaja + altoPM:
            return True
    if xPM <= 80 and not (yPM>344 and yPM<356):
        return True
    if xPM < 25:
        spritePacman.rect.left = ANCHO - 50
    return False

def verificarParedDerecha(spritePacman, listaCajas):
    xDerecha = spritePacman.rect.left + spritePacman.rect.width

    yPM = spritePacman.rect.bottom
    xPM = spritePacman.rect.left
    anchoPM = spritePacman.rect.width
    altoPM = spritePacman.rect.height
    for caja in listaCajas:
        xCaja = caja.rect.left
        yCaja = caja.rect.bottom
        altoCaja = caja.rect.height
        if xPM+anchoPM > xCaja-6 and xPM+anchoPM < xCaja and yPM > yCaja - altoCaja and yPM < yCaja + altoPM:
            return True
    if xDerecha >= 725 and not (yPM>340 and yPM<354):
        return True
    if xDerecha >ANCHO - 25:
        spritePacman.rect.left = 50
    return False

def escrbirPuntaje(textoPuntaje, ventana):
    ventana.blit(textoPuntaje, (625, 60))

def moverArriba(sprite, listaCajas, velocidad):
    if verificarParedArriba(sprite, listaCajas):
        sprite.rect.bottom -= 0
        return True
    else:
        sprite.rect.bottom -= velocidad

def moverAbajo(sprite, listaCajas, velocidad):
    if verificarParedAbajo(sprite, listaCajas):
        sprite.rect.bottom += 0
        return True
    else:
        sprite.rect.bottom += velocidad

def moverIzquierda(sprite, listaCajas, velocidad):
    if verificarParedIzquierda(sprite, listaCajas):
        sprite.rect.left -= 0
        return True
    else:
        sprite.rect.left -= velocidad

def moverDerecha(sprite, listaCajas, velocidad):
    if verificarParedDerecha(sprite, listaCajas):
        sprite.rect.left += 0
        return True
    else:
        sprite.rect.left += velocidad


def moverFantasma1(spriteFantasma, listaCajas, spritePacman):
    xF = spriteFantasma.rect.left
    yF = spriteFantasma.rect.bottom
    xPM = spritePacman.rect.left
    yPM = spritePacman.rect.bottom
    velocidad = 3
    if xF-100<xPM <xF+150 and yF-150<yPM <yF+100:
        pass
    else:
        pass
        '''
        if moverArriba(spriteFantasma, listaCajas, velocidad):
            movimiento = randrange(2,6)
            moverDerecha(spriteFantasma, listaCajas, velocidad):
                if moverAbajo(spriteFantasma, listaCajas, velocidad):
                    if moverIzquierda(spriteFantasma, listaCajas, velocidad):
                        if moverArriba(spriteFantasma, listaCajas, velocidad):
                            pass
                            '''


def moverFantasma2(spriteFantasma, listaCajas, spritePacman):
    xF = spriteFantasma.rect.left
    yF = spriteFantasma.rect.bottom
    xPM = spritePacman.rect.left
    yPM = spritePacman.rect.bottom


def moverFantasma3(spriteFantasma, listaCajas, spritePacman):
    xF = spriteFantasma.rect.left
    yF = spriteFantasma.rect.bottom
    xPM = spritePacman.rect.left
    yPM = spritePacman.rect.bottom



def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Sprites Pac Man
    imgPacman = pygame.image.load("pacman.png")
    spritePacman = pygame.sprite.Sprite()
    spritePacman.image = imgPacman
    spritePacman.rect = imgPacman.get_rect()
    spritePacman.rect.left = ANCHO // 2 - spritePacman.rect.width // 2
    spritePacman.rect.bottom = ALTO // 2 + spritePacman.rect.height + 3
    movimiento = QUIETO
    velocidadPM = 5


    #Sprites fantasmas
    listaFantasmas = []

    #Fantasma 2
    imgFantasma2 = pygame.image.load("fantasmaamarillo.png")
    spriteFantasma2 = pygame.sprite.Sprite()
    spriteFantasma2.image = imgFantasma2
    spriteFantasma2.rect = imgFantasma2.get_rect()
    spriteFantasma2.rect.left = ANCHO // 2 - spriteFantasma2.rect.width*1.75
    spriteFantasma2.rect.bottom = ALTO // 2


    # Fantasma 1
    imgFantasma1 = pygame.image.load("fantasmarojo.png")
    spriteFantasma1 = pygame.sprite.Sprite()
    spriteFantasma1.image = imgFantasma1
    spriteFantasma1.rect = imgFantasma1.get_rect()
    spriteFantasma1.rect.left = ANCHO // 2 - spriteFantasma2.rect.width//2
    spriteFantasma1.rect.bottom = ALTO // 2
    movimientoF1=QUIETO

    # Fantasma 3
    imgFantasma3 = pygame.image.load("fantasmaazul.png")
    spriteFantasma3 = pygame.sprite.Sprite()
    spriteFantasma3.image = imgFantasma3
    spriteFantasma3.rect = imgFantasma3.get_rect()
    spriteFantasma3.rect.left = ANCHO // 2 +spriteFantasma2.rect.width*0.75
    spriteFantasma3.rect.bottom = ALTO // 2

    #Lista cajas
    listaCajas = []
    imgCaja = pygame.image.load("caja.png")
    for x in range(125, 675, 50):
        for y in range(200, 600, 50):
            if (y == 200 and (
                    x == 125 or x == 225 or x == 275 or x == 325 or x == 425 or x == 475 or x == 525 or x == 625)) or (
                    y == 250 and (x == 125 or x == 625)) or (
                    y == 300 and (x == 225 or x == 525 or x == 325 or x == 375 or x == 425)) or (
                    y == 350 and (x == 125 or x == 625)) or (
                    y == 400 and (x == 125 or x == 175 or x == 575 or x == 625 or (x >= 275 and x < 525))) or(
                    y == 500 and (x == 125 or x == 225 or x == 275 or x == 375 or x == 475 or x == 525 or x == 625)) or (y==550and x==375):
                spriteCaja = pygame.sprite.Sprite()
                spriteCaja.image = imgCaja
                spriteCaja.rect = imgCaja.get_rect()
                spriteCaja.rect.left = x
                spriteCaja.rect.bottom = y
                listaCajas.append(spriteCaja)


    # Lista de vidas
    listaVidas = []
    imgVida = pygame.image.load("vida.png")
    xVida = 75
    for k in range(3):
        spriteVida = pygame.sprite.Sprite()
        spriteVida.image = imgVida
        spriteVida.rect = imgVida.get_rect()
        spriteVida.rect.left = xVida
        spriteVida.rect.bottom = 100
        listaVidas.append(spriteVida)
        xVida += 50

    # Lista puntos
    listaPuntos = []
    imgPunto = pygame.image.load("punto.png")
    for x in range(100, 725, 50):
        for y in range(125, 575, 50):
            spritePunto = pygame.sprite.Sprite()
            spritePunto.image = imgPunto
            spritePunto.rect = imgPunto.get_rect()
            spritePunto.rect.left = x - spritePunto.rect.width // 2
            spritePunto.rect.bottom = y + spritePunto.rect.height // 2
            listaPuntos.append(spritePunto)
    for x in range (60, 800, 680):
        spritePunto = pygame.sprite.Sprite()
        spritePunto.image = imgPunto
        spritePunto.rect = imgPunto.get_rect()
        spritePunto.rect.left = x - spritePunto.rect.width // 2
        spritePunto.rect.bottom = 325 + spritePunto.rect.height // 2
        listaPuntos.append(spritePunto)

    #timer
    timer=0


    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_UP and (movimiento==QUIETO or movimiento==DERECHA):
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 90)
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN and (movimiento==QUIETO or movimiento==DERECHA):
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 270)
                    movimiento = ABAJO
                elif evento.key == pygame.K_LEFT and (movimiento==QUIETO or movimiento==DERECHA):
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 180)
                    movimiento = IZQUIERDA
                elif evento.key == pygame.K_RIGHT and (movimiento==QUIETO or movimiento==DERECHA):
                    movimiento = DERECHA

                if evento.key == pygame.K_UP and movimiento==ARRIBA:
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN and movimiento==ARRIBA:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 180)
                    movimiento = ABAJO
                elif evento.key == pygame.K_LEFT and movimiento==ARRIBA:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 90)
                    movimiento = IZQUIERDA
                elif evento.key == pygame.K_RIGHT and movimiento==ARRIBA:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 270)
                    movimiento = DERECHA

                if evento.key == pygame.K_UP and movimiento==ABAJO:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 180)
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN and movimiento==ABAJO:
                    movimiento = ABAJO
                elif evento.key == pygame.K_LEFT and movimiento==ABAJO:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 270)
                    movimiento = IZQUIERDA
                elif evento.key == pygame.K_RIGHT and movimiento==ABAJO:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 90)
                    movimiento = DERECHA

                if evento.key == pygame.K_UP and movimiento==IZQUIERDA:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 270)
                    movimiento = ARRIBA
                elif evento.key == pygame.K_DOWN and movimiento==IZQUIERDA:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 90)
                    movimiento = ABAJO
                elif evento.key == pygame.K_LEFT and movimiento==IZQUIERDA:
                    movimiento = IZQUIERDA
                elif evento.key == pygame.K_RIGHT and movimiento==IZQUIERDA:
                    spritePacman.image = pygame.transform.rotate(spritePacman.image, 180)
                    movimiento = DERECHA

        #Mover PacMan
        if movimiento == ARRIBA:
            moverArriba(spritePacman, listaCajas, velocidadPM)
        elif movimiento == ABAJO:
            moverAbajo(spritePacman, listaCajas, velocidadPM)
        elif movimiento == IZQUIERDA:
            moverIzquierda(spritePacman, listaCajas, velocidadPM)
        elif movimiento == DERECHA:
            moverDerecha(spritePacman, listaCajas, velocidadPM)


        if timer %3==0:
            posicionAnteriorX = spritePacman.rect.left
            posicionAnteriorY = spritePacman.rect.bottom


        # Borrar pantalla
        ventana.fill(NEGRO)
        dibujarMapa(ventana, listaCajas)

        dibujarVidas(ventana, listaVidas)
        dibujarPacMan(ventana, spritePacman)
        dibujarPuntos(ventana, listaPuntos, listaCajas)
        dibujarFantasma1(ventana, spriteFantasma1)
        dibujarFantasma2(ventana, spriteFantasma2)
        dibujarFantasma3(ventana, spriteFantasma3)
        actualizarPuntos(listaPuntos,spritePacman)
        moverFantasma1(spriteFantasma1, listaCajas, spritePacman)
        moverFantasma2(spriteFantasma1, listaCajas, spritePacman)
        moverFantasma3(spriteFantasma1, listaCajas, spritePacman)
        fuente = pygame.font.Font(None, 60)
        textoPuntaje = fuente.render(str(puntaje), 0, (255, 255, 255))
        escrbirPuntaje(textoPuntaje,ventana)


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1 / 40


    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja

# Llamas a la función principal
main()
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

#Estados de juego
MENU = 0
JUGANDO = 1


def dibujarMenu(spritePacmanIN, ventana):
    pygame.draw.rect(ventana, AZUL, (300, 230, 200, 100), 3)

    fuente = pygame.font.Font(None, 60)
    textoPuntaje = fuente.render(("JUGAR"), 0, (255, 255, 255))
    ventana.blit(textoPuntaje, (325, 260))

    ventana.blit(spritePacmanIN.image, spritePacmanIN.rect)
    x = spritePacmanIN.rect.left
    y = spritePacmanIN.rect.bottom
    ancho=spritePacmanIN.rect.width
    if (x==480 and y==250)or (x==480 and y==350) or (x==280 and y==350 or (x==280 and y==250)):
        spritePacmanIN.image = pygame.transform.rotate(spritePacmanIN.image,270)
    if 280<=x<500-ancho//2 and y==250:
        spritePacmanIN.rect.left +=2
    if 250<=y<350 and x==480:
        spritePacmanIN.rect.bottom += 2
    if 300-ancho//2<x<=500 and y==350:
        spritePacmanIN.rect.left -= 2
    if 250<y<=350 and x==280:
        spritePacmanIN.rect.bottom -= 2

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

def actualizarPuntos(listaPuntos, spritePacman, efecto):
    for punto in listaPuntos:
        xPunto = punto.rect.left+7.5
        yPunto = punto.rect.bottom-7.5
        xPM = spritePacman.rect.left
        yPM = spritePacman.rect.bottom
        anchoPM = spritePacman.rect.width
        altoPM = spritePacman.rect.height
        if xPunto>xPM and xPunto<xPM+anchoPM and yPunto>yPM-altoPM and yPunto<yPM:
            listaPuntos.remove(punto)
            efecto.play()
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
    if xPM <= 80 and not (yPM>340 and yPM<350):
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
    if xDerecha >= 725 and not (yPM>340 and yPM<350):
        return True
    if xDerecha >ANCHO - 25:
        spritePacman.rect.left = 50
    return False

def moverArriba(sprite, listaCajas, velocidad):
    if verificarParedArriba(sprite, listaCajas):
        sprite.rect.bottom -= 0
        return False
    else:
        sprite.rect.bottom -= velocidad

def moverAbajo(sprite, listaCajas, velocidad):
    if verificarParedAbajo(sprite, listaCajas):
        sprite.rect.bottom += 0
        return False
    else:
        sprite.rect.bottom += velocidad

def moverIzquierda(sprite, listaCajas, velocidad):
    if verificarParedIzquierda(sprite, listaCajas):
        sprite.rect.left -= 0
        return False
    else:
        sprite.rect.left -= velocidad

def moverDerecha(sprite, listaCajas, velocidad):
    if verificarParedDerecha(sprite, listaCajas):
        sprite.rect.left += 0
        return False
    else:
        sprite.rect.left += velocidad

def moverFantasma1(spriteFantasma, listaCajas, spritePacman):
    xF = spriteFantasma.rect.left
    yF = spriteFantasma.rect.bottom
    xPM = spritePacman.rect.left
    yPM = spritePacman.rect.bottom
    anchoF=spriteFantasma.rect.width
    velocidad = 2.5
    velocidadMax = 5

    if 375<xF<425 and  245<yF<=300:
        moverArriba(spriteFantasma, listaCajas, velocidad)
    if 375<xF<480 and 200<yF<245:
        if 375<xPM<480 and 200<yPM<245:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 475<xF<525 and 145<yF<245:
        if 475 < xPM < 525 and yPM < 245:
            moverArriba(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverArriba(spriteFantasma, listaCajas, velocidad)
    if 275 < xF < 525 and yF < 150:
        if 275 < xPM < 525 and yPM < 150:
            moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverIzquierda(spriteFantasma, listaCajas, velocidad)
    if 275 < xF < 325 and 100<yF<250:
        if 275 < xPM < 325 and 100 < yPM < 250:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if 175 < xF <325 and 200<yF<250:
        if 175 < xPM < 325 and 200 < yPM < 250:
            moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverIzquierda(spriteFantasma, listaCajas, velocidad)
    if 175<xF<225 and yF<250:
        if 175<xPM<225 and yPM<250:
            moverArriba(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverArriba(spriteFantasma, listaCajas, velocidad)
    if xF<225 and yF<150:
        if xPM<225 and yPM<150:
            moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverIzquierda(spriteFantasma, listaCajas, velocidad)
    if xF<125 and yF<300:
        if xPM<125 and yPM<300:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if xF<225 and 250<yF<300:
        if xPM < 225 and 250 < yPM < 300:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 175<xF<225 and 250<yF<350:
        if 175 < xPM < 225 and 250 < yPM < 350:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if 175<xF < 270-anchoF and 300 < yF < 350:
        if 175 < xPM < 270 and 300 < yPM < 350:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 225<xF < 275 and 300 < yF < 450:
        if 225 < xPM < 275 and 300 < yPM < 450:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if 75<xF < 275 and 400 < yF < 450:
        if 75 < xPM < 275 and 400 < yPM < 450:
            moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverIzquierda(spriteFantasma, listaCajas, velocidad)
    if 75<xF < 125 and 400 < yF < 550:
        if 75 < xPM < 125 and 400 < yPM < 550:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if 75<xF < 375-anchoF and 500 < yF < 550:
        if 75 < xPM < 325 and 500 < yPM < 550:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 325<xF < 375 and 400 < yF < 550:
        if 325 < xPM < 375 and 400 < yPM < 550:
            moverArriba(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverArriba(spriteFantasma, listaCajas, velocidad)
    if 325<xF < 425-anchoF and 400 < yF < 450:
        if 325 < xPM < 425 and 400 < yPM < 450:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 375 < xF < 425 and 300 < yF < 450:
        if 375 < xPM < 425 and 300 < yPM < 450:
            moverArriba(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverArriba(spriteFantasma, listaCajas, velocidad)
    if 375 < xF < 570-anchoF and 300 < yF < 350:
        if 375 < xPM < 575 and 300 < yPM < 350:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 525 < xF < 575 and 300 < yF < 450:
        if 525 < xPM < 575 and 300 < yPM < 450:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if 430 < xF < 575 and 400 < yF < 450:
        if 430 < xPM < 575 and 400 < yPM < 450:
            moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverIzquierda(spriteFantasma, listaCajas, velocidad)
    if 425 < xF < 475 and 400 < yF < 550:
        if 425 < xPM < 475 and 400 < yPM < 550:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if 425 < xF < 620-anchoF and 500 < yF < 550:
        if 425 < xPM < 625 and 500 < yPM < 550:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 575 < xF < 625 and 400 < yF < 550:
        if 575 < xPM < 625 and 400 < yPM < 550:
            moverArriba(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverArriba(spriteFantasma, listaCajas, velocidad)
    if 575 < xF < 725-anchoF and 400 < yF < 450:
        if 575 < xPM < 725 and 400 < yPM < 450:
            moverDerecha(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverDerecha(spriteFantasma, listaCajas, velocidad)
    if 675 < xF < 725 and 100 < yF < 450:
        if 675 < xPM < 725 and 100 < yPM < 450:
            moverArriba(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverArriba(spriteFantasma, listaCajas, velocidad)
    if 575<xF < 725 and 100 < yF < 150:
        if 575 < xPM < 725 and 100 < yPM < 150:
            moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverIzquierda(spriteFantasma, listaCajas, velocidad)
    if 575 < xF < 625 and 100 < yF < 250:
        if 575 < xPM < 625 and 100 < yPM < 250:
            moverAbajo(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverAbajo(spriteFantasma, listaCajas, velocidad)
    if 475<xF < 625 and 200 < yF < 250:
        if 475 < xPM < 625 and 200 < yPM < 250:
            moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
        else:
            moverIzquierda(spriteFantasma, listaCajas, velocidad)

def moverFantasma2(spriteFantasma, listaCajas, spritePacman, timer):
    xF = spriteFantasma.rect.left
    yF = spriteFantasma.rect.bottom
    xPM = spritePacman.rect.left
    yPM = spritePacman.rect.bottom
    anchoF = spriteFantasma.rect.width
    altoF = spriteFantasma.rect.height
    velocidad = 5
    velocidadMax = 7.5
    if timer >=5:
        if 325<xF<420-anchoF and 250<yF<=300:
           spriteFantasma.rect.left += velocidad
        if 375<xF<425 and  245<=yF<=300:
            moverArriba(spriteFantasma, listaCajas, velocidad)
        if 375<xF<620 and 200<yF<=247:
            if 375<xPM<620 and 200<yPM<247:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 575 < xF < 625 and 100 < yF < 250:
            if 575 < xPM < 625 and 100 < yPM < 250:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 575<xF < 725 and 100 < yF < 150:
            if 575 < xPM < 725 and 100 < yPM < 150:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 675 < xF < 725 and 100 < yF < 300:
            if 675 < xPM < 725 and 100 < yPM < 300:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 575<xF < 725 and 250 < yF < 300:
            if 575 < xPM < 725 and 250 < yPM < 300:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 575 < xF < 625 and 250 < yF < 350:
            if 575 < xPM < 625 and 250 < yPM < 350:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 525<xF < 625 and 300 < yF < 350:
            if 525 < xPM < 625 and 300 < yPM < 350:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 525 < xF < 575 and 300 < yF < 450:
            if 525 < xPM < 575 and 300 < yPM < 450:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 525<xF < 720-anchoF and 400 < yF < 450:
            if 525 < xPM < 725 and 400 < yPM < 450:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 675 < xF < 725 and 400 < yF < 550:
            if 675 < xPM < 725 and 400 < yPM < 550:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 425<xF < 725 and 500 < yF < 550:
            if 425 < xPM < 725 and 500 < yPM < 550:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 425 < xF < 475 and 400 < yF < 550:
            if 425 < xPM < 475 and 400 < yPM < 550:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 175<xF < 475 and 400 < yF < 450:
            if 175 < xPM < 475 and 400 < yPM < 450:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 175 < xF < 200 and 400 < yF < 550:
            if 175 < xPM < 200 and 400 < yPM < 550:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 75<xF < 225 and 500 < yF < 550:
            if 75 < xPM < 225 and 500 < yPM < 550:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 75 < xF < 125 and 255+altoF < yF < 550:
            if 75 < xPM < 125 and 250 < yPM < 550:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 75<xF < 225-anchoF and 250 < yF < 300:
            if 75 < xPM < 225 and 250 < yPM < 300:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 175 < xF < 200 and 250 < yF < 350:
            if 175 < xPM < 200 and 250 < yPM < 350:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 175<xF < 320-anchoF and 300 < yF < 350:
            if 175 < xPM < 325 and 300 < yPM < 350:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 275 < xF < 325 and 100 < yF < 350:
            if 275 < xPM < 325 and 100 < yPM < 350:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 275<xF < 525 and 100 < yF < 150:
            if 275 < xPM < 525 and 100 < yPM < 150:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 475 < xF < 525 and 100 < yF < 250:
            if 475 < xPM < 525 and 100 < yPM < 250:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)

def moverFantasma3(spriteFantasma, listaCajas, spritePacman, timer):
    xF = spriteFantasma.rect.left
    yF = spriteFantasma.rect.bottom
    xPM = spritePacman.rect.left
    yPM = spritePacman.rect.bottom
    anchoF = spriteFantasma.rect.width
    altoF = spriteFantasma.rect.height
    velocidad = 4.5
    velocidadMax = 9
    if timer>=10:
        if 380 < xF < 475 and 250 < yF <= 300:
            spriteFantasma.rect.left -= velocidad
        if 375 < xF < 425 and 200 <= yF <= 300:
            moverArriba(spriteFantasma, listaCajas, velocidad)
        if 175 < xF < 425 and 200 < yF < 250:
            if 175 < xPM < 415 and 200 < yPM < 250:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 175 < xF < 225 and 200 < yF < 300:
            if 175 < xPM < 225 and 200 < yPM < 300:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 75 < xF < 225 and 250 < yF < 300:
            if 75 < xPM < 225 and 250 < yPM < 300:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 75 < xF < 125 and 250 < yF < 450:
            if 75 < xPM < 125 and 250 < yPM < 450:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 75 < xF < 225-anchoF and 400 < yF < 450:
            if 75 < xPM < 225 and 400 < yPM < 450:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 175 < xF < 225 and 400 < yF < 550:
            if 175 < xPM < 225 and 400 < yPM < 550:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 175 < xF < 375 and 500 < yF < 550:
            if 175 < xPM < 375 and 500 < yPM < 550:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 325 < xF < 375 and 400 < yF < 550:
            if 325 < xPM < 375 and 400 < yPM < 550:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 225 < xF < 375 and 400 < yF < 450:
            if 225 < xPM < 375 and 400 < yPM < 450:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 225 < xF < 275 and 300 < yF < 450:
            if 225 < xPM < 275 and 300 < yPM < 405:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 225 < xF < 420 - anchoF and 300 < yF < 345:
            if 225 < xPM < 425 and 300 < yPM < 350:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 375 < xF < 425 and 300 < yF < 443:
            if 375 < xPM < 425 and 300 < yPM < 443:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 375 < xF < 625-anchoF and 400 < yF < 445:
            if 375 < xPM < 625 and 400 < yPM < 450:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 575 < xF < 625 and 400 < yF < 550:
            if 575 < xPM < 625 and 400 < yPM < 550:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 575 < xF < 725 and 500 < yF < 550:
            if 625 < xPM < 725 and 500 < yPM < 550:
                moverDerecha(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverDerecha(spriteFantasma, listaCajas, velocidad)
        if 675 < xF < 725 and 100 < yF < 550:
            if 675 < xPM < 725 and 100 < yPM < 550:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 575 < xF < 725 and 100 < yF < 150:
            if 575 < xPM < 725 and 100 < yPM < 150:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 575 < xF < 625 and 100 < yF < 350:
            if 575 < xPM < 625 and 100 < yPM < 350:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)
        if 475 < xF < 625 and 300 < yF < 350:
            if 475 < xPM < 625 and 300 < yPM < 350:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 475 < xF < 525 and 100 < yF < 350:
            if 475 < xPM < 525 and 100 < yPM < 550:
                moverArriba(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverArriba(spriteFantasma, listaCajas, velocidad)
        if 275 < xF < 525 and 100 < yF < 150:
            if 275 < xPM < 525 and 100 < yPM < 150:
                moverIzquierda(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverIzquierda(spriteFantasma, listaCajas, velocidad)
        if 275 < xF < 325 and 100 < yF < 245:
            if 275 < xPM < 325 and 100 < yPM < 245:
                moverAbajo(spriteFantasma, listaCajas, velocidadMax)
            else:
                moverAbajo(spriteFantasma, listaCajas, velocidad)



    print(xF, yF)

def verificarColision(listaFantasmas, listaVidas, pacman, perder):

    for fantasma in listaFantasmas:
        xF = fantasma.rect.left
        yF = fantasma.rect.bottom
        anchoF = fantasma.rect.width
        altoF = fantasma.rect.height
        xPM = pacman.rect.left
        yPM = pacman.rect.bottom
        anchoPM = pacman.rect.width
        altoPM = pacman.rect.height
        if (xF<xPM<xF+anchoF or xF<xPM+anchoPM<xF+anchoF) and (yF-altoF<yPM<yF or yF-altoF<yPM-altoPM<yF):
            if len(listaVidas)==3:
                listaVidas.remove(listaVidas[2])
                return True
            elif len(listaVidas)==2:
                listaVidas.remove(listaVidas[1])
                return True
            elif len(listaVidas)==1:
                listaVidas.remove(listaVidas[0])
                perder.play()
                return True

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

    #Sprites Pac Man Inicio
    spritePacmanIN = pygame.sprite.Sprite()
    spritePacmanIN.image = imgPacman
    spritePacmanIN.rect = imgPacman.get_rect()
    spritePacmanIN.rect.left = ANCHO // 2-spritePacmanIN.rect.width//2
    spritePacmanIN.rect.bottom = ALTO // 2 - 50

    #Sprites fantasmas
    listaFantasmas = []

    # Fantasma 1
    imgFantasma1 = pygame.image.load("fantasmarojo.png")
    spriteFantasma1 = pygame.sprite.Sprite()
    spriteFantasma1.image = imgFantasma1
    spriteFantasma1.rect = imgFantasma1.get_rect()
    spriteFantasma1.rect.left = ANCHO // 2 - spriteFantasma1.rect.width // 2
    spriteFantasma1.rect.bottom = ALTO // 2
    listaFantasmas.append(spriteFantasma1)


    #Fantasma 2
    imgFantasma2 = pygame.image.load("fantasmaamarillo.png")
    spriteFantasma2 = pygame.sprite.Sprite()
    spriteFantasma2.image = imgFantasma2
    spriteFantasma2.rect = imgFantasma2.get_rect()
    spriteFantasma2.rect.left = ANCHO // 2 - spriteFantasma2.rect.width*1.75
    spriteFantasma2.rect.bottom = ALTO // 2
    listaFantasmas.append(spriteFantasma2)


    # Fantasma 3
    imgFantasma3 = pygame.image.load("fantasmaazul.png")
    spriteFantasma3 = pygame.sprite.Sprite()
    spriteFantasma3.image = imgFantasma3
    spriteFantasma3.rect = imgFantasma3.get_rect()
    spriteFantasma3.rect.left = ANCHO // 2 +spriteFantasma3.rect.width*0.75
    spriteFantasma3.rect.bottom = ALTO // 2
    listaFantasmas.append(spriteFantasma3)

    #Lista cajas
    listaCajas = []
    imgCaja = pygame.image.load("caja.png")
    for x in range(125, 675, 50):
        for y in range(150, 600, 50):
            if (y == 150 and (x==225 or x==525)) or (y == 200 and (
                    x == 125 or x == 225 or x == 325 or x == 375 or x == 425 or x == 525 or x == 625)) or (
                    y == 250 and (x == 125 or x == 625)) or (
                    y == 300 and (x == 225 or x == 525 or x == 325 or x == 375 or x == 425)) or (
                    y == 350 and (x == 125 or x == 625)) or (
                    y == 400 and (x == 125 or x == 175 or x == 575 or x == 625 or (x >= 275 and x < 525 and not x==375))) or(
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


    #timers
    timer=0
    timer2=0
    wait=0

    #Audios

    pygame.mixer.init()
    comer = pygame.mixer.Sound("pacman_chomp.wav")
    perder = pygame.mixer.Sound("pacman_death.wav")
    pygame.mixer.music.load("pacman-song.mp3")
    pygame.mixer.music.play(-1)


    estado = MENU

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
            elif evento.type == pygame.MOUSEBUTTONDOWN and estado==MENU:
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO//2-128
                yb = ALTO//2-50
                anchoB=256
                altoB=100
                if xm>=xb and xm<=xb+anchoB and ym >=yb and ym<=yb+altoB:
                    estado = JUGANDO
            elif evento.type == pygame.MOUSEBUTTONDOWN and estado==JUGANDO:
                xm, ym = pygame.mouse.get_pos()
                if ANCHO // 2 - 209//2<xm<ANCHO // 2 + 209//2 and ALTO // 3*2<ym<ALTO // 3*2+42:
                    estado = MENU

        if estado == MENU:
            #Borrar pantalla
            ventana.fill(NEGRO)
            dibujarMenu(spritePacmanIN, ventana)


        elif estado == JUGANDO:

            if timer2 <30 and len(listaVidas)>0:
                timer2 += 1 / 40
                #Mover PacMan
                if movimiento == ARRIBA:
                    moverArriba(spritePacman, listaCajas, velocidadPM)
                elif movimiento == ABAJO:
                    moverAbajo(spritePacman, listaCajas, velocidadPM)
                elif movimiento == IZQUIERDA:
                    moverIzquierda(spritePacman, listaCajas, velocidadPM)
                elif movimiento == DERECHA:
                    moverDerecha(spritePacman, listaCajas, velocidadPM)


                # Borrar pantalla
                ventana.fill(NEGRO)
                dibujarMapa(ventana, listaCajas)

                dibujarVidas(ventana, listaVidas)
                dibujarPacMan(ventana, spritePacman)
                dibujarPuntos(ventana, listaPuntos, listaCajas)
                dibujarFantasma1(ventana, spriteFantasma1)
                dibujarFantasma2(ventana, spriteFantasma2)
                dibujarFantasma3(ventana, spriteFantasma3)
                actualizarPuntos(listaPuntos,spritePacman,comer)
                moverFantasma1(spriteFantasma1, listaCajas, spritePacman)
                moverFantasma2(spriteFantasma2, listaCajas, spritePacman, timer)
                moverFantasma3(spriteFantasma3, listaCajas, spritePacman, timer)
                if wait >2:
                    if verificarColision(listaFantasmas, listaVidas, spritePacman, perder):
                        wait=0

                fuente = pygame.font.Font(None, 60)
                textoPuntaje = fuente.render(str(puntaje), 0, (255, 255, 255))
                ventana.blit(textoPuntaje, (625, 60))

                fuente = pygame.font.Font(None, 60)
                textoPuntaje = fuente.render(str(30-int(timer2)), 0, (255, 255, 255))
                ventana.blit(textoPuntaje, (475, 60))

                fuente = pygame.font.Font(None, 60)
                textoPuntaje = fuente.render("TIEMPO: ", 0, (255, 255, 255))
                ventana.blit(textoPuntaje, (275,60))


            elif timer2>30 or len(listaVidas)==0:
                fuente = pygame.font.Font(None, 60)
                texto = fuente.render(("FIN DEL JUEGO"), 0, (255, 255, 255))
                ventana.blit(texto, (250, 260))
                imgBtnJugar = pygame.image.load("botonvolver.png")
                ventana.blit(imgBtnJugar, (ANCHO // 2 - 209//2, ALTO // 3*2))




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1 / 40
        wait+=1/40



    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()  # Por ahora, solo dibuja

# Llamas a la función principal
main()
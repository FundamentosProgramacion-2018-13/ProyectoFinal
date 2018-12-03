#----------------------

# Zoe Caballero Dominguez
# A01747247
# Grupo 04
# Proyecto Final Fundamentos de programación

#Créditos:
#Imágenes pertenecen a:
# https://www.facebook.com/bogo.teccem/photos
# y https://www.facebook.com/TecCEM/

#----------------------


#Librerias
import pygame
from random import randint


#Dimensiones de la pantalla
ANCHO = 800
ALTO = 600


#Variables globales
BLANCO =(225,225,225)
PISO = ALTO + 10
AZUL = (70,90,182)
NEGRO =(0,0,0)


#Estados
MENU = 1
JUGAR = 2
INSTRUCCIONES = 3
HIGH_SCORE = 4
GAMEOVER = 5
GANAR = 6


#Estados de movimiento
QUIETO = 1


#Funciones:


def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarObstaculo(ventana, listaObstaculos):
    for obstaculo in listaObstaculos:
        ventana.blit(obstaculo.image, obstaculo.rect)


def dibujarEstrellas(ventana, listaEstrellas):
    for estrella in listaEstrellas:
        ventana.blit(estrella.image, estrella.rect)


def moverObstaculo(listaObstaculo, xFondo):
    for obstaculo in listaObstaculo:

        if xFondo < -3200:     # Cambia la velocidad para aumentar la dificultad
            obstaculo.rect.left -= 11

        else:
            obstaculo.rect.left -= 10


def moverEstrellas(listaEstrellas, xFondo):
    for estrella in listaEstrellas:

        if xFondo < -3200:
            estrella.rect.left -= 11    #Cambia la velocidad

        else:
            estrella.rect.left -= 11


def dibujarMenu(ventana, imgFondoMenu):
    ventana.blit (imgFondoMenu, (0,0))


def dibujarInstrucciones (ventana, imgInstrucciones, imgRegresar):
    ventana.blit(imgInstrucciones, (0,0))
    ventana.blit(imgRegresar, (50, 520))


def dibujarHighScore (ventana, imgHighScore, imgRegresar):
    ventana.blit(imgHighScore, (0, 0))
    ventana.blit(imgRegresar, (50, 520))


def dibujarFondos(ventana, fondo1, fondo2, fondo3,fondo4, fondo5, xFondo):
    xf = xFondo
    yf = 0
    ventana.blit(fondo1, (xf,yf))
    ventana.blit(fondo2, (xf + 800, yf))
    ventana.blit(fondo3, (xf + 1600, yf))
    ventana.blit(fondo4, (xf + 2400, yf))
    ventana.blit(fondo5, (xf + 3200, yf))
    ventana.blit(fondo1, (xf + 4000, yf))
    ventana.blit(fondo2, (xf + 4800, yf))
    ventana.blit(fondo3, (xf + 5600, yf))
    ventana.blit(fondo4, (xf + 6400, yf))
    ventana.blit(fondo5, (xf + 7200, yf))


def dibujarVidas(ventana, listaVidas):
    for vida in listaVidas:
        ventana.blit(vida.image, vida.rect)


def verificarColisionObstaculos(listaLibros, spritePersonaje,efectoColision):
    for libros  in listaLibros:
        xP = spritePersonaje.rect.left
        yP = spritePersonaje.rect.bottom
        wP = spritePersonaje.rect.width

        xL = libros.rect.left
        yL = libros.rect.bottom
        wL = libros.rect.width
        hL = libros.rect.height

         #Colisión
        if (xP  + wP >= xL + 30 and xP + wP <= xL + wL+30 and yP >= yL - hL) or (xP<= xL + wL - 30 and xP >= xL  - 30 and yP >= yL + hL):
            efectoColision.play()
            listaLibros.remove(libros)
            return True


def quitarVidas(listaVidas, colision):
    for vida in listaVidas:

        if colision:
            listaVidas.remove(vida)
            break


def sumarPuntaje(colisionEstrella, saltoExitoso, puntaje):

    if colisionEstrella:
        puntaje += 100
        return puntaje

    elif saltoExitoso:
        puntaje += 1
        return puntaje

    else:
        return puntaje


def verificarColisionEstrella(listaEstrellas, spritePersonaje,efectoEstrella):
    for estrella in listaEstrellas:
        xP = spritePersonaje.rect.left
        yP = spritePersonaje.rect.bottom
        wP = spritePersonaje.rect.width
        hP = spritePersonaje.rect.height

        xE = estrella.rect.left
        yE = estrella.rect.bottom
        wE = estrella.rect.width
        hE = estrella.rect.height

        #Colisiçon
        if (xP + wP >= xE and xP + wP <= xE + wE and yP + hP <= yE) or (xP <= xE + wE and xP >= xE and yP + hP >= yE):
            efectoEstrella.play()
            listaEstrellas.remove(estrella)
            return True


def verificarSaltoExitoso(listaLibros, spritePersonaje):
    for libros in listaLibros:
        xP = spritePersonaje.rect.left
        yP = spritePersonaje.rect.bottom
        wP = spritePersonaje.rect.width

        xL = libros.rect.left
        yL = libros.rect.bottom
        wL = libros.rect.width
        hL = libros.rect.height

        if ((xP + wP >= xL and xP + wP <= xL + wL) and not (yP >= yL - hL)) or ((xP <= xL + wL and xP >= xL) and not(yP >= yL - hL)):
            return True


def crearListaPuntajes(archivo):
    entrada = open(archivo, "r", encoding="UTF-8")
    datos = []

    for linea in entrada:
        cantidad = linea.split("&")
        datos.append(int(cantidad[1]))

    entrada.close()
    return datos


def modificarArchivo(archivo, total, listaPuntajes):
    salida = open(archivo, "w", encoding="UTF - 8")
    contador = 0
    marcador = 1

    for dato in listaPuntajes:
        if total >= dato and contador == 0:
            listaPuntajes.append(total)
            contador += 1
    listaPuntajes.sort()
    listaPuntajes.reverse()
    listaPuntajes.remove(listaPuntajes[5])

    for cantidad in listaPuntajes:
        salida.write("%d&%d&\n" % (marcador, cantidad))
        marcador += 1

    salida.close()


def dibujar():
    #Inciar pygame
    pygame.init()
    #Crear ventana
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    #Variables iniciales
    estado = MENU
    velocidad1 = 10
    velocidad2 = 11
    xFondo = 0
    movimiento = QUIETO
    puntaje = 0
    bonus = 0
    total = 0

    #Menu
    imgFondoMenu = pygame.image.load("menu.png")

    #Fondos
    imgFondo1 = pygame.image.load("fondo tec 5.png")
    imgFondo2 = pygame.image.load("fondo tec 4.png")
    imgFondo3 = pygame.image.load("fondo tec 3.png")
    imgFondo4 = pygame.image.load("fondo tec 2.png")
    imgFondo5 = pygame.image.load("fondo tec 1.png")

    #Personaje:
    imgPersonajeDerecha = pygame.image.load("borrego1.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonajeDerecha
    spritePersonaje.rect= imgPersonajeDerecha.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = PISO

    #Vatiables salto
    saltando = False
    dY = 25

    #Vidas:
    listaVidas = []
    imgVidas = pygame.image.load("cafe.png")
    x = 20
    y = 60
    for k in range(3):
        spriteVidas = pygame.sprite.Sprite()
        spriteVidas.image = imgVidas
        spriteVidas.rect = imgVidas.get_rect()
        spriteVidas.rect.bottom = y
        spriteVidas.rect.left = x
        x += 30
        listaVidas.append(spriteVidas)


    #Obstaculos:
    listaLibros = []
    imgLibros = pygame.image.load("libros apilar.png")
    anchoLibro = 119

    comienzo = 400
    for k in range (17):
        spriteLibros = pygame.sprite.Sprite()
        spriteLibros.image = imgLibros
        spriteLibros.rect = imgLibros.get_rect()

        spriteLibros.rect.left = randint(comienzo, comienzo+anchoLibro)
        comienzo += 300

        spriteLibros.rect.bottom = PISO + 5
        listaLibros.append(spriteLibros)


    #Estrellas
    listaEstrellas = []
    imgEstrella = pygame.image.load("estrella.png")
    anchoEstrella = 50
    comienzo = 1000
    for k in range(8):
        spriteEstrella = pygame.sprite.Sprite()
        spriteEstrella.image= imgEstrella
        spriteEstrella.rect = imgEstrella.get_rect()
        spriteEstrella.rect.left = randint(comienzo, comienzo + anchoEstrella)
        comienzo += 500
        spriteEstrella.rect.bottom = PISO - 300
        listaEstrellas.append(spriteEstrella)


    #Instrucciones
    imgInstrucciones = pygame.image.load("instrucciones.png")
    imgRegresar = pygame.image.load("regresar.png")

    #Audios
    pygame.mixer.init()
    pygame.mixer.music.load("musicaDeFondo.mp3")
    pygame.mixer.music.play(-1)
    efecto = pygame.mixer.Sound("salto.wav")
    efectoColision = pygame.mixer.Sound("colision.wav")
    efectoEstrella = pygame.mixer.Sound("estrella.wav")


    #Texto
    fuente = pygame.font.SysFont("monospace", 50)

    #Game over
    imgPerder = pygame.image.load("GAME OVER.png")

    #High score
    imgHighScore = pygame.image.load("HighScore.png")

     #Ganar
    imgGanar = pygame.image.load ("ganaste.png")

    while not termina:
        #Eventos:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

            elif evento.type == pygame.MOUSEBUTTONUP: #Configuracion del click para cambiar de estados en el menu
                xm, ym = pygame.mouse.get_pos() # y, x del mouse

                if (xm>194 and xm<618 and ym>265 and ym<334) and estado == MENU:
                    estado = JUGAR

                elif (xm > 194 and xm < 618 and ym > 351 and ym < 419) and estado == MENU:
                    estado = INSTRUCCIONES

                elif (xm>194 and xm<618 and ym>440 and ym<507) and estado == MENU:
                    estado = HIGH_SCORE

                elif (xm>=50 and xm <= 100 and ym<=570 and ym>=520) and (estado == INSTRUCCIONES or estado == HIGH_SCORE):
                    estado = MENU

            elif evento.type == pygame.KEYDOWN:
                key = evento.key
                if key == pygame.K_UP:
                    saltando = True
                    efecto.play()

            elif evento.type == pygame.KEYUP:
                    if not saltando:
                        movimiento = QUIETO


        #Borrar Pantalla
        ventana.fill(BLANCO)

        if estado == MENU:
            #DIBUJAR MENU
            dibujarMenu(ventana, imgFondoMenu)

        elif estado == INSTRUCCIONES:
            #Dibujar instrucciones
            dibujarInstrucciones(ventana, imgInstrucciones, imgRegresar)

        elif estado == JUGAR:
            #FONDO
            dibujarFondos(ventana, imgFondo1,imgFondo2,imgFondo3,imgFondo4,imgFondo5, xFondo)
            pygame.draw.rect(ventana, AZUL, (0, 0, 800, 70))

            #Cambio de velocidades
            if xFondo > -7200:
                xFondo -= velocidad1
            if xFondo < -3200 and xFondo > -7200:
                xFondo -= velocidad2

            #Final del juego si el jugador tiene minimo 1 vida
            if xFondo <= -7200:
                if len(listaVidas) > 1:
                    for vida in listaVidas:
                        bonus += 200
                        listaVidas.remove(vida)

                elif len(listaVidas) == 1:
                    bonus = 200
                total = puntaje + bonus
                estado = GANAR

            # Actualizar
            moverObstaculo(listaLibros, xFondo)
            moverEstrellas(listaEstrellas,xFondo)

            colisionObstaculo = verificarColisionObstaculos(listaLibros, spritePersonaje,efectoColision)
            quitarVidas(listaVidas, colisionObstaculo)

            #Revisar para aumentar puntaje
            saltoExitoso = verificarSaltoExitoso(listaLibros, spritePersonaje)
            colisionEstrella = verificarColisionEstrella(listaEstrellas, spritePersonaje,efectoEstrella)

            #Sumar puntaje
            puntaje = sumarPuntaje(colisionEstrella, saltoExitoso,puntaje)

            #Mostrar puntaje
            if puntaje > 0:
                texto = fuente.render("Puntaje: %d" % puntaje, 1, BLANCO)
                ventana.blit(texto, (520, 15))
            else:
                texto = fuente.render("Puntaje: 0", 1, BLANCO)
                ventana.blit(texto, (520, 15))

            #Dibujar
            dibujarObstaculo(ventana, listaLibros)
            dibujarEstrellas(ventana, listaEstrellas)
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarVidas(ventana, listaVidas)

            #Movimiento y salto
            if movimiento == QUIETO:
                spritePersonaje.rect.bottom = spritePersonaje.rect.bottom

            if saltando:
                alturaSalto = dY + 325
                spritePersonaje.rect.bottom -= dY

                if spritePersonaje.rect.bottom <= alturaSalto:
                    dY = -dY

                if spritePersonaje.rect.bottom >= PISO:
                    dY = -dY
                    saltando = False
                    movimiento = QUIETO


            #Perder si ya no hay vidas
            if len(listaVidas) == 0:
                estado = GAMEOVER


        elif estado == HIGH_SCORE:
            #Leer archivo y mostrar resultados
            archivo = open ("highScore.txt", "r", encoding="UTF-8")
            dibujarHighScore(ventana, imgHighScore, imgRegresar)

            y = 200
            cadena = ""

            for linea in archivo:
                palabras = linea.split("&")
                texto = fuente.render("%s.- %s" % (palabras[0], palabras[1]), 1, BLANCO)
                ventana.blit(texto, (350, y))
                y += 50

        #Perdió
        elif estado == GAMEOVER:
            ventana.blit(imgPerder, (0,0))

        #Ganó
        elif estado == GANAR:
            ventana.blit(imgGanar, (0, 0))

            #Puntaje
            texto = fuente.render("Puntaje: %d" % puntaje, 1, BLANCO)
            ventana.blit(texto, (50, 15))

            #Puntos extra
            texto = fuente.render("Bonus por vidas: %d" % bonus, 1, BLANCO)
            ventana.blit(texto, (50, 50))

            #Puntaje final
            texto = fuente.render("Puntaje Final: %d" % total, 1, BLANCO)
            ventana.blit(texto, (300, 15))


        pygame.display.flip()
        reloj.tick(40)

    #Modificar puntaje si el jugador gana
    if estado == GANAR:
        listaPuntajes = crearListaPuntajes("highScore.txt")
        modificarArchivo("highScore.txt", total, listaPuntajes)


    pygame.quit()


#Función principal
def main():
    dibujar()


#Llamar a main
main()
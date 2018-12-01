#Francisco Ariel Arenas Enciso
#A01369122
#Desarrollo de un videojuego mediante Pygame (Proyecto final)

'Importación de librerías'
import pygame
import random
import time

pygame.init()                                           #Se inicializa pygame

'Declaración de variables globales'
ANCHO = 800                                             #Ancho de la pantalla
ALTO = 600                                              #Alto de la pantalla

'Colores'
#Color         #R       #G      #B
Blanco =      (255,     255,    255)
Negro =       (0,       0,      0)
Rojo =        (255,     0,      0)
Azul =        (0,       0,      255)

'Estados'
MENU = 1
JUGANDO = 2
CONTROLES = 3
MARCADORES = 4


'Función para dibujar al personaje'
def dibujarPersonaje(ventana, imagen, x, y):
    ventanaDeJuego = ventana                    #Se define la pantalla de juego
    imagenMario = imagen                        #Se define la imagen del personaje
    x = x                                       #Posición en 'x' de la imagen del personaje
    y = y                                       #Posición en 'y' de la imagen del personaje
    ventanaDeJuego.blit(imagenMario, (x, y))    #Se dibuja al personaje en la ventana


'Función que dibuja al primer obstáculo'
def dibujarObstaculoUno(ventana, imagen, xObstaculo, yObstaculo):
    ventanaDeJuego = ventana                    #Se define la pantalla de juego
    imagenObstaculo = imagen                    #Se define la imagen del obstáculo
    x = xObstaculo                              #Posición en 'x' de la imagen
    y = yObstaculo                              #Posición en 'y' de la imagen
    ventanaDeJuego.blit(imagenObstaculo, (x, y))


'Función que dibuja al segundo obstáculo'
def dibujarObstaculoDos(ventana, imagen, xObstaculo, yObstaculo):
    ventanaDeJuego = ventana                    #Se define la pantalla de juego
    imagenObstaculo = imagen                    #Se define la imagen del obstáculo
    x = xObstaculo                              #Posición en 'x' de la imagen
    y = yObstaculo                              #Posición en 'y' de la imagen
    ventanaDeJuego.blit(imagenObstaculo, (x, y))


'Función que dibuja al tercer obstáculo'
def dibujarObstaculoTres(ventana, imagen, xObstaculo, yObstaculo):
    ventanaDeJuego = ventana                    #Se define la pantalla de juego
    imagenObstaculo = imagen                    #Se define la imagen del obstáculo
    x = xObstaculo                              #Posición en 'x' de la imagen
    y = yObstaculo                              #Posición en 'y' de la imagen
    ventanaDeJuego.blit(imagenObstaculo, (x, y))


'Función que dibuja a la moneda'
def dibujarMoneda(ventana, imagen, xMoneda, yMoneda):
    ventanaDeJuego = ventana                    #Se define la pantalla de juego
    imagenMoneda = imagen                       #Se define la imagen de la moneda
    x = xMoneda                                 #Posición en 'x' de la imagen
    y = yMoneda                                 #Posición en 'y' de la imagen
    ventanaDeJuego.blit(imagenMoneda, (x, y))


'Función para puntos'
def hacerPuntaje(ventana, monedasAcumuladas):
    ventanaDeJuego = ventana
    fuenteTexto = pygame.font.SysFont(None, 25)
    texto = fuenteTexto.render("Monedas recolectadas: " + str(monedasAcumuladas), True, Negro)
    ventanaDeJuego.blit(texto, (0, 0))


'Función para dibujar los botones'
def dibujarBotones(ventana, x, y, ancho, alto, imagenUno, imagenDos):
    ventanaDeJuego = ventana                                        #Se carga la ventana
    mouse = pygame.mouse.get_pos()                                  #Obtiene la posición del mouse para poder...
                                                                    #...actualizar la imagen

    if x + ancho > mouse[0] > x and y + alto > mouse[1] > y:        #Se pregunta respecto la posición del mouse
        ventanaDeJuego.blit(imagenDos, (x, y))                      #Se actuliza la imagen del botón
    else:
        ventanaDeJuego.blit(imagenUno, (x, y))                      #Si no pasa nada, no se actualiza


'Función para dibujar la pantalla de GameOver'
def dibujarPerdio(ventana, imagen, sonido):
    sonido.play()
    imagenPerdio = imagen                             #Se define la imagen del personaje
    ventanaDeJuego = ventana                          #Se define la pantalla de juego
    ventanaDeJuego.blit(imagenPerdio, (0,0))          #Se dibuja la imagen
    pygame.display.update()                           #Se actualiza el display de pygame
    time.sleep(3)                                     #Se establece cuánto tiempo se quiere ver esta pantalla
    dibujarJuego()                                    #Se lleva al jugador al menu


'Función para dibujar la pantalla de Limite'
def dibujarLimite(ventana, imagen, sonido):
    sonido.play()
    imagenLimite = imagen                             #Se define la imagen del personaje
    ventanaDeJuego = ventana                          #Se define la pantalla de juego
    ventanaDeJuego.blit(imagenLimite, (0,0))          #Se dibuja la imagen
    pygame.display.update()                           #Se actualiza el display de pygame
    time.sleep(1)                                     #Se establece cuánto tiempo se quiere ver esta pantalla
    dibujarJuego()                                    #Se lleva al jugador al menu


'Función para actualizar el puntje'
def actualizarPuntos(puntosJugador):
    if puntosJugador > 0:                             #Se pregunta si el jugador tuvo un puntaje mayor a 0
        archivo = open("Puntos.txt", "w")             #Se abre el archivo
        archivo.write(str(puntosJugador))             #Se actualiza el archivo
        archivo.close()                               #Se cierra el archivo


'Estructura del programa (se dibuja todo lo anterior'
def dibujarJuego():
    ventanaDeJuego = pygame.display.set_mode((ANCHO, ALTO))    #Se crea la pantalla
    pygame.display.set_caption("Mamma mia! It's a kart!")      #Nombre del juego
    logo = pygame.image.load("Logo.png")                       #Se carga la imagen para el logo
    pygame.display.set_icon(logo)                              #Logo en ventana
    reloj = pygame.time.Clock()                                #Limitar FPS


    ### Imágen del personaje ###
    imagenMario = pygame.image.load("marioJuego.png")          #Se carga la imagen
    anchoImagen = 80                                           #De la imagen, se obtiene el ancho
    x = ANCHO * 0.45                                           #Posición en 'x'
    y = ALTO * 0.8                                             #Posición en 'y'
    cambioEnX = 0                                              #Contador para actualizar posición
    ### Imágen del personaje ###

    ### Imágen obstáculo ###
    imagenObstaculo = pygame.image.load("obstaculo.png")       #Se carga la imagen
    anchoObstaculo = 80                                        #De la imagen, se obtiene el ancho
    altoObstaculo = 70                                         #De la imagen, se obtiene el alto
    xObstaculo = random.randrange(0, ANCHO)                    #Posición en 'x'
    yObstaculo = -600                                          #Posición en 'y'
    velocidad = 10                                             #Velocidad de caída del objeto

    imagenObstaculoDos = pygame.image.load("obstaculoDos.png") #Se carga la imagen
    anchoObstaculoDos = 80                                     #De la imagen, se obtiene el ancho
    altoObstaculoDos = 70                                      #De la imagen, se obtiene el alto
    xObstaculoDos = random.randrange(0, ANCHO)                 #Posición en 'x'
    yObstaculoDos = -650                                       #Posición en 'y'
    velocidadDos = 0.5                                         #Velocidad de caída del objeto

    imagenObstaculoTres = pygame.image.load("obstaculoTres.png") #Se carga la imagen
    anchoObstaculoTres = 80                                      #De la imagen, se obtiene el ancho
    altoObstaculoTres = 70                                       #De la imagen, se obtiene el alto
    xObstaculoTres = random.randrange(0, ANCHO)                  #Posición en 'x'
    yObstaculoTres = -650                                        #Posición en 'y'
    velocidadTres = 0.1                                          #Velocidad de caída del objeto
    ### Imágen obstáculo ###

    ### Imágen moneda ###
    imagenMoneda = pygame.image.load("moneda.png")             #Se carga la imagen
    anchoMoneda = 80                                           #De la imagen, se obtiene el ancho
    altoMoneda = 70                                            #De la imagen, se obtiene el alto
    xMoneda = random.randrange(0, ANCHO)                       #Posición en 'x'
    yMoneda = -600                                             #Posición en 'y'
    velocidadMoneda = 20                                       #Velocidad de caída del objeto
    ### Imágen moneda ###

    ### Puntaje Monedas ###
    monedasColectadas = 0                                      #Se establece el contador de monedas
    ### Puntaje Monedas ###

    ### Imágenes de fondo y botones ###
    imagen = [
        pygame.image.load("fondoNivelBase.png"),
        pygame.image.load("FondoPerdio.png"),
        pygame.image.load("fondoMenu.png"),
        pygame.image.load("jugarUno.png"),
        pygame.image.load("jugarDos.png"),
        pygame.image.load("controlUno.png"),
        pygame.image.load("controlDos.png"),
        pygame.image.load("puntosUno.png"),
        pygame.image.load("puntosDos.png"),
        pygame.image.load("fondoLimite.png"),
        pygame.image.load("regresarUno.png"),
        pygame.image.load("regresarDos.png"),
        pygame.image.load("fondoPuntos.png"),
        pygame.image.load("fondoControles.png")
    ]
    ### Imágenes de fondo y botones ###

    ### ANIMACIÓN MENU ###
    imagenMarioMenu = pygame.image.load("marioMenu.png")        #Se carga la imagen delpersonaje como animación en Menú
    xMario = -200                                               #Se establece la posición del personaje en 'x'
    yMario = 500                                                #Se establece la posición del personaje en 'y'
    ### ANIMACIÓN MENU ###

    ### ESTADO ###
    estadoJuego = MENU
    ### ESTADO ###

    ### AUDIO ###
    pygame.mixer.init()
    pygame.mixer.music.load("Juego.wav")
    pygame.mixer.music.play(-1)
    musica = [
        pygame.mixer.Sound("Colision.wav"),
        pygame.mixer.Sound("Moneda.wav"),
        pygame.mixer.Sound("GameOver.wav"),
        pygame.mixer.Sound("Puntos.wav"),
        pygame.mixer.Sound("Jugar.wav"),
        pygame.mixer.Sound("Limite.wav"),
        pygame.mixer.Sound("Creditos.wav")
    ]
    ### AUDIO ###

    ### ARCHIVO ###
    archivoPuntos = open("Puntos.txt", "r")                    #Se abre el archivo para leer

    puntosOriginales = archivoPuntos.readline()                #Se lee la línea

    archivoPuntos.close()                                      #Se cierra el archivo
    ### ARCHIVO ###

    puntosJugador = 0                                          #Contdador para actualizar el puntaje

    terminado = False                                          #¿Se acabó el juego?, NO

    #pygame.init()
    ### CICLO PRINCIPAL ###
    while not terminado:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()                                  #El jugador quiere salir del juego
                quit()

            ### Movimiento de la imagen con teclado ###
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    cambioEnX -= 15
                elif evento.key == pygame.K_RIGHT:
                    cambioEnX += 15

            if evento.type == pygame.KEYUP:
                if evento.key == pygame.K_LEFT or evento.key == pygame.K_RIGHT:
                    cambioEnX = 0
            ### Movimiento de la imagen con teclado ###

            ### MOUSE ###
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                anchoBoton = 150
                altoBoton = 50
                xBotonUno = 150
                yBotonUno = 360
                xBotonDos = 480
                yBotonDos = 360
                xBotonTres = 315
                yBotonTres = 420
                xBotoncCuatro = 330
                yBotonCuatro = 450
                if xm >= xBotonUno and xm <= xBotonUno + anchoBoton and ym >= yBotonUno and ym <= yBotonUno + altoBoton:
                    pygame.mixer.music.pause()
                    musica[4].play()
                    estadoJuego = JUGANDO
                elif xm >= xBotonDos and xm <= xBotonDos + anchoBoton and ym >= yBotonDos and ym <= yBotonDos + altoBoton:
                    pygame.mixer.music.pause()
                    musica[3].play()
                    estadoJuego = MARCADORES
                elif xm >= xBotonTres and xm <= xBotonTres + anchoBoton and ym >= yBotonTres and ym <= yBotonTres + altoBoton:
                    pygame.mixer.music.pause()
                    musica[6].play()
                    estadoJuego = CONTROLES
                elif xm >= xBotoncCuatro and xm <= xBotoncCuatro + anchoBoton and ym >= yBotonCuatro and ym <= yBotonCuatro + altoBoton:
                    pygame.mixer.music.unpause()
                    estadoJuego = MENU
            ### MOUSE ###

        if estadoJuego == JUGANDO:
            pygame.mixer.music.unpause()
            x += cambioEnX                                         #Se actualiza la posición de la imagen
            yObstaculo += velocidad                                #Se actuliza la posición de 'y' del obstaculo
            yObstaculoDos += velocidadDos                          #Se actualiza la posición de 'y' del segundo obstáculo
            yObstaculoTres += velocidadTres                        #Se actualiza la posición de 'y' del tercer obstáculo
            yMoneda += velocidadMoneda                             #Se actuliza la posición de 'y' de la moneda
            ventanaDeJuego.blit(imagen[0], (0,0))                  #Se dibuja el fondo del juego
            dibujarPersonaje(ventanaDeJuego, imagenMario, x, y)    #Se dibuja el personaje
            dibujarObstaculoUno(ventanaDeJuego, imagenObstaculo, xObstaculo, yObstaculo)           #Se dibuja un obstáculo
            dibujarObstaculoDos(ventanaDeJuego, imagenObstaculoDos, xObstaculoDos, yObstaculoDos)  #Se dibuja otro obstáculo
            dibujarObstaculoTres(ventanaDeJuego, imagenObstaculoTres, xObstaculoTres, yObstaculoTres) #Otro obstáculo
            dibujarMoneda(ventanaDeJuego, imagenMoneda, xMoneda, yMoneda)                 #Se dibuja la moneda
            hacerPuntaje(ventanaDeJuego, monedasColectadas)        #Se imprime el contador de monedas

            ### Limites de para la pantalla ###
            if x > ANCHO - anchoImagen or x < 0:
                pygame.mixer.music.stop()                          #Se detiene la música
                dibujarLimite(ventanaDeJuego, imagen[9], musica[5])
                estadoJuego = MENU
            ### Limites de para la pantalla ###

            ### Actualización de posición de los obstáculos ###
            if yObstaculo > ALTO:                                  #Condición para saber si el objeto sale de la pantalla
                yObstaculo = 0 - altoObstaculo                     #Al hacerlo, su posición en 'y' debe ser como la original
                xObstaculo = random.randrange(0, ANCHO)            #También se genera una nueva posición en 'x'

            if yObstaculoDos > ALTO:                               #Condición para saber si el objeto sale de la pantalla
                yObstaculoDos = 0 - altoObstaculoDos               #Al hacerlo, su posición en 'y' debe ser como la original
                xObstaculoDos = random.randrange(0, ANCHO)         #También se genera una nueva posición en 'x'

            if yObstaculoTres > ALTO:                              #Condición para saber si el objeto sale de la pantalla
                yObstaculoTres = 0 - altoObstaculoTres             #Al hacerlo, su posición en 'y' debe ser como la original
                xObstaculoTres = random.randrange(0, ANCHO)        #También se genera una nueva posición en 'x'
            ### Actualización de posición de los obstáculos ###

            ### Actualización de posición de moneda ###
            if yMoneda > ALTO:                                     #Condición para saber si el objeto sale de la pantalla
                yMoneda = 0 - altoMoneda                           #Al hacerlo, su posición en 'y' debe ser como la original
                xMoneda = random.randrange(0, ANCHO)               #También se genera una nueva posición en 'x'
            ### Actualización de posición de moneda ###

            ### Colsiones con obstáculos ###
            if y < yObstaculo + altoObstaculo:
                if x > xObstaculo and x < xObstaculo + anchoObstaculo or x + anchoImagen > xObstaculo and x + anchoImagen < xObstaculo + anchoObstaculo:
                    pygame.mixer.music.stop()
                    musica[0].play()
                    dibujarPerdio(ventanaDeJuego, imagen[1], musica[2])
                    estadoJuego = MENU                             #Se vuelve al menu
            if y < yObstaculoDos + altoObstaculoDos:
                if x > xObstaculoDos and x < xObstaculoDos + anchoObstaculoDos or x + anchoImagen > xObstaculoDos and x + anchoImagen < xObstaculoDos + anchoObstaculoDos:
                    pygame.mixer.music.stop()
                    musica[0].play()
                    dibujarPerdio(ventanaDeJuego, imagen[1],  musica[2])
                    estadoJuego = MENU                             #Se vuelve al menu
            if y < yObstaculoTres + altoObstaculoTres:
                if x > xObstaculoTres and x < xObstaculoTres + anchoObstaculoTres or x + anchoImagen > xObstaculoTres and x + anchoImagen < xObstaculoTres + anchoObstaculoTres:
                    pygame.mixer.music.stop()
                    musica[0].play()
                    dibujarPerdio(ventanaDeJuego, imagen[1],  musica[2])
                    estadoJuego = MENU                             #Se vuelve al menu
            ### Colsiones con obstáculos ###

            puntos = False                                         #Bandera para actualizar puntaje

            ### Colisiones con moneda ###
            if y < yMoneda + altoMoneda:
                if x > xMoneda and x < xMoneda + anchoMoneda or x + anchoImagen > xMoneda and x + anchoImagen < xMoneda + anchoMoneda:
                    yMoneda = 0 - altoMoneda                       #Se regresa a la posición 'y' incial
                    xMoneda = random.randrange(0, ANCHO)           #Se genera una nueva posición en 'x' para la moneda
                    musica[1].play()
                    monedasColectadas += 1                         #Se actualiza el contador
                    velocidad += 0.5                               #Se incrementa la velocidad con cada vuelta
                    puntos = True                                  #Actualizar bandera
                    if monedasColectadas >= 5:
                        velocidadDos = 3 + monedasColectadas       #Aparece un nuevo obstáculo
                    if monedasColectadas >= 10:
                        velocidadTres = 6 + monedasColectadas      #Aparece un nuevo obstáculo
            ### Colisiones con moneda ###

            if puntos == True:
                puntosJugador += 1
                actualizarPuntos(puntosJugador)


        elif estadoJuego == MARCADORES:
            ventanaDeJuego.blit(imagen[12], (0, 0))
            fuenteTexto = pygame.font.SysFont(None, 30)
            texto = fuenteTexto.render("Monedas recolectadas en tu última ronda: " + str(puntosOriginales), True, Negro)
            ventanaDeJuego.blit(texto, (200, 270))
            dibujarBotones(ventanaDeJuego, 330, 450, 150, 50, imagen[10], imagen[11])
            pygame.display.update()
            reloj.tick(15)


        elif estadoJuego == CONTROLES:
            ventanaDeJuego.blit(imagen[13], (0, 0))
            dibujarBotones(ventanaDeJuego, 330, 450, 150, 50, imagen[10], imagen[11])
            pygame.display.update()
            reloj.tick(15)


        elif estadoJuego == MENU:
            ventanaDeJuego.blit(imagen[2], (0, 0))                                             #Dibuja Menu
            dibujarBotones(ventanaDeJuego, 150, 360, 150, 50, imagen[3], imagen[4])            #Dibuja botón
            dibujarBotones(ventanaDeJuego, 480, 360, 150, 50, imagen[7], imagen[8])            #Dibuja botón
            dibujarBotones(ventanaDeJuego, 315, 420, 150, 50, imagen[5], imagen[6])            #Dibuja botón
            ventanaDeJuego.blit(imagenMarioMenu, (xMario, yMario))                             #Dibuja personaje
            xMario += 5                 #Se actualiza la posición del personaje
            if xMario > ANCHO + 30:     #Si sale de la pantalla la imagen...
                xMario = -200           #...su posición 'x' se reinicia
            pygame.display.update()
            reloj.tick(15)

        pygame.display.update()                                #Se actualiza pygame (lo mismo que 'flip()')
        reloj.tick(30)                                         #Cantidad de FPS

    pygame.quit()                                              #Se cierra pygame


'Función main que ejecutará el juego'
def main():
    dibujarJuego()                              #Se llama a la función que contiene el ciclo principal


main()                                          #Se llama a main



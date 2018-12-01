#Marco González Elizalde A01376527
#Proyecto Final de Introducción a la programación Semestre 2018-13

import pygame
from random import randint

"""Ya que decidi mover la respuesta del programa al click del boton del mouse derecho a solo cuando se está
en el estado de juego en que se muestra el boton (el menú o cuando se pierde), esto resultó en que la respuesta
sea lenta y que no reaccione al primer click. No encontré la forma de arreglar esto obteniendo un resultado
que me convenciera así que decidí dejarlo así. Le pido de favor darle click a los botones cuantas veces sea necesario
para que se ejecute la acción. Muchas Gracias"""

#Dimensiones de pantalla
ANCHO = 800
ALTO = 600
#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255,0,0)
VERDE = (59,179,34)
VERDE_BOSQUE =(34,139,34)
VERDE_LIMA = (50,205,50)
AZUL = (0,191,255)
ROSA = (255,20,147)
MAGENTA = (139,0,139)
LIMON = (255,250,205)
NARANJA = (255,128,0)
#Estados
MENU = 1
JUGANDO = 2
GANAR = 3
PERDER = 4
estadoJuego = MENU
#Movimiento
QUIETO = 0
IZQUIERDA = 1
DERECHA = 2
SALTO = 3

def dibujarPersonaje(ventana, sprite):
    ventana.blit(sprite.image, sprite.rect)


def dibujarMeteorito(ventana, lista):
    #Visita cada uno de los datos de los enemigos
    for meteorito in lista:
        ventana.blit(meteorito.image, meteorito.rect)


def actualizarMeteoritos(ventana, lista, velocidad):
    for meteorito in lista:
        if meteorito.rect.bottom > ALTO -5:
            lista.remove(meteorito)
        else:
            meteorito.rect.bottom += velocidad


def crearMeteoritos(imgMeteoritoA, imgMeteoritoB, cantidad, lista):
    for k in range (cantidad):
        tipo = randint(1,2)
        spriteMeteorito = pygame.sprite.Sprite()
        if tipo == 1:
            spriteMeteorito.image = imgMeteoritoA
            spriteMeteorito.rect = imgMeteoritoA.get_rect()
            spriteMeteorito.rect.left = randint(0, ANCHO - spriteMeteorito.rect.width)
            spriteMeteorito.rect.bottom = 0
        if tipo == 2:
            spriteMeteorito.image = imgMeteoritoB
            spriteMeteorito.rect = imgMeteoritoB.get_rect()
            spriteMeteorito.rect.left = randint(0, ANCHO - spriteMeteorito.rect.width)
            spriteMeteorito.rect.bottom = 0
        lista.append(spriteMeteorito)


def verificarColisionMeteorito(listaMeteoritos, spriteMono):
    xSprite, ySprite, anchoSprite, altoSprite = spriteMono.rect
    for meteorito in listaMeteoritos:
        xMeteorito, yMeteorito, anchoMeteorito, altoMeteorito = meteorito.rect
        if ((xSprite >= xMeteorito and xSprite <= xMeteorito + anchoMeteorito) and (ySprite - altoSprite <= yMeteorito))\
            or ((xSprite + anchoSprite >= xMeteorito and xSprite + anchoSprite <= xMeteorito + anchoMeteorito)
                and (ySprite - altoSprite <= yMeteorito)):
                global estadoJuego
                estadoJuego = PERDER
                return True
    return False

def guardarPuntaje(timer, archivo):
    puntajes = open(archivo , "r")
    puntajeOriginal = float(puntajes.readline())
    if timer > puntajeOriginal:
        salida = open(archivo , "w")
        salida.write(str(timer))
        salida.close()
    puntajes.close()


def leerPuntaje(archivo):
    entrada = open(archivo, "r")
    puntaje = entrada.readline()
    entrada.close()
    return puntaje[:5]


def dibujar():
    #Inicializar motor pygame
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    #Menu
    global estadoJuego
    imgBotJugar = pygame.image.load("botonJugar.png")
    #Perder
    imgBotSi = pygame.image.load("button_si.png")
    imgBotNo = pygame.image.load("button_no.png")

    #FONDO
    #...

    #PUNTAJE
    #Contador de tiempo
    timer = 0
    timerViejo = 0
    nivel = 1

    # TEXTO
    fuente = pygame.font.SysFont("monospace", 40)  # Crea una fuente para poder generar letreros
    fuenteGrande = pygame.font.SysFont("monospace", 70)
    fuentePequeña = pygame.font.SysFont("monospace", 20)

    #AUDIO
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("splat.wav")
    impacto = pygame.mixer.Sound("crash.wav")
    pygame.mixer.music.load("rainstorm.mp3")
    pygame.mixer.music.play(-1)

    #PERSONAJES
    #Mono de palitos
    movimiento = QUIETO
    contadorMov = 0
    velocidadMono = 4.5
    listaSpritesMono = []
    imgMono = pygame.image.load("monoQuieto.png")
    spriteMono = pygame.sprite.Sprite() #Sprite vacio
    spriteMono.image = imgMono
    spriteMono.rect = imgMono.get_rect() #Coordenadas vacias
    spriteMono.rect.left = ANCHO//2
    spriteMono.rect.bottom = ALTO
    listaSpritesMono.append(spriteMono)
    #Movimiento DERECHA
    imgMonoDer1 = pygame.image.load("monoDerecha1.png")
    spriteMonoDer1 = pygame.sprite.Sprite()  # Sprite vacio
    spriteMonoDer1.image = imgMonoDer1
    spriteMonoDer1.rect = imgMonoDer1.get_rect()  # Coordenadas vacias
    spriteMonoDer1.rect.left = ANCHO // 2
    spriteMonoDer1.rect.bottom = ALTO
    listaSpritesMono.append(spriteMonoDer1)
    imgMonoDer2 = pygame.image.load("monoDerecha2.png")
    spriteMonoDer2 = pygame.sprite.Sprite()  # Sprite vacio
    spriteMonoDer2.image = imgMonoDer2
    spriteMonoDer2.rect = imgMonoDer2.get_rect()  # Coordenadas vacias
    spriteMonoDer2.rect.left = ANCHO // 2
    spriteMonoDer2.rect.bottom = ALTO
    listaSpritesMono.append(spriteMonoDer2)
    # Movimiento IZQUIERDA
    imgMonoIzq1 = pygame.image.load("monoIzquierda1.png")
    spriteMonoIzq1 = pygame.sprite.Sprite()  # Sprite vacio
    spriteMonoIzq1.image = imgMonoIzq1
    spriteMonoIzq1.rect = imgMonoIzq1.get_rect()  # Coordenadas vacias
    spriteMonoIzq1.rect.left = ANCHO // 2
    spriteMonoIzq1.rect.bottom = ALTO
    listaSpritesMono.append(spriteMonoIzq1)
    imgMonoIzq2 = pygame.image.load("monoIzquierda2.png")
    spriteMonoIzq2 = pygame.sprite.Sprite()  # Sprite vacio
    spriteMonoIzq2.image = imgMonoIzq2
    spriteMonoIzq2.rect = imgMonoIzq2.get_rect()  # Coordenadas vacias
    spriteMonoIzq2.rect.left = ANCHO // 2
    spriteMonoIzq2.rect.bottom = ALTO
    listaSpritesMono.append(spriteMonoIzq2)

    #Enemigos
    #Meteoritos
    listaMeteoritos = []
    velocidadMeteoritos = 2
    cantidadMeteoritos = 2
    nuevoSpawn = ALTO - 5
    imgMeteoritoA = pygame.image.load("meteoritoA.png")
    imgMeteoritoB = pygame.image.load("meteoritoB.png")
    crearMeteoritos(imgMeteoritoA, imgMeteoritoB, cantidadMeteoritos, listaMeteoritos)

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    movimiento = IZQUIERDA
                elif evento.key == pygame.K_d:
                    movimiento = DERECHA
                elif evento.key == pygame.K_s:
                    movimiento = QUIETO
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xMouse, yMouse = pygame.mouse.get_pos()
                xBoton = ANCHO // 2 - 100
                yBoton = ALTO // 2 - 100
                anchoBoton = 200
                altoBoton = 80
                if xMouse >= xBoton and xMouse <= xBoton + anchoBoton and yMouse >= yBoton and yMouse <= yBoton + altoBoton:
                    estadoJuego = JUGANDO

        if estadoJuego == MENU:
            ventana.fill(NEGRO)
            titulo = fuenteGrande.render("SURVIVAL", 0, BLANCO)
            letreroPuntaje = fuentePequeña.render("HIGHSCORE:", 0, BLANCO)
            highscore = leerPuntaje("puntaje.txt")
            letreroHighscore = fuentePequeña.render("%s segundos" %highscore, 0, BLANCO)
            instruccionesA = fuentePequeña.render("COMO JUGAR:", 0, BLANCO)
            instruccionesB = fuentePequeña.render("A - Izquierda", 0, BLANCO)
            instruccionesC = fuentePequeña.render("S - Quedarse Quieto", 0, BLANCO)
            instruccionesD = fuentePequeña.render("D - Derecha", 0, BLANCO)
            ventana.blit(titulo, (ANCHO//2-165, ALTO//2-230))
            ventana.blit(imgBotJugar, (ANCHO//2-100, ALTO//2-100))
            ventana.blit(letreroPuntaje, (ANCHO//2 - 300, ALTO//2+120))
            ventana.blit(letreroHighscore, (ANCHO // 2 - 300, ALTO // 2 + 150))
            ventana.blit(instruccionesA, (ANCHO//2 +130, ALTO//2 +80))
            ventana.blit(instruccionesB, (ANCHO // 2 + 130, ALTO // 2 + 110))
            ventana.blit(instruccionesC, (ANCHO // 2 + 130, ALTO // 2 + 140))
            ventana.blit(instruccionesD, (ANCHO // 2 + 130, ALTO // 2 + 170))
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    termina = True
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    xMouse, yMouse = pygame.mouse.get_pos()
                    xBoton = ANCHO // 2 - 100
                    yBoton = ALTO // 2 - 100
                    anchoBoton = 200
                    altoBoton = 80
                    if xMouse >= xBoton and xMouse <= xBoton + anchoBoton and yMouse >= yBoton and yMouse <= yBoton + altoBoton:
                        estadoJuego = JUGANDO


        elif estadoJuego == PERDER:
            ventana.fill(BLANCO)
            letrero = fuenteGrande.render("HAS PERDIDO", 0, NEGRO)
            retry = fuente.render("¿Jugar de nuevo?", 0, NEGRO)
            sobrevivido = fuente.render("Tiempo Sobrevivido:", 0, ROJO)
            letreroTimer = fuente.render("%.2f segundos" %timer, 0, ROJO)
            ventana.blit(letrero, (185,ALTO//2-200))
            ventana.blit(retry, (210, ALTO//2+30))
            ventana.blit(sobrevivido, (190, ALTO//2-100))
            ventana.blit(letreroTimer, (250, ALTO//2-40))
            ventana.blit(imgBotSi, (280, ALTO//2+100))
            ventana.blit(imgBotNo, (450, ALTO//2+100))

            guardarPuntaje(timer, "puntaje.txt")

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    termina = True
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    xMouse, yMouse = pygame.mouse.get_pos()
                    xBotonSi = 280
                    yBotonSi = ALTO//2+100
                    xBotonNo = 450
                    yBotonNo = ALTO // 2+100
                    anchoBoton = 80
                    altoBoton = 50
                    if xMouse >= xBotonSi and xMouse <= xBotonSi + anchoBoton and yMouse >= yBotonSi and yMouse <= yBotonSi + altoBoton:
                        listaMeteoritos.clear()
                        crearMeteoritos(imgMeteoritoA,imgMeteoritoB,2,listaMeteoritos)
                        contadorMov = 0
                        nivel = 1
                        timer = 0
                        timerViejo = 0
                        velocidadMeteoritos = 2
                        movimiento = QUIETO
                        estadoJuego = JUGANDO
                        for sprite in listaSpritesMono:
                            sprite.rect.left = ANCHO//2
                    if xMouse >= xBotonNo and xMouse <= xBotonNo + anchoBoton and yMouse >= yBotonNo and yMouse <= yBotonNo + altoBoton:
                        listaMeteoritos.clear()
                        crearMeteoritos(imgMeteoritoA,imgMeteoritoB,2,listaMeteoritos)
                        contadorMov = 0
                        nivel = 1
                        timer = 0
                        timerViejo = 0
                        velocidadMeteoritos = 2
                        movimiento = QUIETO
                        for sprite in listaSpritesMono:
                            sprite.rect.left = ANCHO//2
                        estadoJuego = MENU

        elif estadoJuego == GANAR:
            ventana.fill(BLANCO)
            letrero = fuenteGrande.render("HAS GANADO", 0, NEGRO)
            retry = fuente.render("¿Jugar de nuevo?", 0, NEGRO)
            ventana.blit(letrero, (190,ALTO//2-150))
            ventana.blit(retry, (210, ALTO//2-40))
            ventana.blit(imgBotSi, (270, ALTO//2+40))
            ventana.blit(imgBotNo, (450, ALTO//2+40))

            guardarPuntaje(timer, "puntaje.txt")

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    termina = True
                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    xMouse, yMouse = pygame.mouse.get_pos()
                    xBotonSi = 270
                    yBotonSi = ALTO//2+40
                    xBotonNo = 450
                    yBotonNo = ALTO // 2+40
                    anchoBoton = 80
                    altoBoton = 50
                    if xMouse >= xBotonSi and xMouse <= xBotonSi + anchoBoton and yMouse >= yBotonSi and yMouse <= yBotonSi + altoBoton:
                        listaMeteoritos.clear()
                        crearMeteoritos(imgMeteoritoA,imgMeteoritoB,2,listaMeteoritos)
                        contadorMov = 0
                        nivel = 1
                        timer = 0
                        timerViejo = 0
                        velocidadMeteoritos = 2
                        movimiento = QUIETO
                        estadoJuego = JUGANDO
                        for sprite in listaSpritesMono:
                            sprite.rect.left = ANCHO//2
                    if xMouse >= xBotonNo and xMouse <= xBotonNo + anchoBoton and yMouse >= yBotonNo and yMouse <= yBotonNo + altoBoton:
                        listaMeteoritos.clear()
                        crearMeteoritos(imgMeteoritoA,imgMeteoritoB,2,listaMeteoritos)
                        contadorMov = 0
                        nivel = 1
                        timer = 0
                        timerViejo = 0
                        velocidadMeteoritos = 2
                        movimiento = QUIETO
                        for sprite in listaSpritesMono:
                            sprite.rect.left = ANCHO//2
                        estadoJuego = MENU

        elif estadoJuego == JUGANDO:
            #Actualización de estado del juego
            #Dificultad
            if timer > timerViejo+10 and timer <= timerViejo + 10.03:
                velocidadMeteoritos += 1
                nivel += 1
                timerViejo = timer

            #Fin del Juego
            if nivel == 10:
                estadoJuego = GANAR

            #Meteoritos
            actualizarMeteoritos(ventana, listaMeteoritos, velocidadMeteoritos)
            # AREGLAR LINEA DE SPAWN DE NUEVOS METEORITOS
            if listaMeteoritos[0].rect.bottom > nuevoSpawn:
                crearMeteoritos(imgMeteoritoA, imgMeteoritoB, cantidadMeteoritos, listaMeteoritos)
                impacto.play()

            #Colisiones
            if verificarColisionMeteorito(listaMeteoritos, spriteMono) == True:
                 efecto.play()

            #Limitacion de movimiento a los bordes
            if spriteMono.rect.left < 5 and spriteMonoDer1.rect.left < 5 and spriteMonoDer2.rect.left < 5\
                    and spriteMonoIzq1.rect.left < 5 and spriteMonoIzq2.rect.left < 5:
                for sprite in listaSpritesMono:
                    sprite.rect.left = 5
            elif spriteMono.rect.left > ANCHO - 80\
                    and spriteMonoIzq1.rect.left > ANCHO - 80 and spriteMonoDer1.rect.left > ANCHO - 80\
                    and spriteMonoIzq2.rect.left > ANCHO - 80and spriteMonoDer2.rect.left > ANCHO - 80:
                for sprite in listaSpritesMono:
                    sprite.rect.left = ANCHO -80

            # Movimiento de personaje
            if movimiento == IZQUIERDA:
                spriteMono.rect.left -= velocidadMono
                spriteMonoIzq1.rect.left -= velocidadMono
                spriteMonoDer1.rect.left -= velocidadMono
                spriteMonoIzq2.rect.left -= velocidadMono
                spriteMonoDer2.rect.left -= velocidadMono
            elif movimiento == DERECHA:
                spriteMono.rect.left += velocidadMono
                spriteMonoIzq1.rect.left += velocidadMono
                spriteMonoDer1.rect.left += velocidadMono
                spriteMonoIzq2.rect.left += velocidadMono
                spriteMonoDer2.rect.left += velocidadMono

            ventana.fill(NEGRO)
            #Cosas a dibujar
            #PERSONAJE
            if contadorMov > 10:
                contadorMov = 0
            if movimiento == QUIETO:
                dibujarPersonaje(ventana, spriteMono)
            elif movimiento == DERECHA and contadorMov <= 5:
                dibujarPersonaje(ventana, spriteMonoDer1)
                contadorMov += 1
            elif movimiento == DERECHA and contadorMov > 5 and contadorMov <= 10:
                dibujarPersonaje(ventana, spriteMonoDer2)
                contadorMov += 1
            elif movimiento == IZQUIERDA and contadorMov <= 5:
                dibujarPersonaje(ventana, spriteMonoIzq1)
                contadorMov += 1
            elif movimiento == IZQUIERDA and contadorMov > 5 and contadorMov <= 10:
                dibujarPersonaje(ventana, spriteMonoIzq2)
                contadorMov += 1

            #Dibujar METEORITOS
            dibujarMeteorito(ventana, listaMeteoritos)

            # Dibujar texto
            cronometro = fuente.render("Tiempo Jugado: %.2f" % timer, 1, ROJO)
            textoNivel = fuente.render("Nivel: %d" %nivel, 1, BLANCO)
            ventana.blit(cronometro, (50, 50))
            ventana.blit(textoNivel, (50, 550))

            timer += 1/40

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()
#Definir movimiento del personaje

def main():
    dibujar()


main()
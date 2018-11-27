# Autor: Saúl Figueroa Conde.
# Matrícula: A01747306.
# Grupo 02
# Descripción: Este es mi juego "Le petit lapin" (El conejito, en francés). Este es el resultado final de toda la
# planeación que se indicó en el documento de la propuesta inicial. Ya que, durante este semestre, he estado aprendiendo
# el lenguaje de la programación y francés por otro lado, decidí juntar ambos y ponerle un título en francés a mi
# juego :)  ~Fue realmente divertido para mí hacer este juego e incluso estoy considerando hacer una novela visual (otro
# genero de juego) en el futuro. En cualquier caso, espero que cualquiera que pruebe este pequeño juego, lo disfrute
# tanto como yo disfruté el programarlo.
#----------------------------------------------------------------------------------------------------------------------


import pygame  # Librería de pygame
from random import randint # para generar valorea aleatorios.

# Dimensiones de la pantalla (800 x 600).
ANCHO = 800
ALTO = 600

# Colores Globales. Usualmente, procuro no declarar variables a nivel global; sin embargo, no vi ningún problema con
# hacer referencia a únicamente tres colores.
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad. Puro blanco.
VERDE_BANDERA = (27, 94, 32)  # un poco de rojo, más de verde y un poco de azul.
ROJO = (255, 0, 0)  # únicamente rojo.


# Se declara la función escribirPuntaje, que recibe como parámetros el puntaje de la partida actual y el nombre del
# archivo donde se almacena el puntaje más alto. Solo se sobre-escribe el archivo original si el puntaje de la partida
# actual es mayor al anterior.
def escribirPuntaje(score, archivo):
    fileW = open(archivo, "w") # Se abre el archivo. Se especifica que se va a escribir (modo).

    record = str(score)  # Se convierte el puntaje a string (cadena de texto).
    fileW.write(record) # Se sobre-escribe el archivo con el nuevo record.
    fileW.close()  # Se cierra el archivo, ya que por el momento no habrá otras modificaciones.


# Se declara la función leerPuntaje, que recibe como parámetro el nombre del archivo donde se almacenan los puntajes. La
# lee el último mayor puntaje registrado y lo regresa.
def leerPuntaje(archivo):
    fileO = open(archivo, "r") # 'r' de read-mode.

    for line in fileO:
        puntaje = int(line)
    fileO.close()

    return puntaje


# Se declara la función colisionesZanahorias que verifica si el conejito atrapo a alguna zanahoria. Recibe como
# parámetros el sprite del conejito y la lista de zanahorias, para regresar si hubo o no alguna colisión entre el conejo
# y alguno de los elementos de la lista (zanahorias). Regresa 'True' o 'False'.
def colisionesZanahorias(spriteConejo, listaZanahorias):
    huboZanahoria = False

    for i in range(len(listaZanahorias) - 1, -1, -1):
        zanahoria = listaZanahorias[i]

        xb = spriteConejo.rect.left + 30
        yb = spriteConejo.rect.bottom - 38
        xe, ye, anchoe, altoe = zanahoria.rect

        if xb + 13 >= xe and xb - 13 <= xe + anchoe and yb >= ye and yb <= ye + altoe:
            listaZanahorias.remove(zanahoria)  # Adiós puerquito ;_;
            huboZanahoria = True
            return huboZanahoria


# Se declara la función colisionesPuercos, que recibe como parámetros el sprite del conejito y la lista de puercos
# alados. Esta función es muy parecida a la función anterior y regresa, al final, si el conejito fue golpeado por algún
# puerco o no.
def colisionesPuercos(spriteConejo, listaPuercos):
    huboChoque = False

    for j in range(len(listaPuercos)-1, -1, -1):
        puerco = listaPuercos[j]

        xb = spriteConejo.rect.left + 30
        yb = spriteConejo.rect.bottom - 38
        xe, ye, anchoe, altoe = puerco.rect

        if xb + 13 >= xe and xb - 13  <= xe + anchoe and yb >= ye and yb <= ye + altoe:
            listaPuercos.remove(puerco)  # ~Adiós puerquito~ ;_;
            huboChoque = True
            return huboChoque


# Se declara la función dibujarFondo, que recibe como parámetros la superficie(ventana) y el spriteFondo (así decidí
# llamar a mi background image). Esta función se encarga de dibujar los fondos de pantalla para distintas funciones.
def dibujarFondo(ventana, spriteFondo):
    ventana.blit(spriteFondo.image, spriteFondo.rect)


# Se declara la función dibujarButton, que recibe como parámetros la superficie (ventana) y el spriteButton (imagen del
# botón). La función se encarga de dibujar los botones en pantalla.
def dibujarButton(ventana, spriteButton):
    ventana.blit(spriteButton.image, spriteButton.rect)


# Se declara la función dibujarLabel, que recibe como parámetros la superficie (ventana) y el spriteLabel.
# La función se encarga de dibujar los letreros (imagenes) en pantalla.
def dibujarLabel(ventana, spriteLabel):
    ventana.blit(spriteLabel.image, spriteLabel.rect)


# Se declara la función dibujarzanahorias. Similar a las otras funciones 'dibujar'. Esta función se encarga de dibujar
# las zanahorias.
def dibujarZanahorias(ventana, listaZanahorias):
    for zanahoria in listaZanahorias:
        ventana.blit(zanahoria.image, zanahoria.rect)


# Se declara la función dibujarPuercos, que dibuja los puercos :)
def dibujarPuercos(ventana, listaPuercos):
    for puerco in listaPuercos:
        ventana.blit(puerco.image, puerco.rect)


# Se declara la función dibujarConejo, que dibuja al personaje principal.
def dibujarConejo(ventana, spriteConejo):
    ventana.blit(spriteConejo.image, spriteConejo.rect)


# Se declara la función animarZanahorias que recibe como parámetro la lista de zanahorias y
# actualiza los trazos de las zanahorias.
def animarZanahorias(listaZanahorias):
    for zanahoria in listaZanahorias:
        zanahoria.rect.bottom += 3

        if zanahoria.rect.bottom >= 800:
            listaZanahorias.remove(zanahoria)


# Se declara la función animarPuercos que recibe como parámetro la lista de puercos, el cuadro de animación de puercos y
# actualiza los trazos de los puercos.
def animarPuercos(listaPuercos, cuadroPuercos):
    for puerco in listaPuercos:
        puerco.rect.bottom += 5
        puerco.image = pygame.image.load("pig{}.gif".format(cuadroPuercos))

        if puerco.rect.bottom >= 800:
            listaPuercos.remove(puerco)


# Se declara la función animarConejoIzquierda que recibe como parámetro el sprite del conejito, el cuadro de animación
# del conejito y actualiza los trazos del conejito.
def animarConejoIzquierda(spriteConejo, cuadroSpriteConejo):
    spriteConejo.image = pygame.image.load("leftbunny{}.gif".format(cuadroSpriteConejo))


# Se declara la función animarConejoDerecha que se encarga de hacer lo mismo que la función anterior, pero para cuando
# se mueve el conejo a la derecha.
def animarConejoDerecha(spriteConejo, cuadroSpriteConejo):
    spriteConejo.image = pygame.image.load("rightbunny{}.gif".format(cuadroSpriteConejo))


# se declara la función gameOver, que muestra la pantalla de 'muerte' cuando el jugador ha perdido.
def gameOver():

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, se inicia asumiendo que no.

    # Reproducir música de fondo
    pygame.mixer.music.load("gameOver.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    # Color de fondo azul.
    ventana.fill(ROJO)

    # imagenes de botones

    imgButton = pygame.image.load("button_regresar.png")
    spriteButton = pygame.sprite.Sprite()
    spriteButton.image = imgButton
    spriteButton.rect = imgButton.get_rect()
    spriteButton.rect.left = ANCHO // 2 - 90
    spriteButton.rect.bottom = ALTO - 60

    imgLabelOver = pygame.image.load("fin.gif")
    spriteOver = pygame.sprite.Sprite()
    spriteOver.image = imgLabelOver
    spriteOver.rect = imgLabelOver.get_rect()
    spriteOver.rect.left = ANCHO // 2 - 390
    spriteOver.rect.bottom = ALTO // 2 + 188

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente.
        # Procesa los eventos que recibe.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en el botón de salir.
                termina = True  # Para terminar el ciclo.

            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Cuando se presiona una tecla.
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO // 2 - 90
                yb = ALTO - 110

                anchoB = 200
                altoB = 50

                # Cuando se da click en un botón:
                if xm >= xb and xm <= xb + anchoB and ym >= yb and ym <= yb + altoB:
                    pygame.mixer.music.stop()
                    main()

        dibujarButton(ventana, spriteButton)
        dibujarLabel(ventana, spriteOver)

        pygame.display.flip()  # Actualiza trazos.
        reloj.tick(50)  # 50 fps.

    # Después del ciclo principal:
    pygame.quit()  # termina pygame.


# Se declara la función ending que se encarga de mostrar la pantalla de 'fin' cuando el jugador ha acabado el juego.
def ending():

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará.
    reloj = pygame.time.Clock()  # Para limitar los fps.
    termina = False  # Bandera para saber si termina la ejecución.

    # Reproducir música de fondo
    pygame.mixer.music.load("ending.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    # Color de fondo azul.
    ventana.fill(BLANCO)

    # imagenes de botones
    imgButton = pygame.image.load("button_regresar.png")
    spriteButton = pygame.sprite.Sprite()
    spriteButton.image = imgButton
    spriteButton.rect = imgButton.get_rect()
    spriteButton.rect.left = ANCHO // 2 - 90
    spriteButton.rect.bottom = ALTO - 60

    imgLabelEnding = pygame.image.load("ending.gif")
    spriteEnding = pygame.sprite.Sprite()
    spriteEnding.image =  imgLabelEnding
    spriteEnding.rect =  imgLabelEnding.get_rect()
    spriteEnding.rect.left = ANCHO // 2 - 228
    spriteEnding.rect.bottom = ALTO // 2 + 188

    while not termina:  # Ciclo principal.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en el botón de salir.
                termina = True  # Para terminar el ciclo.

            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Cuando se presiona una tecla.
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO // 2 - 90
                yb = ALTO - 110

                anchoB = 200
                altoB = 50

                # Cuando se da click en un botón:
                if xm >= xb and xm <= xb + anchoB and ym >= yb and ym <= yb + altoB:
                    pygame.mixer.music.stop()
                    main()

        dibujarButton(ventana, spriteButton)
        dibujarLabel(ventana, spriteEnding)

        pygame.display.flip()  # Actualiza trazos.
        reloj.tick(50)  # 50 fps.

    # Después del ciclo principal:
    pygame.quit()  # termina pygame.


# Se declara la función creditos que muestra los creditos, vaya la redundancia.
def creditos():
     # Para el color de fondo.
    NEGRO = (0, 0, 0)

    # Crea una ventana de ANCHO x ALTO.
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde se dibujará.
    reloj = pygame.time.Clock()  # Para limitar los fps.
    termina = False  # Bandera para saber si termina la ejecución.

    # Reproducir música de fondo:
    pygame.mixer.music.load("credits.wav")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    # Color de fondo negro.
    ventana.fill(NEGRO)

    # imagenes de botones.

    imgButton = pygame.image.load("button_regresar.png")
    spriteButton = pygame.sprite.Sprite()
    spriteButton.image = imgButton
    spriteButton.rect = imgButton.get_rect()
    spriteButton.rect.left = ANCHO // 2 - 90
    spriteButton.rect.bottom = ALTO - 60

    imgLabelCreditos = pygame.image.load("creditsLabel.gif")
    spriteCreditos = pygame.sprite.Sprite()
    spriteCreditos.image = imgLabelCreditos
    spriteCreditos.rect = imgLabelCreditos.get_rect()
    spriteCreditos.rect.left = ANCHO // 2 - 220
    spriteCreditos.rect.bottom = ALTO // 2 + 180


    while not termina:  # Ciclo principal.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en el botón de salir.
                termina = True  # Para terminar el ciclo.

            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Cuando se presiona una tecla.
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO // 2 - 90
                yb = ALTO - 110

                anchoB = 200
                altoB = 50

                # Cuando se da click en un botón:
                if xm >= xb and xm <= xb + anchoB and ym >= yb and ym <= yb + altoB:
                    main()

        dibujarButton(ventana, spriteButton)
        dibujarLabel(ventana, spriteCreditos)

        pygame.display.flip()  # Actualiza trazos.
        reloj.tick(50)  # 50 fps.

    # Después del ciclo principal:
    pygame.quit()  # termina pygame.


# Se declara la función main donde el usuario podrá ver una menu del juego y elegir la opción que prefiera.
def main():

    # Para reproducir sonido en python:
    pygame.mixer.pre_init(44100, 16, 2, 4096)

    # Inicializar el motor de pygame...
    pygame.init()

    # Se declaran las vidas del jugador.
    lives = 3

    #Se declaran las variables corrspondientes al valor del puntaje.
    archivo = "Score.txt"
    highScore = leerPuntaje(archivo)

    if highScore == 0:
        highScore = "0000"

    score = 0

    # Se crea una ventana de ANCHO x ALTO.
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Se crea la ventana donde se dibujará.
    reloj = pygame.time.Clock()  # Para limitar los fps.
    termina = False  # Bandera para saber si termina la ejecución del programa.

    # Reproducir música de fondo:
    pygame.mixer.music.load("menu.mp3")
    pygame.mixer.music.set_volume(0.8)
    pygame.mixer.music.play(-1)

    # Imagen de fondo:
    imgFondo = pygame.image.load("mainmenu.jpg")
    spriteFondo = pygame.sprite.Sprite()
    spriteFondo.image = imgFondo
    spriteFondo.rect = imgFondo.get_rect()
    spriteFondo.rect.left = 0
    spriteFondo.rect.bottom = ALTO

    # imagenes de botones

    imgButton = pygame.image.load("button_jugar.png")
    spriteButton = pygame.sprite.Sprite()
    spriteButton.image = imgButton
    spriteButton.rect = imgButton.get_rect()
    spriteButton.rect.left = ANCHO // 2 - 90
    spriteButton.rect.bottom = ALTO // 2 + 60

    imgButton2 = pygame.image.load("button_creditos.png")
    spriteButton2 = pygame.sprite.Sprite()
    spriteButton2.image = imgButton2
    spriteButton2.rect = imgButton2.get_rect()
    spriteButton2.rect.left = ANCHO // 2 - 90
    spriteButton2.rect.bottom = ALTO // 2 + 120

    imgButton3 = pygame.image.load("button_salir.png")
    spriteButton3 = pygame.sprite.Sprite()
    spriteButton3.image = imgButton3
    spriteButton3.rect = imgButton3.get_rect()
    spriteButton3.rect.left = ANCHO // 2 - 90
    spriteButton3.rect.bottom = ALTO // 2 + 180

    imgLabel1 = pygame.image.load("title.gif")
    spriteLabel1 = pygame.sprite.Sprite()
    spriteLabel1.image = imgLabel1
    spriteLabel1.rect = imgLabel1.get_rect()
    spriteLabel1.rect.left = ANCHO // 2 - 285
    spriteLabel1.rect.bottom = ALTO // 2 - 10

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # Si el usuario hizo click en el botón de salir.
                termina = True  # Para terminar el ciclo.

            elif evento.type == pygame.MOUSEBUTTONDOWN:  # Cuando se presiona una tecla.
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO // 2 - 90
                yb = ALTO // 2 + 10

                xb2 = ANCHO // 2 - 90
                yb2 = ALTO // 2 + 70

                xb3 = ANCHO // 2 - 90
                yb3 = ALTO // 2 + 130

                anchoB = 200
                altoB = 50

                # Cuando se da click en un botón:
                if xm >= xb and xm <= xb + anchoB and ym >= yb and ym <= yb + altoB:
                    pygame.mixer.music.stop()
                    jugar(lives, score, archivo)

                elif xm >= xb2 and xm <= xb2 + anchoB and ym >= yb2 and ym <= yb2 + altoB:
                    pygame.mixer.music.stop()
                    creditos()

                elif xm >= xb3 and xm <= xb3 + anchoB and ym >= yb3 and ym <= yb3 + altoB:
                    pygame.mixer.music.stop()
                    pygame.quit()

        dibujarFondo(ventana, spriteFondo)
        dibujarButton(ventana, spriteButton)
        dibujarButton(ventana, spriteButton2)
        dibujarButton(ventana, spriteButton3)
        dibujarLabel(ventana, spriteLabel1)

        fontPuntaje = pygame.font.SysFont("helvetica", 30)
        fontPuntaje.set_bold(True)
        scoreTextMenu = fontPuntaje.render("Mayor puntaje: {}".format(highScore), True, [0, 0, 0])
        ventana.blit(scoreTextMenu, (ANCHO//2 - 130, ALTO - 80))

        spriteFondo.rect.left -= 1
        if spriteFondo.rect.left <= -1595:
            spriteFondo.rect.left = 0
        pygame.display.flip()  # Actualiza LOS trazos.
        reloj.tick(50)  # 50 fps.

    # Después del ciclo principal:
    pygame.quit()  # terminar pygame.


# Se declara la función jugar, que recibe como parámetros las vidas del jugadro, el puntaje actual (0) y el nombre del
# archivo donde se almacena el mayor puntaje. Aquí es donde se ejecuta el juego principal.
def jugar(lives, score, archivo):

    # Para checar si se está presionando alguna tecla.
    leftIsPressed = False
    rightIsPressed = False

    # Para checar si hubo una colision.
    huboChoque = False
    huboZanahoria = False

    # Para acabar el juego.
    timeOut = 0

    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Reproducir música de fondo.
    musica = pygame.mixer.Sound("main.wav")
    musica.set_volume(0.5)
    pygame.mixer.Channel(0).play(musica, loops = -1)

    # Imagen de fondo.
    imgFondo = pygame.image.load("mainbackground.jpg")
    spriteFondo = pygame.sprite.Sprite()
    spriteFondo.image = imgFondo
    spriteFondo.rect = imgFondo.get_rect()
    spriteFondo.rect.left = 0
    spriteFondo.rect.bottom = ALTO

    # personaje principal (conejo):

    imgConejo = pygame.image.load("leftbunny1.gif")
    spriteConejo = pygame.sprite.Sprite()
    spriteConejo.image = imgConejo
    spriteConejo.rect = imgConejo.get_rect()
    spriteConejo.rect.left = ANCHO // 2
    spriteConejo.rect.bottom = ALTO

    # enemigos (puercos alados):
    listaPuercos = []
    imgPuerco = pygame.image.load("pig1.gif")

    # items para ganar puntos (zanahorias):
    listaZanahorias = []
    imgZanahoria = pygame.image.load("carrot.gif")

    cuadroSpriteConejo = 1  # Para mostrar la primera image de spriteConejo.
    animationSpeed = 3  # Para manejar la velocidad de la animación.
    generarPuerco = 50 # Para controlar la velocidad a la que se generan puercos alados.
    generarZanahoria = 30  # Para controlar la velocidad a la que se generan zanahorias.
    cuadroPuercos = 0

    while not termina:  # Ciclo principal.
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True  # Queremos terminar el ciclo.

            elif evento.type == pygame.KEYDOWN:  # Cuando se presiona una tecla.

                if evento.key == pygame.K_LEFT:  # Cuando se presiona la tecla especificada.
                    leftIsPressed = True

                elif evento.key == pygame.K_RIGHT:
                    rightIsPressed = True

            elif evento.type == pygame.KEYUP:  # Cuando se suelta la tecla especificada.

                if evento.key == pygame.K_LEFT:
                    leftIsPressed = False
                    spriteConejo.image = pygame.image.load("leftbunny1.gif")

                elif evento.key == pygame.K_RIGHT:
                    rightIsPressed = False
                    spriteConejo.image = pygame.image.load("rightbunny1.gif")

        # Generar puercos.
        if generarPuerco == 50:
            spritePuerco = pygame.sprite.Sprite()
            spritePuerco.image = imgPuerco
            spritePuerco.rect = imgPuerco.get_rect()
            spritePuerco.rect.left = randint(10, ANCHO - 120)
            spritePuerco.rect.bottom = randint(-1000, -100)
            listaPuercos.append(spritePuerco)
            generarPuerco = 0

        if generarZanahoria == 30:
            spriteZanahoria = pygame.sprite.Sprite()
            spriteZanahoria.image = imgZanahoria
            spriteZanahoria.rect = imgZanahoria.get_rect()
            spriteZanahoria.rect.left = randint(20, ANCHO - 150)
            spriteZanahoria.rect.bottom = randint(-1000, -100)
            listaZanahorias.append( spriteZanahoria)
            generarZanahoria = 0

        generarPuerco += 1
        generarZanahoria += 1

        if leftIsPressed:

            if cuadroSpriteConejo == 1:
                musica = pygame.mixer.Sound("jump.wav")
                musica.set_volume(0.2)
                pygame.mixer.Channel(1).play(musica)

            if cuadroSpriteConejo == 8:
                cuadroSpriteConejo = 1

            if animationSpeed == 3:
                cuadroSpriteConejo += 1  # Cambia a la siguiente imagen del sprite.
                animarConejoIzquierda(spriteConejo, cuadroSpriteConejo)
                animationSpeed = 0

            else:
                animationSpeed += 1

            if spriteConejo.rect.left > 0:
                spriteConejo.rect.left -= 6

        elif rightIsPressed:

            if cuadroSpriteConejo == 1:
                musica = pygame.mixer.Sound("jump.wav")
                musica.set_volume(0.2)
                pygame.mixer.Channel(1).play(musica)

            if cuadroSpriteConejo == 8:
                cuadroSpriteConejo = 1

            if animationSpeed == 3:
                cuadroSpriteConejo += 1  # Cambia a la siguiente imagen del sprite.
                animarConejoDerecha(spriteConejo, cuadroSpriteConejo)
                animationSpeed = 0

            else:
                animationSpeed += 1

            if spriteConejo.rect.left < 725:
                spriteConejo.rect.left += 6

        cuadroPuercos += 1

        if cuadroPuercos == 4:
            cuadroPuercos = 1

        animarPuercos(listaPuercos, cuadroPuercos)
        animarZanahorias(listaZanahorias)
        huboChoque = colisionesPuercos(spriteConejo, listaPuercos)
        huboZanahoria = colisionesZanahorias(spriteConejo, listaZanahorias)

        if huboChoque:
            colision = pygame.mixer.Sound("damage.wav")
            colision.set_volume(0.8)
            pygame.mixer.Channel(2).play(colision)
            lives -= 1
            huboChoque == False
            if lives <= 0:
                pygame.mixer.stop()
                gameOver()

        if huboZanahoria:
            comer = pygame.mixer.Sound("carrot.wav")
            comer.set_volume(0.8)
            pygame.mixer.Channel(2).play(comer)
            score += 250
            huboZanahoria == False


        dibujarFondo(ventana, spriteFondo)
        dibujarConejo(ventana, spriteConejo)
        dibujarPuercos(ventana, listaPuercos)
        dibujarZanahorias(ventana, listaZanahorias)

#----------------------------------------------------------------------------------------------------------------------
        # Muestra la vidas del jugador.
        font = pygame.font.SysFont("helvetica", 30)
        font.set_bold(True)
        livesText = font.render("Vidas: {}".format(lives), True, [255, 0, 0])
        ventana.blit(livesText, (20, 20))

        # Muestra el puntaje del jugador.

        font2 = pygame.font.SysFont("helvetica", 30)
        font2.set_bold(True)
        scoreText = font2.render("Puntaje: {}".format(score), True, [255, 0, 0])
        ventana.blit(scoreText, (20, 60))

        if timeOut == 5500:
            pygame.mixer.stop()
            puntajeMayor = leerPuntaje(archivo)
            if score > puntajeMayor:
                escribirPuntaje(score, archivo)

            ending()

        else:
            timeOut += 1
#----------------------------------------------------------------------------------------------------------------------
        pygame.display.flip()  # Actualiza los trazos.
        reloj.tick(50)  # 50 fps.

    # Después del ciclo principal.
    pygame.quit()  # termina pygame. Bye-bye.


# Se llama a la función main para que empiece a correr el programa.
main()
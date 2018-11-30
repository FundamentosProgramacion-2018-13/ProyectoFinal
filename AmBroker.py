#encoding: UTF-8
#Autor: Arturo Márquez Olivar. A01376086.
#Ejecuta un pequeño video juego creado por el autor del código.


import pygame
from random import randint


#Dimensiones de la pantalla.
ANCHO = 800
ALTO = 600


#Colores.
BLANCO = (255, 255, 255)  #R, G , B.
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (159, 227, 247)
NEGRO = (0, 0, 0)


#Estados:
MENU = 1
PLAY = 2
GAMEOVER = 3
SCORES = 4
PAUSE = 5
RULES = 6


#Estados de movimiento:
CAYENDO = 1
DERECHA = 2
IZQUIERDA = 3


#Dibuja el fondo del menú quieto.
def dibujarFondoMenu(ventana, imgMenu):
    ventana.blit(imgMenu, (0, 0))


#Dibuja el fondo del juego corriendo.
def dibujarFondo(ventana, imgFondo):
    ventana.blit(imgFondo, (0,0))


#Dibuja al cohete.
def dibujarCohete(ventana, spriteCohete):
    ventana.blit(spriteCohete.image, spriteCohete.rect)


#Dibuja la línea que va a ser obstaculo en medio de la pantalla.
def dibujarLinea(ventana, yLineas, alturas):
    for k in range(len(yLineas)):
        pygame.draw.rect(ventana, NEGRO, (400, yLineas[k], 12, alturas[k]))


#Actualiza las líneas agregandolas a las listas y borra las que ya hayan salido de la pantalla.
def actualizarLineas(yLineas, alturaLineas):
    for k in range(len(yLineas)):
        caida = 7
        yLineas[k] += caida
        if yLineas[k] >= 600 + 150:
            largo = randint(50, 140)
            yLineas.append(yLineas[-1] - 120 - largo)
            alturaLineas.append(largo)
            if yLineas[k] >= 700:
                del (yLineas[k])
                del (alturaLineas[k])


#Revisa si hubo impacto entre el cohete y las líneas obstaculo.
def verificarColisiones(yLineas, alturaLineas, xCohete, yCohete):
    for pX in range(20, 51): #Compara cada punto donde está el cohete en la imágen con los puntos de la línea
        for pY in range(15, 65, 5):
            for k in range(len(yLineas)):
                xLinea, yLinea, anchoLinea, altoLinea = (400, yLineas[k], 12, alturaLineas[k])
                if xCohete + pX >= xLinea and xCohete + pX <= xLinea + anchoLinea and yCohete - pY >= yLinea and yCohete - pY <= yLinea + altoLinea:
                    estado = "GAMEOVER"
                    return estado


#Dibuja una línea que el cohete al cruzar por ahí va sumar puntos.
def dibujarLineaScore(ventana):
    pygame.draw.rect(ventana, AZUL, (400, 0, 12, 600))


#Verifica si el cohete pasó por las coorednadas de la línea Score para sumar puntos.
score = 0
def verificarScores(xCohete, yCohete):
    global score
    for pX in range(20, 51): #Compara cada punto donde está el cohete en la imágen con los puntos de la línea
        for pY in range(10, 65, 5):
            if xCohete + pX >= 400 and xCohete + pX <= 400 + 12 and yCohete - pY >= 0 and yCohete - pY <= 0 + 600:
                score += 5
                return score


#Dibuja un rectángulo decoratorio que enmarca al score.
def dibujarRectScore(ventana):
    pygame.draw.rect(ventana, BLANCO, (15, 15, 100, 45), 1)


#Regresa el juego al inicio si le indicaron reiniciarlo.
listaScores = [] #Lista donde se van a guardar todos los scores del juego.
def reset(spriteCohete):
    spriteCohete.rect.left = 175
    spriteCohete.rect.bottom = ALTO - ALTO//4 + spriteCohete.rect.height//2
    movimiento = "CAYENDO"
    global score, listaScores
    scoreTotal = score-5
    listaScores.append(scoreTotal) #Aquí guarda el record obtenido en cada juego antes de reiniciarlo
    score = 0
    return movimiento


#Escribe en un archivo los puntajes y los puede ir actualizando para poder mandarlos a leer.
def ordenarScores():
    salida = open("puntajes.txt", "w", encoding = "UTF-8")
    listaScores.sort()
    if len(listaScores) == 1:
        salida.write("Top 1 : %.4d\nTop 2 : 0000\nTop 3 : 0000\nTop 4 : 0000\nTop 5 : 0000" % int(listaScores[-1]))
    elif len(listaScores) == 2:
        salida.write("Top 1 : %.4d\nTop 2 : %.4d\nTop 3 : 0000\nTop 4 : 0000\nTop 5 : 0000" % (int(listaScores[-1]), int(listaScores[-2])))
    elif len(listaScores) == 3:
        salida.write("Top 1 : %.4d\nTop 2 : %.4d\nTop 3 : %.4d\nTop 4 : 0000\nTop 5 : 0000" % (
            int(listaScores[-1]), int(listaScores[-2]), int(listaScores[-3])))
    elif len(listaScores) == 4:
        salida.write("Top 1 : %.4d\nTop 2 : %.4d\nTop 3 : %.4d\nTop 4 : %.4d\nTop 5 : 0000" % (
            int(listaScores[-1]), int(listaScores[-2]), int(listaScores[-3]), int(listaScores[-4])))
    elif len(listaScores) >= 5:
        salida.write("Top 1 : %.4d\nTop 2 : %.4d\nTop 3 : %.4d\nTop 4 : %.4d\nTop 5 : %.4d" % (
            int(listaScores[-1]), int(listaScores[-2]), int(listaScores[-3]), int(listaScores[-4]), int(listaScores[-5])))
    else:
        salida.write("Top 1 : 0000\nTop 2 : 0000\nTop 3 : 0000\nTop 4 : 0000\nTop 5 : 0000")
    salida.close()


#Lee el archivo de texto previamente creado para separarlo por líneas y así poder mandarlo a imprimir en la pantalla.
def leerScores():
    entrada = open("puntajes.txt", "r", encoding = "UTF-8")
    puntaje = []
    for linea in entrada:
        texto = linea.split("\n")
        puntaje.append(texto)
    entrada.close()
    return puntaje


#Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  #Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Cohete.
    imgCohete = pygame.image.load("cohete.png")
    spriteCohete = pygame.sprite.Sprite()
    spriteCohete.image = imgCohete
    spriteCohete.rect = imgCohete.get_rect()
    spriteCohete.rect.left = 175
    spriteCohete.rect.bottom = ALTO - ALTO//4 + spriteCohete.rect.height//2
    movimiento = CAYENDO

    #Líneas:
    yLineas = [0, -150, -300, -450, -600]
    alturaLineas = [30, 30, 30, 30, 60]

    #Imágenes del fondo en el juego y su botón.
    imgFondo = pygame.image.load("fondoJuego.jpg")
    imgFondoMovible = pygame.image.load("fondoMovible.png")
    yFondo = 0
    btnPause = pygame.image.load("pause.png")

    #Imágen del fondo del menú y sus botónes.
    imgMenu = pygame.image.load("fondoMenu.png")
    imgMenuMovible = pygame.image.load("fondoMovibleMenu.png")
    yFondo2 = 0
    btnPlay = pygame.image.load("play.png")
    btnScores = pygame.image.load("scores.png")
    btnRules = pygame.image.load("rules.png")

    #Imágen del fondo Pause y sus botónes.
    imgPause = pygame.image.load("fondoPause.png")
    btnContinue = pygame.image.load("continue.png")
    btnExit = pygame.image.load("exit.png")
    btnMenu = pygame.image.load("menu.png")

    #Imágen del fondo GAME OVER.
    imgGameOver = pygame.image.load("fondoGameOver.png")
    btnAgain = pygame.image.load("again.png")
    #Tambíen usará el botón Menú.

    #Imágen del fondo de Scores.
    imgScores = pygame.image.load("fondoScores.png")
    imgScoresTapa = pygame.image.load("fondoScoresTapa.png")
    btnBack = pygame.image.load("back.png")

    #Imágen del fondo Rules.
    imgRules = pygame.image.load("fondoLearn.png")
    btnArrow = pygame.image.load("arrow.png")

    #Estado inicial:
    estado = MENU

    #Audio:
    pygame.mixer.init()
    vuelta = pygame.mixer.Sound("vuelta.wav")
    boton = pygame.mixer.Sound("boton.wav")
    choque = pygame.mixer.Sound("lost.wav")
    pygame.mixer.music.load("musicaFondo.wav")
    pygame.mixer.music.play(-1)

    #Texto:
    fuente = pygame.font.SysFont("monospace", 40)

    #Score.
    global score


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if estado == PLAY:
                    if evento.key == pygame.K_RIGHT:
                        if movimiento == CAYENDO or spriteCohete.rect.left <= 330:
                            vuelta.play()
                            movimiento = DERECHA
                    elif evento.key == pygame.K_LEFT:
                        if movimiento == CAYENDO or spriteCohete.rect.left >= 470:
                            vuelta.play()
                            movimiento = IZQUIERDA
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                if estado == MENU:
                    #Botón Play:
                    xPlay = ANCHO // 2 - 55
                    yPlay = ALTO // 2 - 22
                    anchoPlay = 105
                    altoPlay = 45
                    #Botón High Scores:
                    xScores = ANCHO // 2 - 78
                    yScores = ALTO // 2 + 47
                    anchoScores = 150
                    altoScores = 45
                    #Botón Rules:
                    xRules = ANCHO // 2 - 55
                    yRules = ALTO // 2 + 115
                    anchoRules = 110
                    altoRules = 45
                    if xm >= xPlay and xm <= xPlay + anchoPlay and ym >= yPlay and ym <= yPlay + altoPlay:
                        boton.play()
                        reseteo = reset(spriteCohete)
                        if reseteo == "CAYENDO":
                            movimiento = CAYENDO
                            estado = PLAY
                    elif xm >= xScores and xm <= xScores + anchoScores and ym >= yScores and ym <= yScores + altoScores:
                        boton.play()
                        estado = SCORES
                    elif xm >= xRules and xm <= xRules + anchoRules and ym >= yRules and ym <= yRules + altoRules:
                        boton.play()
                        estado = RULES
                elif estado == SCORES:
                    #Botón Back:
                    xBack = ANCHO//7
                    yBack = 3*ALTO//4 + 20
                    anchoBack = 100
                    altoBack = 45
                    if xm >= xBack and xm <= xBack + anchoBack and ym >= yBack and ym <= yBack + altoBack:
                        boton.play()
                        estado = MENU
                elif estado == RULES:
                    #Botón Arrow:
                    xArrow = 25
                    yArrow = 535
                    anchoArrow = 40
                    altoArrow = 40
                    if xm >= xArrow and xm <= xArrow + anchoArrow and ym >= yArrow and ym <= yArrow + altoArrow:
                        boton.play()
                        estado = MENU
                elif estado == PLAY:
                    xPause = ANCHO - 60
                    yPause = ALTO // 2 - 20
                    anchoPause = 40
                    altoPause = 40
                    if xm >= xPause and xm <= xPause + anchoPause and ym >= yPause and ym <= yPause + altoPause:
                        boton.play()
                        estado = PAUSE
                elif estado == PAUSE:
                    #Botón Continue:
                    xContinue = ANCHO // 4
                    yContinue = ALTO // 2 - 22
                    anchoContinue = 150
                    altoContinue = 45
                    #Botón Main Menu:
                    xMenu = ANCHO // 4
                    yMenu = ALTO // 2 + 50
                    anchoMenu = 150
                    altoMenu = 45
                    #Botón Exit:
                    xExit = ANCHO // 4
                    yExit = ALTO // 2 + 120
                    anchoExit = 90
                    altoExit = 40
                    if xm >= xContinue and xm <= xContinue + anchoContinue and ym >= yContinue and ym <= yContinue + altoContinue:
                        boton.play()
                        estado = PLAY
                    elif xm >= xMenu and xm <= xMenu + anchoMenu and ym >= yMenu and ym <= yMenu + altoMenu:
                        boton.play()
                        reseteo = reset(spriteCohete)
                        if reseteo == "CAYENDO":
                            movimiento = CAYENDO
                            estado = MENU
                    elif xm >= xExit and xm <= xExit + anchoExit and ym >= yExit and ym <= yExit + altoExit:
                        boton.play()
                        exit()
                elif estado == GAMEOVER:
                    #Botón Try Again:
                    xAgain = ANCHO // 2 - 55
                    yAgain = ALTO // 2 - 22
                    anchoAgain = 135
                    altoAgain = 45
                    #Botón Main Menu:
                    xMenu2 = ANCHO // 2 - 62
                    yMenu2 = ALTO // 2 + 47
                    anchoMenu2 = 150
                    altoMenu2 = 45
                    if xm >= xAgain and xm <= xAgain + anchoAgain and ym >= yAgain and ym <= yAgain + altoAgain:
                        boton.play()
                        reseteo = reset(spriteCohete)
                        if reseteo == "CAYENDO":
                            movimiento = CAYENDO
                            estado = PLAY
                    elif xm >= xMenu2 and xm <= xMenu2 + anchoMenu2 and ym >= yMenu2 and ym <= yMenu2 + altoMenu2:
                        boton.play()
                        reseteo = reset(spriteCohete)
                        if reseteo == "CAYENDO":
                            movimiento = CAYENDO
                            estado = MENU


        #Muestra una pantalla dando opción a jugar o a ver los High Scores.
        if estado == MENU:
            dibujarFondoMenu(ventana, imgMenu)
            ventana.blit(imgMenuMovible, (0, yFondo2))
            ventana.blit(imgMenuMovible, (0, yFondo2 - 620))
            yFondo2 += 1
            if yFondo2 >= 620:
                yFondo2 = 0
            ventana.blit(btnPlay, (ANCHO // 2 - 55, ALTO // 2 - 22))
            ventana.blit(btnScores, (ANCHO // 2 - 78, ALTO// 2 + 47))
            ventana.blit(btnRules, (ANCHO // 2 - 55, ALTO // 2 + 115))


        #Cuando el estado está en Scores, muestra una nueva pantalla con las 5 puntuaciones más altas.
        elif estado == SCORES:
            ventana.blit(imgScores, (0,0))
            ventana.blit(btnBack, (ANCHO//7, 3*ALTO//4 + 20))
            ordenarScores()
            listaPuntajes = leerScores()
            puntaje1 = fuente.render(str(listaPuntajes[0]), 1, BLANCO)
            ventana.blit(puntaje1, (ANCHO // 3, ALTO // 3))
            puntaje2 = fuente.render(str(listaPuntajes[1]), 1, BLANCO)
            ventana.blit(puntaje2, (ANCHO // 3, ALTO // 3 + 45))
            puntaje3 = fuente.render(str(listaPuntajes[2]), 1, BLANCO)
            ventana.blit(puntaje3, (ANCHO // 3, ALTO // 3 + 90))
            puntaje4 = fuente.render(str(listaPuntajes[3]), 1, BLANCO)
            ventana.blit(puntaje4, (ANCHO // 3, ALTO // 3 + 135))
            puntaje5 = fuente.render(str(listaPuntajes[4]), 1, BLANCO)
            ventana.blit(puntaje5, (ANCHO // 3, ALTO // 3 + 180))
            ventana.blit(imgScoresTapa, (0,0))


        #Muestra una pantalla con una pequeña guía para jugar.
        elif estado == RULES:
            ventana.blit(imgRules, (0, 0))
            ventana.blit(btnArrow, (25, 535))


        #Corre el juego normal pudiendo llevar el puntaje en pantalla y opción de pausa.
        elif estado == PLAY:
            if spriteCohete.rect.bottom >= 630 or spriteCohete.rect.bottom <= 0:
                estado = GAMEOVER
            if movimiento == CAYENDO:
                spriteCohete.rect.bottom += 4
            elif movimiento == DERECHA:
                if spriteCohete.rect.left >= 550:
                    movimiento = CAYENDO
                else:
                    spriteCohete.rect.left += 60
                    spriteCohete.rect.bottom -= 17
            elif movimiento == IZQUIERDA:
                if spriteCohete.rect.left <= 175:
                    movimiento = CAYENDO
                else:
                    spriteCohete.rect.left -= 60
                    spriteCohete.rect.bottom -= 17

            actualizarLineas(yLineas, alturaLineas)
            verificacionColision = verificarColisiones(yLineas, alturaLineas, spriteCohete.rect.left, spriteCohete.rect.bottom)
            if verificacionColision == "GAMEOVER":
                choque.play()
                estado = GAMEOVER
            verificarScores(spriteCohete.rect.left, spriteCohete.rect.bottom)

            #Dibuja primero el fondo de la pantalla y encima coloca la imágen de las estrellas moviendose.
            dibujarFondo(ventana, imgFondo)
            ventana.blit(imgFondoMovible, (0, yFondo))
            ventana.blit(imgFondoMovible, (0, yFondo - 620))
            yFondo += 3
            if yFondo >= 620:
                yFondo = 0
            ventana.blit(btnPause, (ANCHO - 60, ALTO//2 -20))
            dibujarLineaScore(ventana)
            dibujarLinea(ventana, yLineas, alturaLineas)
            dibujarCohete(ventana, spriteCohete)
            dibujarRectScore(ventana)

            #Dibujar Texto:
            texto = fuente.render("%.4d" % (score), 1, BLANCO)
            ventana.blit(texto, (15, 15))


        #Detiene el juego mientras está en este estado y muestra opciones para Reanudar, Salir al menú o salir del juego.
        elif estado == PAUSE:
            ventana.blit(imgPause, (0,0))
            ventana.blit(btnContinue, (ANCHO // 4, ALTO // 2 - 22))
            ventana.blit(btnMenu, (ANCHO // 4, ALTO // 2 + 50))
            ventana.blit(btnExit, (ANCHO // 4, ALTO // 2 + 120 ))


        #Muestra una pantalla cuando perdiste dentro del juego y de ahí puedes iniciar el juego nuevamente o ir al menú principal.
        elif estado == GAMEOVER:
            ventana.blit(imgGameOver, (0, 0))
            ventana.blit(btnAgain, (ANCHO // 2 - 55, ALTO // 2 - 15))
            ventana.blit(btnMenu, (ANCHO // 2 - 62, ALTO // 2 + 47))


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


#Función principal, aquí resuelves el problema7
def main():
    dibujar()


#Llamas a la función principal
main()
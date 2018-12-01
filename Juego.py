# Encoding: UTF-8
# Autor: Oscar Alejandro Torres Maya, A01377686
# Descripción: Proyecto Final, videojuego

import pygame   #Importa librería de pygame
from random import randint  #Importa la función randint de la librería random

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

#Colores
AZUL = (96,111,140)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)
VERDE = (76,145,65)

#Estados de juego
MENU = 1
JUGANDO = 2
FINAL = 3
PUNTAJES = 4


#Dibuja al personaje en la pantalla
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


#Dibuja a los enemigos en la pantalla
def dibujarEnemigos(ventana, listaEnemigos, listaEnemigos2):
    for enemigo in listaEnemigos:     # VISITAR O ACCEDER A CADA ELEMENTO
        ventana.blit(enemigo.image, enemigo.rect)  # IMAGEN , LUGAR

    for enemigo2 in listaEnemigos2:   # VISITAR O ACCEDER A CADA ELEMENTO
        ventana.blit(enemigo2.image, enemigo2.rect) # IMAGEN , LUGAR


#Dibuja a los árboles en la pantalla
def dibujarObstaculo(ventana,spriteObstaculo):
    ventana.blit(spriteObstaculo.image, spriteObstaculo.rect) # IMAGEN , LUGAR


#Dibuja el bonus en la pantalla
def dibujarBonus(ventana,spriteBonus):
    ventana.blit(spriteBonus.image, spriteBonus.rect) # IMAGEN , LUGAR


#Mueve a los enemigos
def moverEnemigos(listaEnemigos,listaEnemigos2):
    for enemigo in listaEnemigos: #Mueve a todos los enemigos
        enemigo.rect.left -= 5 #Velocidad del cazador verde por pixel

    for enemigo2 in listaEnemigos2: #Mueve a todos los enemigos
        enemigo2.rect.left += 5 #Velocidad del cazador naranja por pixel


#Dibuja las opciones del menú
def dibujarMenu(ventana, imgBotonJugar, imgBotonSalir, imgHighscore):
    ventana.blit(imgBotonJugar, (ANCHO//2-110, ALTO//3-50))
    ventana.blit(imgBotonSalir, (ANCHO//2-110, ALTO//3+100))
    ventana.blit(imgHighscore, (ANCHO//2-110, ALTO - 160))


#Verifica si el conejo y cazador chocaron
def verificarColision(listaEnemigos, listaEnemigos2, spritePersonaje):
        for cazador in range(len(listaEnemigos)-1, -1, -1):
            enemigo = listaEnemigos[cazador]
            # Conejo vs cazador derecha
            xPersonaje, yPersonaje, anchoPersonaje, altPersonaje = spritePersonaje.rect
            xEnemigo, yEnemigo, anchoEnemigo, altEnemigo = enemigo.rect

            #PUNTO INFERIOR Y SUPERIOR IZQUIERDO
            if xPersonaje >= xEnemigo and xPersonaje <= xEnemigo+anchoEnemigo and yPersonaje+altPersonaje >= yEnemigo and yPersonaje <= yEnemigo+altEnemigo:
                listaEnemigos.remove(enemigo)  #Colisionaron
                return True

            #PUNTO INFERIOR Y SUPERIOR DERECHO
            elif xPersonaje+anchoPersonaje >= xEnemigo and xPersonaje <= xEnemigo+anchoEnemigo and yPersonaje+altPersonaje >= yEnemigo and yPersonaje <= yEnemigo+altEnemigo:
                listaEnemigos.remove(enemigo)  #Colisionaron
                return True

        for cazador2 in range(len(listaEnemigos2)-1, -1, -1):
            enemigo2 = listaEnemigos2[cazador2]
            # Conejo vs cazador izquierda
            xPersonaje, yPersonaje, anchoPersonaje, altPersonaje = spritePersonaje.rect
            xEnemigo2, yEnemigo2, anchoEnemigo2, altEnemigo2 = enemigo2.rect

            # PUNTO INFERIOR Y SUPERIOR IZQUIERDO
            if xPersonaje >= xEnemigo2 and xPersonaje <= xEnemigo2 + anchoEnemigo2 and yPersonaje + altPersonaje >= yEnemigo2 and yPersonaje <= yEnemigo2 + altEnemigo2:
                listaEnemigos2.remove(enemigo2)  #Colisionaron
                return True

            # PUNTO INFERIOR Y SUPERIOR DERECHO
            elif xPersonaje + anchoPersonaje >= xEnemigo2 and xPersonaje <= xEnemigo2 + anchoEnemigo2 and yPersonaje + altPersonaje >= yEnemigo2 and yPersonaje <= yEnemigo2 + altEnemigo2:
                listaEnemigos2.remove(enemigo2)  #Colisionaron
                return True


#Dibuja el menú cuando acaba el juego
def dibujarMenuFinal(ventana, imgBotonSalir, imgHome, imgIntento2, tiempo):
    ventana.blit(imgHome, (ANCHO - 120, ALTO - 100))
    ventana.blit(imgBotonSalir, (ANCHO // 2 - 110, ALTO//3 + 75))
    ventana.blit(tiempo, (ANCHO//2-250, 100))
    ventana.blit(imgIntento2, (ANCHO-220, ALTO-80))


#Verifica si agarró el bonus el usuario
def agregarBonus(spriteBonus, spritePersonaje):
    xPersonaje, yPersonaje, anchoPersonaje, altoPersonaje = spritePersonaje.rect
    xBonus, yBonus, anchoBonus, altoBonus = spriteBonus.rect
    #Hace la condición de que agarre el bonus
    if xPersonaje >= xBonus and xPersonaje <= xBonus+anchoBonus and yPersonaje+altoPersonaje >= yBonus and yPersonaje <= yBonus+altoBonus:
        spriteBonus.remove()
        spriteBonus.rect.left = randint(80, ANCHO - 80)
        spriteBonus.rect.bottom = int(randint(0, ALTO) / 100 + 0.5) * 100
        return True
    # Hace la condición de que agarre el bonus
    elif xPersonaje+anchoPersonaje >= xBonus and xPersonaje <= xBonus+anchoBonus and yPersonaje+altoPersonaje >= yBonus and yPersonaje <= yBonus+altoBonus:
        spriteBonus.remove()
        spriteBonus.rect.left = randint(80, ANCHO - 80)
        spriteBonus.rect.bottom = int(randint(0, ALTO) / 100 + 0.5) * 100
        return True
    else:
        pass


#Le paso todos los archivos para después utilizarlos
def dibujar():
    pygame.init() #Inicializa el motor de pygame
    ventana = pygame.display.set_mode((ANCHO, ALTO))  #Crea la ventana donde dibujará, Crea una ventana de ANCHO x ALTO
    reloj = pygame.time.Clock()  #Para limitar los frames por segundo
    termina = False  #Condición para que siga el juego, si es True, termina


    #Carga al personaje
    imgPersonaje = pygame.image.load("Conejo.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 340
    spritePersonaje.rect.bottom = 300
    #ALTO//2 + spritePersonaje.rect.height//2

    #Carga a los enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("CazadorIzquierda.png")
    for k in range(5): #Genera 5 enemigos
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
        spriteEnemigo.rect.bottom = int(randint(0, ALTO)/100+0.5) * 100
        listaEnemigos.append(spriteEnemigo) #Mete a los enemigos a la lista

    listaEnemigos2 = []
    imgEnemigo2 = pygame.image.load("CazadorDerecha.png")
    for i in range(5): #Genera 5 enemigos
        spriteEnemigo2 = pygame.sprite.Sprite()
        spriteEnemigo2.image = imgEnemigo2
        spriteEnemigo2.rect = imgEnemigo2.get_rect()
        spriteEnemigo2.rect.left = randint(0, ANCHO) - ANCHO
        spriteEnemigo2.rect.bottom = int(randint(0, ALTO)/100+0.5) * 100
        listaEnemigos2.append(spriteEnemigo2) #Mete a los enemigos a la lista


    #Cargar obstáculos
    imgObstaculo = pygame.image.load("arbol.png")
    spriteObstaculo = pygame.sprite.Sprite()
    spriteObstaculo.image = imgObstaculo
    spriteObstaculo.rect = imgObstaculo.get_rect()
    spriteObstaculo.rect.left = randint(70,ANCHO-70)
    spriteObstaculo.rect.bottom = int(randint(80,ALTO-80)/100+0.5) * 100

    #Cargar bonus
    imgBonus = pygame.image.load("BonoZanahoria.png")
    spriteBonus = pygame.sprite.Sprite()
    spriteBonus.image = imgBonus
    spriteBonus.rect = imgBonus.get_rect()
    spriteBonus.rect.left = randint(80,ANCHO-80)
    spriteBonus.rect.bottom = int(randint(80,ALTO-80)/100+0.5) * 100

    #Fondos
    imgFondoInicio = pygame.image.load("imgFondo1.jpg")
    imgFondoJugando = pygame.image.load("imgFondo2.jpg")
    imgFondoFinal = pygame.image.load("imgFondo3.jpg")

    #Menú
    imgBotonJugar = pygame.image.load("jugar.png")
    imgBotonSalir = pygame.image.load("salir.png")
    imgHighscore = pygame.image.load("Highscores.png")

    #Menú final
    imgHome = pygame.image.load("home.png")
    imgIntento2 = pygame.image.load("intentar.png")

    #Estado incial
    estado = MENU

    #Tiempo
    timer = 0 #Acumulador de tiempo de regeneración enemigos
    nuevoTiempo = 0 #Acumulador de puntuación

    #Fuente de texto
    fuente = pygame.font.SysFont("monospace", 64)

    #Carga la música
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)
    efectoSonido = pygame.mixer.Sound("sonidoConejo.wav")


    while not termina:  # Ciclo principal, Mientras la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

            #Estado jugando
            elif estado == JUGANDO and evento.type == pygame.KEYDOWN:
                xPersonaje, yPersonaje, anchoPersonaje, altoPersonaje = spritePersonaje.rect
                xObstaculo, yObstaculo, anchoObstaculo, altoObstaculo = spriteObstaculo.rect
                if evento.key == pygame.K_UP:
                    #Hace cumplir que no pase por el obstáculo
                    if xPersonaje >= xObstaculo-anchoPersonaje and xPersonaje <= xObstaculo+anchoObstaculo and yPersonaje-altoPersonaje*2 <= yObstaculo and yPersonaje >= yObstaculo+altoObstaculo:
                        pass
                    elif yPersonaje-altoPersonaje <= 0:
                        pass
                    else:
                        spritePersonaje.rect.bottom -= 100
                elif evento.key == pygame.K_DOWN:
                    # Hace cumplir que no pase por el obstáculo
                    if xPersonaje >= xObstaculo-anchoPersonaje and xPersonaje <= xObstaculo+anchoObstaculo and yPersonaje+altoPersonaje*2 >= yObstaculo and yPersonaje <= yObstaculo:
                        pass
                    elif yPersonaje+altoPersonaje >= ALTO:
                        pass
                    else:
                        spritePersonaje.rect.bottom += 100
                elif evento.key == pygame.K_RIGHT:
                    # Hace cumplir que no pase por el obstáculo
                    if xPersonaje+anchoPersonaje*2 >= xObstaculo and xPersonaje+anchoPersonaje <= xObstaculo+anchoObstaculo and yPersonaje+altoPersonaje >= yObstaculo and yPersonaje <= yObstaculo:
                        pass
                    elif xPersonaje+anchoPersonaje*2 >= ANCHO:
                        pass
                    else:
                        spritePersonaje.rect.left += 65
                elif evento.key == pygame.K_LEFT:
                    # Hace cumplir que no pase por el obstáculo
                    if xPersonaje+anchoPersonaje >= xObstaculo and xPersonaje-anchoPersonaje*2 <= xObstaculo+anchoObstaculo and yPersonaje+altoPersonaje >= yObstaculo and yPersonaje <= yObstaculo:
                        pass
                    elif xPersonaje-anchoPersonaje*2 <= -49:
                        pass
                    else:
                        spritePersonaje.rect.left -= 65


            elif estado == PUNTAJES and evento.type == pygame.MOUSEBUTTONUP:
                xMouse, yMouse = pygame.mouse.get_pos()  # Captura las coordenadas en las que hiciste click
                xHome = ANCHO - 120
                yHome = ALTO - 100
                xIntentar = ANCHO - 220
                yIntentar = ALTO - 80
                #Condición si el usuario hace click en home
                if xMouse >= xHome and xMouse <= xHome + 120 and yMouse >= yHome and yMouse <= yHome + 100:  # Condicion para el boton
                    nuevoTiempo = 0
                    spritePersonaje.rect = imgPersonaje.get_rect()
                    spritePersonaje.rect.left = 350
                    spritePersonaje.rect.bottom = 300
                    listaEnemigos.clear()
                    listaEnemigos2.clear()
                    spriteObstaculo.rect.left = randint(70, ANCHO - 70)
                    spriteObstaculo.rect.bottom = int(randint(80, ALTO - 80) / 100 + 0.5) * 100
                    spriteBonus.rect.left = randint(80, ANCHO - 80)
                    spriteBonus.rect.bottom = int(randint(80, ALTO - 80) / 100 + 0.5) * 100
                    estado = MENU
                #Condición si hace click en salir
                elif xMouse >= 0 and xMouse <= 221 and yMouse >= ALTO-100 and yMouse <= ALTO:
                    termina = True
                #Condición si hace click en reintentar
                elif xMouse >= xIntentar and xMouse <= xIntentar + ANCHO - 220 and yMouse >= yIntentar and yMouse <= yIntentar + ALTO - 80:
                    nuevoTiempo = 0
                    spritePersonaje.rect = imgPersonaje.get_rect()
                    spritePersonaje.rect.left = 350
                    spritePersonaje.rect.bottom = 300
                    listaEnemigos.clear()
                    listaEnemigos2.clear()
                    spriteObstaculo.rect.left = randint(70, ANCHO - 70)
                    spriteObstaculo.rect.bottom = int(randint(80, ALTO - 80) / 100 + 0.5) * 100
                    spriteBonus.rect.left = randint(80, ANCHO - 80)
                    spriteBonus.rect.bottom = int(randint(80, ALTO - 80) / 100 + 0.5) * 100
                    estado = JUGANDO


            #Probar botones del botón final
            elif estado == FINAL and evento.type == pygame.MOUSEBUTTONUP:
                xMouse, yMouse = pygame.mouse.get_pos()  # Captura las coordenadas en las que hiciste click
                # Preguntar si solto el mouse dentro del boton de home
                xHome = ANCHO - 120
                yHome = ALTO - 100
                xBotonSalir = ANCHO//2 - 110
                yBotonSalir = ALTO//3 + 75
                xIntentar = ANCHO - 220
                yIntentar = ALTO - 80
                #Condición para establecer el juego en 0
                if xMouse >= xHome and xMouse <= xHome + 120 and yMouse >= yHome and yMouse <= yHome + 100:  # Condicion para el boton
                    nuevoTiempo = 0
                    spritePersonaje.rect = imgPersonaje.get_rect()
                    spritePersonaje.rect.left = 350
                    spritePersonaje.rect.bottom = 300
                    listaEnemigos.clear()
                    listaEnemigos2.clear()
                    spriteObstaculo.rect.left = randint(70, ANCHO - 70)
                    spriteObstaculo.rect.bottom = int(randint(80, ALTO - 80) / 100 + 0.5) * 100
                    spriteBonus.rect.left = randint(80, ANCHO-80)
                    spriteBonus.rect.bottom = int(randint(80, ALTO-80) / 100 + 0.5) * 100
                    estado = MENU
                # Condición para click en botón salir
                elif xMouse >= xBotonSalir and xMouse <= xBotonSalir+221 and yMouse >= yBotonSalir and yMouse <= yBotonSalir +100:
                    termina = True
                # Condición para establecer el juego en 0
                elif xMouse >= xIntentar and xMouse <= xIntentar+ANCHO-220 and yMouse >= yIntentar and yMouse <= yIntentar+ALTO-80:
                    nuevoTiempo = 0
                    spritePersonaje.rect = imgPersonaje.get_rect()
                    spritePersonaje.rect.left = 350
                    spritePersonaje.rect.bottom = 300
                    listaEnemigos.clear()
                    listaEnemigos2.clear()
                    spriteObstaculo.rect.left = randint(70, ANCHO - 70)
                    spriteObstaculo.rect.bottom = int(randint(80, ALTO - 80) / 100 + 0.5) * 100
                    spriteBonus.rect.left = randint(80, ANCHO - 80)
                    spriteBonus.rect.bottom = int(randint(80, ALTO-80) / 100 + 0.5) * 100
                    estado = JUGANDO

            #Estado menú
            elif estado == MENU and evento.type == pygame.MOUSEBUTTONUP:
                xMouse, yMouse = pygame.mouse.get_pos() #Captura las coordenadas en las que hiciste click
                # Preguntar si solto el mouse dentro del boton
                xBoton = ANCHO//2-110
                yBoton = ALTO//3-50
                xBotonSalir = ANCHO//2-110
                yBotonSalir = ALTO//3+100
                xBotonPuntajes = ANCHO//2-110
                yBotonPuntajes = ALTO-160
                #Condición si hace click en jugar
                if xMouse >= xBoton and xMouse <= xBoton+220 and yMouse >= yBoton and yMouse <= yBoton+100: #Condicion para el boton
                    estado = JUGANDO
                #Condición si hace click en salir
                elif xMouse >= xBotonSalir and xMouse <= xBotonSalir+220 and yMouse >= yBotonSalir and yMouse <= yBotonSalir+100:
                    termina = True
                #Condición si hace click en highscore
                elif xMouse >= xBotonPuntajes and xMouse <= xBotonPuntajes+220 and yMouse >= yBotonPuntajes and yMouse <= yBotonPuntajes+100:
                    estado = PUNTAJES


        #Estado jugando
        if estado == JUGANDO:
            ventana.blit(imgFondoJugando, (0, 0))
            #Tiempo real
            nuevoTiempo += 1 / 40
            #Tiempo de regeneración
            timer += 1 / 40
            #Ciclo para que se generen los cazadores
            if timer >= 1:
                timer = 0

                #Carga los enemigos
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
                spriteEnemigo.rect.bottom = int(randint(0, ALTO)/100+0.5) * 100
                listaEnemigos.append(spriteEnemigo)

                spriteEnemigo2 = pygame.sprite.Sprite()
                spriteEnemigo2.image = imgEnemigo2
                spriteEnemigo2.rect = imgEnemigo2.get_rect()
                spriteEnemigo2.rect.left = -randint(0, ANCHO) - ANCHO
                spriteEnemigo2.rect.bottom = int(randint(0, ALTO)/100+0.5) * 100
                listaEnemigos2.append(spriteEnemigo2)

            moverEnemigos(listaEnemigos,listaEnemigos2)
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos, listaEnemigos2)
            dibujarObstaculo(ventana, spriteObstaculo)
            #Imprime el tiempo
            texto = fuente.render("Tiempo %d" % int(nuevoTiempo), 1, ROJO)
            ventana.blit(texto, (ANCHO // 2 + 90, 20))
            #Verifica si chocaron
            if verificarColision(listaEnemigos, listaEnemigos2, spritePersonaje) == True:
                efectoSonido.play()
                estado = FINAL
            #Verifica si agarró el bonus
            elif agregarBonus(spriteBonus,spritePersonaje) == True:
                nuevoTiempo = nuevoTiempo+2
            #Genera el bonus
            elif nuevoTiempo >= 5 or nuevoTiempo >= 10 or nuevoTiempo >= 15:
                dibujarBonus(ventana, spriteBonus)

        #Estado de menú principal
        elif estado == MENU:
            ventana.blit(imgFondoInicio, (0,0))
            dibujarMenu(ventana, imgBotonJugar, imgBotonSalir, imgHighscore)

        #Estado de highscore
        elif estado == PUNTAJES:
            ventana.blit(imgFondoInicio,(0,0))
            ventana.blit(imgHome, (ANCHO - 120, ALTO - 100))
            ventana.blit(imgBotonSalir, (0, ALTO -100))
            ventana.blit(imgIntento2, (ANCHO - 220, ALTO - 80))

            #Se lee el archivo que contiene el puntaje anterior
            puntajeAnterior = open("Puntajes.txt", "r")
            primerLinea = puntajeAnterior.readline()
            puntaje = str(primerLinea)
            score = fuente.render("Mejor puntaje: %s segundos" % puntaje, 1, ROJO)
            ventana.blit(score, (100,ALTO//2))
            puntajeAnterior.close()


        #Estado de menú final
        elif estado == FINAL:
            ventana.blit(imgFondoFinal, (0,0))
            tiempo = fuente.render(str("Tu puntuación es: %d" % int(nuevoTiempo)), 1, ROJO)
            dibujarMenuFinal(ventana, imgBotonSalir, imgHome, imgIntento2,tiempo)

            #Leo el archivo donde esta el puntaje anterior
            puntajeAnterior = open("Puntajes.txt", "r")
            primerLinea = puntajeAnterior.readline()
            puntaje = int(primerLinea)
            puntajeActual = nuevoTiempo // 1
            #Comparo si el actual es mayor que el anterior
            if puntajeActual > puntaje:
                mejorScore = open("Puntajes.txt", "w")
                mejorScore.write("%d" % puntajeActual)
                mejorScore.close()
            puntajeAnterior.close()


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 frames por segundo

    # Después del ciclo principal
    pygame.quit()  # termina pygame

# Función principal, aquí resuelves el problema
def main():
    dibujar()

# Llamas a la función principal
main()
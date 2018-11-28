# Encoding: UTF-8
# Autor: Oscar Alejandro Torres Maya, A01377686
# Descripción: Proyecto Final, videojuego

import pygame   #Importa librería de pygame
from random import randint  #Importa función randint

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

#Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
NEGRO = (0,0,0)
VERDE = (76,145,65)

#Estados de juego
MENU = 1
JUGANDO = 2


def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos(ventana, listaEnemigos, listaEnemigos2):
    for enemigo in listaEnemigos:     # VISITAR O ACCEDER A CADA ELEMENTO
        ventana.blit(enemigo.image, enemigo.rect)  # IMAGEN , LUGAR

    for enemigo2 in listaEnemigos2:   # VISITAR O ACCEDER A CADA ELEMENTO
        ventana.blit(enemigo2.image, enemigo2.rect)


def dibujarObstaculo(ventana,spriteObstaculo):
    for i in range(10):
        ventana.blit(spriteObstaculo.image, spriteObstaculo.rect)


def dibujarBonus(ventana,spriteBonus):
    ventana.blit(spriteBonus.image, spriteBonus.rect)


def moverEnemigos(listaEnemigos,listaEnemigos2):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 1

    for enemigo2 in listaEnemigos2:
        enemigo2.rect.left += 1


def dibujarMenu(ventana, imgBotonJugar, imgBotonSalir):
    ventana.blit(imgBotonJugar, (ANCHO//2-110, ALTO//3-50))
    ventana.blit(imgBotonSalir, (ANCHO//2-110, ALTO//3+100))


def verificarColision(listaEnemigos, spritePersonaje):
        for e in range(len(listaEnemigos)-1, -1, -1):
            enemigo = listaEnemigos[e]
            # Bala vs enemigo
            xpersonaje = spritePersonaje.rect.left
            ypersonaje = spritePersonaje.rect.bottom
            xenemigo, yenemigo, aenemigo, altenemigo = enemigo.rect
            if xpersonaje >= xenemigo-90 and xpersonaje <= xenemigo+aenemigo+293 and ypersonaje >= yenemigo and ypersonaje <= yenemigo+altenemigo+80:
                listaEnemigos.remove(enemigo) #Le pego!!!
                spritePersonaje.remove()
                spritePersonaje.kill()
                break


def dibujar():
    pygame.init() #Inicializa el motor de pygame
    #Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  #Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  #Para limitar los fps
    termina = False  #Bandera para saber si termina la ejecución, iniciamos suponiendo que no


    #CARGAR AL PERSONAJE
    imgPersonaje = pygame.image.load("Conejo.jpg")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect() #Pregunta dimensiones x, y.
    spritePersonaje.rect.left = 350
    spritePersonaje.rect.bottom = ALTO//2 + spritePersonaje.rect.height//2


    #CARGAR ENEMIGOS
    listaEnemigos = []
    imgEnemigo = pygame.image.load("CazadorIzquierda.png")
    for k in range(5):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
        spriteEnemigo.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteEnemigo) # METER OBJETOS A LA LISTA
    listaEnemigos2 = []
    imgEnemigo2 = pygame.image.load("CazadorDerecha.png")
    for k in range(5):
        spriteEnemigo2 = pygame.sprite.Sprite()
        spriteEnemigo2.image = imgEnemigo2
        spriteEnemigo2.rect = imgEnemigo2.get_rect()
        spriteEnemigo2.rect.left = randint(0, ANCHO) - ANCHO
        spriteEnemigo2.rect.bottom = randint(0, ALTO)
        listaEnemigos2.append(spriteEnemigo2) # METER OBJETOS A LA LISTA


    #Cargar obstáculos
    imgObstaculo = pygame.image.load("arbol.png")
    spriteObstaculo = pygame.sprite.Sprite()
    spriteObstaculo.image = imgObstaculo
    spriteObstaculo.rect = imgObstaculo.get_rect()
    spriteObstaculo.rect.left = randint(0,ANCHO)
    spriteObstaculo.rect.bottom = randint(0,ALTO)


    #Cargar bonus
    imgBonus = pygame.image.load("BonoZanahoria.png")
    spriteBonus = pygame.sprite.Sprite()
    spriteBonus.image = imgBonus
    spriteBonus.rect = imgBonus.get_rect()
    spriteBonus.rect.left = randint(0,ANCHO)
    spriteBonus.rect.bottom = randint(0,ALTO)


    #Menú
    imgBotonJugar = pygame.image.load("jugar.png")
    imgBotonSalir = pygame.image.load("salir.png")

    estado = MENU


    #Tiempo
    timer = 0 #Acumulador de tiempo
    nuevoTiempo = 0


    #Fuente de texto
    fuente = pygame.font.SysFont("monospace", 64)


    #AUDIO
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)

    #efecto = pygame.mixer.Sound("shoot.wav")


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

            elif evento.type == pygame.KEYDOWN:  #CUANDO PRESIONO LA TELCA, Moviendo=ARRIBA para hacer que se mueva mientras tengo presionada la tecla
                if evento.key == pygame.K_UP:
                    spritePersonaje.rect.bottom -= 80
                elif evento.key == pygame.K_DOWN:
                    spritePersonaje.rect.bottom += 80
                elif evento.key == pygame.K_RIGHT:
                    spritePersonaje.rect.left += 90
                elif evento.key == pygame.K_LEFT:
                    spritePersonaje.rect.left -= 90

            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos() #Captura las coordenadas en las que hiciste click
                print(xm,",",ym)
                # Preguntar si solto el mouse dentro del boton
                xboton = ANCHO//2-110
                yboton = ALTO//3-50
                xbotonSalir = ANCHO//2-110
                ybotonSalir = ALTO//3+100
                if xm >= xboton and xm <= xboton+220 and ym >= yboton and ym <= yboton+100: #Condicion para el boton
                    estado = JUGANDO
                elif xm >= xbotonSalir and xm <= xbotonSalir+220 and ym >= ybotonSalir and ym <= ybotonSalir+100:
                    termina = True


        if estado == JUGANDO:
            ventana.fill(VERDE)
            nuevoTiempo += 1 / 40
            texto = fuente.render("Tiempo %0.2f" % nuevoTiempo, 1, ROJO)
            ventana.blit(texto, (ANCHO // 2 + 90, 20))
            if timer >= 2:
                timer = 0
                #REPRODUCIR MUSICA
                #efecto.play()

                #ENEMIGO
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
                spriteEnemigo.rect.bottom = randint(0, ALTO)
                listaEnemigos.append(spriteEnemigo)  # METER OBJETOS A LA LISTA

                spriteEnemigo2 = pygame.sprite.Sprite()
                spriteEnemigo2.image = imgEnemigo2
                spriteEnemigo2.rect = imgEnemigo2.get_rect()
                spriteEnemigo2.rect.left = randint(0, ANCHO) + ANCHO
                spriteEnemigo2.rect.bottom = randint(0, ALTO)
                listaEnemigos2.append(spriteEnemigo2)  # METER OBJETOS A LA LISTA

            moverEnemigos(listaEnemigos,listaEnemigos2)

            if nuevoTiempo >= 3:
                dibujarBonus(ventana, spriteBonus)

            # Dibujar, aquí haces todos los trazos que requieras
            dibujarPersonaje(ventana,spritePersonaje)
            dibujarEnemigos(ventana,listaEnemigos,listaEnemigos2)
            dibujarObstaculo(ventana,spriteObstaculo)
            verificarColision(listaEnemigos, spritePersonaje)


        elif estado == MENU:
            ventana.fill(NEGRO)
            dibujarMenu(ventana, imgBotonJugar, imgBotonSalir)  #Dibujar todas las opciones del menú

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/40

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja

# Llamas a la función principal
main()
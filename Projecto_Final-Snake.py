# Jose Luis Mata Lomelí
# A01377205
# Fundamentos de Programación: Grupo 02
# Profesor Roberto Martinez Roman
# Proyecto Final
# Objetivo: Lograr una recreación del juego Snake en Pygame

#Librerias
import pygame
import random


pygame.init()   #Iniciar el motor de Pygame

#Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)


#Dimensiones de la pantalla
Ancho = 800
Alto = 600

Ventana = pygame.display.set_mode((Ancho, Alto)) #Crear Ventana
pygame.display.set_caption('La viborini') #Nombre dado a la ventana

reloj = pygame.time.Clock() #Limitar Frames

font = pygame.font.SysFont(None, 25)


def Snake(Lista):
    # Dibujar Serpiente
    for i in Lista:
        pygame.draw.rect(Ventana, NEGRO, [i[0], i[1], 10, 10])

def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()


#Mensajes de texto
def message(msg, color, Y_displace = 0):
    textSurf, textRect = text_objects(msg,color)
    textRect.center = (Ancho / 2), (Alto / 2) + Y_displace
    Ventana.blit(textSurf, textRect)


# Juego
def game():

    Exit = False
    gameOver = False

    #Posicion de la Serpiente
    Serpiente_x = Ancho / 2
    Serpiente_y = Alto / 2

    cambio_x = 0
    cambio_y = 0

    #Posicion de la Manzana

    Manzana_x = round(random.randrange(0, Ancho-10)/10.0)*10.0
    Manzana_y = round(random.randrange(0, Alto-10)/10.0)*10.0

    #Para manejar el largo de la serpiente
    Lista = []
    Largo = 2

    while not Exit:

        while gameOver == True:

            Ventana.fill(VERDE)

            message("GAME OVER!",
                    ROJO,
                    -50)

            message("Presiona C para continuar o Q para terminar",
                    NEGRO,
                    50)

            pygame.display.update()

            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_q:
                        Exit = True
                        gameOver = False

                    if event.key == pygame.K_c:
                        game()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                Exit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    cambio_x = -10
                    cambio_y = 0

                elif event.key == pygame.K_RIGHT:
                    cambio_x = 10
                    cambio_y = 0

                elif event.key == pygame.K_UP:
                    cambio_y = -10
                    cambio_x = 0

                elif event.key == pygame.K_DOWN:
                    cambio_y = 10
                    cambio_x = 0


        if Serpiente_x >= Ancho or Serpiente_x < 0 or Serpiente_y >= Alto or Serpiente_y < 0:
            gameOver = True


        Serpiente_x += cambio_x
        Serpiente_y += cambio_y
        Ventana.fill(VERDE)

        #Manzana
        pygame.draw.rect(Ventana, ROJO, (Manzana_x, Manzana_y, 10, 10))

        #Serpiente
        Cabeza = []
        Cabeza.append(Serpiente_x)
        Cabeza.append(Serpiente_y)
        Lista.append(Cabeza)

        if len(Lista) > Largo:
            del Lista[0]

            for Segmento in Lista[:-1]:
                if Segmento == Cabeza:
                    gameOver = True

        Snake(Lista)

        pygame.display.update()

        # Si pasas sobre la manzana..
        if Serpiente_x == Manzana_x and Serpiente_y == Manzana_y:
            #Crear otra
            Manzana_x = round(random.randrange(0, Ancho - 10) / 10.0) * 10.0
            Manzana_y = round(random.randrange(0, Alto - 10) / 10.0) * 10.0
            Largo += 5


        reloj.tick(15)

    pygame.quit()
    quit()

game()

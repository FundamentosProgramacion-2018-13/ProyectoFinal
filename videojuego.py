# encoding: UTF-8
# Autor: Humberto Carrillo Gómez
# Beta de un juego.

import pygame   # Librería de pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul

puntuacion = 0
contadorEnemigos = 0
# Estados

MENU = 1
Jugando = 2
gameOver = 3

# Estados de Movimiento
QUIETO = 1
ABAJO = 2
ARRIBA = 3

audioFinal = True

# Audio
pygame.mixer.init()
pygame.mixer.music.load("Lost Woods - The Legend of Zelda Ocarina of Time.mp3")
pygame.mixer.music.play(-1)

efecto = pygame.mixer.Sound("OOT_YoungLink_Attack1.wav")
efectoCorazonPerdido = pygame.mixer.Sound('OOT_YoungLink_Hurt3.wav')
efectoFinDelJuego = pygame.mixer.Sound('OOT_YoungLink_Scream1.wav')


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)     # Dibujar una imagen en la ventana


def dibujarEnemigos(ventana, listaEnemigos):
    # Visitar a cada elemento
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -= 1


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)

def dibujarCorazones(ventana, listaCorazones):
    posicionxCorazon = 750
    posicionyCorazon = 0
    for corazon in listaCorazones:
        ventana.blit(corazon.image, (posicionxCorazon, posicionyCorazon))
        posicionxCorazon -= 40


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.x += 2


def dibujarMenu(ventana, imgBtnJugar, imgFondoMenu):
    ventana.blit(imgFondoMenu, (0,0))
    ventana.blit(imgBtnJugar, (ANCHO//2-128, ALTO//3))


def dibujarGameOver(ventana, imgFondoFinal, texto):
    ventana.blit(imgFondoFinal, (0, 0))
    ventana.blit(texto, (ANCHO//2, ALTO//2))


def perderCorazones(listaCorazones):
    for corazon in listaCorazones:
            listaCorazones.remove(corazon)
            if len(listaCorazones) >0:
                efectoCorazonPerdido.play()
            elif len(listaCorazones) == 0:
                efectoFinDelJuego.play()
            break




def verificarColision(listaEnemigos, listaBalas, listaCorazones, puntuacion, contadorEnemigos):
    for bala in listaBalas:
        for enemigo in listaEnemigos:
            #bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe = enemigo.rect.left
            ye = enemigo.rect.bottom
            ae = enemigo.rect.width
            alte = enemigo.rect.height
            if xb>= xe and xb<= xe+ae and yb>= ye and yb <= ye + alte:
                # Le pegó!!!!!!
                puntuacion += 10
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                break
        # Perder un corazon
            if xe == ANCHO - 810:
                    listaEnemigos.remove(enemigo)
                    perderCorazones(listaCorazones)




def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje
    imgPersonaje = pygame.image.load("idle link.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()              # Dimensiones asignadas al sprite
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = ALTO//2 + spritePersonaje.rect.height//2

    # Enemigos
    listaEnemigos= []
    imgEnemigo = pygame.image.load("enemigo.png")
    for k in range (20):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
        spriteEnemigo.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteEnemigo)

    # Corazones
    listaCorazones = []
    imgCorazon = pygame.image.load('corazon.png')
    for k in range (3):
        spriteCorazon = pygame.sprite.Sprite()
        spriteCorazon.image = imgCorazon
        listaCorazones.append(spriteCorazon)

    # Proyectiles/balas
    listaBalas = []
    imgBala = pygame.image.load("Flecha.png")



    # Menú
    imgBtnJugar = pygame.image.load("button_play.png")
    imgReiniciar = pygame.image.load('reset.png')
    estado = MENU
    moviendo = QUIETO

    #posición del fondo
    xf = 0

    # Tiempo

    timer = 0  #Acumulador de tiempo



    #Imagen de fondo
    imgFondo = pygame.image.load("forest.png")
    imgFondoMenu = pygame.image.load('fondo Menu.jpg')
    imgFondoFinal = pygame.image.load('fondo Final.jpg')

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    #spritePersonaje.rect.bottom -= 5
                    moviendo = ARRIBA
                elif evento.key == pygame. K_DOWN:
                    #spritePersonaje.rect.bottom += 5
                    moviendo = ABAJO
                elif evento.key == pygame.K_z:
                    # Crear una bala
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalas.append(spriteBala)
            elif evento.type == pygame.KEYUP:
                moviendo = QUIETO

            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm, ",", ym)
                # Preguntar si soltó el mouse dentro del botón
                xb = ANCHO//2-128
                yb = ALTO//3
                if xm>= xb and xm <= xb +256 and ym>=yb and ym<=yb + 100:
                    estado = Jugando


        # Borrar pantalla
        ventana.fill(BLANCO)

        if estado == Jugando:
            #Tiempo
            if timer >= 2:
                timer = 0               # Reiniciar timer
                # Crear una bala cada dos segundos
                efecto.play()
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                spriteBala.rect.bottom = spritePersonaje.rect.bottom
                listaBalas.append(spriteBala)
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(0, ANCHO) + ANCHO
                spriteEnemigo.rect.bottom = randint(0, ALTO)
                listaEnemigos.append(spriteEnemigo)


            # Actualizar enemigos
            moverEnemigos(listaEnemigos)
            # Actualizar Balas, enemigos, corazones y puntos
            moverBalas(listaBalas)
            verificarColision(listaEnemigos, listaBalas, listaCorazones, puntuacion, contadorEnemigos)
            # MoverPersonaje
            if moviendo == ARRIBA and spritePersonaje.rect.bottom > 30:
                spritePersonaje.rect.bottom -= 10
            elif moviendo == ABAJO and spritePersonaje.rect.bottom < 600:
                spritePersonaje.rect.bottom += 10


        # Dibujar, aquí haces todos los trazos que requieras
            ventana.blit(imgFondo, (xf, 0))
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)
            dibujarCorazones(ventana, listaCorazones)
            if len(listaCorazones) == 0:
                estado = gameOver



        elif estado == MENU:
            # Dibujar menú
            dibujarMenu(ventana, imgBtnJugar, imgFondoMenu)
        elif estado == gameOver:
            # Texto en la pantalla
            fuente = pygame.font.SysFont("monospace", 34)
            texto = fuente.render("tu puntuacion %d" % puntuacion, 1, ROJO)
            dibujarGameOver(ventana, imgFondoFinal, texto)



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

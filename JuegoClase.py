#Joshua Sánchez Martínez
#Juego, una nave defiende su planeta de naves invasoras


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
NEGRO = (0,0,0)


#Estados
MENU = 1
JUGANDO = 2
INSTRUCCIONES = 3
MAS = 4
HISTORIA = 5


#Estados de movimiento
QUIETO = 1
ABAJO = 2
ARRIBA = 3
DERECHA = 4
IZQUIERDA = 5


def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)
# Estructura básica de un programa que usa pygame para dibujar


def dibujarEnemigos(ventana, listaEnemigos):
    #Visitar a cada elemento
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def moverEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.bottom +=1


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:bala.rect.bottom -= 2


def dibujarMenu(ventana, imgBtnJugar,imgBtnMas,imgBtnAyuda,imgBtnHistoria):
    ventana.blit(imgBtnJugar, (ANCHO//2-350, ALTO - 400))
    ventana.blit(imgBtnMas, (ANCHO // 2 - 350, ALTO - 200))
    ventana.blit(imgBtnAyuda, (ANCHO // 2 + 200, ALTO - 550))
    ventana.blit(imgBtnHistoria, (ANCHO // 2 - 150, ALTO - 300))

def dibujarBotones(ventana, imgBtn1,imgBtn2,imgBtn3,imgBtn4,imgBtn5):
    ventana.blit(imgBtn1, (ANCHO//2 - 120, ALTO - 200))
    ventana.blit(imgBtn2, (ANCHO // 2 + 50, ALTO - 200))
    ventana.blit(imgBtn3, (ANCHO // 2 + 50, ALTO - 300))
    ventana.blit(imgBtn4, (ANCHO // 2 + 220, ALTO - 200))
    ventana.blit(imgBtn5, (ANCHO // 2 -370 , ALTO - 200))

def dibujarAtras(ventana, imgBtnAtras):
    ventana.blit(imgBtnAtras, (ANCHO//2, ALTO - 100))




def verificarColision(listaEnemigos, listaBalas):
    for k in range (len(listaBalas)-1,-1,-1):
        bala=listaBalas[k]
        for e in range (len(listaEnemigos)-1,-1,-1):  #Recorrer con Indices
            enemigo = listaEnemigos[e]
            #bala VS enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                # Le pegó!!!!
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)

                break


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Personaje
    imgPersonaje = pygame.image.load("jugador.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect= imgPersonaje.get_rect()
    spritePersonaje.rect.left = 350
    spritePersonaje.rect.bottom = ALTO-100 + spritePersonaje.rect.height//2

    #Enemigos
    listaEnemigos = []
    listaExplosion = []
    imgEnemigo = pygame.image.load("enemigo.png")
    imgEnemigo1 = pygame.image.load("enemigo1.png")
    imgEnemigo2 = pygame.image.load("enemigo2.png")
    imgEnemigo3 = pygame.image.load("enemigo3.png")

    #for k in range(20):
        #spriteEnemigo = pygame.sprite.Sprite()
        #spriteEnemigo.image = imgEnemigo
        #spriteEnemigo.rect = imgEnemigo.get_rect()
        #spriteEnemigo.rect.left = randint(-800, ANCHO) #AREA DONDE SE GENERAN
        #spriteEnemigo.rect.bottom = randint (-600, -ALTO) + ALTO
        #listaEnemigos.append(spriteEnemigo)

    #Proyectiles/balas
    listaBalas = []
    imgBala = pygame.image.load("plasmaBala.png")
    imgExplosion = pygame.image.load("explosion.png")

    #Menú
    imgBtnJugar = pygame.image.load("button.png")
    imgBtnMas = pygame.image.load("buttonMas.png")
    imgBtnAyuda = pygame.image.load("buttonInterrogacion.png")
    imgBtnAtras = pygame.image.load("button (1).png")
    imgBtnHistoria = pygame.image.load("button_h.png")
    imgFondo = pygame.image.load("fondoJuego.jpg")
    imgFondoInicio = pygame.image.load("FI.png")
    imgBtnAbajo = pygame.image.load("button_v.png")
    imgBtnArriba = pygame.image.load("button (3).png")
    imgBtnDerecha = pygame.image.load("button (1).png")
    imgBtnIzquierda = pygame.image.load("button.png")
    imgBtnEspacio = pygame.image.load("button (2).png")

    estado = MENU


    moviendo = QUIETO

    xf = 0

    #TIEMPO
    timer = 0   #Acumulador de tiempo

    #TEXTO
    fuente = pygame.font.SysFont("monospace", 64)

    #AUDIO
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)     #-1 para infinito y 1 para momentaneo


    efecto = pygame.mixer.Sound("shoot.wav")


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    moviendo = ARRIBA
                    #spritePersonaje.rect.bottom -= 5
                elif evento.key == pygame.K_DOWN:
                    moviendo = ABAJO
                    #spritePersonaje.rect.bottom += 5
                elif evento.key == pygame.K_RIGHT:
                    moviendo = DERECHA
                    #spritePersonaje.rect.bottom += 5
                elif evento.key == pygame.K_LEFT:
                    moviendo = IZQUIERDA
                    #spritePersonaje.rect.bottom += 5
                elif evento.key == pygame.K_SPACE:
                    #Crear una bala
                    efecto.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left-40 + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom-70
                    listaBalas.append(spriteBala)
            elif evento.type == pygame.KEYUP:
                moviendo = QUIETO
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm,",",ym)
                #Preguntar si soltó el mouse dentro del botón iniciar
                xb = ANCHO//2-350
                yb= ALTO//3
                if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb+100:
                    estado = JUGANDO
                elif xm >= ANCHO//2+200 and xm <= (ANCHO//2+200) and ym >= ALTO//3-550 and ym <= (ALTO//3-550):
                    estado = INSTRUCCIONES
                elif xm >= ANCHO//2-350 and xm <= ANCHO//2-350 and ym >= ALTO-200 and ym <= ALTO-200:
                    estado = MAS
                elif xm >= ANCHO//2-150 and xm <= ANCHO//2-150 and ym >= ALTO-300 and ym <= ALTO-300:
                    estado =  HISTORIA


        # Borrar pantalla
        #ventana.blit(imgFondoInicio, (0, 0))
        #ventana.fill(NEGRO)

        if estado == JUGANDO:

            #TIEMPO
            if timer >= 2:  #>Tiene que llegar a 2
                timer = 0   #Vuelve a ser cero

            #Actualizar enemigos
                for k in range(2):
                    spriteEnemigo1 = pygame.sprite.Sprite()
                    spriteEnemigo1.image = imgEnemigo1
                    spriteEnemigo1.rect = imgEnemigo1.get_rect()
                    spriteEnemigo1.rect.left = randint(100, 700)  # AREA DONDE SE GENERAN
                    spriteEnemigo1.rect.bottom = randint(-600, -ALTO) + ALTO
                    listaEnemigos.append(spriteEnemigo1)
                for k in range(2):
                    spriteEnemigo2 = pygame.sprite.Sprite()
                    spriteEnemigo2.image = imgEnemigo2
                    spriteEnemigo2.rect = imgEnemigo2.get_rect()
                    spriteEnemigo2.rect.left = randint(100, 700)  # AREA DONDE SE GENERAN
                    spriteEnemigo2.rect.bottom = randint(-600, -ALTO) + ALTO
                    listaEnemigos.append(spriteEnemigo2)
                for k in range(1):
                    spriteEnemigo3 = pygame.sprite.Sprite()
                    spriteEnemigo3.image = imgEnemigo3
                    spriteEnemigo3.rect = imgEnemigo3.get_rect()
                    spriteEnemigo3.rect.left = randint(100, 700)  # AREA DONDE SE GENERAN
                    spriteEnemigo3.rect.bottom = randint(-600, -ALTO) + ALTO
                    listaEnemigos.append(spriteEnemigo3)
                if timer >= 2:  # >Tiene que llegar a 2
                    timer = 0

                    for k in range(6):
                        spriteEnemigo = pygame.sprite.Sprite()
                        spriteEnemigo.image = imgEnemigo
                        spriteEnemigo.rect = imgEnemigo.get_rect()
                        spriteEnemigo.rect.left = randint(100, 700)  # AREA DONDE SE GENERAN
                        spriteEnemigo.rect.bottom = randint(-600, -ALTO) + ALTO
                        listaEnemigos.append(spriteEnemigo)
                    for k in range(3):
                        spriteEnemigo1 = pygame.sprite.Sprite()
                        spriteEnemigo1.image = imgEnemigo1
                        spriteEnemigo1.rect = imgEnemigo1.get_rect()
                        spriteEnemigo1.rect.left = randint(100, 700)  # AREA DONDE SE GENERAN
                        spriteEnemigo1.rect.bottom = randint(-600, -ALTO) + ALTO
                        listaEnemigos.append(spriteEnemigo1)
                    for k in range(4):
                        spriteEnemigo2 = pygame.sprite.Sprite()
                        spriteEnemigo2.image = imgEnemigo2
                        spriteEnemigo2.rect = imgEnemigo2.get_rect()
                        spriteEnemigo2.rect.left = randint(100, 700)  # AREA DONDE SE GENERAN
                        spriteEnemigo2.rect.bottom = randint(-600, -ALTO) + ALTO
                        listaEnemigos.append(spriteEnemigo2)
                    for k in range(3):
                        spriteEnemigo3 = pygame.sprite.Sprite()
                        spriteEnemigo3.image = imgEnemigo3
                        spriteEnemigo3.rect = imgEnemigo3.get_rect()
                        spriteEnemigo3.rect.left = randint(100, 700)  # AREA DONDE SE GENERAN
                        spriteEnemigo3.rect.bottom = randint(-600, -ALTO) + ALTO
                        listaEnemigos.append(spriteEnemigo3)

            if moviendo == ARRIBA:
                spritePersonaje.rect.bottom -= 10
            elif moviendo == ABAJO:
                spritePersonaje.rect.bottom += 10
            elif moviendo == DERECHA:
                spritePersonaje.rect.left += 10
            elif moviendo == IZQUIERDA:
                spritePersonaje.rect.left -= 10
            moverEnemigos(listaEnemigos)
            moverBalas(listaBalas)

            verificarColision(listaEnemigos, listaBalas)

            # Dibujar, aquí haces todos los trazos que requieras

            ventana.blit(imgFondo, (0,xf))
            xf += 1
            if xf != 0:
                ventana.blit(imgFondo, (0, xf-600))
                ventana.blit(imgFondo, (0, xf-1200))
                ventana.blit(imgFondo, (0, xf-1800))
                ventana.blit(imgFondo, (0, xf-2400))
                ventana.blit(imgFondo, (0, xf-3000))
                ventana.blit(imgFondo, (0, xf-3600))
                ventana.blit(imgFondo, (0, xf-4200))
                ventana.blit(imgFondo, (0, xf-4800))
                ventana.blit(imgFondo, (0, xf-5400))
                ventana.blit(imgFondo, (0, xf-6000))
                ventana.blit(imgFondo, (0, xf-6600))
                ventana.blit(imgFondo, (0, xf-7200))
                ventana.blit(imgFondo, (0, xf-7800))
                ventana.blit(imgFondo, (0, xf-8400))
                ventana.blit(imgFondo, (0, xf-9000))
                ventana.blit(imgFondo, (0, xf-9600))
                ventana.blit(imgFondo, (0, xf-10200))
                ventana.blit(imgFondo, (0, xf-10800))
                ventana.blit(imgFondo, (0, xf-11400))
                ventana.blit(imgFondo, (0, xf-12000))
                ventana.blit(imgFondo, (0, xf-12600))
                ventana.blit(imgFondo, (0, xf-13200))
                ventana.blit(imgFondo, (0, xf-13800))
                ventana.blit(imgFondo, (0, xf-14400))
                xf += 1

            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalas)


        elif estado == MENU:

            #Dibujar menú
            ventana.blit(imgFondoInicio, (0, 0))
            dibujarMenu(ventana, imgBtnJugar, imgBtnMas, imgBtnAyuda, imgBtnHistoria)

        elif estado == INSTRUCCIONES:

            #Dibujar menú
            ventana.blit(imgFondoInicio, (0, 0))
            texto = fuente.render("Flechasd de dirección = movimiento,espacio = disparar" % xf, 1, ROJO)
            ventana.blit(texto, (ANCHO // 2 - 400, 50))
            dibujarBotones(ventana, imgBtnIzquierda, imgBtnAbajo, imgBtnArriba, imgBtnDerecha, imgBtnEspacio)
            dibujarAtras(ventana,imgBtnAtras)

        elif estado == MAS:

            #Dibujar menú
            dibujarMenu(ventana, imgBtnJugar,imgBtnMas,imgBtnAyuda,imgBtnHistoria)
            dibujarAtras(ventana,imgBtnAtras)

        elif estado == HISTORIA:

            texto = fuente.render("Tu mision es sobrevivir al ataque invasor en un determinado tiempo, dispara para lograr tu cometido" % xf, 1, ROJO)
            ventana.blit(texto, (ANCHO // 2 - 400, 50))
            dibujarAtras(ventana,imgBtnAtras)

        # Texto en la pantalla
        #texto = fuente.render("Valor de xf %d" % xf, 1, ROJO)
        #ventana.blit(texto, (ANCHO // 2 - 400, 50))







        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/20

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
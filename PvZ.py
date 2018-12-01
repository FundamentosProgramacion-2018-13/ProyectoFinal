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
CAFE = (166,94,46)

global listaMarcador

listaMarcador=[0]



#estados
MENU = 1
GAME = 2
OVER = 3

QUIETO=1
ARRIBA=3
ABAJO=2
IZQ=4
DER=5


#imagen botón
imgBoton = pygame.image.load("button_jugar.png")
imgBoton2 = pygame.image.load("button_jugar.png")


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spriteRondo):
    ventana.blit(spriteRondo.img, spriteRondo.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.img, enemigo.rect)


def actualizarEnemigos(listaEnemigos):

    for enemigo in listaEnemigos:
        xe=enemigo.rect.left

        if xe == 200:
            enemigo.rect.left+=50
        if xe == 600:
            enemigo.rect.left-=50
        ye = enemigo.rect.bottom
        if ye == 200:
            enemigo.rect.bottom += 50
        if ye == 400:
            enemigo.rect.bottom -= 50

        enemigo.rect.left+=randint(-20,20)




def dibujarBasket(ventana, listaBasket):
    for balon in listaBasket:
        ventana.blit(balon.image,balon.rect)


def actualizarBasket(listaBasket,ciclo):

    for balon in listaBasket:
        balon.rect.left += 20
        if ciclo%4==0:
            listaBasket.remove(balon)




def verificarColision(listaBasket, listaEnemigos,efecto3):
    #recorrer listas al revés
    for k in range(len(listaBasket)-1,-1,-1):
        balon = listaBasket[k]
        borrarBalas = False
        for e in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[e]
            #bala vs enemigo
            xb = balon.rect.left
            yb= balon.rect.bottom
            xe,ye, anchoe, altoe = enemigo.rect
            if xb>=xe and xb<xe+anchoe and yb>=ye and yb<=ye+altoe:
                efecto3.play()
                listaEnemigos.remove(enemigo)
                borrarBalas = True
                break
        if borrarBalas:
            listaBasket.remove(balon)

def checarColisionJugador(listaEnemigos,spriteRondo,efecto2):

    rondo = spriteRondo
    borrarRondo = False
    for e in range(len(listaEnemigos)-1,-1,-1):
        enemigo = listaEnemigos[e]
        #jugador vs enemigo
        xb, yb, anchoe,altoe = rondo.rect

        xe,ye, anchoe, altoe = enemigo.rect
        if xb>=xe and xb<xe+anchoe and yb>=ye and yb<=ye+altoe:
            listaEnemigos.remove(enemigo)
            efecto2.play()
            borrarRondo = True
            break
    if borrarRondo== True:

        return True


def actualizarEnemigos2(listaEnemigos2):

    for enemigo in listaEnemigos2:
        xe = enemigo.rect.left

        if xe == 200:
            enemigo.rect.left += 50
        if xe == 600:
            enemigo.rect.left -= 50

        ye = enemigo.rect.bottom
        if ye == 200:
            enemigo.rect.bottom += 50
        if ye == 400:
            enemigo.rect.bottom -= 50

        enemigo.rect.bottom += randint(-20, 20)



def dibujar():

    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    listaJugador=[]
    imgRondo= pygame.image.load("rondo.png")

    spriteRondo= pygame.sprite.Sprite()
    spriteRondo.img = imgRondo
    spriteRondo.rect = imgRondo.get_rect()
    spriteRondo.rect.left = 0
    spriteRondo.rect.bottom = ALTO//2 + spriteRondo.rect.height//2
    listaJugador.append(spriteRondo)


    #enemigos
    listaEnemigos = []
    imgEnemigo = pygame.image.load("kobe.png")
    for k in range (randint(3,7)):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.img = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(50,ANCHO-50)
        spriteEnemigo.rect.bottom = randint(50,ALTO-50)
        listaEnemigos.append(spriteEnemigo)
    listaEnemigos2 = []
    imgEnemigo = pygame.image.load("kobe.png")
    for k in range(randint(3,7)):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.img = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(50, ANCHO-50)
        spriteEnemigo.rect.bottom = randint(50, ALTO-50)
        listaEnemigos2.append(spriteEnemigo)

    #bala
    imgBasket = pygame.image.load("basket.png")
    listaBasket = []


    #estado del juego
    ESTADO = MENU

    imgFondo = pygame.image.load("fondo.jpg")

    xFondo = 0




    #tiempo
    timer=0
    pygame.mixer.init()
    efecto =pygame.mixer.Sound("Farmacia 2000 6.wav")
    efecto2 = pygame.mixer.Sound("Wrong Buzzer - Sound Effect.wav")
    efecto3 = pygame.mixer.Sound("Farmacia 2000 7.wav")

    pygame.mixer.music.load("Space - Jam.mp3")
    pygame.mixer.music.play(-1)

    #texto
    fuente = pygame.font.SysFont("monospace",54)
    ciclo=0




    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        ciclo += 1



        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir

                termina = True      # Queremos terminar el ciclo




            if listaEnemigos==[]:
                for k in range(randint(3, 7)):
                    spriteEnemigo = pygame.sprite.Sprite()
                    spriteEnemigo.img = imgEnemigo
                    spriteEnemigo.rect = imgEnemigo.get_rect()
                    spriteEnemigo.rect.left = randint(50, ANCHO-50)
                    spriteEnemigo.rect.bottom = randint(50, ALTO-50)
                    listaEnemigos.append(spriteEnemigo)
            if listaEnemigos2==[]:
                for k in range(randint(3, 7)):
                    spriteEnemigo = pygame.sprite.Sprite()
                    spriteEnemigo.img = imgEnemigo
                    spriteEnemigo.rect = imgEnemigo.get_rect()
                    spriteEnemigo.rect.left = randint(50, ANCHO-50)
                    spriteEnemigo.rect.bottom = randint(50, ALTO-50)
                    listaEnemigos2.append(spriteEnemigo)

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    spriteRondo.rect.bottom -= 20


                elif evento.key == pygame.K_DOWN:
                    spriteRondo.rect.bottom += 20

                elif evento.key == pygame.K_LEFT:
                    spriteRondo.rect.left -= 20

                elif evento.key == pygame.K_RIGHT:
                    spriteRondo.rect.left += 20


                elif evento.key == pygame.K_z:
                    efecto.play()
                    spriteBasket= pygame.sprite.Sprite()
                    spriteBasket.image = imgBasket
                    spriteBasket.rect = imgBasket.get_rect()
                    spriteBasket.rect.left = spriteRondo.rect.left+10
                    spriteBasket.rect.bottom = spriteRondo.rect.bottom-30
                    listaBasket.append(spriteBasket)
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm,ym = pygame.mouse.get_pos()
                xb = ANCHO//2-128
                yb= ALTO//2-50
                anchob= 256
                altob=100

                if xm>=xb and xm<=xb+anchob and ym>=yb and ym<=yb+altob and ESTADO==MENU:
                    ESTADO = GAME
                    timer=0
                    spriteBasket = pygame.sprite.Sprite()
                    spriteBasket.image = imgBasket
                    spriteBasket.rect = imgBasket.get_rect()
                    spriteBasket.rect.left = spriteRondo.rect.width
                    spriteBasket.rect.bottom = spriteRondo.rect.bottom

                if xm>=xb and xm<=xb+anchob and ym>=yb and ym<=yb+altob and ESTADO==OVER:
                    ESTADO = MENU
                    timer=0
                    spriteBasket = pygame.sprite.Sprite()
                    spriteBasket.image = imgBasket
                    spriteBasket.rect = imgBasket.get_rect()
                    spriteBasket.rect.left = spriteRondo.rect.width
                    spriteBasket.rect.bottom = spriteRondo.rect.bottom






        #Preguntar estado del juego
        if ESTADO == MENU:

            ventana.fill(NEGRO)
            ventana.blit(imgBoton,(ANCHO//2-128,ALTO//2-50))

        elif ESTADO == GAME:

            #Actualizar objetos
            actualizarEnemigos2(listaEnemigos2)
            actualizarEnemigos(listaEnemigos)
            actualizarBasket(listaBasket,ciclo)
            verificarColision(listaBasket,listaEnemigos,efecto3)
            verificarColision(listaBasket, listaEnemigos2,efecto3)


            # Borrar pantalla
            ventana.fill(CAFE)
            ventana.blit(imgFondo,(xFondo,0))


            dibujarPersonaje(ventana,spriteRondo)
            dibujarEnemigos(ventana,listaEnemigos)
            dibujarEnemigos(ventana, listaEnemigos2)
            dibujarBasket(ventana,listaBasket)


            #dibujarTexto
            texto = fuente.render("Timer: %.3f"%timer,1,ROJO)
            ventana.blit(texto, (200,100))

            if checarColisionJugador(listaEnemigos,spriteRondo,efecto2)==True or checarColisionJugador(listaEnemigos2,spriteRondo,efecto2)==True:
                ESTADO=OVER

        if ESTADO == MENU:

            spriteRondo = pygame.sprite.Sprite()
            spriteRondo.img = imgRondo
            spriteRondo.rect = imgRondo.get_rect()
            spriteRondo.rect.left = 0
            spriteRondo.rect.bottom = ALTO // 2 + spriteRondo.rect.height // 2



            timer=0
            ventana.fill(NEGRO)
            ventana.blit(imgBoton,(ANCHO//2-128,ALTO//2-50))
            texto = fuente.render("HighScore: %.3fs" % (max(listaMarcador)), 1, ROJO)
            ventana.blit(texto, (200, 100))

        if ESTADO == OVER:

            listaEnemigos=[]
            listaEnemigos2=[]

            Highscore=0


            timer-=1/10


            ventana.fill(NEGRO)

            marcador=timer

            if marcador >= Highscore :
                listaMarcador.append(marcador)

            texto = fuente.render("Your Score: %.3fs" % marcador, 1, ROJO)
            ventana.blit(texto, (200, 100))
            ventana.blit(imgBoton2, (ANCHO // 2 - 128, ALTO // 2 - 50))



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(10)  # 40 fps

        timer+=1/10


    # Después del ciclo principal
    pygame.quit()  # termina pygame



# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
salida = open("HIGHSCORE.txt", "w")


main()


salida.write("Highest Score: %3f\n"% (max(listaMarcador)))
salida.close()
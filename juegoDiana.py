#Autor: Diana Marisol Medina Bravo
#Proyecto Final Juego
#A01748753
#Grupo 4

import pygame
from random import randint
#import math
#import random

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO= (0,0,0)

#Estados DE JUEGO
MENU=1
JUGANDO=2
NIVEL2=3
NIVEL3=4
GAMEOVER=5
FINNIVEL1=6
FINNIVEL2=7
FINNIVEL3=8

#Estados de movimiento
QUIETO=1
DERECHA=2
IZQUIERDA=3

# Direccion del gordito
GordoX=5
GordoY=5

def dibujarGordito(ventana,spriteGordito):
    #imagen,posición
    ventana.blit(spriteGordito.image,spriteGordito.rect)

def dibujarEntrenador(ventana, spriteEntrenador):
        ventana.blit(spriteEntrenador.image, spriteEntrenador.rect)

def dibujarZanahorias(ventana,listaZanahorias):
    for bala in listaZanahorias:
        ventana.blit(bala.image, bala.rect)

def moverGordito(spriteGordito):
    global GordoX, GordoY
    spriteGordito.rect.left = spriteGordito.rect.left + GordoX
    spriteGordito.rect.bottom = spriteGordito.rect.bottom + GordoY

    #print(spriteGordito.rect.left,spriteGordito.rect.top,spriteGordito.rect.bottom,spriteGordito.rect.right)

    if spriteGordito.rect.right >= 800 or spriteGordito.rect.left <= 0 :
        GordoX = -GordoX

    if spriteGordito.rect.bottom >= 450 or spriteGordito.rect.top <= 0:
        GordoY = -GordoY


def moverEntrenador(spriteEntrenador):
    spriteEntrenador.rect.left=1

def moverZanahorias(listaZanahorias):
    for balas in listaZanahorias:
        balas.rect.bottom -=15

def dibujarMenu(ventana, imgBtnJugar,fuente2):
    ventana.blit(imgBtnJugar,(ANCHO//2-128, ALTO//4))
    texto = fuente2.render("+Existen 3 niveles", 1, NEGRO)
    ventana.blit(texto, ((ANCHO // 2 ), 450))
    texto = fuente2.render("+Para disparar presiona «z»", 1, NEGRO)
    ventana.blit(texto, ((ANCHO // 2 ), 500))


def ponerFinNivel1(ventana,imgFinJuego,fuente,imgNivel2,imgMenu):
    ventana.blit(imgFinJuego, (0, 0))
    texto = fuente.render("SE ACABO EL TIEMPO", 1, NEGRO)
    ventana.blit(texto, ((ANCHO // 2 - 100), 50))
    ventana.blit(imgNivel2,(100, ALTO//2 -80))
    ventana.blit(imgMenu, (100, 100))

def ponerFinNivel2(ventana,imgFinJuego,fuente,imgNivel3,imgMenu):
    ventana.blit(imgFinJuego, (0, 0))
    texto = fuente.render("SE ACABO EL TIEMPO", 1, NEGRO)
    ventana.blit(texto, ((ANCHO // 2 - 100), 50))
    ventana.blit(imgNivel3, (100, ALTO // 2 -80))
    ventana.blit(imgMenu,(100,100))


def ponerFinNivel3(ventana,imgFinJuego,fuente,imgMenu):
    ventana.blit(imgFinJuego, (0, 0))
    texto = fuente.render("SE ACABO EL TIEMPO", 1, NEGRO)
    ventana.blit(texto, ((ANCHO // 2 - 100), 50))
    ventana.blit(imgMenu, (100, 100))


def verificarColision(listaZanahorias,spriteGordito,calorias):

    #Se visita cada elemento de la lista de mayor a menor
    for k in range(len(listaZanahorias)-1,-1,-1):
        bala=listaZanahorias[k]
        enemigo= spriteGordito
        #bala vs enemigo
        xb=bala.rect.left
        yb= bala.rect.bottom
        xe,ye,ae,alte=enemigo.rect

        if xb>=xe and xb<=xe+ae and yb>=ye and yb<=ye+alte:
            #Le pegó!!!
            calorias+=5
            listaZanahorias.remove(bala)
            #Termina el ciclo que recorre a los enemigos.

        return calorias

    return calorias


def verificarSiSeSale(listaZanahorias):

    for k in range(len(listaZanahorias)-1,-1,-1):
        bala=listaZanahorias[k]
        techo=0
        #bala vs techo
        xb=bala.rect.top
        #print(xb)
        #yb= bala.rect.bottom
        xe= techo
        if xb<=xe:
            #Se salió!!!
            #Termina el ciclo que recorre a los enemigos.
            return 0

def verPuntajeMasAlto(calorias,archivo):
    entrada = open(archivo, "r")

    highScore = 0
    for linea in entrada:
        a = int(linea)
        if a <= calorias:
            highScore = calorias
        else:
            highScore = a
    entrada.close()

    salida = open(archivo, "w")
    salida.write("%s\n" % (highScore))
    salida.close()

    return highScore

def ponerGameOver(ventana,fuente,imgMenu):
    texto = fuente.render("GAME OVER", 1, ROJO)
    ventana.blit(texto, ((ANCHO // 2 - 100), 50))
    ventana.blit(imgMenu, (100, 100))

# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    myfont = pygame.font.SysFont("monospace", 25)

    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #Personaje
    imgGordito=pygame.image.load("gordito.png")
    spriteGordito=pygame.sprite.Sprite()
    spriteGordito.image=imgGordito
    spriteGordito.rect=imgGordito.get_rect()
    spriteGordito.rect.left=randint(0,ANCHO-150)
    spriteGordito.rect.bottom= randint(125,ALTO-450)

    #Enemigo
    imgEntrenador=pygame.image.load("Entrenador.png")
    spriteEntrenador=pygame.sprite.Sprite()
    spriteEntrenador.image=imgEntrenador
    spriteEntrenador.rect=imgEntrenador.get_rect()
    spriteEntrenador.rect.left=0
    spriteEntrenador.rect.bottom= ANCHO//2 + spriteEntrenador.rect.width*2

    #Balas Zanahorias
    listaZanahorias=[]
    imgBala= pygame.image.load("zanahoria.png")

    #Menú
    imgFondo1=pygame.image.load("fondo1.jpg")
    imgBtnJugar=pygame.image.load("btnJugar.png")
    imgNivel2=pygame.image.load("button.png")
    imgNivel3=pygame.image.load("button (1).png")
    imgMenu=pygame.image.load("button (2).png")

    #Fondo
    imgFondo=pygame.image.load("parque..png")

    #Fondo Fin del juego
    imgFinJuego=pygame.image.load("finJuego.png")

    estado=MENU

    timer=0

    #velocidad=0

    # Texto
    fuente = pygame.font.SysFont("monospace", 64)
    fuente2=pygame.font.SysFont("monospace", 30)

    xFONDO=0

    calorias=0

    moviendo=QUIETO

    # Audio
    pygame.mixer.init()
    #musicaFondo=pygame.mixer.music.load("Bouncey.mp3")
    #musicaFondo = pygame.mixer.music.load("Emotional_Aftermath.mp3")
    musicaFondo = pygame.mixer.music.load("CancionGameDiana.mp3")
    efecto = pygame.mixer.Sound("shoot.wav")


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            #oprimir tecla, tipo de evento
            elif evento.type==pygame.KEYDOWN:
                #se pregunta ya la tecla
                if evento.key==pygame.K_LEFT:
                    #spritePersonaje.rect.bottom-=5
                    moviendo=IZQUIERDA

                elif evento.key==pygame.K_RIGHT:
                    #spritePersonaje.rect.bottom +=5
                    moviendo=DERECHA
                elif evento.key== pygame.K_z:
                    #Crear una bala
                    spriteZanahorias= pygame.sprite.Sprite()
                    spriteZanahorias.image=imgBala
                    spriteZanahorias.rect=imgBala.get_rect()
                    pygame.mixer.Sound.play(efecto)
                    #x de baja      coordenada personaje+ alto del personaje
                    spriteZanahorias.rect.left=spriteEntrenador.rect.left + spriteEntrenador.rect.width/2
                    #y de bala
                    spriteZanahorias.rect.bottom=spriteEntrenador.rect.bottom
                    listaZanahorias.append(spriteZanahorias)
            #No importa que tecla
            #elif evento.type==pygame.KEYUP:
             #   moviendo=QUIETO
            #elif evento.type==pygame.MOUSEBUTTONUP:
                #get_pos regresa una dupla, por eso se pueden poner dos variable
             #   xm,ym= pygame.mouse.get_pos()
              #  print(xm,",",ym)
                #Preguntar si soltó el mouse dentro del boton
               # xb=ANCHO//2-128
                #yb=ALTO//3
                #if pygame.mouse.get_pressed():
                 #   if xm>=xb and xm<=xb+256 and ym>=yb and ym<=yb+100:
                  #      estado= JUGANDO
                   #     timer=0


        # Borrar pantalla
        #ventana.fill(NEGRO)

        if estado == JUGANDO:
            xFONDO=0


            if timer>=90:
                estado=FINNIVEL1
                pygame.mixer.music.stop()
            #print(timer)

            #Mover personaje
            if moviendo==IZQUIERDA:
                spriteEntrenador.rect.left -=10
                if spriteEntrenador.rect.left<=0:
                    spriteEntrenador.rect.left+=10
            elif moviendo==DERECHA:
                spriteEntrenador.rect.left +=10
                if spriteEntrenador.rect.right>=800:
                    spriteEntrenador.rect.left-=10
            #Actualizar enemigos
            moverZanahorias(listaZanahorias)


            moverGordito(spriteGordito)

            calorias = verificarColision(listaZanahorias,spriteGordito,calorias)

            if verificarSiSeSale(listaZanahorias) == 0:
                listaZanahorias=[]
                estado=GAMEOVER

            ventana.blit(imgFondo,(xFONDO,0))
            xFONDO-=1
            dibujarGordito(ventana,spriteGordito)
            #moverGordito(spriteGordito)
            dibujarEntrenador(ventana, spriteEntrenador)
            dibujarZanahorias(ventana,listaZanahorias)
            verPuntajeMasAlto(calorias,"score.txt")

            tiempo = myfont.render("Time: {:02f}".format(timer), 1, (NEGRO))
            ventana.blit(tiempo, (650, 50))
            puntaje = myfont.render("Calorias: {:d}".format(calorias), 1, (NEGRO))
            ventana.blit(puntaje, (650, 100))
            nivel = fuente2.render("Nivel 1", 1, NEGRO)
            ventana.blit(nivel, (20, 20))

        elif estado==NIVEL2:
            xFONDO=0
            if timer>=60:
                estado=FINNIVEL2
                pygame.mixer.music.stop()
            #print(timer)

            #Mover personaje
            if moviendo==IZQUIERDA:
                spriteEntrenador.rect.left -=10
                if spriteEntrenador.rect.left<=0:
                    spriteEntrenador.rect.left+=10
            elif moviendo==DERECHA:
                spriteEntrenador.rect.left +=10
                if spriteEntrenador.rect.right>=800:
                    spriteEntrenador.rect.left-=10

            #Actualizar enemigos
            moverZanahorias(listaZanahorias)


            moverGordito(spriteGordito)
            calorias = verificarColision(listaZanahorias, spriteGordito, calorias)

            if verificarSiSeSale(listaZanahorias)== 0:
                listaZanahorias=[]
                estado=GAMEOVER

            ventana.blit(imgFondo,(xFONDO,0))
            xFONDO-=1
            dibujarGordito(ventana,spriteGordito)
            #moverGordito(spriteGordito)
            dibujarEntrenador(ventana, spriteEntrenador)
            dibujarZanahorias(ventana,listaZanahorias)
            verPuntajeMasAlto(calorias, "score.txt")

            tiempo = myfont.render("Time: {:02f}".format(timer), 1, (NEGRO))
            ventana.blit(tiempo, (650, 50))
            puntaje = myfont.render("Calorias: {:d}".format(calorias), 1, (NEGRO))
            ventana.blit(puntaje, (650, 100))
            nivel = fuente2.render("Nivel 2", 1, NEGRO)
            ventana.blit(nivel, (20, 20))


        elif estado==NIVEL3:
            xFONDO = 0
            if timer >= 30:
                estado = FINNIVEL3
                pygame.mixer.music.stop()
            #print(timer)

            # Mover personaje
            if moviendo == IZQUIERDA:
                spriteEntrenador.rect.left -= 10
                if spriteEntrenador.rect.left <= 0:
                    spriteEntrenador.rect.left += 10
            elif moviendo == DERECHA:
                spriteEntrenador.rect.left += 10
                if spriteEntrenador.rect.right >= 800:
                    spriteEntrenador.rect.left -= 10

            # Actualizar enemigos
            moverZanahorias(listaZanahorias)

            moverGordito(spriteGordito)
            calorias = verificarColision(listaZanahorias, spriteGordito, calorias)

            if verificarSiSeSale(listaZanahorias) == 0:
                listaZanahorias = []
                estado = GAMEOVER

            ventana.blit(imgFondo, (xFONDO, 0))
            xFONDO -= 1
            dibujarGordito(ventana, spriteGordito)
            # moverGordito(spriteGordito)
            dibujarEntrenador(ventana, spriteEntrenador)
            dibujarZanahorias(ventana, listaZanahorias)
            verPuntajeMasAlto(calorias, "score.txt")

            tiempo = myfont.render("Time: {:02f}".format(timer), 1, (NEGRO))
            ventana.blit(tiempo, (650, 50))
            puntaje = myfont.render("Calorias: {:d}".format(calorias), 1, (NEGRO))
            ventana.blit(puntaje, (650, 100))
            nivel = fuente2.render("Nivel 3", 1, NEGRO)
            ventana.blit(nivel, (20, 20))



        elif estado==MENU:
            #Dibujar MENU
            ventana.blit(imgFondo1,(0,0))
            dibujarMenu(ventana, imgBtnJugar,fuente2)
            cal=verPuntajeMasAlto(calorias,"score.txt")
            puntaje = myfont.render("HIGHEST SCORE: {:d}".format(cal), 1, (NEGRO))
            ventana.blit(puntaje,(400, 250))
            #puntaje = myfont.render("Calorias: {:d}".format(cal), 1, (NEGRO))
            if evento.type==pygame.MOUSEBUTTONUP:
                #get_pos regresa una dupla, por eso se pueden poner dos variable
                xm,ym= pygame.mouse.get_pos()
                #print(xm,",",ym)
                #Preguntar si soltó el mouse dentro del boton
                xb=ANCHO//2-128
                yb=ALTO//4
                if pygame.mouse.get_pressed():
                    if xm>=xb and xm<=xb+256 and ym>=yb and ym<=yb+100:
                        estado= JUGANDO
                        pygame.mixer.music.play(1)
                        timer=0
                        calorias=0

        elif estado==FINNIVEL1:
            #ventana.blit(imgFinJuego, (0, 0))
            #xFONDO -= 0
            ponerFinNivel1(ventana, imgFinJuego, fuente,imgNivel2,imgMenu)
            cal = verPuntajeMasAlto(calorias, "score.txt")
            puntaje = myfont.render("HIGHEST SCORE: {:d}".format(cal), 1, (BLANCO))
            ventana.blit(puntaje, (500, 100))
            calorias = verificarColision(listaZanahorias, spriteGordito, calorias)
            puntajeCal = myfont.render("CALORIAS: {:d}".format(calorias), 1, (BLANCO))
            ventana.blit(puntajeCal, (500, 150))
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                #print(xm, ",", ym)
                # Preguntar si soltó el mouse dentro del boton
                xb = 100
                yb = ALTO // 2 -80
                xmenu=100
                ymenu=100
                if pygame.mouse.get_pressed():
                    if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                        timer = 0
                        calorias=0
                        estado = NIVEL2
                        pygame.mixer.music.play(1)
                    if xm >= xmenu and xm <= xmenu + 256 and ym >= ymenu and ym <= ymenu + 100:
                        estado = MENU
                        timer = 0
                        calorias=0


        elif estado==FINNIVEL2:
            ponerFinNivel2(ventana,imgFinJuego,fuente,imgNivel3,imgMenu)
            cal = verPuntajeMasAlto(calorias, "score.txt")
            puntaje = myfont.render("HIGHEST SCORE: {:d}".format(cal), 1, (BLANCO))
            ventana.blit(puntaje, (500, 100))
            calorias = verificarColision(listaZanahorias, spriteGordito, calorias)
            puntajeCal = myfont.render("CALORIAS: {:d}".format(calorias), 1, (BLANCO))
            ventana.blit(puntajeCal, (500, 150))
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                #print(xm, ",", ym)
                # Preguntar si soltó el mouse dentro del boton
                xb = 100
                yb = ALTO // 2 -80
                xmenu = 100
                ymenu = 100
                if pygame.mouse.get_pressed():
                    if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                        estado = NIVEL3
                        pygame.mixer.music.play(1)
                        calorias=0
                        timer = 0
                    if xm >= xmenu and xm <= xmenu + 256 and ym >= ymenu and ym <= ymenu + 100:
                        estado = MENU
                        timer = 0
                        calorias=0



        elif estado==FINNIVEL3:
            ponerFinNivel3(ventana, imgFinJuego, fuente, imgMenu)
            cal = verPuntajeMasAlto(calorias, "score.txt")
            puntaje = myfont.render("HIGHEST SCORE: {:d}".format(cal), 1, (BLANCO))
            ventana.blit(puntaje, (500, 100))
            calorias = verificarColision(listaZanahorias, spriteGordito, calorias)
            puntajeCal = myfont.render("CALORIAS: {:d}".format(calorias), 1, (BLANCO))
            ventana.blit(puntajeCal, (500, 150))
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                #print(xm, ",", ym)
                # Preguntar si soltó el mouse dentro del boton
                xb = 100
                yb = 100
                if pygame.mouse.get_pressed():
                    if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                        estado = MENU
                        timer = 0
                        calorias=0


        elif estado==GAMEOVER:
            pygame.mixer.music.stop()
            ventana.fill(NEGRO)
            ponerGameOver(ventana,fuente,imgMenu)
            cal=verPuntajeMasAlto(calorias, "score.txt")
            puntaje = myfont.render("HIGHEST SCORE: {:d}".format(cal), 1, (BLANCO))
            ventana.blit(puntaje, (500, 100))
            calorias = verificarColision(listaZanahorias, spriteGordito, calorias)
            puntajeCal=myfont.render("CALORIAS: {:d}".format(calorias), 1, (BLANCO))
            ventana.blit(puntajeCal, (500, 150))
            if evento.type == pygame.MOUSEBUTTONUP:
                pygame.event.clear()
                xm, ym = pygame.mouse.get_pos()
                #print(xm, ",", ym)
                # Preguntar si soltó el mouse dentro del boton
                xb = 100
                yb = 100
                if pygame.mouse.get_pressed():
                    if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                        estado = MENU
                        timer = 0
                        calorias=0


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer += 1/40


    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Solo dibuja
    print("""Proyecto Final
Diana Marisol Medina Bravo
A01748753
Grupo 04""")


# Llamas a la función principal
main()
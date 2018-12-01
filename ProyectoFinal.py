# encoding: UTF-8
# Autor: Luis Armando Miranda Alcocer
# Juego

import math
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
POSTJUEGO=3

#Estados de Movimiento
QUIETO = 1
DERECHA = 2
IZQUIERDA = 3



# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePlato):
    ventana.blit(spritePlato.image, spritePlato.rect)

def dibujarVidas(ventana, spriteVida3, spriteVida2, spriteVida1, spriteVida0, VIDASTotal):
    if VIDASTotal==3:
        ventana.blit(spriteVida3.image, spriteVida3.rect)
    elif VIDASTotal==2:
        ventana.blit(spriteVida2.image, spriteVida2.rect)
    elif VIDASTotal==1:
        ventana.blit(spriteVida1.image,spriteVida1.rect)
    elif VIDASTotal==0:
        ventana.blit(spriteVida0.image, spriteVida0.rect)



def dibujarEsferas1(ventana, listaEsferas1):
    for esfera1 in listaEsferas1:
        ventana.blit(esfera1.image, esfera1.rect)


def actualizarEsferas1(listaEsferas1):
    for esfera1 in listaEsferas1:   # VISITA cada esfera1
        esfera1.rect.bottom += 3

def dibujarEsferas5(ventana, listaEsferas5):
    for esfera5 in listaEsferas5:
        ventana.blit(esfera5.image, esfera5.rect)

def actualizarEsferas5(listaEsferas5):
    for esfera5 in listaEsferas5:   # VISITA cada esfera5
        esfera5.rect.bottom += 3

def dibujarEsferasm5(ventana, listaEsferasm5):
    for esferam5 in listaEsferasm5:
        ventana.blit(esferam5.image, esferam5.rect)

def actualizarEsferasm5(listaEsferasm5):
    for esferam5 in listaEsferasm5:   # VISITA cada esferam5
        esferam5.rect.bottom += 3


def verificarColisiones(spritePlato, listaEsferas1, PUNTOS):
    # recorre las listas al revés
    a=0 #Acumulador puntos 1
    for k in range(len(listaEsferas1)-1,-1,-1):
        esfera1 = listaEsferas1[k]
        borrarEsfera1 = False
        xp = esfera1.rect.left
        yp = esfera1.rect.bottom
        xe, ye, anchoe, altoe = spritePlato.rect
        if xp>=xe and xp<=xe+anchoe and yp>=ye and yp<=ye+altoe:
            listaEsferas1.remove(esfera1)   # borra de la lista
            borrarEsfera1 = True
            a += 1
            break
    return a+PUNTOS


def verificarColisiones5(spritePlato, listaEsferas5,PUNTOS5):
    # recorre las listas al revés
    a=0
    for k in range(len(listaEsferas5)-1,-1,-1):
        esfera5 = listaEsferas5[k]
        borrarEsfera5 = False
        xp = esfera5.rect.left
        yp = esfera5.rect.bottom
        xe, ye, anchoe, altoe = spritePlato.rect
        if xp>=xe and xp<=xe+anchoe and yp>=ye and yp<=ye+altoe:
            listaEsferas5.remove(esfera5)   # borra de la lista
            borrarEsfera5 = True
            a += 5
            break
    return a + PUNTOS5


def verificarColisionesm5(spritePlato, listaEsferasm5,PUNTOSm5):
    # recorre las listas al revés
    a=0
    for k in range(len(listaEsferasm5)-1,-1,-1):
        esferam5 = listaEsferasm5[k]
        borrarEsferam5 = False
        xp = esferam5.rect.left
        yp = esferam5.rect.bottom
        xe, ye, anchoe, altoe = spritePlato.rect
        if xp>=xe and xp<=xe+anchoe and yp>=ye and yp<=ye+altoe:
            listaEsferasm5.remove(esferam5)   # borra de la lista
            borrarEsferam5 = True
            a -= 5
            break
    return a + PUNTOSm5

def verificarCaida1(listaEsferas1, VIDAS1):
    # recorre las listas al revés
    a=0 #Acumulador puntos 1
    for k in range(len(listaEsferas1)-1,-1,-1):
        esfera1 = listaEsferas1[k]
        borrarEsfera1 = False
        yp = esfera1.rect.bottom
        ye = ALTO
        if yp >= ye:
            listaEsferas1.remove(esfera1)   # borra de la lista
            borrarEsfera1 = True
            a -= 1
            break
    return a+VIDAS1


def verificarCaida5(listaEsferas5, VIDAS5):
    # recorre las listas al revés
    a=0 #Acumulador vidas5
    for k in range(len(listaEsferas5)-1,-1,-1):
        esfera5 = listaEsferas5[k]
        yp = esfera5.rect.bottom
        ye = ALTO
        if  yp >= ye:
            listaEsferas5.remove(esfera5)   # borra de la lista
            a -= 1
            break
    return a+VIDAS5

def archivo(PUNTOStotales, nombre):
    lista=[]
    salida = open("Resultados.txt", "w")  # Abrir un archivo de texto con los resultados. w es para escribir
    #print("%s,%.2d" % (nombre, PUNTOStotales))
    salida.write("Resultados\n")
    salida.write("%s,%d\n" % (nombre, PUNTOStotales))  # \n es para que coloque en el archivo por renglones

    salida.close()  # Cerrar archivo

def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # DATOS
    PUNTOS = 0
    PUNTOS5 = 0
    PUNTOSm5=0
    VIDAS1=0
    VIDAS5=0

    # personaje principal
    imgPlato = pygame.image.load("Plato.png")
    spritePlato = pygame.sprite.Sprite()  # sprite vacío
    spritePlato.image = imgPlato
    spritePlato.rect = imgPlato.get_rect()
    spritePlato.rect.left = ANCHO//2 - spritePlato.rect.width//2
    spritePlato.rect.bottom = ALTO - 10- spritePlato.rect.width//2

    movimiento = QUIETO

    # Esferas1
    listaEsferas1 = []  # Lista vacía de esferas1
    imgEsferas1 = pygame.image.load("Esfera1.jpg")

    # Esferas5
    listaEsferas5 = []  # Lista vacía de esferas5
    imgEsferas5 = pygame.image.load("Esfera5.jpg")

    # Esferasm5
    listaEsferasm5 = []  # Lista vacía de esferasm5
    imgEsferasm5 = pygame.image.load("Esferam5.jpg")
    #Vidas
    imgVida3= pygame.image.load("Vidas3.jpg")
    spriteVida3=pygame.sprite.Sprite()
    spriteVida3.image=imgVida3
    spriteVida3.rect = imgVida3.get_rect()
    spriteVida3.rect.left = ANCHO -95
    spriteVida3.rect.bottom = 28

    imgVida2 = pygame.image.load("Vidas2.jpg")
    spriteVida2 = pygame.sprite.Sprite()
    spriteVida2.image = imgVida2
    spriteVida2.rect = imgVida2.get_rect()
    spriteVida2.rect.left = ANCHO -95
    spriteVida2.rect.bottom = 28

    imgVida1 = pygame.image.load("Vidas1.jpg")
    spriteVida1 = pygame.sprite.Sprite()
    spriteVida1.image = imgVida1
    spriteVida1.rect = imgVida1.get_rect()
    spriteVida1.rect.left = ANCHO -95
    spriteVida1.rect.bottom = 28

    imgVida0 = pygame.image.load("Vidas0.jpg")
    spriteVida0 = pygame.sprite.Sprite()
    spriteVida0.image = imgVida0
    spriteVida0.rect = imgVida0.get_rect()
    spriteVida0.rect.left = ANCHO -95
    spriteVida0.rect.bottom = 28

    # Estado del juego
    estado = MENU       # Inicial

    # Imágenes para el menú
    imgBtnJugar = pygame.image.load("btnJugar.png")

    # Imágenes para el juego
    imgFondo = pygame.image.load("FondoJuego.png")
    xFondo = 0

    # TIEMPO
    time=0
    timer = 0  #Acumulador de tiempo
    timel= 0 #Acumulador de tiempo 2
    timep=0


    # Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("shoot.wav")
    pygame.mixer.music.load("Essence.mp3")
    pygame.mixer.music.play(-1) #-1 para reproducción infninita

    # TEXTO
    fuente = pygame.font.SysFont("monospace", 54)  #Tamaño 54
    alfa = 0


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente   ############################################
        # Procesa los eventos que recibe

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type==pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    #spritePlato.rect.left -= 5
                    movimiento=IZQUIERDA
                elif evento.key == pygame.K_RIGHT:
                    #spritePlato.rect.right += 5
                    movimiento= DERECHA
            elif evento.type == pygame.MOUSEBUTTONDOWN: #Para presionar botón, y empezar a jugar
                xm, ym = pygame.mouse.get_pos()
                xb = ANCHO//2-64
                yb= ALTO//2-25
                anchoB= 128 #Valores del botón
                altoB= 50 #Valores del botón
                if xm>=xb and xm <=xb+anchoB and ym>=yb and ym <= yb+altoB:
                    estado = JUGANDO


        #Pregunta en qué estado está el juego
        if estado ==MENU:
            #  Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgBtnJugar,(ANCHO//2-64, ALTO//2-25))  #x,y
            fuente = pygame.font.Font(None, 30)
            anuncioMenu = fuente.render("Puedes moverte con las teclas derecha e izquierda", 1, AZUL)
            anuncioMenu2= fuente.render("Atrapa todos las esferas positivas para juntar puntos y pasar el semestre",1,AZUL)
            anuncioMenu3= fuente.render("¡Cuidado! Dejar caer esferas o atrapar puntos negativos te quitarán vidas",1,AZUL)
            anuncioMenu4= fuente.render("Sólo tienes 3 vidas/parciales para pasar",1,AZUL)
            ventana.blit(anuncioMenu, (50, 50))
            ventana.blit(anuncioMenu2, (50,80))
            ventana.blit(anuncioMenu3, (50, 110))
            ventana.blit(anuncioMenu4, (50,140))


        elif estado== JUGANDO:
            #Actualizar objetos
            actualizarEsferas1(listaEsferas1)
            actualizarEsferas5(listaEsferas5)
            actualizarEsferasm5(listaEsferasm5)
            alfa += 5
            PUNTOS= verificarColisiones(spritePlato, listaEsferas1, PUNTOS)
            PUNTOS5= verificarColisiones5(spritePlato, listaEsferas5, PUNTOS5)
            PUNTOSm5= verificarColisionesm5(spritePlato, listaEsferasm5, PUNTOSm5)
            VIDAS1= verificarCaida1(listaEsferas1, VIDAS1)
            VIDAS5= verificarCaida5(listaEsferas5, VIDAS5)
            VIDAS = VIDAS1 + VIDAS5
            VIDASTotal= 3+VIDAS
            #print(VIDASTotal)
            PUNTOStotales= PUNTOS+PUNTOS5+PUNTOSm5
            if PUNTOStotales < 0:
                estado = POSTJUEGO
                negativos = fuente.render("Llegaste a puntos negativos, perdiste", 1, ROJO)
                ventana.blit(negativos, (20, 20))
            if VIDASTotal == 0:
                estado = POSTJUEGO
            if PUNTOStotales>=100:
                PUNTOStotales=100
                estado= POSTJUEGO



            ventana.blit(spritePlato.image, spritePlato.rect)
            if timer >=8:
                timer = 0
                for k in range(1):
                    spriteEsfera1 = pygame.sprite.Sprite()
                    spriteEsfera1.image = imgEsferas1
                    spriteEsfera1.rect = imgEsferas1.get_rect()
                    spriteEsfera1.rect.left = randint(200, ANCHO - 200)
                    spriteEsfera1.rect.bottom = randint(-50, 50)
                    listaEsferas1.append(spriteEsfera1)
            if timel >=27:
                for k in range(1):
                    spriteEsfera5 = pygame.sprite.Sprite()
                    spriteEsfera5.image = imgEsferas5
                    spriteEsfera5.rect = imgEsferas5.get_rect()
                    spriteEsfera5.rect.left = randint(200, ANCHO - 200)
                    spriteEsfera5.rect.bottom = randint(-50, 50)
                    listaEsferas5.append(spriteEsfera5)
                    timel = 0
                    timer=0

            if timep >= 15:
                for k in range(2):
                    spriteEsferam5 = pygame.sprite.Sprite()
                    spriteEsferam5.image = imgEsferasm5
                    spriteEsferam5.rect = imgEsferasm5.get_rect()
                    spriteEsferam5.rect.left = randint(200, ANCHO - 200)
                    spriteEsferam5.rect.bottom = randint(-50, 50)
                    listaEsferasm5.append(spriteEsferam5)
                    timep=0


            #Mover personaje
            if movimiento == DERECHA:
                spritePlato.rect.left += 8
                if spritePlato.rect.left >= 740:
                    spritePlato.rect.left -= 8
            elif movimiento == IZQUIERDA:
                spritePlato.rect.left -= 8
                if spritePlato.rect.left <= 0:
                    spritePlato.rect.left += 8

            #  Borrar pantalla
            ventana.fill(NEGRO)
            ventana.blit(imgFondo, (xFondo,0))
            ventana.blit(imgFondo, (xFondo+ 800,0)) #800 es el áncho de la imágen


            #Dibujar,
            dibujarPersonaje(ventana, spritePlato)
            dibujarEsferas1(ventana, listaEsferas1)
            dibujarEsferas5(ventana, listaEsferas5)
            dibujarEsferasm5(ventana, listaEsferasm5)
            dibujarVidas(ventana, spriteVida3,spriteVida2, spriteVida1, spriteVida0, VIDASTotal)


            #Dibujar texto
            texto= fuente.render("Tiempo: %.3f"%time, 1, ROJO)
            ventana.blit(texto, (20,20))
            puntuaje= fuente.render("Puntuaje: %d"%PUNTOStotales,1, ROJO)
            ventana.blit(puntuaje, (20,50))


        elif estado== POSTJUEGO:
            ventana.fill(NEGRO)
            #Texto final
            fin=fuente.render("GAME OVER",3,ROJO)
            ventana.blit(fin,(350,100))
            puntuacion= fuente.render("Tu puntuación fue: %d"%PUNTOStotales,1,ROJO)
            ventana.blit(puntuacion, (300, 150))
            #nombre = input("Teclea tu nombre para guardar tu información: ")
            nombre=("nombre")
            archivo(PUNTOStotales, nombre)
            if VIDASTotal==0 and PUNTOStotales<70:
                text= fuente.render("¡Ups! No has podido pasar el semestre",1,ROJO)
                ventana.blit(text, (150, 200))
            elif VIDASTotal==0 and PUNTOStotales>=70 and PUNTOStotales<=99:
                text= fuente.render("Has logrado pasar el semestre",1,ROJO)
                ventana.blit(text, (200, 200))
            elif VIDASTotal==0 and PUNTOStotales==100 or PUNTOStotales==100:
                text=fuente.render("¡Felicidades! Eres el campeón del juego",1,ROJO)
                ventana.blit(text, (200, 200))
            elif PUNTOStotales<0:
                text= fuente.render("¡Oh no! Tus puntos han llegado a números negativos", 1, ROJO)
                ventana.blit(text, (150,200))


            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_KP_ENTER:
                        VIDASTotal=3
                        PUNTOStotales=0
                        PUNTOS = 0
                        PUNTOS5 = 0
                        PUNTOSm5 = 0
                        VIDAS1 = 0
                        VIDAS5 = 0
                        estado = MENU


        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        time += 1/40
        timer += 1/14
        timel += 1/10
        timep += 1/8


    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
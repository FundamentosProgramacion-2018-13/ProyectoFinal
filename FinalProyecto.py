# encoding: UTF-8
# Autor: Damián Iván García Ravelo
# Eco-Car: Un carro vs basura
#Las imágenes mostradas ni los sonidos mostrados no son de mi propiedad, son usadas con fines de entretenimiento. Si necesitas
# la imágen con gusto comparto las páginas de donde fueron tomadas

#Librerias a importar
import pygame   # Librería de pygame
from random import randint #Librerias

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
NEGRO= (0,0,0)
ROJO = (255, 0, 0)

#ESTADOS del juego
MENU = 1
INFORMACION = 2
JUGANDO = 3
JUGANDO2 = 4
PUNTAJES = 5
PERDISTEINTERMEDIO = 6
PERDISTEAVANZADO= 7

#Estados de movimiento
QUIETO = 1

def dibujarFondo(ventana, background): #dibujar pantalla mientrtas se esta jugando
    ventana.blit(background,(0,0))

# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image,spritePersonaje.rect)

def dibujarEnemigos(ventana, listaEnemigos): #Dibujo de la basura
    #VISITAR a cada elemento
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image,enemigo.rect)

def dibujarEnemigosP(ventana,listaPilas): #Dibujo de las pilas
    #VISITAR a cada elemento
    for enemigoPoderoso in listaPilas:
        ventana.blit(enemigoPoderoso.image,enemigoPoderoso.rect)

def moverEnemigos(listaEnemigos): #Movimiento de los enemigos
    for enemigo in listaEnemigos:
        enemigo.rect.bottom+=1

def moverEnemigosP(listaPilas): #Movimiento de los enemigos
    for enemigoPoderoso in listaPilas:
        enemigoPoderoso.rect.bottom+=2

def dibujarBalas(ventana, listaBalas): #Dibujo de las balas
    for bala in listaBalas:
        ventana.blit(bala.image,bala.rect)

def moverBalas(listaBalas): #Movimiento de las balas
    for bala in listaBalas:
        bala.rect.y -= 3

def dibujarMenu(ventana, imgAvanzado, imgIntermedio, imgInformacion, imgPuntaje): #Dibujo del menú de inicio
    ventana.blit(imgInformacion,(274,198))
    ventana.blit(imgIntermedio,(272,66))
    ventana.blit(imgAvanzado,(292,330))
    ventana.blit(imgPuntaje,(299,462))

def verificarColision(listaEnemigos, listaBalas): #Bala vs Enemigo
    pygame.mixer.init()
    efectoColision = pygame.mixer.Sound("pum.wav")  # archivos cortos
    for k in range (len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        for e in range (len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[e]
            #bala vs enemigo
            xb=bala.rect.left
            yb=bala.rect.bottom
            wb=bala.rect.width
            hb=bala.rect.height

            xe=enemigo.rect.left
            ye=enemigo.rect.bottom
            we=enemigo.rect.width

            if xb+wb>=xe and xb<=xe+we and yb<=ye+35:
                #Le pego
                efectoColision.set_volume(0.5)
                efectoColision.play()
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                break

def verificarColisionP(listaBalas, listaPilas): #bala vs enemigo
    pygame.mixer.init()
    efectoColision = pygame.mixer.Sound("pum.wav")
  # archivos cortos
    for k in range (len(listaBalas)-1, -1, -1):
        bala = listaBalas[k]
        for e in range (len(listaPilas)-1,-1,-1):
            enemigo = listaPilas[e]
            #bala vs enemigo
            xb=bala.rect.left
            yb=bala.rect.bottom
            wb=bala.rect.width
            hb=bala.rect.height

            xe=enemigo.rect.left
            ye=enemigo.rect.bottom
            we=enemigo.rect.width

            if (xb+wb>=xe and xb<=xe+we and yb>=ye and yb<=ye+60):
                efectoColision.set_volume(0.5)
                efectoColision.play()
                listaPilas.remove(enemigo)
                listaBalas.remove(bala)
                break

def verificarColisionSuelo(listaPilas): #pila vs suelo
    for e in range (len(listaPilas)-1,-1,-1):
        enemigo = listaPilas[e]
        #bala vs enemigo

        ye=enemigo.rect.bottom

        if (ye>=ALTO):
            listaPilas.remove(enemigo)
            return True


def verificarColisionSueloE(listaEnemigos): #basura vs suelo
    for e in range (len(listaEnemigos)-1,-1,-1):
        enemigo = listaEnemigos[e]
        #bala vs enemigo

        ye=enemigo.rect.bottom

        if (ye>=ALTO):
            listaEnemigos.remove(enemigo)
            return True


def dibujar(): #funcion para dibujar en la pantalla
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    background = pygame.image.load("background.jpg") #pone el background




#Personaje
    imgPersonaje = pygame.image.load("carrito.png")
    spritePersonaje=pygame.sprite.Sprite()
    spritePersonaje.image= imgPersonaje
    spritePersonaje.rect=imgPersonaje.get_rect()
    spritePersonaje.rect.left=ANCHO//2 + spritePersonaje.rect.width//2
    spritePersonaje.rect.bottom= ALTO


#Enemigos
    listaEnemigos=[]
    imgEnemigo=pygame.image.load("boteBasura.png")
    for k in range(25): #5 enemigos generados
        spriteEnemigo=pygame.sprite.Sprite()
        spriteEnemigo.image=imgEnemigo
        spriteEnemigo.rect=imgEnemigo.get_rect()
        spriteEnemigo.rect.bottom=randint(0,0)
        spriteEnemigo.rect.left=randint(70,ANCHO-80-spriteEnemigo.rect.width)
        listaEnemigos.append(spriteEnemigo)

    listaPilas=[]
    imgPila= pygame.image.load("pila.png")
    for k in range(1):
        spritePila=pygame.sprite.Sprite()
        spritePila.image=imgPila
        spritePila.rect=imgPila.get_rect()
        spritePila.rect.left=randint(70,ANCHO-80-spritePila.rect.width)
        spritePila.rect.bottom=randint(0,0)
        listaPilas.append(spritePila)

#Balas
    listaBalas=[]
    imgBala=pygame.image.load("bala.png")

#VIDA
    vida=pygame.image.load("corazon.png")
    sinvida=pygame.image.load("sinvida.png")

#Estado principal es el menu
    estado = MENU

    yf=0 #y DEL FONDO

    #MENU
    imgInformacion = pygame.image.load("informacion.png")
    imgIntermedio = pygame.image.load("intermedio.png")
    imgPuntaje = pygame.image.load("puntajes.png")
    imgAvanzado = pygame.image.load("avanzado.png")
    imgRegresar = pygame.image.load("regresar.png")
    imgCreditos = pygame.image.load("paginaInformacion.png")
    imgScore= pygame.image.load("score.png")
    derrota = pygame.image.load("derrota.png")
    estado = MENU

    #Fondo
    imgFondo = pygame.image.load("FondoJuego.jpg")

    moviendo = QUIETO

    #Acumuladores de tiempo
    timer=0
    enemigoBasura=0
    enemigoPila=0
    tiempoSobrevividoIntermedio=0
    tiempoSobrevividoAvanzado=0

    #texto
    fuente = pygame.font.SysFont("comicsansms",20)
    fuente.set_bold(True)
    #audio
    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.load("musicaFondo.mp3") #musica larga, desde el menú
    pygame.mixer.music.play(-1) #-1 para que se quede en un loop infinito


    efecto = pygame.mixer.Sound("shoot.wav") #archivos cortos

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type==pygame.KEYDOWN:
                if spritePersonaje.rect.left>=70:
                    if evento.key==pygame.K_a:
                        spritePersonaje.rect.left-= 35 #cada tecleo se mueve arriba=pygame.K_RIGHT:
                if spritePersonaje.rect.left + spritePersonaje.rect.width <= ANCHO-80:
                    if evento.key==pygame.K_d:
                        spritePersonaje.rect.left+=35 #cada tecleo se mueve abajo
                #elif evento.type == pygame.K_SPACE:
                    #moviendo= QUIETO
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm,",",ym)
                #Preguntar si spltó el mouse dentro del botón
                xb = 272
                yb= 198
                if xm>=xb and xm<=xb+251 and ym>=yb and ym<=yb+66:
                    estado = JUGANDO

                xb = 292
                yb= 330
                if xm>=xb and xm<=xb+216 and ym>=yb and ym<=yb+66:
                    estado = JUGANDO2

                xb = 274
                yb= 66
                if xm>=xb and xm<=xb+277 and ym>=yb and ym<=yb+66:
                    estado = INFORMACION

                xb = 299
                yb= 462
                if xm>=xb and xm<=xb+202 and ym>=yb and ym<=yb+66:
                    estado = PUNTAJES


        # Borrar pantalla
        ventana.fill(NEGRO)
        dibujarFondo(ventana, background)

        if estado == JUGANDO:
            #texto en la pantalla
            tiempoSobrevividoIntermedio+=1/40

            ##TIEMPO
            if timer >=1.5:
                timer=0

                # Crear una bala CADA 2 SEGUNDOS
                efecto.set_volume(0.4)
                efecto.play() #NReproduce el fodno de muscia
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width //2 - spriteBala.rect.width//2
                spriteBala.rect.bottom = spritePersonaje.rect.bottom - spritePersonaje.rect.height
                listaBalas.append(spriteBala)

            elif enemigoBasura >=1.5:
                enemigoBasura = 0
                #genera enemigo cada 2 segundso
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(70, ANCHO-80-spriteEnemigo.rect.width)
                spriteEnemigo.rect.bottom = randint(0, ALTO)-ALTO
                listaEnemigos.append(spriteEnemigo)

            elif enemigoPila >= 5:
                enemigoPila = 0
                spritePila = pygame.sprite.Sprite()
                spritePila.image = imgPila
                spritePila.rect = imgPila.get_rect()
                spritePila.rect.left=randint(70, ANCHO-80-spritePila.rect.width)
                spritePila.rect.bottom = randint(0, ALTO)-ALTO
                listaPilas.append(spritePila)

            #Actualizar enemigos
            #Mover personaje
            moverEnemigos(listaEnemigos)
            moverEnemigosP(listaPilas)
            moverBalas(listaBalas)
            verificarColision(listaEnemigos, listaBalas)
            verificarColisionP(listaPilas,listaBalas)


            ventana.blit(imgFondo,(yf,0))
            ventana.blit(vida,(750,10))
            dibujarEnemigos(ventana,listaEnemigos)
            dibujarEnemigosP(ventana,listaPilas)
            dibujarBalas(ventana, listaBalas)
            dibujarPersonaje(ventana,spritePersonaje)
            for x in range(10):
                color = randint(0, 255), randint(0, 255), randint(0, 255)
                texto = fuente.render("Llevas : %d seg" % tiempoSobrevividoIntermedio,2, color)
                ventana.blit(texto,(10,10))

            if verificarColisionSuelo(listaPilas)==True or verificarColisionSueloE(listaEnemigos)==True:
                estado=PERDISTEINTERMEDIO
                pygame.mixer.init()
                efectoGameover = pygame.mixer.Sound("gameover.wav")
                efectoGameover.play()







        elif estado == JUGANDO2: #Dificultad avanzada
            tiempoSobrevividoAvanzado+=1/40
            ##TIEMPO
            if timer >=1.5:
                timer=0

                # Crear una bala CADA 2 SEGUNDOS
                efecto.play() #NReproduce el fodno de muscia
                spriteBala = pygame.sprite.Sprite()
                spriteBala.image = imgBala
                spriteBala.rect = imgBala.get_rect()
                spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width //2 - spriteBala.rect.width//2
                spriteBala.rect.bottom = spritePersonaje.rect.bottom - spritePersonaje.rect.height
                listaBalas.append(spriteBala)
            elif enemigoBasura>=0.5:
                enemigoBasura=0
                #genera enemigo cada 2 segundso
                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = randint(70, ANCHO-80-spriteEnemigo.rect.width)
                spriteEnemigo.rect.bottom = randint(0, ALTO) - ALTO
                listaEnemigos.append(spriteEnemigo)
            elif enemigoPila>=3:
                enemigoPila=0
                spritePila = pygame.sprite.Sprite()
                spritePila.image = imgPila
                spritePila.rect = imgPila.get_rect()
                spritePila.rect.left=randint(70, ANCHO-80-spritePila.rect.width)
                spritePila.rect.bottom = randint(0, ALTO)-ALTO
                listaPilas.append(spritePila)
            #Actualizar enemigos
            #Mover personaje
            moverEnemigos(listaEnemigos)
            moverEnemigosP(listaPilas)
            moverBalas(listaBalas)
            verificarColision(listaEnemigos, listaBalas)
            verificarColisionP(listaPilas,listaBalas)

            # Dibujar, aquí haces todos los trazos que requieras

            ventana.blit(imgFondo,(yf,0))
            ventana.blit(vida,(750,10))
            dibujarEnemigos(ventana,listaEnemigos)
            dibujarEnemigosP(ventana,listaPilas)
            dibujarBalas(ventana, listaBalas)
            dibujarPersonaje(ventana,spritePersonaje)
            for x in range(10):
                color = randint(0, 255), randint(0, 255), randint(0, 255)
                texto = fuente.render("Llevas : %d seg" % tiempoSobrevividoAvanzado,1, color)
                ventana.blit(texto,(10,10))

            if verificarColisionSuelo(listaPilas)==True or verificarColisionSueloE(listaEnemigos)==True:
                estado=PERDISTEAVANZADO
                pygame.mixer.init()
                efectoGameover = pygame.mixer.Sound("gameover.wav")
                efectoGameover.play()



        elif estado==INFORMACION:
            ventana.blit(imgRegresar,(10,10))
            ventana.blit(imgCreditos,(0,0))

            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                xb= 10
                yb= 10

                if xm>=xb and xm<=xb+178 and ym>=yb and ym<=yb+56:
                    estado= MENU
        elif estado==PUNTAJES:
            ventana.blit(imgScore,(0,0))
            ventana.blit(imgRegresar,(10,10))

            puntajeAntiguoI = open("PuntajeIntermedio.txt", "r")
            linea = puntajeAntiguoI.readline()
            puntajeI = str(linea)
            scoreIntermedio=fuente.render("Tiempo sobrevivido: %s seg" % puntajeI,1,ROJO)
            ventana.blit(scoreIntermedio,(480,500))
            puntajeAntiguoI.close()

            puntajeAntiguoA = open("PuntajeAvanzado.txt", "r")
            dato = puntajeAntiguoA.readline()
            puntajeA = str(dato)
            scoreAvanzado=fuente.render("Tiempo sobrevivido: %s seg" % puntajeA,10,ROJO)
            ventana.blit(scoreAvanzado,(0,500))
            puntajeAntiguoA.close()


            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                xb= 10
                yb= 10

                if xm>=xb and xm<=xb+178 and ym>=yb and ym<=yb+56:
                    estado= MENU
        elif estado==PERDISTEINTERMEDIO:

            ventana.blit(imgFondo,(yf,0))
            ventana.blit(sinvida,(750,10))
            ventana.blit(imgRegresar,(10,10))
            ventana.blit(derrota,(0,0))
            tiempoIntermedio = fuente.render("Sobreviviste : %d seg" % tiempoSobrevividoIntermedio, 1, ROJO)
            ventana.blit(tiempoIntermedio, (ANCHO // 2, 0))

            puntajeAntiguoI = open("PuntajeIntermedio.txt", "r")
            linea = puntajeAntiguoI.readline()
            puntaje = int(linea)
            score = tiempoSobrevividoIntermedio//1
            if puntaje < score:
                nuevoPuntajeI = open("PuntajeIntermedio.txt", "w")
                nuevoPuntajeI.write("%d" % score)
                nuevoPuntajeI.close()
            puntajeAntiguoI.close()

            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                xb= 10
                yb= 10

                if xm>=xb and xm<=xb+178 and ym>=yb and ym<=yb+56:
                    estado= MENU

        elif estado==PERDISTEAVANZADO:
            ventana.blit(imgFondo,(yf,0))
            ventana.blit(sinvida,(750,10))
            ventana.blit(imgRegresar,(10,10))
            ventana.blit(derrota,(0,0))
            tiempoAvanzado = fuente.render("Sobreviviste : %d seg" % tiempoSobrevividoAvanzado, 1, ROJO)
            ventana.blit(tiempoAvanzado, (ANCHO // 2, 0))

            puntajeAntiguoA = open("PuntajeAvanzado.txt", "r")
            linea = puntajeAntiguoA.readline()
            puntaje = int(linea)
            score = tiempoSobrevividoAvanzado//1

            if puntaje < score:
                nuevoPuntajeA = open("PuntajeAvanzado.txt", "w")
                nuevoPuntajeA.write("%d" % score)
                nuevoPuntajeA.close()
            puntajeAntiguoA.close()

            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                xb= 10
                yb= 10

                if xm>=xb and xm<=xb+178 and ym>=yb and ym<=yb+56:
                    estado= MENU

        elif estado == MENU:
            #Dibujar menú
            tiempoSobrevividoIntermedio=0
            tiempoSobrevividoAvanzado=0
            listaEnemigos=[]
            listaPilas=[]
            listaBalas=[]
            dibujarMenu(ventana, imgAvanzado,imgInformacion,imgIntermedio,imgPuntaje)

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(120)  # 40 fps
        timer += 1/20
        enemigoBasura += 1/20
        enemigoPila += 1/20
    # Después del ciclo principal


    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja



# Llamas a la función principal
main()
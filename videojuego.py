import pygame   # Librería de pygame
from random import randint
# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
NEGRO=(0,0,0)
BLANCO=(255,255,255)

#Declarar estados Menu
MENU=1
PRINCIPIANTE=2
MEDIO=3
AVANZADO=4
PERDISTE=5
GANASTE=6


#movimientos
IZQUIERDA=5
DERECHA=6
QUIETO=7


puntos=0


# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image,spritePersonaje.rect)   #dibujar imagen en ventana)

def dibujarGota(ventana, listaGotas):
    #visitar a cada elemento
    for gota in listaGotas:
        ventana.blit(gota.image,gota.rect)

def dibujarSol(ventana, listaSoles):
    #visitar a cada elemento
    for sol in listaSoles:
        ventana.blit(sol.image,sol.rect)


def moverGotas(listaGotas,velocidad):
    for gota in listaGotas:
        gota.rect.bottom+=velocidad

def moverSoles(listaSoles,velocidad):
    for sol in listaSoles:
        sol.rect.bottom+=velocidad

def dibujarMenu(ventana,imgBtnPrin,imgBtnNor,imgBtnAvan):
    ventana.blit(imgBtnPrin,(ANCHO//3-150,ALTO//3))
    ventana.blit(imgBtnNor, (ANCHO // 3 +50, ALTO // 3))
    ventana.blit(imgBtnAvan, (ANCHO // 3 +250, ALTO // 3))


def reiniciar():
    listaSoles = []
    listaGotas = []
    tiempo = 0
    puntos = 0
    return listaGotas,listaSoles,tiempo,puntos

def verificarColision(personaje, listaGotas):
    for k in range(len(listaGotas)-1,-1,-1):    #genera el indice no objeto   recorrerlas al reves
        gota=listaGotas[k]                       #la bala va a ser la que este en la posicion k
        #personaje vs gotas
        xb=gota.rect.left
        yb=gota.rect.bottom
        xe, ye, ae, ale=personaje.rect
        if xb >=xe and xb<=xe+ae and yb>=ye and yb<=ye+ale:
            #le pegó
            listaGotas.remove(gota)
            #listaBalas.remove(bala)

            return True

def sumarPuntos(personaje, listaSoles):
    global puntos
    for k in range(len(listaSoles)-1,-1,-1):    #genera el indice no objeto   recorrerlas al reves
        sol=listaSoles[k]                       #la bala va a ser la que este en la posicion k
        #personaje vs soles
        xb=sol.rect.left
        yb=sol.rect.bottom
        xe, ye, ae, ale=personaje.rect
        if xb >=xe and xb<=xe+ae and yb>=ye and yb<=ye+ale:
            #le pegó
            listaSoles.remove(sol)
            puntos += 1

            break                  #ya no revisa despues de pegar a enemigo
    return puntos


def ganar(puntos, total):
    if puntos==total:
        return True


def leerHighscoreP(tiempo):
    archivo = open("puntajeP.txt", "r")
    tiempoP = float(archivo.readline())
    if tiempoP > tiempo:
        agregar=open("puntajeP.txt", "w")
        agregar.write("%.2f" % tiempo)
        agregar.close()

def imprimirHighScore(fuente,ventana):
    puntajeP=open("puntajeP.txt","r")
    principiante=float(puntajeP.readline())
    highScoreP = fuente.render("Principiante: %.2f seg" % principiante, 1, BLANCO)
    ventana.blit(highScoreP, (ANCHO//2, ALTO - 150))

    puntajeM=open("puntajeM.txt","r")
    normal = float(puntajeM.readline())
    highScoreM = fuente.render("Normal: %.2f seg" % normal, 1, BLANCO)
    ventana.blit(highScoreM, (ANCHO//2, ALTO - 100))

    puntajeA = open("puntajeA.txt", "r")
    avanzado = float(puntajeA.readline())
    highScoreA = fuente.render("Avanzado: %.2f seg" % avanzado, 1, BLANCO)
    ventana.blit(highScoreA, (ANCHO//2, ALTO - 50))



def leerHighscoreM(tiempo):
    archivo = open("puntajeM.txt", "r")
    tiempoM = float(archivo.readline())
    if tiempoM > tiempo:
        agregar = open("puntajeM.txt", "w")
        agregar.write("%.2f" % tiempo)
        agregar.close()

def leerHighscoreA(tiempo):
    archivo = open("puntajeA.txt", "r")
    tiempoA = float(archivo.readline())
    if tiempoA > tiempo:
        agregar = open("puntajeA.txt", "w")
        agregar.write("%.2f" % tiempo)
        agregar.close()




def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #personaje
    imgPersonaje=pygame.image.load("arana2.png")    #carga imagen
    spritePersonaje=pygame.sprite.Sprite()      #hace sprite de la imagen
    spritePersonaje.image=imgPersonaje            #se asigna sprite a imagen
    spritePersonaje.rect=imgPersonaje.get_rect()   #pide dimensiones de la imagen para el sprite
    spritePersonaje.rect.left=ANCHO//2-spritePersonaje.rect.width//2                       #posicion en x =0
    spritePersonaje.rect.bottom= ALTO    #posicion en y =la mitad + la mitad de la imagen para que esté centrada


    #gotas
    listaGotas=[]
    imgGotas=pygame.image.load("gota.png")



    #soles
    listaSoles=[]
    imgSoles=pygame.image.load("sol2 (Personalizado) (1).png")


    #fondo
    imgFondo=pygame.image.load("fondo.png")

    #menu
    imgBtnPrin=pygame.image.load("button_principiante.png")
    imgBtnNor = pygame.image.load("button_normal.png")
    imgBtnAvan = pygame.image.load("button_avanzado.png")
    imgBtnRegresarMenu=pygame.image.load("button_jugar-otra-vez.png")

    estado= MENU

    moviendo=QUIETO

    timer=0
    tiempoP=0
    tiempoM=0
    tiempoA=0

    fuente = pygame.font.SysFont("monospace", 20)
    titulo=pygame.font.SysFont("monospace", 100)


    # audio
    pygame.mixer.init()
    pygame.mixer.music.load("cancion.mp3")
    pygame.mixer.music.play(-1)

    efecto=pygame.mixer.Sound("gota.wav")



    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            if evento.type==pygame.KEYDOWN:      #si se presiona la tecla
                if evento.key==pygame.K_LEFT:        #si va tecla arriba  se mueve hacia arriba
                    moviendo=IZQUIERDA
                elif evento.key==pygame.K_RIGHT:    #si presionan la de abajo va hacuia abajo
                    moviendo=DERECHA
            elif evento.type==pygame.KEYUP:
                moviendo=QUIETO



            elif evento.type==pygame.MOUSEBUTTONUP:    #hasta que suelte el botón
                xm, ym = pygame.mouse.get_pos()      #datos de coordenadas en x y de donde se hace click
                #preguntar si solto el mouse dentro del botón
                if estado == MENU:
                    xb=ANCHO//3-150
                    yb=ALTO//3
                    if xm >=xb and xm<=xb+175 and ym>= yb and ym<=yb+60:
                        estado=PRINCIPIANTE

                    xb = ANCHO // 3 +50
                    yb = ALTO // 3
                    if xm >= xb and xm <= xb + 175 and ym >= yb and ym <= yb + 60:
                        estado = MEDIO
                    xb = ANCHO // 3 +250
                    yb = ALTO // 3
                    if xm >= xb and xm <= xb + 175 and ym >= yb and ym <= yb + 60:
                        estado = AVANZADO
                if estado == PERDISTE or estado==GANASTE:
                    xb=100
                    yb=ALTO//2+200
                    if xm >= xb and xm <= xb + 175 and ym >= yb and ym <= yb + 60:
                        estado=MENU
                        tiempoA =0
                        tiempoM =0
                        tiempoP = 0
                        listaSoles = []
                        listaGotas = []
                        global puntos
                        puntos=0
                        imgPersonaje = pygame.image.load("arana2.png")  # carga imagen
                        spritePersonaje = pygame.sprite.Sprite()  # hace sprite de la imagen
                        spritePersonaje.image = imgPersonaje  # se asigna sprite a imagen
                        spritePersonaje.rect = imgPersonaje.get_rect()  # pide dimensiones de la imagen para el sprite
                        spritePersonaje.rect.left = ANCHO // 2 - spritePersonaje.rect.width // 2  # posicion en x =0
                        spritePersonaje.rect.bottom = ALTO  # posicion en y =la mitad + la mitad de la imagen para que esté centrada


        if estado==PRINCIPIANTE:
            total=10

        elif estado==MEDIO:
            total=20
        elif estado==AVANZADO:
            total=30

        # Borrar pantalla
        ventana.fill(NEGRO)
        ventana.blit(imgFondo, (0, 0))
        if estado==PRINCIPIANTE:
            tiempoP += 1 / 50
            #Mover personaje
            if moviendo==IZQUIERDA:
                spritePersonaje.rect.left -= 5
            if moviendo==DERECHA:
                spritePersonaje.rect.left+=5
            if moviendo==QUIETO:
                pass
            if timer>=1:
                timer=0
                # enemigo
                efecto.play()
                spriteGotas = pygame.sprite.Sprite()
                spriteGotas.image = imgGotas
                spriteGotas.rect = imgGotas.get_rect()
                spriteGotas.rect.left = randint(0, ANCHO)
                spriteGotas.rect.bottom = randint(-5, 0)
                listaGotas.append(spriteGotas)

                spriteSoles = pygame.sprite.Sprite()
                spriteSoles.image = imgSoles
                spriteSoles.rect = imgSoles.get_rect()
                spriteSoles.rect.left = randint(0, ANCHO)
                spriteSoles.rect.bottom = randint(-5, 0)
                listaSoles.append(spriteSoles)
            #actualizar enemigos
            moverGotas(listaGotas,3)
            moverSoles(listaSoles,3)
            sumarPuntos(spritePersonaje, listaSoles)
            verificar=verificarColision(spritePersonaje,listaGotas)
            ganado=ganar(puntos,total)
            if verificar==True:
                estado=PERDISTE
            if ganado==True:
                estado=GANASTE

            ventana.blit(imgFondo,(0,0))
            dibujarPersonaje(ventana,spritePersonaje)
            dibujarGota(ventana,listaGotas)
            dibujarSol(ventana,listaSoles)
            texto = fuente.render("Score: %d/10" % puntos, 1, BLANCO)
            ventana.blit(texto, (50, ALTO - 50))
            marcador=fuente.render("Tiempo: %.2f seg" % tiempoP,1,BLANCO)
            ventana.blit(marcador, (ANCHO-200, 50))
        elif estado==MEDIO:
            tiempoM+=1/50
            # Mover personaje
            if moviendo == IZQUIERDA:
                spritePersonaje.rect.left -= 7
            if moviendo == DERECHA:
                spritePersonaje.rect.left += 7
            if moviendo == QUIETO:
                pass
            if timer >= 0.5:
                timer = 0
                efecto.play()
                spriteGotas = pygame.sprite.Sprite()
                spriteGotas.image = imgGotas
                spriteGotas.rect = imgGotas.get_rect()
                spriteGotas.rect.left = randint(0, ANCHO)
                spriteGotas.rect.bottom = randint(-100, 0)
                listaGotas.append(spriteGotas)

                spriteSoles = pygame.sprite.Sprite()
                spriteSoles.image = imgSoles
                spriteSoles.rect = imgSoles.get_rect()
                spriteSoles.rect.left = randint(0, ANCHO)
                spriteSoles.rect.bottom = randint(-100, 0)
                listaSoles.append(spriteSoles)
            # actualizar enemigos
            moverGotas(listaGotas,5)
            moverSoles(listaSoles,5)
            sumarPuntos(spritePersonaje, listaSoles )
            verificar = verificarColision(spritePersonaje, listaGotas)
            ganado = ganar(puntos, total)
            if verificar == True:
                estado = PERDISTE
            if ganado == True:
                estado = GANASTE

            ventana.blit(imgFondo, (0, 0))
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarGota(ventana, listaGotas)
            dibujarSol(ventana, listaSoles)
            texto = fuente.render("Score: %d/20" % puntos, 1, BLANCO)
            ventana.blit(texto, (50, ALTO - 50))
            marcador = fuente.render("Tiempo: %.2f seg" % tiempoM, 1, BLANCO)
            ventana.blit(marcador, (ANCHO - 200, 50))

        elif estado==AVANZADO:
            tiempoA += 1 / 50
            # Mover personaje
            if moviendo == IZQUIERDA:
                spritePersonaje.rect.left -= 9
            if moviendo == DERECHA:
                spritePersonaje.rect.left += 9
            if moviendo == QUIETO:
                pass
            if timer >= 0.5:
                timer = 0
                efecto.play()
                spriteGotas = pygame.sprite.Sprite()
                spriteGotas.image = imgGotas
                spriteGotas.rect = imgGotas.get_rect()
                spriteGotas.rect.left = randint(0, ANCHO)
                spriteGotas.rect.bottom = randint(-100, 0)
                listaGotas.append(spriteGotas)

                spriteSoles = pygame.sprite.Sprite()
                spriteSoles.image = imgSoles
                spriteSoles.rect = imgSoles.get_rect()
                spriteSoles.rect.left = randint(0, ANCHO)
                spriteSoles.rect.bottom = randint(-100, 0)
                listaSoles.append(spriteSoles)
            # actualizar enemigos
            moverGotas(listaGotas,10)
            moverSoles(listaSoles,10)
            sumarPuntos(spritePersonaje, listaSoles, )
            verificar = verificarColision(spritePersonaje, listaGotas)
            ganado = ganar(puntos, total)
            if verificar == True:
                estado = PERDISTE
            if ganado == True:
                estado = GANASTE

            ventana.blit(imgFondo, (0, 0))
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarGota(ventana, listaGotas)
            dibujarSol(ventana, listaSoles)
            texto = fuente.render("Score: %d/30" % puntos, 1, BLANCO)
            ventana.blit(texto, (50, ALTO - 50))
            marcador = fuente.render("Tiempo: %.2f seg" % tiempoA, 1, BLANCO)
            ventana.blit(marcador, (ANCHO - 200, 50))

        elif estado==MENU: #dibujar Menu
            dibujarMenu(ventana,imgBtnPrin,imgBtnNor,imgBtnAvan)
            highScore=titulo.render("High Score: ",1,BLANCO)
            ventana.blit(highScore,(0,ALTO-300))
            imprimirHighScore(fuente,ventana)


        elif estado==PERDISTE:
            texto =titulo.render("PERDISTE", 100, BLANCO)
            ventana.blit(texto, (150, ALTO//2-100))
            ventana.blit(imgBtnRegresarMenu, (100, ALTO//2+200))
            marcador = fuente.render("Recogiste %d de %d soles que necesitas" % (puntos,total), 1, BLANCO)
            ventana.blit(marcador, (150, ALTO-200))


        elif estado==GANASTE:
            texto = titulo.render("GANASTE", 100, BLANCO)
            ventana.blit(texto, (100, ALTO // 2))
            ventana.blit(imgBtnRegresarMenu, (100, ALTO // 2 + 200))
            if tiempoP !=0:
                tiempo=tiempoP
                leerHighscoreP(tiempo)
            elif tiempoM !=0:
                tiempo=tiempoM
                leerHighscoreM(tiempo)
            elif tiempoA !=0:
                tiempo=tiempoA
                leerHighscoreA(tiempo)
            puntaje=fuente.render( "Tiempo: %.2f seg"% tiempo,1,BLANCO)
            ventana.blit(puntaje, (150, ALTO - 200))
            imprimirHighScore(fuente,ventana)



        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(50)  # 40 fps
        timer += 1 / 50

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
#Irma Gómez Carmona, A01747743
#Videojuego Bob esponja    30/11/2018
#Proyecto Final

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)

listaJugadores1=[]

#Estados
MENU = 6
JUGANDO = 7
TABLA_JUGADORES=8
PERDEDOR=9
GANADOR=10
INSTRUCCIONES=11

#Estados de movimiento

QUIETO=1
ARRIBA=2
ABAJO=3
DERECHA=4
IZQUIERDA=5


# Estructura básica de un programa que usa pygame para dibujar

def dibujarPersonaje(ventana, spriteEsponjaD): #dibuja a Bob
    ventana.blit(spriteEsponjaD.image, (spriteEsponjaD.rect.left, spriteEsponjaD.rect.bottom))


def actualizarBob(spriteEsponjaD, imgEsponja): #cambia la direccion de Bob segun el movimeinto
    spriteEsponjaD.image = imgEsponja


def dibujarEnemigos(ventana, listaPlanctons): #dibuja los plancton
    for k in listaPlanctons:
        ventana.blit(k.image, k.rect)


def actualizarPlanctons(listaPlanctons):
    velocidad=4
    #Posiciones del plancton 1
    p1x=listaPlanctons[0].rect.left
    p1y=listaPlanctons[0].rect.bottom
    #movimientos de los otros planctons en base al plancton 1
    if p1x<=206 and p1y==26+listaPlanctons[0].rect.height:
        listaPlanctons[0].rect.left+=velocidad
        listaPlanctons[1].rect.left-=velocidad
    elif p1x==210 and p1y<=290+listaPlanctons[0].rect.height:
        listaPlanctons[0].rect.bottom+=velocidad
        listaPlanctons[1].rect.bottom-=velocidad
        listaPlanctons[2].rect.left += velocidad
    elif p1x>=50:
        listaPlanctons[0].rect.left -= velocidad
        listaPlanctons[1].rect.left += velocidad
    else:
        listaPlanctons[0].rect.bottom-=velocidad
        listaPlanctons[1].rect.bottom += velocidad
        listaPlanctons[2].rect.left -= velocidad


def dibujarIngredientes(ventana, listaIngredientes): #dibuja ingredientes
    for k in listaIngredientes:
        ventana.blit(k.image, k.rect)


def verificarColisionesPlancton(ventana, spriteEsponjaD, listaPlanctons,efecto):
    for k in range (len(listaPlanctons)-1,-1,-1):
        plancton=listaPlanctons[k]
        xP=plancton.rect.left
        yP=plancton.rect.bottom
        anchoP=plancton.rect.width
        altoP=plancton.rect.height

        xS=spriteEsponjaD.rect.left
        yS=spriteEsponjaD.rect.bottom
        anchoS=spriteEsponjaD.rect.width
        altoS = spriteEsponjaD.rect.height

        if xP+2>=xS-2 and xP+2<=xS+anchoS-2 and yP-2 >= yS+2 and yP-4 <= yS + altoS-2:  #si chocan bob y plnkton
            efecto.play()  #sonido de golpe
            imgGolpe=pygame.image.load("golpe.png") #imagen de golpe
            spriteG = pygame.sprite.Sprite()  # Sprite vacío
            spriteG.image = imgGolpe
            spriteG.rect = imgGolpe.get_rect()
            spriteG.rect.left = xP+anchoP//2
            spriteG.rect.bottom = yP
            ventana.blit(spriteG.image, spriteG.rect)
            return "salir"



def bajarI(dicIngredientes, listaIngredientes):
    for y in range(0,12):
        #panes abajo
        if y==0 or y==3 or y==6 or y==9:
            limite = 480
        #panes arriba
        elif y==1 or y==4 or y==7 or y==10:
            limite = 440
        #carnes
        elif y==2 or y==5 or y==8 or y==11:
            limite = 460

        if dicIngredientes[y]=="Abajo":
            # el ingredinte va a bajar hasta llegar a su límite
            if listaIngredientes[y].rect.bottom<=limite:
                listaIngredientes[y].rect.bottom+=3


def bajarIngredientes(spriteEsponjaD, listaIngredientes, dicIngredientes):
    suma=0
    score=0
    xS = spriteEsponjaD.rect.left
    yS = spriteEsponjaD.rect.bottom
    anchoS = spriteEsponjaD.rect.width
    altoS = spriteEsponjaD.rect.height
    for k in range (len(listaIngredientes)-1,-1,-1):
        Ingrediente=listaIngredientes[k]
        xI=Ingrediente.rect.left
        yI=Ingrediente.rect.bottom
        anchoI=Ingrediente.rect.width
        altoI=Ingrediente.rect.height
        #cuando bob pase sobre el ingrediente , éste va a bajar
        if xI >= xS and xI <= xS + anchoS and yI >= yS and yI <= yS + altoS:
            dicIngredientes[k]="Abajo"
            score = 300
    bajarI(dicIngredientes, listaIngredientes)
    return score



def verificarTodosAbajo(dicIngredientes): #verificar que todos los ingredientes estan en modo Abajo
    for k in dicIngredientes:
        if dicIngredientes[k]=="quieto":
            return False
    return True

def dibujar():
    #Archivo de los jugadores
    datosT=[]
    datos=[]
    contador=1
    archivoJugadores=open("Jugadores.csv","r",encoding="UTF-8")
    titulo=archivoJugadores.readline()
    for linea in archivoJugadores: #lee cada linea
        datos=linea.split(",")
        datos[0]=int(datos[0])
        datos[1]=int(datos[1])
        datos[2]=int(datos[2])
        datosT.append(datos)
    if len(datosT)>0:
        contador+=datos[0] #contador de jugador

    archivoJugadores.close()

    #Iniciación de las variables
    tiempo=0
    timer=0
    Estado=6
    movimiento = QUIETO
    score=0


    #Audio
    pygame.mixer.init()
    efecto = pygame.mixer.Sound("sGolpe.wav")
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)



    dicIngredientes = {0: "quieto", 1: "quieto", 2: "quieto", 3: "quieto", 4: "quieto", 5: "quieto", 6: "quieto",
                       7: "quieto", 8: "quieto", 9: "quieto", 10: "quieto", 11: "quieto"}

    # Fondos y botones
    imgFondo = pygame.image.load("fondo2.png")

    imgFondoM = pygame.image.load("fondoMenu.png")
    imgB_jugar= pygame.image.load("button_jugar.png")

    imgB_jugador = pygame.image.load("button_jugadores.png")
    imgFondoJ = pygame.image.load("fondoJugadores.jpg")

    imgB_instrucciones=pygame.image.load("button_instrucciones.png")

    imfF_Perdiste=pygame.image.load("fondoPerdiste.jpg")
    imfF_Ganaste = pygame.image.load("fondoGanaste.png")

    imgBmenu=pygame.image.load("button_menu.png")

    # Esponja
    imgEsponjaD = pygame.image.load("esponjaDerecha.png")
    imgEsponjaI = pygame.image.load("esponjaIzquierda.png")

    spriteEsponjaD = pygame.sprite.Sprite()  # Sprite vacío
    spriteEsponjaD.image = imgEsponjaD
    spriteEsponjaD.rect = imgEsponjaD.get_rect()
    spriteEsponjaD.rect.left = ANCHO // 2 - spriteEsponjaD.rect.width // 2
    spriteEsponjaD.rect.bottom = ALTO // 2 - 10

    # Planktons
    imgPlancton = pygame.image.load("plancton2.png")
    listaPlanctons=[]

    for k in range(3):
        spritePlancton=pygame.sprite.Sprite()
        spritePlancton.image = imgPlancton
        spritePlancton.rect = imgPlancton.get_rect()
        listaPlanctons.append(spritePlancton)
    #Plancton1
    listaPlanctons[0].rect.bottom=89
    listaPlanctons[0].rect.left=50
    # Plancton2
    listaPlanctons[1].rect.bottom = 353
    listaPlanctons[1].rect.left = 700
    # Plancton3
    listaPlanctons[2].rect.bottom = 217
    listaPlanctons[2].rect.left = 230


    # Ingredientes
    imgPanAbajo = pygame.image.load("panAbajo.jpg")
    imgPanArriba = pygame.image.load("panArriba.jpg")
    imgCarne = pygame.image.load("carne.jpg")
    listaIngredientes=[]
    sumaX=120

    for pAB in range (4):

        spritePanAbajo = pygame.sprite.Sprite()  # Sprite vacío
        spritePanAbajo.image = imgPanAbajo
        spritePanAbajo.rect = imgPanAbajo.get_rect()
        spritePanAbajo.rect.left = sumaX
        spritePanAbajo.rect.bottom = 351
        listaIngredientes.append(spritePanAbajo)

        spritePanArriba = pygame.sprite.Sprite()  # Sprite vacío
        spritePanArriba.image = imgPanArriba
        spritePanArriba.rect = imgPanArriba.get_rect()
        spritePanArriba.rect.left = sumaX
        spritePanArriba.rect.bottom = 87
        listaIngredientes.append(spritePanArriba)

        spriteCarne = pygame.sprite.Sprite()  # Sprite vacío
        spriteCarne.image = imgCarne
        spriteCarne.rect = imgCarne.get_rect()
        spriteCarne.rect.left = sumaX
        spriteCarne.rect.bottom = 215
        listaIngredientes.append(spriteCarne)

        sumaX += 165  # los ingredientes estan separados por 165 pixeles

    #Instrucciones
    imgIns = pygame.image.load("instrucciones.png")
    spriteI = pygame.sprite.Sprite()  # Sprite vacío
    spriteI.image = imgIns
    spriteI.rect = imgIns.get_rect()
    spriteI.rect.left = 240
    spriteI.rect.bottom = 120+spriteI.rect.height

    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        # Procesa los eventos que recibe

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    actualizarBob(spriteEsponjaD,imgEsponjaI)
                    movimiento=5
                elif evento.key == pygame.K_RIGHT:
                    actualizarBob(spriteEsponjaD, imgEsponjaD)
                    movimiento=4
                elif evento.key == pygame.K_UP:
                    movimiento=2
                elif evento.key == pygame.K_DOWN:
                    movimiento=3
            elif evento.type==pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos() #posicion del ratón
                #botones del menú
                xb = 150
                yb = 280
                anchoB = 150
                altoB = 45

                yb2 = 380
                yb3= 480

                #boton para regresar al menú
                xbM=20
                ybM=20

                if xm >= xb and xm <= xb + anchoB and ym >= yb and ym <= yb + altoB:
                    Estado = JUGANDO
                elif xm >= xb and xm <= xb + anchoB and ym >= yb2 and ym <= yb2 + altoB:
                    Estado = TABLA_JUGADORES
                elif xm >= xb and xm <= xb + anchoB and ym >= yb3 and ym <= yb3 + altoB:
                    Estado = INSTRUCCIONES
                elif xm >= xbM and xm <= xbM + anchoB and ym >= ybM and ym <= ybM + altoB:
                    Estado = MENU

        xPos=spriteEsponjaD.rect.left
        yPos=spriteEsponjaD.rect.bottom
    #Zonas en las que Bob puede moverse
        if movimiento==DERECHA and xPos>=50 and xPos+4 <= 700:
            if yPos == 290 or yPos == 26 or (yPos>=152 and yPos<=160):
                spriteEsponjaD.rect.left += 4
        elif movimiento == IZQUIERDA and xPos <= 700 and xPos-4 >=50:
            if yPos == 290 or yPos == 26 or (yPos>=152 and yPos<=160):
                spriteEsponjaD.rect.left -= 4
        elif movimiento == ARRIBA and ((xPos <= 700 and xPos >= 694) or (xPos >= 50 and xPos <= 52) or (xPos >= 522 and xPos <= 536) or (xPos >= 202 and xPos <= 212) or ((xPos >= 366 and xPos <= 374) and (yPos >= 26 and yPos <= 158))):
            # (spriteEsponjaD.rect.left==50 or spriteEsponjaD.rect.left==700)
            if yPos - 4 >= 26 and xPos != (xPos >= 362 and xPos <= 370):
                spriteEsponjaD.rect.bottom -= 4
        elif movimiento == ABAJO and ((xPos <= 700 and xPos >= 694) or (xPos >= 50 and xPos <= 52) or (xPos >= 522 and xPos <= 536) or (xPos >= 202 and xPos <= 212) or ((xPos >= 366 and xPos <= 374) and (yPos >= 26 and yPos <= 157))):
            if yPos + 4 <= 290:
                spriteEsponjaD.rect.bottom += 4
        if Estado==MENU:
            ventana.fill(BLANCO)
            ventana.blit(imgFondoM, (0, 0))
            ventana.blit(imgB_jugar, (150, 280))
            ventana.blit(imgB_jugador, (150, 380))
            ventana.blit(imgB_instrucciones, (150, 480))
        elif Estado==INSTRUCCIONES:
            ventana.fill(BLANCO)
            ventana.blit(imgFondoJ, (0, 0))
            fuenteT = pygame.font.SysFont("monospace", 45, 2)
            t1 = fuenteT.render("Instrucciones", 1, VERDE_BANDERA)
            ventana.blit(t1, (210, 35))
            ventana.blit(spriteI.image, spriteI.rect)
            ventana.blit(imgBmenu, (20, 20))
        elif Estado==TABLA_JUGADORES:
            posy=140
            tituloS=titulo.split(",")
            ventana.fill(BLANCO)
            ventana.blit(imgFondoJ, (0, 0))
            ventana.blit(imgBmenu, (20, 20))
            fuenteT = pygame.font.SysFont("monospace", 45, 2)
            fuenteT2 = pygame.font.SysFont("monospace", 30, 2)
            fuente = pygame.font.SysFont("monospace", 30, 1)
            t1 = fuenteT.render("Jugadores", 1, ROJO)
            t2 = fuenteT2.render("%s  %s  %s"%(tituloS[0],tituloS[1],tituloS[2][0:6]), 1, VERDE_BANDERA)
            ventana.blit(t1, (270, 35))
            ventana.blit(t2, (200, 100))
            for jugador in datosT:
                cadena=str(jugador)
                cadena=cadena[1:len(cadena)-1]
                cadena=cadena.split(",")
                linea=t1 = fuente.render("%s    %s     %s"%(cadena[0],cadena[1],cadena[2]), 1, NEGRO)
                ventana.blit(t1, (260, posy))
                posy+=50

        elif Estado==GANADOR:
            ventana.fill(BLANCO)
            ventana.blit(imfF_Ganaste, (0, 0))
            fuenteT = pygame.font.SysFont("monospace", 45, 2)
            fuente = pygame.font.SysFont("monospace", 40, 1)
            t1 = fuenteT.render("GANASTE", 1, VERDE_BANDERA)
            t2 = fuente.render("SCORE: %d " % listaJugadores1[0][1], 1, BLANCO)
            t3 = fuente.render("TIEMPO: %d s" % listaJugadores1[0][2], 1, BLANCO)
            ventana.blit(t1, (280, 50))
            ventana.blit(t2, (265, 110))
            ventana.blit(t3, (265, 160))
        elif Estado==PERDEDOR:
            ventana.fill(BLANCO)
            ventana.blit(imfF_Perdiste, (0, 0))
            fuenteT = pygame.font.SysFont("monospace", 45, 2)
            fuente = pygame.font.SysFont("monospace", 40,1)
            t1 = fuenteT.render("GAME OVER", 1, ROJO)
            t2=fuente.render("SCORE: %d "%listaJugadores1[0][1], 1, BLANCO)
            t3=fuente.render("TIEMPO: %d s"% listaJugadores1[0][2], 1, BLANCO)
            ventana.blit(t1, (25, 10))
            ventana.blit(t2, (18, 80))
            ventana.blit(t3, (18, 120))
        if timer>=3:
            timer=0
        elif Estado==JUGANDO:

            # Borrar pantalla
            ventana.fill(BLANCO)
            ventana.blit(imgFondo, (0, 0))

            dibujarIngredientes (ventana, listaIngredientes)
            dibujarPersonaje(ventana, spriteEsponjaD)  # Dibuja a bobEsponja
            dibujarEnemigos(ventana, listaPlanctons)

            #Actualizar movimientos Plancton
            actualizarPlanctons(listaPlanctons)

            # Bajar ingredientes
            score += bajarIngredientes(spriteEsponjaD, listaIngredientes, dicIngredientes)

            fuente = pygame.font.SysFont("monospace", 30)
            texto = fuente.render("Score: %d" % score, 1, BLANCO)
            texto2= fuente.render("Tiempo: %d" % int(tiempo), 1, BLANCO)
            ventana.blit(texto, (65, 540))
            ventana.blit(texto2, (450, 540))

            #Verificar Colisiones Bob Con Plancton
            datosJugador=contador,score,int(tiempo)
            if verificarColisionesPlancton(ventana,spriteEsponjaD,listaPlanctons,efecto)=="salir" and timer>=1:
                listaJugadores1.append(datosJugador)
                Estado=PERDEDOR

            elif verificarTodosAbajo(dicIngredientes) and timer>=2.8: #si ya bajaron todos los ingredientes gana
                Estado = GANADOR
                listaJugadores1.append(datosJugador)
        
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        tiempo+=1/40 #tiempo jugando 
        timer+=1/40  #tiempo que llega máximo a 2 para cambiar de estado

    #escribir en el documento los datos del nuevo jugador y los datos anteriores
    salida=open("Jugadores.csv","w",encoding="UTF-8")
    salida.write(titulo)
    if len(datosT)>0:
        for i in range(0,len(datosT)):
            salida.write("%d,%s,%s\n"%(datosT[i][0],datosT[i][1],datosT[i][2])) #los datos anteriores se agregan de nuevo al documento
    salida.write("%d,%d,%d\n"%(datosJugador[0],datosJugador[1],datosJugador[2]))
    salida.close()
    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
















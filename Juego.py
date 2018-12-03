#Alexys Martín Coate Reyes

import pygame
from random import randint

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0,0,0)

#Estados
MENU = 1
JUGANDO = 2
PERDIDO = 3
GANADO = 4
PUNTUACIONES = 5

#Estados de movimiento
QUIETO = 0
ARRIBA = 1
ABAJO = 2
DERECHA = 3
IZQUIERDA = 4

listaPuntajes = []

##### Posición - Alto - Ancho (Botones) #####
#Botón (INICIAR JUEGO)
BTN_IniciarJuego_ALTO = 91
BTN_IniciarJuego_ANCHO = 169
posBTN_IniciarJuego = (ANCHO // 2 - BTN_IniciarJuego_ANCHO // 2, ALTO * .6-BTN_IniciarJuego_ALTO//2)

#Botón (MENU)
BTN_Menu_ALTO = 91
BTN_Menu_ANCHO = 117
posBTN_Menu = (ANCHO // 2 - BTN_Menu_ANCHO // 2, ALTO * .6-BTN_Menu_ALTO//2)

#Botón (PUNTUACION)
BTN_Puntuaciones_ALTO = 91
BTN_Puntuaciones_ANCHO = 169
posBTN_Puntuaciones = (ANCHO // 2 - BTN_Puntuaciones_ANCHO // 2, ALTO * .6-BTN_Puntuaciones_ALTO//2)

#####MENU#####

def dibujarMenu(ventana, BTN_IniciarJuego, FONDO_Menu, BTN_Puntuaciones, posBTN_Puntuaciones):
    # Sprite para la imagen de fondo
    ventana.blit(FONDO_Menu, (0, 0))
    #Sprite para el botón (INICIAR JUEGO)
    ventana.blit(BTN_IniciarJuego, (posBTN_IniciarJuego[0] , posBTN_IniciarJuego[1]))
    ventana.blit(BTN_Puntuaciones, (posBTN_Puntuaciones[0], posBTN_Puntuaciones[1]))

#####JUGANDO#####

def dibujarPlantilla(ventana, juegoPlantilla1, plantilla1_ANCHO, plantilla1_ALTO):
    ventana.blit(juegoPlantilla1, (0,0))
    if plantilla1_ANCHO < ANCHO:
        ventana.blit(juegoPlantilla1, (plantilla1_ANCHO, 0))
    if plantilla1_ALTO < ALTO:
        ventana.blit(juegoPlantilla1, (0,plantilla1_ALTO))

def dibujarPersonajes(ventana, spritePersonaje, listaSatelites):
    #Dibuja el personaje principal
    ventana.blit(spritePersonaje.image, spritePersonaje.rect) #Dibuja una imagen en la vetana (imgaen, tamaño)

    #Dibujar Aliados
    #Crear satelites
    for satelite in listaSatelites:
        ventana.blit(satelite.image, satelite.rect)


def dibujarObjetivos(ventana, spritePlaneta):
    ventana.blit(spritePlaneta.image, spritePlaneta.rect)

def dibujarEnemigos(ventana, listaEnemigos):
    cambio = QUIETO

    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)
        enemigo.rect.bottom += 1


    #Dibujar disparos de enemigos



def dibujarDisparos(ventana, listaMisiles, listaEnemigos):
    #Dibujar los misiles
    for bala in listaMisiles:
        ventana.blit(bala.image, bala.rect)

    #Mueve los misiles
    for bala in listaMisiles:
        bala.rect.bottom -= 10

    #Verificar colisión
    for bala in listaMisiles:
        for enemigo in listaEnemigos:
            #Bala vs enemigo
            xb = bala.rect.left
            yb = bala.rect.bottom
            xe = enemigo.rect.left
            ye = enemigo.rect.bottom
            ae = enemigo.rect.width
            alte = enemigo.rect.height
            if xb >= xe and xb <= xe+ae and yb >= ye and yb <= ye+alte:
                #Eliminar enemigo y bala
                listaEnemigos.remove(enemigo)
                listaMisiles.remove(bala)
                break

def verificarColision(listaEnemigos, spritePersonaje, ventana, BTN_Menu, FONDOperdiste):
    for enemigo in listaEnemigos:
        xE = enemigo.rect.left
        yE = enemigo.rect.bottom
        wE = enemigo.rect.width
        hE = enemigo.rect.height
        xP = spritePersonaje.rect.left
        yP = spritePersonaje.rect.bottom
        wP = spritePersonaje.rect.width
        hP = spritePersonaje.rect.height
        if xP >= xE and xP <= xE+wE and yP >= yE and yP <= yE+hE:
            estado = PERDIDO
            dibujarPerdido(ventana, BTN_Menu, FONDOperdiste)

def dibujarItems(ventana, listaItems):
    #Dibuja el item
    for item in listaItems:
        ventana.blit(item.image, item.rect)
        item.rect.bottom += 3


##### ACCIONES ######



#############################################################################################

#####PUNTUACIONES#####
def dibujarPuntuaciones(ventana, BTN_Puntuaciones):
    ventana.blit(BTN_Puntuaciones, (posBTN_Puntuaciones[0], posBTN_Puntuaciones[1]))

#####PERDISTE#####
def dibujarPerdido(ventana, BTN_Menu, FONDOperdiste, evento, BTN_Menu_ALTO, posBTN_Menu):
    ventana.blit(FONDOperdiste, (0,0))
    ventana.blit(BTN_Menu, (posBTN_Menu[0], posBTN_Menu[1]))


#######################################################################################

def dibujar():

    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

###########################################################################################

    #Personaje
    imgPersonaje = pygame.image.load("PERSONAJEnave.gif")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = ANCHO//2 -spritePersonaje.rect.width//2
    spritePersonaje.rect.bottom = ALTO*.8
    #anchoPersonaje = (spritePersonaje.rect.left, ANCHO//2+spritePersonaje.rect.width//2)

    #Objetivo a proteger
    imgPlaneta = pygame.image.load("OBJplanetaTierra.gif")
    spritePlaneta = pygame.sprite.Sprite()
    spritePlaneta.image = imgPlaneta
    spritePlaneta.rect = imgPlaneta.get_rect()
    spritePlaneta.rect.left = ANCHO//2 - spritePlaneta.rect.width//2
    spritePlaneta.rect.bottom = ALTO*1.2

    # Disparos
    # Balas
    listaMisiles = []
    imgMisil = pygame.image.load("Misil.png")
    #Balas Satelites
    listaMisilesSatelites = []
    imgMisilSatelite = pygame.image.load("DisparoSatelite.png")

    # Satelites
    listaSatelites = []
    imgSatelite = pygame.image.load("Satelite.png")


    contador = 0
    for s in range(4):
        spriteSatelite = pygame.sprite.Sprite()
        spriteSatelite.image = imgSatelite
        spriteSatelite.rect = imgSatelite.get_rect()
        if contador == 0:
            spriteSatelite.rect.left = ANCHO*.05
            spriteSatelite.rect.bottom = ALTO * .95
        if contador == 1:
            spriteSatelite.rect.left = ANCHO*.25
            spriteSatelite.rect.bottom = ALTO * .95
        if contador == 2:
            spriteSatelite.rect.left = ANCHO*.65
            spriteSatelite.rect.bottom = ALTO * .95
        if contador == 3:
            spriteSatelite.rect.left = ANCHO*.85
            spriteSatelite.rect.bottom = ALTO * .95
        listaSatelites.append(spriteSatelite)
        contador += 1


    #Enemigos
    listaEnemigos = []
    imgEnemigo1 = pygame.image.load("Enemigo1.png")
    for n in range(10):
        spriteEnemigo1 = pygame.sprite.Sprite()
        spriteEnemigo1.image = imgEnemigo1
        spriteEnemigo1.rect = imgEnemigo1.get_rect()
        spriteEnemigo1.rect.bottom = ANCHO*.1
        spriteEnemigo1.rect.left = randint(ANCHO*.1,ANCHO*.9)
        listaEnemigos.append(spriteEnemigo1)

    #Items
    listaItems = []
    #Cajas de poder
    imgItemPoder = pygame.image.load("ITEMescudo.png")
    imgBomba = pygame.image.load("Bomba.png")
    imgVida = pygame.image.load("ITEMvida.png")
    imgCaja = pygame.image.load("ITEMcaja.png")


##### Cargar Botones y Fondos #####

#####Botones#####
    #Botón (INICIAR JUEGO)
    BTN_IniciarJuego = pygame.image.load("BTNgameStart.png")

    #Botón (MENU)
    BTN_Menu = pygame.image.load("BTNmenu.png")
    BTN_Menu_ALTO = 91
    BTN_Menu_ANCHO = 117
    posBTN_Menu = (ANCHO*.435, ALTO*.8)

    #Botón (REGRESAR)
    #BTN_Regresar = pygame.image.load("RegresarBTN.png")
    #BTN_Regresar_ALTO = 50
    #BTN_Regresar_ANCHO = 93
    #posBTN_Regresar = (ANCHO*.9-BTN_Regresar_ANCHO//2, ALTO*.9-BTN_Regresar_ALTO//2)

    #Botón (PUNTUACIONES)
    BTN_Puntuaciones = pygame.image.load("BTNpuntuaciones.png")
    BTN_Puntuaciones_ANCHO = 177
    BTN_Puntuaciones_ALTO = 91
    posBTN_Puntuaciones = (ANCHO*.05, ALTO*.2)


#####Fondos#####

    #Fondo Juego
    juegoPlantilla1 = pygame.image.load("FONDOespacio.png")
    plantilla1_ANCHO = 640
    plantilla1_ALTO = 640

    #Fondo Menu
    FONDO_Menu = pygame.image.load("FONDOmenu.gif")

    #Fondo Perdiste
    FONDOperdiste = pygame.image.load("FONDOperdiste.jpg")
    gameOver = pygame.image.load("BTNgameOver2.gif")


    #Fondo Puntuaciones
    FONDO_Puntuaciones = pygame.image.load("FONDOpuntuaciones.jpg")
    TITULOpuntuaciones = pygame.image.load("TITULOpuntaje.png")
    TITULO_Ancho = 378
    TITULO_Alto = 96
    posTITULOpunt = (ANCHO//2-TITULO_Ancho//2, ALTO*.1)

    ###########################################################################################

    estado = MENU

    moviendo = QUIETO
    cambio = DERECHA

    # TEXTO
    TXTpuntuacion = pygame.font.SysFont("monospace", 32)
    puntos = 0
    TXTvida = pygame.font.SysFont("monospace", 24)
    HP = 100
    TXTtiempo = pygame.font.SysFont("monospace", 24)
    TIMER = 0
    TXTmarcador = pygame.font.SysFont("monospace", 26)

    # AUDIO
    pygame.mixer.init()
    pygame.mixer.music.load("Musica Atari.mp3")
    pygame.mixer.music.play(-1)

    efectoDisparo = pygame.mixer.Sound("SFXdisparoNuevo.wav")
    efectoExplosion = pygame.mixer.Sound("ExplisionEnemigo.wav")
    efectoBomba = pygame.mixer.Sound("ExplosionBomba.wav")

    # TIEMPO
    tAparecerItems = 0  # Acumulador de tiempo
    tAparecerEnemigos = 0
    tDisparoSatelites = 0

    cantidadEnemigos = 3
    vDisparoSatelites = 1

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm,ym = pygame.mouse.get_pos()
                print(xm,ym)
                #if xm >= posBTN_IniciarJuego[0] and xm <= posBTN_IniciarJuego[0]+BTN_IniciarJuego_ANCHO and ym >= posBTN_IniciarJuego[1] and ym <= posBTN_IniciarJuego[1]+BTN_IniciarJuego_ALTO:
                 #   estado = JUGANDO
                #if xm >= posBTN_Regresar[0] and xm <= posBTN_Regresar[0]+BTN_Regresar_ANCHO and ym >= posBTN_Regresar[1] and ym <= posBTN_Regresar[1]+BTN_Regresar_ALTO:
                 #   estado = MENU
                #if xm >= posBTN_Menu[0] and xm <= posBTN_Menu[0]+BTN_Menu_ANCHO and ym >= posBTN_Menu[1] and ym <= posBTN_Menu[1]+BTN_Menu_ALTO:
                 #   estado = MENU
            #Acciones de teclas
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_s:
                    moviendo = ABAJO
                elif evento.key == pygame.K_w:
                    moviendo = ARRIBA
                elif evento.key == pygame.K_d:
                    moviendo = DERECHA
                elif evento.key == pygame.K_a:
                    moviendo = IZQUIERDA
                elif evento.key == pygame.K_SPACE:
                    # Crear una bala
                    spriteMisil = pygame.sprite.Sprite()
                    spriteMisil.image = imgMisil
                    spriteMisil.rect = imgMisil.get_rect()
                    spriteMisil.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width//2 - spriteMisil.rect.width//2
                    spriteMisil.rect.bottom = spritePersonaje.rect.bottom - spriteMisil.rect.height - 20
                    listaMisiles.append(spriteMisil)
                    efectoDisparo.play()

        ventana.fill(NEGRO)

        if estado == MENU:
            dibujarMenu(ventana, BTN_IniciarJuego, FONDO_Menu, BTN_Puntuaciones, posBTN_Puntuaciones)


            if evento.type == pygame.MOUSEBUTTONUP:
                xm,ym = pygame.mouse.get_pos()
                if xm >= posBTN_IniciarJuego[0] and xm <= posBTN_IniciarJuego[0]+BTN_IniciarJuego_ANCHO and ym >= posBTN_IniciarJuego[1] and ym <= posBTN_IniciarJuego[1]+BTN_IniciarJuego_ALTO:
                    estado = JUGANDO
                    HP = 100
                    cantidadEnemigos = 3
                    puntos = 0
                    TIMER = 0
                    vDisparoSatelites = 1
                    listaEnemigos.clear()
                    listaItems.clear()
                    listaMisiles.clear()
                    listaMisilesSatelites.clear()
                    spritePersonaje.rect.left = ANCHO // 2 - spritePersonaje.rect.width // 2
                    spritePersonaje.rect.bottom = ALTO * .8
                if xm >= posBTN_Puntuaciones[0] and xm <= posBTN_Puntuaciones[0]+BTN_Puntuaciones_ANCHO and ym >= posBTN_Puntuaciones[1] and ym <= posBTN_Puntuaciones[1]+BTN_Puntuaciones_ALTO:
                    estado = PUNTUACIONES

        elif estado == JUGANDO:

            #if evento.type == pygame.MOUSEBUTTONUP:
             #   xm,ym = pygame.mouse.get_pos()
              #  if xm >= posBTN_Regresar[0] and xm <= posBTN_Regresar[0]+BTN_Regresar_ANCHO and ym >= posBTN_Regresar[1] and ym <= posBTN_Regresar[1]+BTN_Regresar_ALTO:
               #     estado = MENU

            # TIEMPO
            if tAparecerEnemigos >= 2:
                tAparecerEnemigos = 0
                cantidadEnemigos += 1
                #Aparece enemigos cada cierto timepo
                for k in range(cantidadEnemigos):
                    spriteEnemigo1 = pygame.sprite.Sprite()  # Crea el enemigo
                    spriteEnemigo1.image = imgEnemigo1
                    spriteEnemigo1.rect = imgEnemigo1.get_rect()
                    spriteEnemigo1.rect.left = randint(ANCHO*.1, ANCHO*.9)
                    spriteEnemigo1.rect.bottom = ANCHO*.1
                    listaEnemigos.append(spriteEnemigo1)

            if tDisparoSatelites >= vDisparoSatelites:
                tDisparoSatelites = 0
                #Dibujar balas satelites
                for satelite in listaSatelites:
                    spriteDisparoSatelite = pygame.sprite.Sprite()
                    spriteDisparoSatelite.image = imgMisilSatelite
                    spriteDisparoSatelite.rect = imgMisilSatelite.get_rect()
                    spriteDisparoSatelite.rect.bottom = satelite.rect.bottom - spriteDisparoSatelite.rect.height*4
                    spriteDisparoSatelite.rect.left = satelite.rect.left + satelite.rect.width//2 - spriteDisparoSatelite.rect.width//2
                    listaMisiles.append(spriteDisparoSatelite)
                #Dibuja las balas de los satelites
                for disparo in listaMisilesSatelites:
                    ventana.blit(disparo, disparo.rect)
                    disparo.rect.bottom += 1
                    if disparo.rect.bottom <= 0:
                        listaMisilesSatelites.remove(disparo)

            #Dibujar los Items
            if tAparecerItems >= 10:
                tAparecerItems = 0
                seleccion = randint(0,2)
                if seleccion == 0:                          #Aparecen Bombas aleatorias
                    spriteBomba = pygame.sprite.Sprite()
                    spriteBomba.image = imgBomba
                    spriteBomba.rect = imgItemPoder.get_rect()
                    spriteBomba.rect.left = randint(ANCHO * .1, ANCHO * .9)
                    spriteBomba.rect.bottom = -50
                    listaItems.append(spriteBomba)
                if seleccion == 1:                          #Aparecen Vidas aleatorios
                    spriteItemVida = pygame.sprite.Sprite()
                    spriteItemVida.image = imgVida
                    spriteItemVida.rect = imgVida.get_rect()
                    spriteItemVida.rect.left = randint(ANCHO * .1, ANCHO * .9)
                    spriteItemVida.rect.bottom = -50
                    listaItems.append(spriteItemVida)
                if seleccion == 3:                          #Aparecen Escudos aleatorias
                    spriteEscudo = pygame.sprite.Sprite()
                    spriteEscudo.image = imgItemPoder
                    spriteEscudo.rect = imgItemPoder.get_rect()
                    spriteEscudo.rect.left = randint(ANCHO * .1, ANCHO * .9)
                    spriteEscudo.rect.bottom = -50
                    listaItems.append(spriteEscudo)
                if seleccion == 2:                          #Aparecen Aceleraciones de disparos aleatorias
                    spriteDiamante = pygame.sprite.Sprite()
                    spriteDiamante.image = imgCaja
                    spriteDiamante.rect = imgCaja.get_rect()
                    spriteDiamante.rect.left = randint(ANCHO * .1, ANCHO * .9)
                    spriteDiamante.rect.bottom = -50
                    listaItems.append(spriteDiamante)
            for item in listaItems:
                xITEM = item.rect.left
                yITEM = item.rect.bottom
                wITEM = item.rect.width
                hITEM = item.rect.height
                xP = spritePersonaje.rect.left
                yP = spritePersonaje.rect.bottom
                #Remover y activar los items
                if xP >= xITEM and xP <= xITEM + wITEM and yP >= yITEM and yP <= yITEM + hITEM: #Comprobar colisión con el jugador
                    if item.image == imgBomba:
                        puntos += len(listaEnemigos)*5
                        listaEnemigos.clear()
                        efectoBomba.play()
                    elif item.image == imgVida:
                        HP += 50
                    elif item.image == imgCaja: #Si se agarra un diamante
                        #Acelerar la velocidad de disparo de los satelites
                        if vDisparoSatelites > .1:
                            vDisparoSatelites -= .3
                    elif item.image == imgItemPoder: #Si se agarra un escudo
                        HP += 50
                    listaItems.remove(item)


            ###ACCIONES DE FUNCIONSES###
            dibujarPlantilla(ventana, juegoPlantilla1, plantilla1_ANCHO, plantilla1_ALTO)

            #Dibujar personaje
            dibujarPersonajes(ventana, spritePersonaje, listaSatelites)
            dibujarObjetivos(ventana, spritePlaneta)
            #dibujarDisparos(ventana,listaMisiles, listaEnemigos)
            # Dibujar los misiles
            for bala in listaMisiles:
                ventana.blit(bala.image, bala.rect)

            # Mueve los misiles
            for bala in listaMisiles:
                bala.rect.bottom -= 10
                #Si la bala llega a la posición 0 se borra
                if bala.rect.bottom <= 0:
                    listaMisiles.remove(bala)

            # Verificar colisión
            for bala in listaMisiles:
                for enemigo in listaEnemigos:
                    # Bala vs enemigo
                    xb = bala.rect.left
                    yb = bala.rect.bottom
                    xe = enemigo.rect.left
                    ye = enemigo.rect.bottom
                    ae = enemigo.rect.width
                    alte = enemigo.rect.height
                    if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte:
                        # Eliminar enemigo y bala
                        listaEnemigos.remove(enemigo)
                        listaMisiles.remove(bala)
                        efectoExplosion.play()
                        puntos += 10
                        break
            #Dibujar enemigos
            dibujarEnemigos(ventana, listaEnemigos)

            dibujarItems(ventana, listaItems)

            #verificarColision(listaEnemigos, spritePersonaje, ventana, BTN_Menu, FONDOperdiste)

            for enemigo in listaEnemigos:
                xE = enemigo.rect.left
                yE = enemigo.rect.bottom
                wE = enemigo.rect.width
                hE = enemigo.rect.height
                xP = spritePersonaje.rect.left
                yP = spritePersonaje.rect.bottom
                xT = spritePlaneta.rect.bottom
                yT = spritePlaneta.rect.left
                wT = spritePlaneta.rect.width
                hT = spritePlaneta.rect.height
                #if xE >= xT and xE <= xT + wT and yE >= yT and yE <= yT + hT:
                 #   estado == PERDIDO
                #Quitar vida en las colisiones
                if xP >= xE and xP <= xE + wE and yP >= yE and yP <= yE + hE: #Comprobar colisión con el jugador
                    HP -= 25
                    listaEnemigos.remove(enemigo)
                if xE >= 290 and xE <= 510 and yE >= 500: #Comprobar la colisión con la tierra
                    HP = 50
                if xE >= 40 and xE <= 128 and yE >= 470: #Comprobar colisión con el satelite 1
                    HP -= 10
                    listaEnemigos.remove(enemigo)
                if xE >= 200 and xE <= 290 and yE >= 470: #Comprobar colisión con el satelite 2
                    HP -= 10
                    listaEnemigos.remove(enemigo)
                if xE >= 520 and xE <= 610 and yE >= 470: #Comprobar colisión con el satelite 3
                    HP -= 10
                    listaEnemigos.remove(enemigo)
                if xE >= 680 and xE <= 770 and yE >= 470: #Comprobar colisión con el satelite 4
                    HP -= 10
                    listaEnemigos.remove(enemigo)


                if yE >= 820 or xE >= 800 or xE <= -10:
                    listaEnemigos.remove(enemigo)



            #Botón de Prueba
            #ventana.blit(BTN_Regresar, (posBTN_Regresar[0],posBTN_Regresar[1]))

            #Condicionales de movimiento
            #Personaje
            if moviendo == ARRIBA:
                spritePersonaje.rect.bottom -= 5
            elif moviendo == ABAJO:
                spritePersonaje.rect.bottom += 5
            elif moviendo == DERECHA:
                spritePersonaje.rect.left += 5
            elif moviendo == IZQUIERDA:
                spritePersonaje.rect.left -= 5

            #Enemigos
            for enemigo in listaEnemigos:
                limite = enemigo.rect.left
                if limite == 700:
                    cambio = IZQUIERDA
                elif limite == 50:
                    cambio = DERECHA
                if cambio == IZQUIERDA:
                    enemigo.rect.left -= 3
                elif cambio == DERECHA:
                    enemigo.rect.left += 3

            # Texto en la pantalla
            puntuacion = TXTpuntuacion.render("Puntuación: {}".format(puntos), 1, BLANCO)
            ventana.blit(puntuacion, (ANCHO*.02, ALTO*.02))
            vida = TXTvida.render("Vida: {}" .format(HP), 1, ROJO)
            ventana.blit(vida, (ANCHO*.7, ALTO*.02))
            TIEMPO = TXTtiempo.render("Tiempo: {}".format(int(TIMER)), 1, AZUL)
            ventana.blit(TIEMPO, (ANCHO * .02, ALTO * .1))

            if HP <= 0:
                #listaPuntajes.append(puntos)
                #listaPuntajes.sort()
                #for puntaje in listaPuntajes:
                 #   salida.write("{}\n" .format(puntaje))
                estado = PERDIDO
                salida = open("Puntuaciones.txt", "w")
                salida.write(str(puntos))
                salida.close()
                print(puntos)
                print(listaPuntajes)

        elif estado == PERDIDO:
            #dibujarPerdido(ventana, BTN_Menu, FONDOperdiste, evento)
            #Si se da click en el botón...
            ventana.blit(FONDOperdiste, (0, 0))
            ventana.blit(gameOver, (ANCHO*.25, ALTO*.2))
            ventana.blit(BTN_Menu, (ANCHO*.435, ALTO*.8))
            #Carga el botón de menú y configura la acción
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if xm >= posBTN_Menu[0] and xm <= posBTN_Menu[0]+BTN_Menu_ANCHO and ym >= posBTN_Menu[1] and ym <= posBTN_Menu[1]+BTN_Menu_ALTO:
                   estado = MENU


        elif estado == PUNTUACIONES:
            #Dibujar el fondo y el título
            ventana.blit(FONDO_Puntuaciones, (0, 0))
            ventana.blit(TITULOpuntuaciones, (posTITULOpunt[0], posTITULOpunt[1]))
            #Carga el archivo
            salida = open("Puntuaciones.txt", "r")
            informacion = salida.read()
            #Dibujar la puntuación
            marcador = TXTmarcador.render("""{}""" .format(informacion), 1, BLANCO)
            ventana.blit(marcador, (ANCHO//2-15, ALTO //2))
            salida.close()
            # Carga el botón de menú y configura la acción
            ventana.blit(BTN_Menu, (ANCHO * .435, ALTO * .8))
            if evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                if xm >= posBTN_Menu[0] and xm <= posBTN_Menu[0] + BTN_Menu_ANCHO and ym >= posBTN_Menu[1] and ym <= \
                        posBTN_Menu[1] + BTN_Menu_ALTO:
                    estado = MENU

        pygame.display.flip()
        reloj.tick(40)
        tAparecerEnemigos += 1/40   #FPS en el denominador
        tAparecerItems += 1/40
        tDisparoSatelites += 1/40
        TIMER += 1/40
    pygame.quit()

    salida.write(listaPuntajes)

def main():
    dibujar()

main()
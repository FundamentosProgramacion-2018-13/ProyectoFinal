#Autor: Víctor Manuel Rodríguez Loyola
#Videojuego The Last Axolote

import pygame   # Librería de pygame
import random

#Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

#Carriles
carrilArriba= 230
carrilAbajo= ALTO-140
carrilCentral= ALTO//2+50
todosloscarriles=[carrilAbajo,carrilCentral,carrilArriba]


#Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (115, 195, 108)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO=(0,0,0)

#Estados
MENU=1
JUGANDO=2
CREDITOS=3
MEJORESPUNTAJES=4
PERDISTE=5
GANASTE=6
pygame.mixer.init()

#Estados de movimiento
QUIETO= 1
ARRIBA= 2
ABAJO=  3

puntos=[]
vida=[100]

# Estructura básica de un programa que usa pygame para dibujar
def dibujarPersonaje(ventana, spritePlanta):
    ventana.blit(spritePlanta.image,spritePlanta.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)

def dibujarTrajineras(ventana, listaTrajineras):
    for traj in listaTrajineras:
        ventana.blit(traj.image, traj.rect)

def dibujarLatas(ventana, listaLatas):
    for lata in listaLatas:
        ventana.blit(lata.image, lata.rect)


def actualizarEnemigos(listaEnemigos):
    for enemigo in listaEnemigos:
        enemigo.rect.left -=4

def actualizarTrajineras(listaTrajineras):
    for traj in listaTrajineras:
        traj.rect.left -=4

def actualizarLatas(listaLatas):
    for lata in listaLatas:
        lata.rect.left -=3


def dibujarBalas(ventana, listafuego):
    for bala in listafuego:
        ventana.blit(bala.image, bala.rect)


def actualizarBalas(listafuego):
    for bala in listafuego:
        bala.rect.left +=10


def verificarColisiones(listafuego,listaEnemigos,listaTrajineras,puntos):
    nuevosPuntos=[]
    #recorre las listas al revés
    for k in range (len(listafuego)-1,-1,-1):
        bala= listafuego[k]
        borrarBala=False
        for e in range(len(listaEnemigos)-1,-1,-1):
            enemigo = listaEnemigos[e]
            xb=bala.rect.left
            yb=bala.rect.bottom
            xe,ye,anchoe,altoe= enemigo.rect
            if xb>=xe and xb<=xe+anchoe and yb>=ye and yb<=ye+altoe:
                listaEnemigos.remove(enemigo) #borra el enemigo de la lista
                borrarBala= True
                puntos.append(20)
                break

        for t in range(len(listaTrajineras)-1,-1,-1):
            traj = listaTrajineras[t]
            xb=bala.rect.left
            yb=bala.rect.bottom
            xe,ye,anchoe,altoe= traj.rect
            if xb>=xe and xb<=xe+anchoe and yb>=ye and yb<=ye+altoe:
                listaTrajineras.remove(traj) #borra el enemigo de la lista
                borrarBala= True
                puntos.append(20)
                break

        if borrarBala:
            listafuego.remove(bala)

    return puntos

def obtenerPuntuacion(puntos):
    listado = []
    highScore= open("PUNTAJES.txt","r")
    pts= str(sum(puntos))
    listado.append(pts)
    listado.sort(reverse=True)

    if len(listado)>3:
        highScores = open("PUNTAJES.txt", "w")
        highScores.write(str(listado[0]))
        highScores.write("\n")
        highScores.write(str(listado[1]))
        highScores.write("\n")
        highScores.write(str(listado[2]))
        highScores.write("\n")
        highScores.close()

    return listado


def perderVida(spriteplanta,vida,listaEnemigos,listaTrajineras):
    xp = spriteplanta.rect.left
    yp = spriteplanta.rect.bottom
    for e in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[e]
        xe, ye, anchoe, altoe = enemigo.rect
        if xp >= xe and xp <= xe + anchoe and yp >= ye and yp <= ye + altoe:
            listaEnemigos.remove(enemigo)
            cuidado=pygame.mixer.Sound("cuidado.wav")
            cuidado.play()
            vida.append(-20)
            break

    for t in range(len(listaTrajineras) - 1, -1, -1):
        traj = listaTrajineras[t]
        xe, ye, anchoe, altoe = traj.rect
        if xp >= xe and xp <= xe + anchoe and yp >= ye and yp <= ye + altoe:
            listaTrajineras.remove(traj)
            cuidado=pygame.mixer.Sound("cuidado.wav")
            cuidado.play()
            vida.append(-20)
            break
    return vida


def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


    #personaje principal
    imgAjolote= pygame.image.load("protagonista3.png")
    spriteAjolote= pygame.sprite.Sprite() #Crea un sprite vacío
    spriteAjolote.image= imgAjolote
    spriteAjolote.rect= imgAjolote.get_rect()
    spriteAjolote.rect.left= 0
    spriteAjolote.rect.bottom= carrilCentral

    #TIMERS
    timer1= 0
    timerJuego=0


    #Trajineras
    listaTrajineras = []
    imgTrajinera = pygame.image.load("trajinera4.png")
    for k in range(1):
        spriteTrajinera = pygame.sprite.Sprite()
        spriteTrajinera.image = imgTrajinera
        spriteTrajinera.rect = imgTrajinera.get_rect()
        spriteTrajinera.rect.left = ANCHO
        spriteTrajinera.rect.bottom = random.choice(todosloscarriles)
        listaTrajineras.append(spriteTrajinera)


    listaEnemigos = []
    imgEnemigo = pygame.image.load("trajinera4.png")
    for k in range (1):
        spriteEnemigo=pygame.sprite.Sprite()
        spriteEnemigo.image=imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = ANCHO
        spriteEnemigo.rect.bottom = random.choice(todosloscarriles)
        listaEnemigos.append(spriteEnemigo)

    #Latas
    listaLatas = []
    imgEnemigo = pygame.image.load("lata4.png")
    for k in range(1):
        spriteLata = pygame.sprite.Sprite()
        spriteLata.image = imgEnemigo
        spriteLata.rect = imgEnemigo.get_rect()
        spriteLata.rect.left = ANCHO
        spriteLata.rect.bottom = random.choice(todosloscarriles)
        listaLatas.append(spriteLata)


    #proyectiles
    imgBala=pygame.image.load("roca4.png")
    listafuego= []

    #Estado del juego
    estado= MENU

    #Imágenes para el menú
    imgFondoMenu= pygame.image.load("TLAMenu.png")
    imgFondoPerdiste= pygame.image.load("PERDIDO2.png")
    imgFondoGanaste= pygame.image.load("GANASTE2.png")
    imgFondoCreditos= pygame.image.load("TLACRED2.png")
    imgFondoPuntajes= pygame.image.load("PUNTAJES2.png")

    #Imágenes para el juego
    imgFondo= pygame.image.load("fondoJUEGO1.png")
    xFondo=0

    carril = 0

    #Audio
    sonidoDisparar = pygame.mixer.Sound("lanzar.wav")
    pygame.mixer.set_num_channels(10)
    if estado==MENU:
        pygame.mixer.music.load("cancionxd.mp3")
        pygame.mixer.music.play(-1)
    elif estado==JUGANDO:
        pygame.mixer.music.load("BGjugando.mp3")
        pygame.mixer.music.play(-1)
    elif estado== PERDISTE:
        pygame.mixer.music.load("muerte.mp3")
        pygame.mixer.music.play(-1)
    elif estado== GANASTE:
        pygame.mixer.music.load("victory.mp3")
        pygame.mixer.music.play(-1)
    elif estado== CREDITOS:
        pygame.mixer.music.load("cancionxd.mp3")
        pygame.mixer.music.play(-1)
    elif estado == MEJORESPUNTAJES:
        pygame.mixer.music.load("cancionxd.mp3")
        pygame.mixer.music.play(-1)


    #Texto
    fuente= pygame.font.SysFont("arial", 30)
    pantallas= pygame.font.SysFont("arial",65)

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo

            elif evento.type == pygame.KEYDOWN:

                if evento.key == pygame.K_UP:
                    if carril==0:
                        carril += 1
                        spriteAjolote.rect.bottom = carrilCentral
                    if carril==1:
                        carril+=0
                        spriteAjolote.rect.bottom=carrilArriba
                    if carril == -1:
                        carril += 1
                        spriteAjolote.rect.bottom = carrilCentral

                elif evento.key == pygame.K_DOWN:
                    if carril==0:
                        carril -= 1
                        spriteAjolote.rect.bottom = carrilAbajo
                    if carril==-1:
                        carril-=0
                        spriteAjolote.rect.bottom= carrilAbajo
                    if carril==1:
                        carril-=1
                        spriteAjolote.rect.bottom = carrilCentral

                elif evento.key == pygame.K_z: #Dispara
                    sonidoDisparar.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spriteAjolote.rect.width
                    spriteBala.rect.bottom = spriteAjolote.rect.bottom
                    listafuego.append(spriteBala)

                elif evento.key == pygame.K_ESCAPE:
                    estado = MENU
                    pygame.mixer.music.load("cancionxd.mp3")
                    pygame.mixer.music.set_volume(1.0)
                    pygame.mixer.music.play(-1)
                    timerJuego=0


            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm,ym= pygame.mouse.get_pos()
                xjugar= ANCHO//2+115
                yjugar= ALTO//2-10
                anchojugar= 2501
                altojugar= 73

                xcreditos = ANCHO // 2 +10
                ycreditos = ALTO // 2 +75
                anchocreditos = 250
                altocreditos = 150

                xpuntajes = ANCHO // 2 + 10
                ypuntajes = ALTO // 2 + 165
                anchopuntajes = 250
                altopuntajes = 60

                if xm>=xjugar and xm<=xjugar+anchojugar and ym>=yjugar and ym<=yjugar+altojugar:
                    estado=JUGANDO
                    pygame.mixer.music.load("BGjugando.mp3")
                    pygame.mixer.music.play(-1)
                if xm>=xcreditos and xm<=xcreditos+anchocreditos and ym>=ycreditos and ym<=yjugar+altocreditos:
                    estado=CREDITOS
                    pygame.mixer.music.load("cancionxd.mp3")
                    pygame.mixer.music.play(-1)
                if xm>=xpuntajes and xm<=xpuntajes+anchopuntajes and ym>=ypuntajes and ym<=ypuntajes+altopuntajes:
                    estado=MEJORESPUNTAJES
                    pygame.mixer.music.load("cancionxd.mp3")
                    pygame.mixer.music.play(-1)


        totalpuntos = sum(puntos)
        totalvida = sum(vida)
        progreso= fuente.render("Progreso: %d"%timerJuego,1,BLANCO)
        ptosFinal= pantallas.render("%d"%totalpuntos, 1, BLANCO)
        ptos = fuente.render("Puntos: %d"%totalpuntos, 1, BLANCO)
        vidaRestante = fuente.render("Vida: %d" % totalvida, 1, BLANCO)


        #Pregunta en qué estado está el juego

        if estado== JUGANDO:
            if timer1 >2:
                timer1=0
                spriteLata = pygame.sprite.Sprite()
                spriteLata.image = imgEnemigo
                spriteLata.rect = imgEnemigo.get_rect()
                spriteLata.rect.left = ANCHO
                spriteLata.rect.bottom = random.choice(todosloscarriles)
                listaLatas.append(spriteLata)

                spriteTrajinera = pygame.sprite.Sprite()
                spriteTrajinera.image = imgTrajinera
                spriteTrajinera.rect = imgTrajinera.get_rect()
                spriteTrajinera.rect.left = ANCHO
                spriteTrajinera.rect.bottom = random.choice(todosloscarriles)
                listaTrajineras.append(spriteTrajinera)

                spriteEnemigo = pygame.sprite.Sprite()
                spriteEnemigo.image = imgEnemigo
                spriteEnemigo.rect = imgEnemigo.get_rect()
                spriteEnemigo.rect.left = ANCHO
                spriteEnemigo.rect.bottom = random.choice(todosloscarriles)
                listaEnemigos.append(spriteEnemigo)


            #Actualizar objetos
            verificarColisiones(listafuego, listaEnemigos,listaTrajineras,puntos)
            perderVida(spriteAjolote,vida,listaEnemigos,listaTrajineras)
            actualizarEnemigos(listaEnemigos)
            actualizarBalas(listafuego)
            actualizarTrajineras(listaTrajineras)

            timerJuego += 1 / 20
            # Borrar pantalla
            ventana.fill(VERDE_BANDERA)
            ventana.blit(imgFondo,(xFondo,0))
            ventana.blit(imgFondo,(xFondo+800,0))
            xFondo-=3
            if xFondo<=-800:
                xFondo=0

            # Dibujar
            dibujarPersonaje(ventana,spriteAjolote)
            dibujarEnemigos(ventana,listaEnemigos)
            dibujarBalas(ventana,listafuego)
            dibujarTrajineras(ventana,listaTrajineras)

            nivel= fuente.render("Nivel 1",1,BLANCO)
            ventana.blit(progreso,(150,20))
            ventana.blit(ptos,(ANCHO-200,20))
            ventana.blit(vidaRestante,(ANCHO-350,20))
            ventana.blit(nivel,(15,20))

            if timerJuego >= 100:
                estado = GANASTE
                pygame.mixer.music.load("victory.mp3")
                pygame.mixer.music.play(0)

            if totalvida == 0:
                estado = PERDISTE
                pygame.mixer.music.load("muerte.mp3")
                pygame.mixer.music.play(0)


        elif estado==MENU:
            # Borrar pantalla
            ventana.fill(BLANCO)
            ventana.blit(imgFondoMenu, (0,0))
        elif estado==GANASTE:
            ventana.fill(BLANCO)
            ventana.blit(imgFondoGanaste, (0, 0))
            ventana.blit(ptosFinal, (ANCHO // 2, ALTO // 2 - 30))
        elif estado== CREDITOS:
            ventana.fill(BLANCO)
            ventana.blit(imgFondoCreditos, (0, 0))
        elif estado== PERDISTE:
            ventana.blit(imgFondoPerdiste, (0, 0))
            ventana.blit(ptosFinal,(ANCHO//2,ALTO//2-30))
        elif estado==MEJORESPUNTAJES:
            ventana.blit(imgFondoPuntajes,(0,0))
            marcadores = obtenerPuntuacion(puntos)
            if len(marcadores)==1:
                texto = fuente.render(str(marcadores[0]), 1, BLANCO)
                ventana.blit(texto, (ALTO // 2 + 50, 160))
            if len(marcadores) == 2:
                texto = fuente.render(str(marcadores[0]), 1, BLANCO)
                ventana.blit(texto, (ALTO // 2 + 50, 160))
                texto2 = fuente.render(str(marcadores[1]), 1, BLANCO)
                ventana.blit(texto2, (ALTO // 2 + 50, 260))
            if len(marcadores) >2:
                texto = fuente.render(str(marcadores[0]), 1, BLANCO)
                ventana.blit(texto, (ALTO // 2 + 50, 160))
                texto2 = fuente.render(str(marcadores[1]), 1, BLANCO)
                ventana.blit(texto2, (ALTO // 2 + 50, 260))
                texto3 = fuente.render(str(marcadores[2]), 1, BLANCO)
                ventana.blit(texto3, (ALTO // 2 + 50, 360))





        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps
        timer1+= 1/40


    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
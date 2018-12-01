# Autor: Erick David Ramírez artínez

import pygame   # Librería de pygame
from random import randint  # Randint se usa para generar algunos números aleatorios

# Dimensiones de la pantalla
ANCHO = 600
ALTO = 800

# Colores
NEGRO = (0, 0, 0)       # Nada de color
VERDE_BANDERA = (36,200,50)
ROJO = (200,0,0)

# Estados del juego
MENU = 1
JUGANDO = 2
PUNTUACION = 3
CREDITOS = 4
SALIR = 5
COMOJUGAR = 6
ganar = False

# Estados de movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
DERECHA  = 4
IZQUIERDA = 5


# Función para dibujar a nuestro personaje principal: Reimu Hakurei
def dibujarPersonaje(ventana, spriteReimu):
    ventana.blit(spriteReimu.image, spriteReimu.rect)


# Función que dibuja los enemigos generados en la oleada
def dibujarEnemigos(ventana, listaEnemigos):
    for Enemigo in listaEnemigos:
        ventana.blit(Enemigo.image, Enemigo.rect)


# Función que da movimiento solo a las hadas
def actualizarHadas(listaHadas):
    for Hada in listaHadas:
        Hada.rect.bottom += 1
        if Hada.rect.bottom > ALTO + Hada.rect.height:
            listaHadas.remove(Hada)


# Función que dibuja los proyectiles generados
def dibujarProyectil(ventana, listaProyectil):
    for Proyectil in listaProyectil:
        ventana.blit(Proyectil.image, Proyectil.rect)


# Función que da movimiento a los proyectiles de Reimu
def actualizarProyectil(listaProyectil):
    for Proyectil in listaProyectil:
        Proyectil.rect.bottom -= 15


# Función que da movimiento a los proyectiles de los espíritus
def actualizarProyectilEnemigo(listaProyectilEnemigo):
    for Proyectil in listaProyectilEnemigo:
        Proyectil.rect.bottom += 15


# Función que verifica si los proyectiles de Reimu dan con el enemigo
def verificarColisiones(listaProyectil, listaEnemigos, puntuacion,puntuacionAux):
    # recorre las listas al revés
    for k in range(len(listaProyectil)-1, -1, -1):
        Proyectil = listaProyectil[k]
        borrarProyectil = False
        for e in range(len(listaEnemigos)-1, -1, -1):
            Enemigo = listaEnemigos[e]
            # Proyectil vs Hada
            xb = Proyectil.rect.left
            yb = Proyectil.rect.bottom
            xe, ye, anchoe, altoe, = Enemigo.rect
            if xb >= xe and xb <= xe + anchoe and yb >= ye and yb <= ye + altoe:
                listaEnemigos.remove(Enemigo)  # borra de la lista
                borrarProyectil = True
                puntuacion += 100
                puntuacionAux += 100
                break
            if yb < 0:
                borrarProyectil = True
                break
        if borrarProyectil:
            listaProyectil.remove(Proyectil)
    return puntuacion,puntuacionAux


# Función que verifica si los proyectiles enemigos dan con Reimu
def verificarColisionesEnemigas(listaProyectilEnemigo, spriteReimu, vidas):
    for k in range(len(listaProyectilEnemigo)-1, -1, -1):
        Proyectil = listaProyectilEnemigo[k]
        borrarProyectil = False
        xb = Proyectil.rect.left
        yb = Proyectil.rect.bottom
        xr, yr, anchor, altor, = spriteReimu.rect
        if xb >= xr and xb <= xr + anchor and yb >= yr and yb <= yr + altor:
            vidas -= 1
            borrarProyectil = True
        if yb > ALTO:
            borrarProyectil = True
        if borrarProyectil:
            listaProyectilEnemigo.remove(Proyectil)
    return vidas


# Función que dibuja la pantalla y los eventos pygame
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO 600 de ancho y 800 de alto
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    # Personaje principal, aquí se genera el modelo y posición de Reimu, nuestro personaje principal
    imgReimu = pygame.image.load("reimu.png")
    spriteReimu = pygame.sprite.Sprite()  # Sprite Vacío
    spriteReimu.image = imgReimu
    spriteReimu.rect = imgReimu.get_rect()
    spriteReimu.rect.left = ANCHO//2 + spriteReimu.rect.width//2
    spriteReimu.rect.bottom = ALTO - spriteReimu.rect.height

    # Al principio Reimu no se mueve a ningun lado
    movimientoV = QUIETO
    movimientoH = QUIETO

    # Proyectiles y sus sprites
    imgProyectil = pygame.image.load("orbeAzul.png")
    listaProyectil = []
    imgProyectilEnemigo = pygame.image.load("orbeRojo.png")
    listaProyectilEnemigo = []

    # Estados del juego iniciales
    estado = MENU    # Inicial
    puntuacion = 0
    puntuacionAux = 0
    oleada = 0
    vidas = 3

    # Imágenes para el menú
    imgMenu = pygame.image.load("fondoMenu.png")
    imgBtnJugar = pygame.image.load("btnjugar.png")
    imgBtnMenu = pygame.image.load("btnmenu.png")
    imgBtnSalir = pygame.image.load("btnsalir.png")
    imgBtnCreditos = pygame.image.load("btncreditos.png")
    imgBtnComoJugar = pygame.image.load("btncomo.png")

    # Imágenes para el juego
    imgFondo = pygame.image.load("cielo.png")
    yFondo = ALTO-1400
    imgFondoPuntuacion = pygame.image.load("fondoPuntuacion.png")
    imgFondoCreditos = pygame.image.load("creditos.png")
    imgFondoComoJugar = pygame.image.load("comojugar.png")

    # Acumuladores de tiempo
    timer1 = 60 # Acumulador de tiempo de oleadas
    timer2 = 0 # Acumulador de tiempo para iniciar la música
    timer3 = 0 # Acumulador de tiempo para disparos enemigos

    # Audio predeterminado, cambia dentro de los estados del juego
    pygame.mixer.init()
    pygame.mixer.music.load("musicaFondo.mp3")
    pygame.mixer.music.play(-1)

    # Fuentes del juego
    fuente = pygame.font.SysFont("forte", 27)
    fuenteGrande = pygame.font.SysFont("forte", 54)

    # Hadas y espíritus, incialmente ninguno
    listaHadas = []  # Lista vacía de Hadas
    listaEspiritus = []

    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Se termina el programa
            # Interacción con el usuario, verifica en que botones hace clic el usuario o que teclas presiona
            # para mover a Reimu, si una flecha se presiona, reimu se mueve a esa dirección, si se suelta el
            # botón, deja de moverse, siguiendo esa lógica Reimu se moverá si se mantienen presionados los botones.
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    movimientoV = ARRIBA
                elif evento.key == pygame.K_DOWN:
                    movimientoV = ABAJO
                elif evento.key == pygame.K_RIGHT:
                    movimientoH = DERECHA
                elif evento.key == pygame.K_LEFT:
                    movimientoH = IZQUIERDA
                elif evento.key == pygame.K_z:  # Disparo
                    spriteProyectil = pygame.sprite.Sprite()
                    spriteProyectil.image = imgProyectil
                    spriteProyectil.rect = imgProyectil.get_rect()
                    spriteProyectil.rect.left = spriteReimu.rect.width // 2 + spriteReimu.rect.left
                    spriteProyectil.rect.bottom = spriteReimu.rect.bottom - spriteReimu.rect.height // 2
                    listaProyectil.append(spriteProyectil)
                    ataqueReimu.play()
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_UP:
                    # spriteReimu.rect.bottom -= 5
                    movimientoV = QUIETO
                elif evento.key == pygame.K_DOWN:
                    # spriteReimu.rect.bottom += 5
                    movimientoV = QUIETO
                elif evento.key == pygame.K_RIGHT:
                    # spriteReimu.rect.left += 5
                    movimientoH = QUIETO
                elif evento.key == pygame.K_LEFT:
                    # spriteReimu.rect.left -= 5
                    movimientoH = QUIETO
            # Verifica la posición de los botones y donde hace clic el usuario
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                xm, ym = pygame.mouse.get_pos()
                xbJ = ANCHO-200
                ybJ = ALTO//2 - 50
                xbC = ANCHO - 200
                ybC = ALTO // 2 + 20
                xbS = ANCHO - 200
                ybS = ALTO // 2 + 90
                xbM = 0
                ybM = 0
                xbCJ = ANCHO-380
                ybCJ = ALTO//2+160
                anchoBJ = 135
                altoBJ = 50
                anchoBC = 173
                altoBC = 50
                anchoBS = 117
                altoBS = 50
                anchoBM = 128
                altoBM = 50
                anchoBCJ = 301
                altoBCJ = 50
                if xm>=xbJ and xm<=xbJ+anchoBJ and ym>=ybJ and ym<=ybJ+altoBJ:
                    estado = JUGANDO
                elif xm>=xbC and xm<=xbC+anchoBC and ym>=ybC and ym<=ybC+altoBC:
                    estado = CREDITOS
                elif xm>=xbS and xm<=xbS+anchoBS and ym>=ybS and ym<=ybS+altoBS:
                    estado = SALIR
                elif xm>=xbM and xm<=xbM+anchoBM and ym>=ybM and ym<=ybM+altoBM:
                    estado = MENU
                elif xm >= xbCJ and xm <= xbCJ + anchoBCJ and ym >= ybCJ and ym <= ybCJ + altoBCJ:
                    estado = COMOJUGAR

        # Estados del juego, lo que se muestra dependiendo de donde estemos
        if estado == MENU:  # Se genera el menú del juego y sus accesos a otras partes del juego
            ventana.fill(NEGRO)
            ventana.blit(imgMenu, (0,0))
            ventana.blit(imgBtnJugar, (ANCHO-200, ALTO//2-50))
            ventana.blit(imgBtnCreditos, (ANCHO-200, ALTO//2+20))
            ventana.blit(imgBtnSalir, (ANCHO-200, ALTO//2+90))
            ventana.blit(imgBtnComoJugar, (ANCHO-380, ALTO//2+160))
            # Oleadas, vida, puntuación, etc. Vuelven a sus valores iniciales
            vidas = 3
            oleada = 0
            puntuacion = 0
            puntuacionAux = 0
            listaEspiritus = []
            listaHadas = []
            listaProyectilEnemigo = []
            listaProyectil = []
            spriteReimu.rect.left = ANCHO // 2 + spriteReimu.rect.width // 2
            spriteReimu.rect.bottom = ALTO - spriteReimu.rect.height
            timer3 = 0
            timer2 = 0
            timer1 = 60

        if estado == COMOJUGAR:  # Muestra las instrucciones
            ventana.blit(imgFondoComoJugar, (0,0))
            ventana.blit(imgBtnMenu, (0, 0))

        if estado == CREDITOS:  # Muestra los créditos
            ventana.blit(imgFondoCreditos, (0,0))
            ventana.blit(imgBtnMenu, (0, 0))

        if estado == SALIR:  # Termina el juego
            termina = True

        elif estado == PUNTUACION:  # Muestra la puntuación final y la puntuación más alta
            if timer2 == 0:
                puntuacionAlta = 0
                listaPuntuaciones = []
                timer2 += 1 / 40
                pygame.mixer.stop()
                pygame.mixer.init()
                pygame.mixer.music.load("musicaFondo3.mp3")
                pygame.mixer.music.play(-1)
                ventana.blit(imgFondoPuntuacion, (0,0))
                textoPuntuacion = fuenteGrande.render("Puntuación: %d" % puntuacion, 1, (80,201,206))

                # Se obtienen las puntuaciones anteriores en una lista y se le agrega la actual
                archivoPuntuacionesR = open("puntuaciones.txt", "r")
                for linea in archivoPuntuacionesR:
                    puntuacionAnterior = ""
                    if linea != "\n":
                        for numero in linea:
                            puntuacionAnterior += str(numero)
                        listaPuntuaciones.append(puntuacionAnterior)
                listaPuntuaciones.append("\n"+str(int(puntuacion)))
                archivoPuntuacionesR.close()

                # Se calcula cual fue la puntuación mayor
                for cadena in listaPuntuaciones:
                    if cadena != "\n":
                        puntuacionComparar = int(cadena)
                        if puntuacionComparar > puntuacionAlta:
                            puntuacionAlta = puntuacionComparar

                textoPuntuacionAlta = fuente.render("Puntuacion más alta: %d" % puntuacionAlta, 1, (80,201,206))

                # Se agregan todas las puntuaciones a un archivo
                archivoPuntuacionesW = open("puntuaciones.txt", "w")
                for k in range(len(listaPuntuaciones)):
                    archivoPuntuacionesW.write(listaPuntuaciones[k])
                archivoPuntuacionesW.close()

            if ganar:  # Si completas la oleada 9, ganas el juego
                ganaste = fuente.render("¡¡¡GANASTE!!!",1, (80,201,206))
                ventana.blit(ganaste, (ANCHO//2-100, 5))

            ventana.blit(textoPuntuacion, (5, ALTO//2-20))
            ventana.blit(textoPuntuacionAlta, (5, ALTO//2+30))
            ventana.blit(imgBtnSalir, (ANCHO-200, ALTO//2+90))
            ventana.blit(imgBtnMenu, (0, 0))

        elif estado == JUGANDO:  # Estado jugando, aquí aparecen enemigos, incrementa el marcador, etc.
            if puntuacionAux > 500:
                puntuacionAux -= 500
                vidas += 1
            ganar = False
            puntuacionAux += 1/10
            puntuacion += 1 / 10

            # Se inicia la música
            if timer2 == 0:
                pygame.mixer.stop()
                pygame.mixer.init()
                ataqueEnemigo = pygame.mixer.Sound("ataqueEnemigo.wav")
                ataqueReimu = pygame.mixer.Sound("ataqueReimu.wav")
                pygame.mixer.music.load("musicaFondo2.mp3")
                pygame.mixer.music.play(-1)
                timer2 = 5

            timer1 -= 1 / 40
            timer3 += 1 / 40

            # Actualizar objetos, enemigos, balas, colisiones y puntuación, los espíritus no se mueven
            actualizarHadas(listaHadas)
            actualizarProyectil(listaProyectil)
            actualizarProyectilEnemigo(listaProyectilEnemigo)

            puntuacion, puntuacionAux = verificarColisiones(listaProyectil, listaHadas, puntuacion,puntuacionAux)
            puntuacion, puntuacionAux = verificarColisiones(listaProyectil, listaEspiritus, puntuacion,puntuacionAux)
            vidas = verificarColisionesEnemigas(listaProyectilEnemigo, spriteReimu, vidas)

            # Se verifica si hay hadas o el timer es 0
            if timer1 < 0 or (listaHadas == [] and listaEspiritus == []):
                listaHadas = []
                listaEspiritus = []
                timer1 = 60
                timer2 += 1/40
                timer3 = 0

            # Si no hay hadas o el timer es 0 entonces genera enemigos
            if timer1 == 60 and timer2 > 10:
                oleada += 1
                if oleada != 10:
                    if oleada > 1:
                        puntuacion += 200
                        puntuacionAux += 200
                    listaHadas = []  # Lista vacía de Hadas
                    imgHada = pygame.image.load("hada1.png")
                    for k in range(2*oleada):  # Los enemigos aumentan de 2 en 2 por cada oleada que transcurre
                        tipoHada = randint(1, 6)  # Genera un número aleatorio para seleccionar el color del hada
                        if tipoHada == 1:
                            imgHada = pygame.image.load("hada1.png")
                        if tipoHada == 2:
                            imgHada = pygame.image.load("hada2.png")
                        if tipoHada == 3:
                            imgHada = pygame.image.load("hada3.png")
                        if tipoHada == 4:
                            imgHada = pygame.image.load("hada4.png")
                        if tipoHada == 5:
                            imgHada = pygame.image.load("hada5.png")
                        spriteHada = pygame.sprite.Sprite()
                        spriteHada.image = imgHada
                        spriteHada.rect = imgHada.get_rect()
                        spriteHada.rect.left = randint(0, ANCHO-spriteHada.rect.width)
                        spriteHada.rect.bottom = randint(0, ALTO // 2)
                        listaHadas.append(spriteHada)

                        listaEspiritus = []
                        imgEspiritu = pygame.image.load("espiritu.png")
                    for k in range(2*oleada):  # Los espíritus se generan igual que las hadas pero de 1 solo color
                        spriteEspiritu = pygame.sprite.Sprite()
                        spriteEspiritu.image = imgEspiritu
                        spriteEspiritu.rect = imgEspiritu.get_rect()
                        spriteEspiritu.rect.left = randint(spriteEspiritu.rect.width, ANCHO-spriteEspiritu.rect.width)
                        spriteEspiritu.rect.bottom = randint(40, ALTO//2)
                        listaEspiritus.append(spriteEspiritu)
                    
                timer2 = 5
            if vidas < 0 or oleada == 10:  # Si pasas la última oleada o pierdes todas las vidas, acaba el juego
                if oleada == 10:
                    ganar = True
                estado = PUNTUACION
                timer2 = 0

            if timer3 > 1:  # Los espíritus disparan cada segundo
                timer3 = 0
                for e in listaEspiritus:
                    spriteProyectilEnemigo = pygame.sprite.Sprite()
                    spriteProyectilEnemigo.image = imgProyectilEnemigo
                    spriteProyectilEnemigo.rect = imgProyectilEnemigo.get_rect()
                    spriteProyectilEnemigo.rect.left = e.rect.width // 2 + e.rect.left
                    spriteProyectilEnemigo.rect.bottom = e.rect.bottom - e.rect.height // 2
                    listaProyectilEnemigo.append(spriteProyectilEnemigo)
                    ataqueEnemigo.play()

            # Mover personaje
            if movimientoV == ARRIBA:
                spriteReimu.rect.bottom -= 5
            elif movimientoV == ABAJO:
                spriteReimu.rect.bottom += 5
            if movimientoH == DERECHA:
                spriteReimu.rect.left += 5
            if movimientoH == IZQUIERDA:
                spriteReimu.rect.left -= 5

            # Fondo del juego
            ventana.fill(VERDE_BANDERA)
            ventana.blit(imgFondo, (0, yFondo))
            ventana.blit(imgFondo, (0, yFondo-1400))  # 1400 es el alto del fondo
            yFondo += 5
            if yFondo == 1400:
                yFondo = 0

            # Se dibujan los enemigos
            dibujarPersonaje(ventana, spriteReimu)
            dibujarEnemigos(ventana, listaHadas)
            dibujarEnemigos(ventana, listaEspiritus)
            dibujarProyectil(ventana, listaProyectil)
            dibujarProyectil(ventana, listaProyectilEnemigo)

            # Se dibujan la puntuación, el reloj y las vidas
            texto = fuente.render("%d" % timer1, 1, (80,201,206))
            textoPuntuacion = fuente.render("%d" % puntuacion, 1, (80,201,206))
            textoVidas = fuente.render("Vidas: %d" % vidas, 1, (80,201,206))
            ventana.blit(texto, (180, 0))
            ventana.blit(textoPuntuacion, (0,0))
            ventana.blit(textoVidas, (380,0))

        pygame.display.flip()  # Actualiza trazos
        reloj.tick(40)  # 40 fps

    pygame.quit()  # termina pygame


# Función principal, aquí se llama a la función que ejecuta el juego
def main():
    dibujar()   # Se ejecuta el juego


# Se ejecuta la función principal con el juego
main()
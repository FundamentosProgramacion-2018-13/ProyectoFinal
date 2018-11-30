# Autor: Luis Humberto Burgueño Paz
# Videojuego


import pygame   # Librería de pygame
from random import randint
import math

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NEGRO = (0, 0, 0)

# Estados
MENU = 1
JUGANDO = 2
COMOJUGAR = 3
SCOREBOARD = 4
GAMEOVER = 5

# Estados de Movimiento
QUIETO = 1
ARRIBA = 2
ABAJO = 3
DERECHA = 4
IZQUIERDA = 5


# Dibuja la nave del jugador.
def dibujarPersonaje(ventana, spriteNaveJugador):
   ventana.blit(spriteNaveJugador.image, spriteNaveJugador.rect)


# Dibuja a los enemigos.
def dibujarEnemigos(ventana, listaEnemigos):
   for enemigo in listaEnemigos:
       ventana.blit(enemigo.image, enemigo.rect)


# Movimiento de los enemigos.
def actualizarEnemigos(listaEnemigos, angulo):
   for enemigo in listaEnemigos: # Visita cada enemigo
       d = 5*math.sin(math.radians(angulo))
       enemigo.rect.bottom += int(d)


# Dibuja las balas del jugador.
def dibujarBalas(ventana, listaBalasAliadas):
   for bala in listaBalasAliadas:
       ventana.blit(bala.image, bala.rect)


# Movimiento de las balas Aliadas.
def actualizarBalas(listaBalasAliadas):
   for bala in listaBalasAliadas:
       bala.rect.left += 30


# Verifica si la bala del jugador conectó con un enemigo.
def verificarColisiones(listaBalasAliadas, listaEnemigos, numEnemigos):
   if len(listaEnemigos) == 0:
       generarEnemigos(listaEnemigos, numEnemigos)
   # recorre las listas al revés
   for k in range(len(listaBalasAliadas)-1, -1, -1):
       bala = listaBalasAliadas[k]
       for e in range(len(listaEnemigos)-1, -1, -1):
           enemigo = listaEnemigos[e]
           # bala vs enemigo
           xb = bala.rect.left
           yb = bala.rect.bottom
           xe, ye, anchoe, altoe = enemigo.rect
           if xb>=xe and xb <= xe + anchoe and yb >= ye and yb <= ye + altoe:
               listaEnemigos.remove(enemigo)   # Borra de la lista
               listaBalasAliadas.remove(bala)
               return 100
           elif xb>ANCHO:
               listaBalasAliadas.remove(bala)
               return 0
   return 0



# Movimiento de los obstáculos.
def actualizarAsteroides(listaAsteroides, velocidadAsteroide):
    for asteroide in listaAsteroides:
        asteroide.rect.left -= velocidadAsteroide
    if asteroide.rect.left <= -ANCHO:
        asteroide.rect.left = ANCHO + 100
        asteroide.rect.bottom = randint(0, ALTO)


# Dibuja los obstáculos.
def dibujarAsteroides(ventana, listaAsteroides):
    for asteroide in listaAsteroides:
        ventana.blit(asteroide.image, asteroide.rect)


# Genera 15 enemigos.
def generarEnemigos(listaEnemigos, numEnemigos):
    imgEnemigo = pygame.image.load("naveEnemiga.png")
    for k in range(numEnemigos):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(2*ANCHO // 3, ANCHO-35)
        spriteEnemigo.rect.bottom = randint(3*ALTO//8-75, 6*ALTO//8)
        listaEnemigos.append(spriteEnemigo)


# Verifica si el jugador chocó con un obstáculo para restarle vida si es necesario.
def verificarChoqueAsteroide(spriteNaveJugador, listaAsteroides):
    xNJ, yNJ, anchoNJ, altoNJ = spriteNaveJugador.rect
    xA, yA, anchoA, altoA = listaAsteroides[0].rect
    if xNJ>=xA and xNJ<=xA+anchoA and yNJ>=yA+25 and yNJ<=yA+altoA-25:
        listaAsteroides[0].rect.left = 2*ANCHO
        listaAsteroides[0].rect.bottom = randint(0, ALTO)
        return 50
    else:
        yNJ += altoNJ
        if xNJ>=xA and xNJ<=xA+anchoA and yNJ>=yA+25 and yNJ<=yA+altoA-25:
            listaAsteroides[0].rect.left = 2*ANCHO
            listaAsteroides[0].rect.bottom = randint(0, ALTO)
            return 50
    return 0


# Dibuja las balas enemigas.
def dibujarBalasEnemigas(ventana, listaBalasEnemigas):
    for bala in listaBalasEnemigas:
        ventana.blit(bala.image, bala.rect)


# Realiza el movimiento de las balas Enemigas.
def actualizarBalasEnemigas(listaBalasEnemigas):
    for bala in listaBalasEnemigas:
        bala.rect.left -= 30


# Verifica si las balas enemigas le dieron al jugador para restarle vida.
def verificarBalas(spriteNaveJugador, listaBalasEnemigas):
    for k in range(len(listaBalasEnemigas) - 1, -1, -1):
        bala = listaBalasEnemigas[k]
        xb = bala.rect.left
        yb = bala.rect.bottom
        xNJ, yNJ, anchoNJ, altoNJ = spriteNaveJugador.rect
        if xb >= xNJ and xb <= xNJ + anchoNJ and yb >= yNJ and yb <= yNJ + altoNJ:
            listaBalasEnemigas.remove(bala)
            return 25
        elif xb < 0:
            listaBalasEnemigas.remove(bala)
            return 0
    return 0


# Verifica que el jugador esté dentro de la zona de juego. Si no está le hace daño.
def verificarJugadorZona(spriteNaveJugador):
    xNJ, yNJ, anchoNJ, altoNJ = spriteNaveJugador.rect
    if xNJ+anchoNJ<=0 or xNJ>=ANCHO or yNJ>=ALTO or yNJ+altoNJ<=0:
        return 1
    return 0


# Verifica si el jugador choca con una nave.
def verificarColisionEnemiga(spriteNaveJugador, listaEnemigos):
    for e in range(len(listaEnemigos) - 1, -1, -1):
        enemigo = listaEnemigos[e]
        # bala vs enemigo
        xNJ, yNJ, anchoNJ, altoNJ = spriteNaveJugador.rect
        xe, ye, anchoe, altoe = enemigo.rect
        if xNJ >= xe and xNJ <= xe + anchoe and yNJ >= ye and yNJ <= ye + altoe:
            listaEnemigos.remove(enemigo)  # Borra de la lista
            return 100
        else:
            yNJ += altoNJ
            if xNJ >= xe and xNJ <= xe + anchoe and yNJ >= ye and yNJ <= ye + altoe:
                listaEnemigos.remove(enemigo)  # Borra de la lista
                return 100
    return 0

# Función Principal de pygame.
def dibujar():
   # Inicializa el motor de pygame
   pygame.init()
   # Crea una ventana de ANCHO x ALTO
   ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
   reloj = pygame.time.Clock()  # Para limitar los fps
   termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


   # Personaje Principal
   imgNaveJugador = pygame.image.load("naveJugador.png")
   spriteNaveJugador = pygame.sprite.Sprite()  # Sprite vacío
   spriteNaveJugador.image = imgNaveJugador
   spriteNaveJugador.rect = imgNaveJugador.get_rect()
   spriteNaveJugador.rect.left = 0
   spriteNaveJugador.rect.bottom = ALTO // 2 + spriteNaveJugador.rect.height // 2

   movimiento = QUIETO

   # Enemigos
   listaEnemigos = [] # Lista vacía de enemigos
   numEnemigos = 15


   # Balas
   imgBalaAliada = pygame.image.load("balaAliada.png")
   listaBalasAliadas = []
   imgBalaEnemiga = pygame.image.load("balaEnemiga.png")
   listaBalasEnemigas = []
   limite = 1.5

   # Asteroides
   listaAsteroides = []
   imgAsteroide = pygame.image.load("asteroides.png")
   for k in range(1):
       spriteAsteroide = pygame.sprite.Sprite()
       spriteAsteroide.image = imgAsteroide
       spriteAsteroide.rect = imgAsteroide.get_rect()
       spriteAsteroide.rect.left = ANCHO
       spriteAsteroide.rect.bottom = randint(0, ALTO)
       listaAsteroides.append(spriteAsteroide)
   velocidadAsteroide = 5

   # Estado del Juego
   estado = MENU   # Inicial

   # Puntaje más alto (archivo)
   entrada = open("mayorPuntaje.txt")
   leermayorPuntaje = entrada.readline()
   mayorPuntaje = int(leermayorPuntaje)
   entrada.close()

   # Imágenes para el menú
   imgBtnJugar = pygame.image.load("btnJugar.png")
   xBtnJ, yBtnJ, anchoBtnJ, altoBtnJ = imgBtnJugar.get_rect() # Dimensiones botón
   imgBtnComoJugar = pygame.image.load("btnComoJugar.png")
   xBtnCJ, yBtnCJ, anchoBtnCJ, altoBtnCJ = imgBtnComoJugar.get_rect()  # Dimensiones botón
   imgBtnScoreboard = pygame.image.load("btnScoreboard.png")
   xBtnS, yBtnS, anchoBtnS, altoBtnS = imgBtnScoreboard.get_rect()  # Dimensiones botón
   imgBtnRegresar = pygame.image.load("btnRegresar.png")
   xBtnR, yBtnR, anchoBtnR, altoBtnR = imgBtnRegresar.get_rect()  # Dimensiones botón
   imgLogoJuego = pygame.image.load("logoJuego.png")
   xL, yL, anchoL, altoL = imgLogoJuego.get_rect()  # Dimensiones Logo
   imgGameOver = pygame.image.load("gameOver.png")
   xGO, yGO, anchoGO, altoGO = imgGameOver.get_rect()   # Dimensiones Game Over
   imgMenuPrincipal = pygame.image.load("btnMenuPrincipal.png")
   xMP, yMP, anchoMP, altoMP = imgMenuPrincipal.get_rect()  # Dimensiones botón

   # Imágenes para el juego
   imgFondo = pygame.image.load("fondoJuego.jpg")
   xFondo = 0
   imgComoJugar = pygame.image.load("comoJugar.png")
   imgHighScore = pygame.image.load("High_score.png")

   # Ángulo
   alfa = 0

   # Tiempo
   timer = 0
   timerBalas = 0

   # Audio
   pygame.mixer.init()
   disparo = pygame.mixer.Sound("shoot.wav")
   pygame.mixer.music.load("musicaFondo.mp3")
   pygame.mixer.music.play(-1)


   # Vida
   escudo = 100
   vida = 50

   # Puntuación
   puntos = 0

   # Texto
   fuenteScore = pygame.font.Font("Demonized.ttf", 108)
   fuenteScoreboard = pygame.font.Font("Demonized.ttf", 75)
   fuenteJuego = pygame.font.Font("Demonized.ttf", 25)



   while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
       # Procesa los eventos que recibe
       for evento in pygame.event.get():
           if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
               termina = True      # Queremos terminar el ciclo
           if estado == JUGANDO:
               if evento.type == pygame.KEYDOWN:
                   if evento.key == pygame.K_UP:
                       movimiento = ARRIBA
                   elif evento.key == pygame.K_DOWN:
                       movimiento = ABAJO
                   elif evento.key == pygame.K_RIGHT:
                       movimiento = DERECHA
                   elif evento.key == pygame.K_LEFT:
                       movimiento = IZQUIERDA
                   elif evento.key == pygame.K_SPACE: #disparo
                       spriteBalaAliada = pygame.sprite.Sprite()
                       spriteBalaAliada.image = imgBalaAliada
                       spriteBalaAliada.rect = imgBalaAliada.get_rect()
                       spriteBalaAliada.rect.left = spriteNaveJugador.rect.width + spriteNaveJugador.rect.left
                       spriteBalaAliada.rect.bottom = spriteNaveJugador.rect.bottom - spriteNaveJugador.rect.height//2
                       listaBalasAliadas.append(spriteBalaAliada)
                       disparo.play()
           if evento.type == pygame.MOUSEBUTTONDOWN:
               xm, ym = pygame.mouse.get_pos()
               if estado == MENU:
                   xbtnJ = ANCHO // 2 - anchoBtnJ // 2
                   yBtnJ = ALTO // 2 - altoBtnJ // 2
                   xBtnCJ = ANCHO // 2 - anchoBtnCJ // 2
                   yBtnCJ = ALTO // 2 + 25 + altoBtnCJ
                   xbtnS = ANCHO // 2 - anchoBtnS // 2
                   yBtnS = ALTO // 2 + 50 + altoBtnCJ + altoBtnS
                   if xm >= xbtnJ and xm <= xbtnJ + anchoBtnJ and ym >= yBtnJ and ym <= yBtnJ + altoBtnJ:
                       estado = JUGANDO
                       timer = 0
                   if xm >= xBtnCJ and xm <= xBtnCJ + anchoBtnCJ and ym >= yBtnCJ and ym <= yBtnCJ + altoBtnCJ:
                       estado = COMOJUGAR
                   if xm >= xbtnS and xm <= xbtnS + anchoBtnS and ym >= yBtnS and ym <= yBtnS + altoBtnS:
                       estado = SCOREBOARD
               elif estado == COMOJUGAR:

                   xbtnR = ANCHO-(3*anchoBtnR)//2
                   yBtnR = ALTO-2*altoBtnR
                   if xm >= xbtnR and xm <= xbtnR + anchoBtnR and ym >= yBtnR and ym <= yBtnR + altoBtnR:
                       estado = MENU
               elif estado == SCOREBOARD:
                   xbtnR = ANCHO - (3 * anchoBtnR) // 2
                   yBtnR = ALTO - 2 * altoBtnR
                   if xm >= xbtnR and xm <= xbtnR + anchoBtnR and ym >= yBtnR and ym <= yBtnR + altoBtnR:
                       estado = MENU
               elif estado == GAMEOVER:
                   xMP = ANCHO//2-anchoMP//2
                   yMP = ALTO-2*altoMP
                   if xm >= xMP and xm <= xMP + anchoMP and ym >= yMP and ym <= yMP + altoMP:
                       estado = MENU
                       vida = 50
                       escudo = 100
                       puntos = 0
                       numEnemigos = 15 -len(listaEnemigos)
                       generarEnemigos(listaEnemigos, numEnemigos)
                       numEnemigos = 15
                       spriteNaveJugador.rect.bottom = ANCHO // 2
                       movimiento = QUIETO
                       limite = 1.5
                       velocidadAsteroide = 5


       # Pregunta en qué estado está el juego
       if estado == MENU:
           # Borrar pantalla
           ventana.fill(NEGRO)
           ventana.blit(imgFondo, (xFondo, 0))
           ventana.blit(imgFondo, (xFondo + 1067, 0))  # 1067 Ancho de la Imagen
           xFondo -= 1
           if xFondo <= -1067:
               xFondo = 0
           ventana.blit(imgBtnJugar, (ANCHO//2-anchoBtnJ//2, ALTO//2-altoBtnJ//2))
           ventana.blit(imgBtnComoJugar, (ANCHO//2 -anchoBtnCJ//2, ALTO//2 + 25 + altoBtnCJ))    # Dejar pixeles de separación
           ventana.blit(imgBtnScoreboard, (ANCHO//2 - anchoBtnS//2, ALTO//2 + 50 + altoBtnCJ + altoBtnS))
           ventana.blit(imgLogoJuego, (ANCHO//2-anchoL//2, ALTO//2-altoL - 50))

       elif estado == COMOJUGAR:
           ventana.fill(BLANCO)
           ventana.blit(imgFondo, (xFondo, 0))
           ventana.blit(imgFondo, (xFondo + 1067, 0))  # 1067 Ancho de la Imagen
           xFondo -= 1
           if xFondo <= -1067:
               xFondo = 0
           ventana.blit(imgComoJugar, (0, 0))
           ventana.blit(imgBtnRegresar, (ANCHO-((3*anchoBtnR)//2), ALTO-2*altoBtnR))

       elif estado == SCOREBOARD:
           ventana.blit(imgFondo, (xFondo, 0))
           ventana.blit(imgFondo, (xFondo + 1067, 0))  # 1067 Ancho de la Imagen
           xFondo -= 1
           if xFondo <= -1067:
               xFondo = 0
           texto = fuenteScoreboard.render("Puntaje", 1, VERDE_BANDERA)
           texto2 = fuenteScoreboard.render("Más", 1, VERDE_BANDERA)
           texto3 = fuenteScoreboard.render("Alto", 1, VERDE_BANDERA)
           score = fuenteScore.render("%d" % mayorPuntaje, 1, VERDE_BANDERA)
           xSc, ySc, anchoSc, altoSc = score.get_rect()
           ventana.blit(imgBtnRegresar, (ANCHO - ((3 * anchoBtnR) // 2), ALTO - 2 * altoBtnR))
           ventana.blit(score, (ANCHO//2-anchoSc//2, ALTO//2+50))
           ventana.blit(texto, (250, 50))
           ventana.blit(texto2, (300, 150))
           ventana.blit(texto3, (300, 250))

       elif estado == GAMEOVER:
           ventana.blit(imgFondo, (xFondo, 0))
           ventana.blit(imgFondo, (xFondo + 1067, 0))  # 1067 Ancho de la Imagen
           xFondo -= 1
           if xFondo <= -1067:
               xFondo = 0
           textoPuntaje = fuenteScoreboard.render("Puntuación:", 1, VERDE_BANDERA)
           textoPuntosFinales = fuenteScoreboard.render("%d" % puntos, 1, VERDE_BANDERA)
           xp, yp, anchop, altop = textoPuntaje.get_rect()
           xpf, ypf, anchopf, altopf = textoPuntosFinales.get_rect()
           ventana.blit(imgGameOver, (ANCHO//2-anchoGO//2, ALTO//2-altoGO//2-200))
           ventana.blit(imgMenuPrincipal, (ANCHO//2-anchoMP//2, ALTO-2*altoMP))
           ventana.blit(textoPuntaje, (ANCHO//2- anchop//2, ALTO//2+altop//2-100))
           ventana.blit(textoPuntosFinales, (ANCHO//2-anchopf//2, ALTO//2+altopf//2))
           if puntos >= mayorPuntaje:
               salida = open("mayorPuntaje.txt", "w")
               salida.write("%d" % puntos)
               salida.close()
               ventana.blit(imgHighScore, (ANCHO//2 + 100, 50))
               mayorPuntaje = puntos




       elif estado == JUGANDO:
           # Actualizar objetos
           actualizarEnemigos(listaEnemigos, alfa)
           alfa += 2
           actualizarBalas(listaBalasAliadas)
           actualizarBalasEnemigas(listaBalasEnemigas)
           actualizarAsteroides(listaAsteroides, velocidadAsteroide)
           puntosPorDestruccion = verificarColisiones(listaBalasAliadas, listaEnemigos, numEnemigos)
           colisionBalaEnemiga = verificarBalas(spriteNaveJugador, listaBalasEnemigas)
           colisionAsteroide = verificarChoqueAsteroide(spriteNaveJugador, listaAsteroides)
           penalizacion = verificarJugadorZona(spriteNaveJugador)
           choque = verificarColisionEnemiga(spriteNaveJugador, listaEnemigos)

           # Mover personaje
           if movimiento==ARRIBA:
               spriteNaveJugador.rect.bottom -= 4
           elif movimiento==ABAJO:
               spriteNaveJugador.rect.bottom += 4
           elif movimiento==DERECHA:
               spriteNaveJugador.rect.left += 4
           elif movimiento==IZQUIERDA:
               spriteNaveJugador.rect.left -= 4

           # Borrar pantalla
           ventana.fill(BLANCO)
           ventana.blit(imgFondo, (xFondo, 0))
           ventana.blit(imgFondo, (xFondo+1067, 0))    # 1067 Ancho de la Imagen
           xFondo-=1
           if xFondo<=-1067:
               xFondo=0
           if timer > 2 and timer <=10:
               limite = 1
               velocidadAsteroide = 8
           elif timer > 10 and timer<=15:
               limite = 0.8
               velocidadAsteroide = 10
           elif timer > 15:
               limite = 0.5
               velocidadAsteroide = 12
           if timerBalas >limite:
               enemigoD = randint(0, len(listaEnemigos)-1)
               spriteBalaEnemiga = pygame.sprite.Sprite()
               spriteBalaEnemiga.image = imgBalaEnemiga
               spriteBalaEnemiga.rect = imgBalaEnemiga.get_rect()
               spriteBalaEnemiga.rect.left = listaEnemigos[enemigoD].rect.width + listaEnemigos[enemigoD].rect.left
               spriteBalaEnemiga.rect.bottom = listaEnemigos[enemigoD].rect.bottom - listaEnemigos[enemigoD].rect.height // 2
               listaBalasEnemigas.append(spriteBalaEnemiga)
               disparo.play()
               timerBalas = 0

           puntos += puntosPorDestruccion
           if escudo >0:
               escudoTexto = fuenteJuego.render("Escudo: %d" % escudo, 1, VERDE_BANDERA)
               ventana.blit(escudoTexto, (50, 0))
               escudo = escudo - colisionAsteroide -colisionBalaEnemiga - penalizacion - choque
               if escudo < 100:
                   escudo += 1/30
           else:
               vidaTexto = fuenteJuego.render("Vida: %d" % vida, 1, VERDE_BANDERA)
               ventana.blit(vidaTexto, (50, 0))
               vida = vida - colisionBalaEnemiga -colisionAsteroide - penalizacion - choque
           if vida <= 0:
               estado = GAMEOVER
           puntosTexto = fuenteJuego.render("Puntos: %d" % puntos, 1, VERDE_BANDERA)
           xpt, ypt, anchopt, altopt = puntosTexto.get_rect()
           ventana.blit(puntosTexto, (ANCHO-25-anchopt, 0))
           dibujarPersonaje(ventana, spriteNaveJugador)
           dibujarEnemigos(ventana, listaEnemigos)
           dibujarBalas(ventana, listaBalasAliadas)
           dibujarAsteroides(ventana, listaAsteroides)
           dibujarBalasEnemigas(ventana, listaBalasEnemigas)
           timer += 1/60
           puntos += 1
           timerBalas += 1/60

       pygame.display.flip()  # Actualiza trazos
       reloj.tick(60)  # 60 fps

   # Después del ciclo principal
   pygame.quit()  # termina pygame


# Función principal. Manda llamar a las otras funciones.
def main():
   dibujar()


# Llamar a la función principal
main()


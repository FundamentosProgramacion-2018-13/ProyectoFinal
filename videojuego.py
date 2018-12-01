# encoding: UTF-8
# Autor: JAVIER ALEXANDRO VARGAS SÁNCHEZ
# Ejemplo VIDEOJUEGO

#-----------------------------------------------------------------------------------------------------------------------
import pygame
from random import randint

# DIMENSIONES PANTALLA:
ANCHO = 800
ALTO = 600


# COLORES_
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
NEGRO = (0, 0, 0)
MIDNIGHTBLUE = (25,25,112)


# ESTADOS_
MENU = 1
JUGANDO = 2
PERDISTE = 3
LEADERBOARD = 4
INSTRUCCIONES = 5
REINTENTAR = 6



#Estados mov
QUIETO = 1
ABAJO = 2
ARRIBA = 3
IZQ = 4
DER = 5
VELOCIDAD = 3


#-----------------------------------------------------------------------------------------------------------------------


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos(ventana, listaEnemigos):
    for enemigo in listaEnemigos:
        ventana.blit(enemigo.image, enemigo.rect)


def moverEnemigosARRIBA(listaEnemigos,spritePersonaje,enemigoVel):
    for enemigo in listaEnemigos:
        if enemigo.rect.bottom > spritePersonaje.rect.bottom:
            enemigo.rect.bottom -= enemigoVel


def moverEnemigosABAJO(listaEnemigos, spritePersonaje,enemigoVel):
     for enemigo in listaEnemigos:
        if enemigo.rect.bottom < spritePersonaje.rect.bottom:
             enemigo.rect.bottom += enemigoVel


def moverEnemigosIZQ(listaEnemigos,spritePersonaje,enemigoVel):
    for enemigo in listaEnemigos:
        if enemigo.rect.left > spritePersonaje.rect.left:
            enemigo.rect.left -= enemigoVel


def moverEnemigosDER(listaEnemigos,spritePersonaje, enemigoVel):
    for enemigo in listaEnemigos:
        if enemigo.rect.left < spritePersonaje.rect.left:
            enemigo.rect.left += enemigoVel


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalasder):
    for bala in listaBalasder:
        bala.rect.left += 10


def moverBalasizq(listaBalasizq):
    for bala in listaBalasizq:
        bala.rect.left -= 10


def moverBalasarriba(listaBalasup):
    for bala in listaBalasup:
        bala.rect.bottom += 10


def moverBalasabajo(listaBalasdown):
    for bala in listaBalasdown:
        bala.rect.bottom -= 10


def dibujarMenu(ventana, imgBtnJugar):
    ventana.blit(imgBtnJugar, (ANCHO // 2 - 128, ALTO // 3+50))

def dibujarLeader(ventana, imgLeaderboard):
    ventana.blit(imgLeaderboard, (ANCHO//2-92.5, ALTO-200))

def dibujarPerdiste(ventana, imgPerdiste):
    ventana.blit(imgPerdiste, (ANCHO//2, ALTO//2))

def dibujarRegresar(ventana, imgRegresar):
    ventana.blit(imgRegresar, (10, ALTO-50))

def dibujarInstrucciones(ventana, botonInstrucciones):
    ventana.blit(botonInstrucciones, (ANCHO//2-96.5, ALTO - 100))

def dibujarReintentar(ventana, imgReintentar):
    ventana.blit(imgReintentar, (550, ALTO-100))


def verificarColision(listaEnemigos, listaBalas,gg,listaKills ):
    for bala in listaBalas:
        for enemigo in listaEnemigos:

            xb = bala.rect.left
            yb = bala.rect.bottom
            xe, ye, ae, alte = enemigo.rect
            if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + alte :

                gg.play()
                listaEnemigos.remove(enemigo)
                listaBalas.remove(bala)
                listaKills.append(1)

def perderHP(spritePersonaje, listaEnemigos,plasma):

    for enemigo in listaEnemigos:
        xPersonaje = spritePersonaje.rect.left
        yPersonaje = spritePersonaje.rect.bottom
        xe, ye, ae, alte = enemigo.rect
        if xPersonaje >= xe and xPersonaje <= xe + ae and yPersonaje >= ye and yPersonaje <= ye + alte:
            plasma.play()

            return True


def spawnearEnemigos(spriteEnemigo,listaEnemigos, imgEnemigo):

        ladoAleatorio = randint (0,3)

        if ladoAleatorio == 0:
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgEnemigo
            spriteEnemigo.rect = imgEnemigo.get_rect()
            spriteEnemigo.rect.left = randint(0, ANCHO)
            spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
            spriteEnemigo.rect.left = randint(ANCHO, ANCHO + 100)
            spriteEnemigo.rect.bottom = randint(0, ALTO)
            listaEnemigos.append(spriteEnemigo)

        elif ladoAleatorio == 1:
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgEnemigo
            spriteEnemigo.rect = imgEnemigo.get_rect()
            spriteEnemigo.rect.left = randint(0, ANCHO)
            spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
            spriteEnemigo.rect.left = randint(-50, 0)
            spriteEnemigo.rect.bottom = randint(0, ALTO)
            listaEnemigos.append(spriteEnemigo)

        elif ladoAleatorio == 2:
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgEnemigo
            spriteEnemigo.rect = imgEnemigo.get_rect()
            spriteEnemigo.rect.left = randint(0, ANCHO)
            spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
            spriteEnemigo.rect.left = randint(0, ANCHO)
            spriteEnemigo.rect.bottom = randint(-50, 0)
            listaEnemigos.append(spriteEnemigo)

        elif ladoAleatorio == 3:
            spriteEnemigo = pygame.sprite.Sprite()
            spriteEnemigo.image = imgEnemigo
            spriteEnemigo.rect = imgEnemigo.get_rect()
            spriteEnemigo.rect.left = randint(0, ANCHO)
            spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
            spriteEnemigo.rect.left = randint(0, ANCHO)
            spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
            listaEnemigos.append(spriteEnemigo)

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

def dibujar():
    pygame.init()

    balazo = pygame.mixer.Sound("balazo.wav")
    balazo.set_volume(0.4)
    gg = pygame.mixer.Sound("oof.wav")
    gg.set_volume(0.5)
    plasma = pygame.mixer.Sound("Plasma.wav")
    plasma.set_volume(0.8)
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False

    # PERSONAJE
    imgPersonaje = pygame.image.load("helii.gif")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = ANCHO// 2 + spritePersonaje.rect.width // 2
    spritePersonaje.rect.bottom= ALTO // 2 + spritePersonaje.rect.height // 2

    # ENEMIGOS
    listaEnemigos = []
    imgEnemigo = pygame.image.load("estrellas.png")

    #Genera enemigos al inicio en las 4 direcciones
    num = randint(1,2)

    for k in range(num):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO)
        spriteEnemigo.rect.bottom = randint(ALTO, ALTO+50)
        spriteEnemigo.rect.left = randint(ANCHO, ANCHO+100)
        spriteEnemigo.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteEnemigo)

    for izq in range(num):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO)
        spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
        spriteEnemigo.rect.left = randint(-50, 0)
        spriteEnemigo.rect.bottom = randint(0, ALTO)
        listaEnemigos.append(spriteEnemigo)

    for arriba in range(num):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO)
        spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
        spriteEnemigo.rect.left = randint(0, ANCHO)
        spriteEnemigo.rect.bottom = randint(-50, 0)
        listaEnemigos.append(spriteEnemigo)

    for abajo in range(num):
        spriteEnemigo = pygame.sprite.Sprite()
        spriteEnemigo.image = imgEnemigo
        spriteEnemigo.rect = imgEnemigo.get_rect()
        spriteEnemigo.rect.left = randint(0, ANCHO)
        spriteEnemigo.rect.bottom = randint(ALTO, ALTO + 50)
        spriteEnemigo.rect.left = randint(0, ANCHO )
        spriteEnemigo.rect.bottom = randint(ALTO, ALTO+50)
        listaEnemigos.append(spriteEnemigo)

    listaBalasder = []
    listaBalasizq = []
    listaBalasup = []
    listaBalasdown = []

    listaKills = []

    sumatoriaBalas = sum(listaBalasder)+sum(listaBalasizq)+sum(listaBalasup)+sum(listaBalasdown)


    estado = MENU

    moviendo = QUIETO

    timer = 0
    cronometro = 0
    pace = 0

    fuente = pygame.font.SysFont("arial", 20)
    font = pygame.font.SysFont("monospace", 64)
    font.get_bold()


    # IMAGENES
    imgBtnJugar = pygame.image.load("button_iniciar-juego.png")
    imgFondo = pygame.image.load("estacionamiento.jpg")
    imgBala = pygame.image.load("bala.png")
    imgPerdiste = pygame.image.load("PERDISTE.png")
    imgLeaderboard = pygame.image.load("button_leaderboard.png")
    imgRegresar = pygame.image.load("button_regresar.png")
    botonInstrucciones = pygame.image.load("button_instrucciones.png")
    imgInstrucciones = pygame.image.load("instrucc.png")
    imgReintentar= pygame.image.load("button_reintentar.png")
    imgMenu = pygame.image.load("fondo.jpg")

    while not termina:

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm, " , ", ym)
                # Preguntar si solto el mouse dentro del boton
                xb = ANCHO // 2 - 128
                yb = ALTO // 3+50

                xl= ANCHO // 2 - 92.5
                yl = ALTO - 200

                xr= 10
                yr = ALTO - 50

                xi= ANCHO//2 - 96.5
                yi= ALTO - 100

                xt= 550
                yt= ALTO - 100

                if xm >= xb and xm <= xb + 256 and ym >= yb and ym <= yb + 100:
                    estado = JUGANDO

                if xm >= xl and xm <= xl + 185 and ym >= yl and ym <= yl + 40:
                    estado = LEADERBOARD

                if xm >= xr and xm <= xr + 142 and ym >= yr and ym <= yr + 40:
                    estado = MENU

                if xm >= xi and xm <= xi + 193 and ym >= yi and ym <= yi + 40:
                    estado = INSTRUCCIONES

                if xm >= xt and xm <= xt + 266 and ym >= yt and ym <= yt + 106:
                    estado = REINTENTAR
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    moviendo = IZQ

                elif evento.key == pygame.K_d:
                    moviendo = DER

                elif evento.key == pygame.K_w:
                    moviendo = ARRIBA

                elif evento.key == pygame.K_s:
                    moviendo = ABAJO


                elif evento.key == pygame.K_RIGHT:
                    # Crear una bala
                    balazo.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalasder.append(spriteBala)

                    if spriteBala.rect.bottom > ANCHO+5:
                        listaBalasder.remove(spriteBala)

                elif evento.key == pygame.K_LEFT:
                    # Crear una bala
                    balazo.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left - spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalasizq.append(spriteBala)

                    if spriteBala.rect.bottom < -5:
                        listaBalasizq.remove(spriteBala)

                elif evento.key == pygame.K_UP:
                    # Crear una bala
                    balazo.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom - spritePersonaje.rect.height
                    listaBalasup.append(spriteBala)

                    if spriteBala.rect.bottom < -5:
                        listaBalasup.remove(spriteBala)


                elif evento.key == pygame.K_DOWN:
                    # Crear una bala
                    balazo.play()
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom
                    listaBalasdown.append(spriteBala)

                    if spriteBala.rect.bottom > ALTO+5:
                        listaBalasdown.remove(spriteBala)

        # Borrar pantalla
        ventana.fill(NEGRO)
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        if estado == JUGANDO:

            cronometro +=1/60

            if spritePersonaje.rect.bottom - spritePersonaje.rect.height >= 0:
                if moviendo == ARRIBA:
                    spritePersonaje.rect.bottom -= VELOCIDAD

            if spritePersonaje.rect.bottom <= ALTO:
                if moviendo == ABAJO:
                    spritePersonaje.rect.bottom += VELOCIDAD

            if spritePersonaje.rect.left + spritePersonaje.rect.width <= ANCHO:
                if moviendo == DER:
                    spritePersonaje.rect.left += VELOCIDAD

            if spritePersonaje.rect.left >= 0:
                if moviendo == IZQ:
                    spritePersonaje.rect.left -= VELOCIDAD


            #Cada cierto tiempo los enemigos empiezan a spawnear más rápido
            if cronometro > 2 and cronometro <10:
                if timer >=1:
                    timer = 0

                    if len(listaEnemigos) > 50:
                        pass
                    else:
                        spawnearEnemigos(spriteEnemigo,listaEnemigos, imgEnemigo)

            if cronometro > 10 and cronometro < 20:
                if timer >= 0.75:
                    timer = 0

                    if len(listaEnemigos) > 50:
                        pass
                    else:
                        spawnearEnemigos(spriteEnemigo, listaEnemigos, imgEnemigo)

            if cronometro > 20 and cronometro < 40:
                if timer >= 0.5:
                    timer = 0

                    if len(listaEnemigos) > 50:
                        pass
                    else:
                        spawnearEnemigos(spriteEnemigo, listaEnemigos, imgEnemigo)

            if cronometro > 40:
                if timer >= 0.25:
                    timer = 0

                    if len(listaEnemigos) > 50:
                        pass
                    else:
                        spawnearEnemigos(spriteEnemigo, listaEnemigos, imgEnemigo)


            enemigoVel = 1.5

            # Actualizar ENEMIGOS / BALASw
            moverEnemigosARRIBA(listaEnemigos, spritePersonaje,enemigoVel)
            moverEnemigosABAJO(listaEnemigos, spritePersonaje,enemigoVel)
            moverEnemigosIZQ(listaEnemigos, spritePersonaje,enemigoVel)
            moverEnemigosDER(listaEnemigos, spritePersonaje,enemigoVel)


            moverBalas(listaBalasder)
            moverBalasizq(listaBalasizq)
            moverBalasabajo(listaBalasup)
            moverBalasarriba(listaBalasdown)


            verificarColision(listaEnemigos, listaBalasder,gg, listaKills)
            verificarColision(listaEnemigos, listaBalasizq,gg, listaKills)
            verificarColision(listaEnemigos, listaBalasup,gg, listaKills)
            verificarColision(listaEnemigos, listaBalasdown,gg, listaKills)



            perderHP(spritePersonaje,listaEnemigos,plasma)

            # Dibujar, aquí haces todos los trazos que requieras
            ventana.blit(imgFondo, (0, 0))
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarEnemigos(ventana, listaEnemigos)
            dibujarBalas(ventana, listaBalasder)
            dibujarBalas(ventana, listaBalasizq)
            dibujarBalas(ventana, listaBalasup)
            dibujarBalas(ventana, listaBalasdown)
            texto = fuente.render("Tiempo: %d s" % cronometro, 1, NEGRO)
            ventana.blit(texto, (ANCHO-150, 15))
            bajas = fuente.render("Aliens: %d" % sum(listaKills), 1, ROJO)
            ventana.blit(bajas, (10,15))


            if perderHP(spritePersonaje,listaEnemigos,plasma) == True:

                estado = PERDISTE
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif estado == MENU:
            ventana.blit(imgMenu,(0,0))
            dibujarMenu(ventana, imgBtnJugar, )
            dibujarLeader(ventana,imgLeaderboard)
            dibujarInstrucciones(ventana,botonInstrucciones)
            pygame.mixer.music.load("Sketches.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.6)

            #pygame.mixer.music.load("Retrobeats.mp3")
            #pygame.mixer.music.play(-1)

        elif estado == PERDISTE:
            pygame.mixer.music.stop()
            ventana.fill(BLANCO)
            ventana.blit(imgPerdiste, (0, 0))
            dibujarRegresar(ventana, imgRegresar)
            dibujarReintentar(ventana, imgReintentar)

            tiempofinal = fuente.render("Tiempo de supervivencia: %d segundos"% cronometro, 1, NEGRO)
            ventana.blit(tiempofinal, (1, ALTO // 2))
            bajasAlien = fuente.render("Alienígenas eliminados: %d " % sum(listaKills), 1, NEGRO)
            ventana.blit(bajasAlien, (1, ALTO //2 + 25))
            puntajetotal = (cronometro//1) * (sum(listaKills))
            scoreAcumulado = fuente.render("Puntos obtenidos: %d kills x %d segundos = %d puntos" %
                                           (sum(listaKills), cronometro, puntajetotal),  1, NEGRO)
            ventana.blit(scoreAcumulado, (1, ALTO // 2 + 50))
#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

            archivo = open("Leaderboard.txt", "r")

            linea = archivo.readline()
            puntaje = int(linea)

            if puntaje < puntajetotal:
                highscore = open("Leaderboard.txt", "w")
                highscore.write("%d" % puntajetotal)
                highscore.close()
            archivo.close()

#///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif estado == LEADERBOARD:

            pygame.mixer.music.stop()
            ventana.fill(BLANCO)
            dibujarRegresar(ventana,imgRegresar)

            archivo = open("Leaderboard.txt", "r")
            linea = archivo.readline()
            puntaje = int(linea)
            puntajetotal = (cronometro//1) * (sum(listaKills))
            scoreAcumulado = font.render("High score: %d puntos" % puntajetotal, 1, NEGRO)

            ventana.blit(scoreAcumulado, (10, ALTO//2-20))
            archivo.close()



#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        elif estado == INSTRUCCIONES:
            pygame.mixer.music.stop()
            ventana.fill(BLANCO)
            ventana.blit(imgInstrucciones, (0,0))
            dibujarRegresar(ventana, imgRegresar)
        elif estado == REINTENTAR:
            listaEnemigos = []
            timer = 0
            cronometro = 0
            pace = 0
            listaBalasder = []
            listaBalasup = []
            listaBalasdown = []
            listaBalasizq = []
            listaKills = []
            balazo.stop()
            gg.stop()
            moviendo = QUIETO
            spritePersonaje.rect.left = ANCHO // 2 + spritePersonaje.rect.width // 2
            spritePersonaje.rect.bottom = ALTO // 2 + spritePersonaje.rect.height // 2
            pygame.mixer.music.load("Sketches.mp3")
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.6)
            estado = JUGANDO


#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

        pygame.display.flip()
        reloj.tick(60)
        timer += 1/60
        pace += 1/60

    pygame.quit()


def main():
    dibujar()

main()


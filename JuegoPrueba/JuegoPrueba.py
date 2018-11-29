#Jesus Zabdiel Sanchez Chavez

#Prueba de juego
import pygame
from random import randint
import time
def dibujar():

    def dibujarAsteroides (ventana, listaEnemigos):
        for enemigo in listaEnemigos:
            ventana.blit (enemigo.image, enemigo.rect)
        if len(listaEnemigos) == 0:
            generarEnemigos()
    def dibujarItems(ventana, listaVidasExtra, listaBalasExtra, contadorItems):

        for item in listaVidasExtra:
            ventana.blit(item.image, item.rect)
        for item in listaBalasExtra:
            ventana.blit(item.image, item.rect)

        if contadorItems > 0 and contadorItems % 500 == 0:
            generarVidaExtra()
            generarBalasExtra()

    def dibujarNave(ventana, spriteNave):

        ventana.blit(spriteNave.image, spriteNave.rect)


    def moverBalas (listaBalas):
        for bala in listaBalas:
            bala.rect.left += 25

    def moverAsteroides (listaEnemigos, velocidadEnemigo):
        for enemigo in listaEnemigos:
            enemigo.rect.left -= velocidadEnemigo
    def moverItems(listaVidasExtra,listaBalasExtra, velocidadEnemigo):
        for item in listaVidasExtra:
            item.rect.left -= velocidadEnemigo
        for item in listaBalasExtra:
            item.rect.left -= velocidadEnemigo
    def dibujarBalas(ventana, listaBalas):
        for bala in listaBalas:
            ventana.blit(bala.image, bala.rect)
    def dibujarMenu(ventana, imgMenu):
        ventana.blit(imgMenu, (0, 0))

    def verificarColision(listaEnemigos, listaBalas, efecto):
        for k in range(len(listaBalas)-1,-1, -1):
            bala = listaBalas[k]
            for e in range(len(listaEnemigos)-1,-1,-1):
                enemigo = listaEnemigos[e]
                xb = bala.rect.left
                yb = bala.rect.bottom
                xe, ye, ae, alte = enemigo.rect

                if xb  >= xe and xb <= xe+ae and yb>= ye and yb <= ye+alte:
                    listaEnemigos.remove(enemigo)
                    listaBalas.remove(bala)
                    efecto.play()
                    break
                #Elimiar balas al salir de la pantalla
                if xb >= ANCHO:
                    listaBalas.remove(bala)
                    break


    def controlarVidas (ventana, listaVidas, listaEnemigos, nave,efecto):
        for vida in listaVidas:
            ventana.blit(vida.image, vida.rect)
            for x in range (len(listaEnemigos) -1,-1,-1):
                enemigo = listaEnemigos[x]
                xNave = nave.rect.left
                yNave = nave.rect.bottom
                xe, ye, ae, alte = enemigo.rect

                if xNave +50  >= xe and xNave+50 <= xe+ae and yNave-50 >= ye and yNave-50 <= ye+alte:
                    listaEnemigos.remove(enemigo)
                    listaVidas.remove(listaVidas[-1])
                    efecto.play()
                    break
                if xe <= -10:
                    listaEnemigos.remove(listaEnemigos[x])
                    break
        return len(listaVidas)

    def controlarItems (listaVidasExtra, listaBalasExtra, nave, listaVidas, balasIniciales, efecto, efecto2):
        xNave = nave.rect.left
        yNave = nave.rect.bottom


        if len(listaVidasExtra) > 0:
            #Vidaextra
            for vida in  range (len(listaVidasExtra) -1,-1,-1):
                vidaExtra = listaVidasExtra[vida]
                xvidaExtra, yvidaExtra, avidasExtra, altvidaExtra = vidaExtra.rect

                if xNave + 50 >= xvidaExtra and xNave + 50 <= xvidaExtra + avidasExtra and yNave - 50 >= yvidaExtra and yNave - 50 <= yvidaExtra + altvidaExtra:
                    spriteVidaExtra = pygame.sprite.Sprite()
                    spriteVidaExtra.image = imgVidaExtra
                    spriteVidaExtra.rect = imgBala.get_rect()
                    spriteVidaExtra.rect.left = 10 + ((len(listaVidas)) * 35)
                    spriteVidaExtra.rect.bottom = 25
                    listaVidas.append(spriteVidaExtra)
                    listaVidasExtra.remove(listaVidasExtra[-1])
                    print("colision")
                    efecto.play()


        #balas extra
        if len(listaBalasExtra) > 0:
            for bala in range(len(listaBalasExtra) - 1, -1, -1):
                balasExtra = listaBalasExtra[bala]
                xbalaExtra, ybalaExtra, abalaExtra, altbalaExtra = balasExtra.rect

                if xNave + 50 >= xbalaExtra and xNave + 50 <= xbalaExtra + abalaExtra and yNave - 50 >= ybalaExtra and yNave - 50 <= ybalaExtra + altbalaExtra:
                    #print(balasIniciales)
                    listaBalasExtra.remove(listaBalasExtra[-1])
                    print("colision")
                    efecto2.play()
                    return True

    def dibujarBestScores(ventana, fuentePerdiste, bestScore):

       bestScorestxt = open("bestScores.txt", "r")
       linea = bestScorestxt.readline()
       datos = linea.split(":")
       bestScore = datos[-1]
       ventana.blit(imgFondo, (0,0))
       ventana.blit(imgRegresar, (ANCHO // 2 - 85, 350))
       texto = fuentePerdiste.render("Best Score: ", 1, BLANCO)
       texto2 = fuentePerdiste.render(bestScore ,1, BLANCO)
       ventana.blit(texto, (ANCHO // 2-150, 100))
       ventana.blit(texto2, (ANCHO // 2-50 , 200))
       bestScorestxt.close()



    def dibujaracercaDe(ventana, fuentea):
        ventana.blit(imgFondo, (0,0))
        ventana.blit(imgRegresar, (ANCHO // 2 - 85, 350))
        texto =(fuentea.render("Proyecto Final, Fundamentos de Programación", 1, BLANCO))
        texto2 = (fuentea.render("Autor: Jesús Zabdiel Sánchez, A01374964", 1, BLANCO))
        texto3 = (fuentea.render("Starship Arcade", 1, BLANCO))
        listaTextos = []
        listaTextos.append(texto)
        listaTextos.append(texto2)
        listaTextos.append(texto3)
        y = 50
        for x in listaTextos:
            ventana.blit(x, (100,y ))
            y += 50





    ANCHO = 800
    ALTO = 600
    NEGRO = (0, 0, 0)
    BLANCO = (250, 250, 250)

    #Estados

    MENU = 1
    JUGANDO = 2
    PERDISTE = 3
    BESTSCORES = 4
    ACERCADE = 5

    #Estados de movimiento del jugar
    QUIETO = 1
    ABAJO = 2
    ARRIBA = 3

    #Archivo de Best Scores


    imgNave = pygame.image.load("Nave.png")
    spriteNave = pygame.sprite.Sprite()
    spriteNave.image = imgNave
    spriteNave.rect = imgNave.get_rect()
    spriteNave.rect.left = 0
    spriteNave.rect.bottom = ALTO //2 + spriteNave.rect.height // 2

    imgNaveColision = pygame.image.load("NaveFondo.png")

    imgMenu = pygame.image.load("Menú.png")

    imgRegresar = pygame.image.load("imagenRegresar.png")

    #Enemigos
    listaEnemigos = []
    imgAsteroide = pygame.image.load("asteroide.png")

    def generarEnemigos():
        for k in range(25):
            spriteAsteroide = pygame.sprite.Sprite()
            spriteAsteroide.image = imgAsteroide
            spriteAsteroide.rect = imgAsteroide.get_rect()
            spriteAsteroide.rect.left = randint(ANCHO-10,1600)
            spriteAsteroide.rect.bottom = randint(0, ALTO)
            listaEnemigos.append(spriteAsteroide)
        return listaEnemigos

    listaEnemigos = generarEnemigos()
    imgBala = pygame.image.load("bala.png")
    imgBalaExtra = pygame.image.load("bala.png")

    listaBalas = []

    listaVidasExtra = []
    listaBalasExtra = []
    imgVidaExtra = pygame.image.load("vida.png")
    def generarVidaExtra ():
        spriteVidaExtra = pygame.sprite.Sprite()
        spriteVidaExtra.image = imgVidaExtra
        spriteVidaExtra.rect = imgBala.get_rect()
        spriteVidaExtra.rect.left = randint(500, 700)
        spriteVidaExtra.rect.bottom = randint(0, ALTO)
        listaVidasExtra.append(spriteVidaExtra)

    def generarBalasExtra():
        spriteBalaExtra = pygame.sprite.Sprite()
        spriteBalaExtra.image = imgBalaExtra
        spriteBalaExtra.rect = imgBala.get_rect()
        spriteBalaExtra.rect.left = randint(500, 700)
        spriteBalaExtra.rect.bottom = randint(0, ALTO)
        listaBalasExtra.append(spriteBalaExtra)



    imgVida = pygame.image.load("vida.png")
    listaVidas = []
    vidasTotales = 3
    posicionVida = 10
    #Agregar cuantas vidas se tendrá al principio

    for k in range(vidasTotales):
        spriteVida = pygame.sprite.Sprite()
        spriteVida.image = imgVida
        spriteVida.rect = imgVida.get_rect()
        spriteVida.rect.left = (posicionVida)
        spriteVida.rect.bottom = (35)
        listaVidas.append(spriteVida)
        posicionVida += 35


    imgFondo = pygame.image.load("Fondo.png")


    estado = MENU
    moviendo = QUIETO
    contadorItems = 0


    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    reloj = pygame.time.Clock()
    termina = False


    #Fuente
    fuente = pygame.font.SysFont("Monospace" , 20)
    fuentePerdiste = pygame.font.SysFont("Monospace", 50)
    fuentea = pygame.font.SysFont("Monospace", 18)

    #Audio
    pygame.mixer.init()

    efectoDisparo = pygame.mixer.Sound("shoot.wav")
    efectoSinBala = pygame.mixer.Sound("sinbalas.wav")
    efectoExplosion = pygame.mixer.Sound("explosion.wav")
    efectoColision = pygame.mixer.Sound("colisionnave.wav")
    efectoVidaExtra = pygame.mixer.Sound("vidaextra.wav")
    efectoBalaExtra = pygame.mixer.Sound("balasextras.wav")
    pygame.mixer.music.load("musicajugando.mp3")
    pygame.mixer.music.play(1)

    score = 0
    bestScore = 0
    balasIniciales = 5

    velocidadEnemigo = 1
    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_UP:
                    moviendo = ARRIBA

                elif evento.key == pygame.K_DOWN:
                    moviendo = ABAJO

                elif evento.key == pygame.K_z:
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spriteNave.rect.left + spriteBala.rect.width
                    spriteBala.rect.bottom = spriteNave.rect.bottom

                    if balasIniciales >0:
                        listaBalas.append(spriteBala)
                        efectoDisparo.play()
                        balasIniciales -= 1
                    if balasIniciales == 0:
                        efectoSinBala.play()

            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym, = pygame.mouse.get_pos()
                print(xm, ",",ym)

                xbotones = 263
                xbotonesFinal= 583
                ybotonJugar = 71


                if xm >= xbotones and xm <= xbotonesFinal and ym >= ybotonJugar and ym <= 163  and estado == MENU:
                    estado = JUGANDO
                elif xm >= xbotones and xm <= xbotonesFinal and ym >= 195 and ym <= 288  and estado == MENU:
                    estado = BESTSCORES
                elif xm >= xbotones and xm <= xbotonesFinal and ym >= 344 and ym <= 441  and estado == MENU:
                    estado = ACERCADE

        #Actualizar Objetos

        if estado == JUGANDO:

            #Dibujar datos de juego
            score += (round(time.perf_counter()) / 500) #Se redondea el contador del tiempo
            ventana.blit(imgBala, (0, 0))
            moverAsteroides(listaEnemigos, velocidadEnemigo)
            if int(score) != 0 and int(score) %4 == 0:
                velocidadEnemigo += .005
            moverBalas(listaBalas)
            item = controlarItems(listaVidasExtra, listaBalasExtra, spriteNave, listaVidas, balasIniciales, efectoVidaExtra, efectoBalaExtra)
            if item == True:
                balasIniciales = balasIniciales + 5
            verificarColision(listaEnemigos, listaBalas, efectoExplosion)
            ventana.fill(NEGRO)
            ventana.blit(imgFondo, (0, 0))
            controlarVidas(ventana, listaVidas, listaEnemigos, spriteNave, efectoColision)
            controlarItems(listaVidasExtra, listaBalasExtra, spriteNave, listaVidas, balasIniciales, efectoVidaExtra, efectoBalaExtra)
            vidasTotales = controlarVidas(ventana, listaVidas, listaEnemigos, spriteNave, efectoColision)
            if vidasTotales == 0:
                estado = PERDISTE
            dibujarNave(ventana, spriteNave)
            dibujarAsteroides(ventana, listaEnemigos)
            dibujarItems(ventana, listaVidasExtra,listaBalasExtra, contadorItems)
            moverItems (listaVidasExtra,listaBalasExtra, velocidadEnemigo)
            contadorItems += 1
            dibujarBalas(ventana, listaBalas)
            textoScore = fuente.render("Score: %d" % (score), 1, BLANCO)
            ventana.blit(textoScore, (ANCHO // 2 - 50, 50))
            textoBalas = fuente.render("x" + str(balasIniciales), 1, BLANCO)
            ventana.blit(textoBalas, (ANCHO // 2 + 200, 10))
            ventana.blit(imgBala, (ANCHO//2 + 175, 12))
            

            if moviendo == ABAJO and spriteNave.rect.bottom <= ALTO: #Evitamos que se salga de la pantalla
                spriteNave.rect.bottom += 5
            elif moviendo == ARRIBA and spriteNave.rect.bottom-80 >=0:
                spriteNave.rect.bottom -=5



        elif estado == MENU:

            dibujarMenu(ventana, imgMenu)
            xm, ym, = pygame.mouse.get_pos()
            if evento.type == pygame.MOUSEBUTTONUP:
                if xm >= 640 and xm <= 770 and ym >= 485 and ym <= 577:
                    break


        elif estado == PERDISTE:
            textoPerdiste = fuentePerdiste.render("Has perdido" , 1 ,BLANCO)
            ventana.blit(textoPerdiste, (250, 150))
            ventana.blit(textoScore, (350,250))
            ventana.blit(imgRegresar, (ANCHO // 2 - 100, 400))
            if score > bestScore:
                bestScorestxt = open("bestScores.txt", "r")
                linea = bestScorestxt.readline()
                verificarScore = linea.split(":")
                if int(verificarScore[-1]) < score:
                    bestScorestxt = open("bestScores.txt", "w")
                    bestScore = score
                    bestScorestxt.write("Mejor puntaje: %d" % bestScore)
                bestScorestxt.close()
            if evento.type == pygame.MOUSEBUTTONUP:
                if xm >= 306 and xm <= 459 and ym >= 408 and ym <= 446:
                    dibujar()

        elif estado == BESTSCORES:
            dibujarBestScores(ventana, fuentePerdiste, bestScore)
            xm, ym, = pygame.mouse.get_pos()
            if evento.type == pygame.MOUSEBUTTONUP:
                if xm >= 322 and xm <= 475 and ym >= 355 and ym <= 394:
                    estado =  MENU

        elif estado == ACERCADE:
            dibujaracercaDe(ventana,fuentea)
            if evento.type == pygame.MOUSEBUTTONUP:
                if xm >= 322 and xm <= 475 and ym >= 355 and ym <= 394:
                    estado =  MENU




        pygame.display.flip()
        reloj.tick(40)


    pygame.quit()

def main():
    dibujar()

main()



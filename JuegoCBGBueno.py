#   Carlos Badillo García
#

import pygame
from random import randint


#   PANTALLA
ancho = 800
alto = 600
suelo = 475
negro = (0, 0, 0)
blanco = (255, 255, 255)

#   ESTADOS
Menu = 1
Jugar = 2
Instrucciones = 3
Puntaje = 4
Derrota = 5
Informacion = 6
Victoria = 7


def dibujarPersonaje(ventana, spritePersonaje):
    ventana.blit(spritePersonaje.image, spritePersonaje.rect)


def dibujarEnemigos(ventana, listaZombies, listaEsqueletos, listaMinotauros, listaHLobos):
    for zombie in listaZombies:
        ventana.blit(zombie.image, zombie.rect)
    for esqueleto in listaEsqueletos:
        ventana.blit(esqueleto.image, esqueleto.rect)
    for minotauro in listaMinotauros:
        ventana.blit(minotauro.image, minotauro.rect)
    for hlobos in listaHLobos:
        ventana.blit(hlobos.image, hlobos.rect)


def moverEnemigos(listaZombies, listaEsqueletos, listaMinotauros, listaHLobos):
    for zombie in listaZombies:
        zombie.rect.left -= 1.75
    for esqueleto in listaEsqueletos:
        esqueleto.rect.left -= 1.25
    for minotauro in listaMinotauros:
        minotauro.rect.left -= 1.25
    for hlobos in listaHLobos:
        hlobos.rect.left -= 2.5


def dibujarBalas(ventana, listaBalas):
    for bala in listaBalas:
        ventana.blit(bala.image, bala.rect)


def moverBalas(listaBalas):
    for bala in listaBalas:
        bala.rect.left += 5


def dibujarCorazones(ventana, vidaPersonaje):
    xc = 12
    for corazon in vidaPersonaje:
        ventana.blit(corazon.image, (xc, 12))
        xc += 50


def quitarVidasPer(choqueD, choqueF, vidaPersonaje):
    for vida in vidaPersonaje:
        if choqueD == True:
            vidaPersonaje.remove(vida)
            break
        elif choqueF == True:
            vidaPersonaje.remove(vida) and vidaPersonaje.remove(vida)


def verificarChoqueDeb(listaZombies, listaEsqueletos, listaHLobos, spritePersonaje):
    for zombie in listaZombies:
        xp = spritePersonaje.rect.left
        yp = spritePersonaje.rect.bottom
        wp = spritePersonaje.rect.width

        xz = zombie.rect.left
        yz = zombie.rect.bottom
        wz = zombie.rect.width
        hz = zombie.rect.height

        if xp >= xz and xp <= xz + wz and xp + wp >= xz and xp + wp <= xz + wz and yp >= yz - hz and yp <= yz:
            listaZombies.remove(zombie)
            return True

    for esqueleto in listaEsqueletos:
        xp = spritePersonaje.rect.left
        yp = spritePersonaje.rect.bottom
        wp = spritePersonaje.rect.width

        xe = esqueleto.rect.left
        ye = esqueleto.rect.bottom
        we = esqueleto.rect.width
        he = esqueleto.rect.height

        if xp >= xe and xp <= xe + we and xp + wp >= xe and xp + wp <= xe + we and yp >= ye - he and yp <= ye:
            listaEsqueletos.remove(esqueleto)
            return True

    for hlobo in listaHLobos:
        xp = spritePersonaje.rect.left
        yp = spritePersonaje.rect.bottom
        wp = spritePersonaje.rect.width

        xhl = hlobo.rect.left
        yhl = hlobo.rect.bottom
        whl = hlobo.rect.width
        hhl = hlobo.rect.height

        if xp >= xhl and xp <= xhl + whl and xp + wp >= xhl and xp + wp <= xhl + whl and yp >= yhl - hhl and yp <= yhl:
            listaHLobos.remove(hlobo)
            return True


def verificarChoqueFuer(listaMinotauros, spritePersonaje):
    for minotauro in listaMinotauros:
        xp = spritePersonaje.rect.left
        yp = spritePersonaje.rect.bottom
        wp = spritePersonaje.rect.width

        xm = minotauro.rect.left
        ym = minotauro.rect.bottom
        wm = minotauro.rect.width
        hm = minotauro.rect.height

        if xp >= xm and xp <= xm + wm and xp + wp >= xm and xp + wp <= xm + wm and yp >= ym - hm and yp <= ym:
            listaMinotauros.remove(minotauro)
            return True


def verificarChoqueEnemigos(listaZombies, listaEsqueletos, listaHLobos, listaMinotauros, listaBalas):
    for bala in listaBalas:
        for zombie in listaZombies:

            xb = bala.rect.left
            yb = bala.rect.bottom

            xz = zombie.rect.left
            yz = zombie.rect.bottom
            wz = zombie.rect.width
            hz = zombie.rect.height

            if xb >= xz and xb <= xz + wz and yb >= yz - hz and yb <= yz:
                listaZombies.remove(zombie)
                listaBalas.remove(bala)
                return True

    for bala in listaBalas:
        for esqueleto in listaEsqueletos:

            xb = bala.rect.left
            yb = bala.rect.bottom

            xe = esqueleto.rect.left
            ye = esqueleto.rect.bottom
            we = esqueleto.rect.width
            he = esqueleto.rect.height

            if xb >= xe and xb <= xe + we and yb >= ye - he and yb <= ye:
                listaBalas.remove(bala)
                break

    for bala in listaBalas:
        for hlobos in listaHLobos:

            xb = bala.rect.left
            yb = bala.rect.bottom

            xhl = hlobos.rect.left
            yhl = hlobos.rect.bottom
            whl = hlobos.rect.width
            hhl = hlobos.rect.height

            if xb >= xhl and xb <= xhl + whl and yb >= yhl - hhl and yb <= yhl:
                listaBalas.remove(bala)
                listaHLobos.remove(hlobos)
                return True

    for bala in listaBalas:
        for minotauro in listaMinotauros:

            xb = bala.rect.left
            yb = bala.rect.bottom

            xm = minotauro.rect.left
            ym = minotauro.rect.bottom
            wm = minotauro.rect.width
            hm = minotauro.rect.height

            if xb >= xm and xb <= xm + wm and yb >= ym - hm and yb <= ym:
                listaBalas.remove(bala)
                listaMinotauros.remove(minotauro)
                return True

def checarPuntaje(choque, puntaje):
    if choque == True:
        puntaje += 15
    else:
        return puntaje


def llegarFinal(spritePersonaje):
    xp = spritePersonaje.rect.left
    wp = spritePersonaje.rect.width

    if xp + wp == 5600:
        return True


def dibujarMenu(ventana, BotonJugar, BotonIns, BotonPun, BotonInfo):
    ventana.blit(BotonJugar, (25, 210))
    ventana.blit(BotonInfo, (25, 280))
    ventana.blit(BotonIns, (25, 350))
    ventana.blit(BotonPun, (25, 420))


def dibujarJuego():
    pygame.init()

    ventana = pygame.display.set_mode((ancho, alto))
    reloj = pygame.time.Clock()
    termina = False

    #   PERSONAJE
    imgPersonaje = pygame.image.load("Personaje.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 0
    spritePersonaje.rect.bottom = (suelo + spritePersonaje.rect.height // 2)

    vidaPersonaje = []
    imgCorazon = pygame.image.load("Corazon.png")
    for x in range(3):
        spriteCorazon = pygame.sprite.Sprite()
        spriteCorazon.image = imgCorazon
        spriteCorazon.rect = imgCorazon.get_rect()
        spriteCorazon.rect.left = 15
        spriteCorazon.rect.bottom = (40 + spriteCorazon.rect.height // 2)
        vidaPersonaje.append(spriteCorazon)

    #   ENEMIGOS
    listaZombies = []
    imgZombie = pygame.image.load("Zombie.png")
    for x in range(60):
        spriteZombie = pygame.sprite.Sprite()
        spriteZombie.image = imgZombie
        spriteZombie.rect = imgZombie.get_rect()
        spriteZombie.rect.left = randint(700, 2299)
        spriteZombie.rect.bottom = randint(0 + spriteZombie.rect.height // 2, suelo + 100)
        listaZombies.append(spriteZombie)

    listaEsqueletos = []
    imgEsqueleto = pygame.image.load("Esqueleto.png")
    for x in range(80):
        spriteEsqueleto = pygame.sprite.Sprite()
        spriteEsqueleto.image = imgEsqueleto
        spriteEsqueleto.rect = imgEsqueleto.get_rect()
        spriteEsqueleto.rect.left = randint(1300, 6400)
        spriteEsqueleto.rect.bottom = randint(0 + spriteEsqueleto.rect.height // 2, suelo + 100)
        listaEsqueletos.append(spriteEsqueleto)

    listaHLobos = []
    imgHLobo = pygame.image.load("HombreLobo.png")
    for x in range(60):
        spriteHLobo = pygame.sprite.Sprite()
        spriteHLobo.image = imgHLobo
        spriteHLobo.rect = imgHLobo.get_rect()
        spriteHLobo.rect.left = randint(1799, 6400)
        spriteHLobo.rect.bottom = randint(0 + spriteHLobo.rect.height // 2, suelo + 100)
        listaHLobos.append(spriteHLobo)

    listaMinotauros = []
    imgMinotauro = pygame.image.load("Minotauro.png")
    for x in range(50):
        spriteMinotauro = pygame.sprite.Sprite()
        spriteMinotauro.image = imgMinotauro
        spriteMinotauro.rect = imgMinotauro.get_rect()
        spriteMinotauro.rect.left = randint(700, 6400)
        spriteMinotauro.rect.bottom = randint(0 + spriteMinotauro.rect.height // 2, suelo + 100)
        listaMinotauros.append(spriteMinotauro)

    #   BALAS
    listaBalas = []
    imgBala = pygame.image.load("Bala.png")

    #   FONDO
    FondoMenu = pygame.image.load("Bosque.png")
    FondoBosque = pygame.image.load("BosqueT.jpg")
    FondoCueva = pygame.image.load("Cueva.png")
    FondoPantano = pygame.image.load("Pantano.jpg")
    FondoCasa = pygame.image.load("CasaEmbr.jpg")
    xf = 0
    FondoNegro = pygame.image.load("Fnegro.jpg")
    Gover = pygame.image.load("Gover.jpg")
    Uwin = pygame.image.load("Uwin.png")

    #   MENU
    BotonJugar = pygame.image.load("BotonJugar.png")
    BotonIns = pygame.image.load("BotonIns.png")
    Ins = pygame.image.load("Instrucciones.png")
    BotonPun = pygame.image.load("BotonPun.png")
    BotonInfo = pygame.image.load("BotonInfo.png")
    Info = pygame.image.load("Informacion.png")
    BotonX = pygame.image.load("BotonX.png")

    estado = Menu

    #   MUSICA
    pygame.mixer.init()
    pygame.mixer.music.load("MusicaJuego.mp3")
    pygame.mixer.music.play(-1)

    #   TEXTO
    fuente = pygame.font.SysFont("castellar", 64)

    while not termina:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                termina = True

            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_a:
                    spritePersonaje.rect.left -= 10
                elif evento.key == pygame.K_d:
                    spritePersonaje.rect.left += 10
                elif evento.key == pygame.K_w:
                    spritePersonaje.rect.bottom -= 20
                elif evento.key == pygame.K_s:
                    spritePersonaje.rect.bottom += 20
                elif evento.key == pygame.K_SPACE:
                    spriteBala = pygame.sprite.Sprite()
                    spriteBala.image = imgBala
                    spriteBala.rect = imgBala.get_rect()
                    spriteBala.rect.left = spritePersonaje.rect.left + spritePersonaje.rect.width
                    spriteBala.rect.bottom = spritePersonaje.rect.bottom - spritePersonaje.rect.width + 18
                    listaBalas.append(spriteBala)

            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                print(xm, ",", ym)

                xbj = 25
                ybj = 210
                if xm >= xbj and xm <= xbj + 201 and ym >= ybj and ym <= ybj + 51:
                    estado = Jugar

                xbj = 25
                ybj = 280
                if xm >= xbj and xm <= xbj + 201 and ym >= ybj and ym <= ybj + 51:
                    estado = Informacion

                xbi = 25
                ybi = 350
                if xm >= xbi and xm <= xbi + 201 and ym >= ybi and ym <= ybi + 51:
                    estado = Instrucciones

                xbp = 25
                ybp = 420
                if xm >= xbp and xm <= xbp + 201 and ym >= ybp and ym <= ybp + 51:
                    estado = Puntaje

                xbx = 745
                ybx = 20
                if xm >= xbx and xm <= xbx + 201 and ym >= ybx and ym <= ybx + 51:
                    estado = Menu

        ventana.fill(blanco)

        if estado == Jugar:

            #   DIBUJAR FONDOS
            ventana.blit(FondoBosque, (xf, 0))
            xf -= .2
            ventana.blit(FondoBosque, ((xf + 800), 0))
            xf -= .2
            ventana.blit(FondoCasa, ((xf + 1600), 0))
            xf -= .2
            ventana.blit(FondoCasa, ((xf + 2400), 0))
            xf -= .2
            ventana.blit(FondoPantano, ((xf + 3200), 0))
            xf -= .2
            ventana.blit(FondoPantano, ((xf + 4000), 0))
            xf -= .2
            ventana.blit(FondoCueva, ((xf + 4800), 0))
            xf -= .2
            ventana.blit(FondoCueva, ((xf + 5600), 0))
            xf -= .2

            #   OTROS
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarCorazones(ventana, vidaPersonaje)

            dibujarEnemigos(ventana, listaZombies, listaEsqueletos, listaMinotauros, listaHLobos)
            dibujarBalas(ventana, listaBalas)

            moverBalas(listaBalas)
            moverEnemigos(listaZombies, listaEsqueletos, listaMinotauros, listaHLobos)

            choqueD = verificarChoqueDeb(listaZombies, listaEsqueletos, listaHLobos, spritePersonaje)
            choqueF = verificarChoqueFuer(listaMinotauros, spritePersonaje)

            choque = verificarChoqueEnemigos(listaZombies, listaEsqueletos, listaMinotauros, listaHLobos, listaBalas)
            puntaje = 0
            puntos = checarPuntaje(choque, puntaje)


            quitarVidasPer(choqueD, choqueF, vidaPersonaje)

            if len(vidaPersonaje) == 0:
                estado = Derrota

            victoria = llegarFinal(spritePersonaje)

            if victoria == True:
                estado = Victoria

        elif estado == Informacion:
            ventana.blit(FondoMenu, (0, 0))
            ventana.blit(Info, (0, 0))
            ventana.blit(BotonX, (745, 20))

        elif estado == Instrucciones:
            ventana.blit(FondoMenu, (0, 0))
            ventana.blit(Ins, (0, 0))
            ventana.blit(BotonX, (745, 20))

        elif estado == Puntaje:
            ventana.blit(FondoMenu, (0, 0))
            ventana.blit(BotonX, (745, 20))
            texto = fuente.render("PUNTOS OBTENIDOS: %d" %puntos)
            ventana.blit(texto, (ancho // 2 - 300, 50))

        elif estado == Derrota:
            ventana.blit(FondoNegro, (0, 0))
            ventana.blit(Gover, (170, 200))

        elif estado == Victoria:
            ventana.blit(FondoNegro, (0, 0))
            ventana.blit(Uwin, (100, 200))

        elif estado == Menu:
            ventana.blit(FondoMenu, (0, 0))
            dibujarMenu(ventana, BotonJugar, BotonIns, BotonPun, BotonInfo)

        pygame.display.flip()
        reloj.tick(40)

    pygame.quit()


def main():
    dibujarJuego()

main()
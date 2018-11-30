import pygame
from random import randint, randrange, uniform

pygame.init()
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mario Dodge")
JUGANDO = 1
MENU = 2
GAMEOVER = 3
velMario = 25


# Personaje
imgMario = pygame.image.load('Mario.png')
spriteMario = pygame.sprite.Sprite()
spriteMario.image = imgMario
spriteMario.rect = imgMario.get_rect()
spriteMario.rect.left = WIDTH / 2 - 25
spriteMario.rect.bottom = HEIGHT / 2 + 35
fondo = pygame.image.load("mario kingdom.jpg")
fondomenu = pygame.image.load("fondomenu.jpg")
botonjugar = pygame.image.load("botonmario.png")
gameOver = pygame.image.load("Game over.jpg")

# Enemigos
listaEnemigos = []
imgEnemigo = pygame.image.load("spiny egg.png")
for k in range(5):
    spriteEnemigo = pygame.sprite.Sprite()
    spriteEnemigo.image = imgEnemigo
    spriteEnemigo.rect = imgEnemigo.get_rect()
    spriteEnemigo.rect.left = randint(1, 100)
    spriteEnemigo.rect.bottom = randint(25, 550)
    spriteEnemigo.speed = [0.1, -0.1]
    listaEnemigos.append(spriteEnemigo)

# Enemigos
listaEnemigos2 = []
imgEnemigo2 = pygame.image.load("spiny egg.png")
for k in range(5):
    spriteEnemigo2 = pygame.sprite.Sprite()
    spriteEnemigo2.image = imgEnemigo
    spriteEnemigo2.rect = imgEnemigo.get_rect()
    spriteEnemigo2.rect.left = randint(1, 750)
    spriteEnemigo2.rect.bottom = randint(50, 100)
    spriteEnemigo2.speed = [0.2, -0.2]
    listaEnemigos2.append(spriteEnemigo2)

# Enemigos
listaEnemigos3 = []
imgEnemigo3 = pygame.image.load("spiny egg.png")
for k in range(4):
    spriteEnemigo3 = pygame.sprite.Sprite()
    spriteEnemigo3.image = imgEnemigo
    spriteEnemigo3.rect = imgEnemigo.get_rect()
    spriteEnemigo3.rect.left = randint(700, 750)
    spriteEnemigo3.rect.bottom = randint(50, 550)
    spriteEnemigo3.speed = [0.4, -0.4]
    listaEnemigos3.append(spriteEnemigo3)
# Enemigos
listaEnemigos4 = []
imgEnemigo4 = pygame.image.load("spiny egg.png")
for k in range(4):
    spriteEnemigo4 = pygame.sprite.Sprite()
    spriteEnemigo4.image = imgEnemigo
    spriteEnemigo4.rect = imgEnemigo.get_rect()
    spriteEnemigo4.rect.left = randint(25, 750)
    spriteEnemigo4.rect.bottom = randint(500, 550)
    spriteEnemigo4.speed = [0.2, -0.2]
    listaEnemigos4.append(spriteEnemigo4)

# sonnidos
musica = pygame.mixer.music.load("musica mario.mp3")
perdiste = pygame.mixer.Sound("smb_gameover.wav")

def dibujarPersonaje(screen, spriteMario):
    screen.blit(spriteMario.image, spriteMario.rect)


def dibujarEnemigos(screen, listaEnemigos):
    for enemigo in listaEnemigos:
        screen.blit(enemigo.image, enemigo.rect)


def dibujarEnemigos2(screen, listaEnemigos2):
    for enemigo in listaEnemigos2:
        screen.blit(enemigo.image, enemigo.rect)


def dibujarEnemigos3(screen, listaEnemigos3):
    for enemigo in listaEnemigos3:
        screen.blit(enemigo.image, enemigo.rect)


def dibujarEnemigos4(screen, listaEnemigos4):
    for enemigo in listaEnemigos4:
        screen.blit(enemigo.image, enemigo.rect)


def moverEnemigos(listaEnemigos, tiempo):
    for spriteEnemigo in listaEnemigos:
        spriteEnemigo.rect.centerx += spriteEnemigo.speed[0] * tiempo
        spriteEnemigo.rect.centery -= spriteEnemigo.speed[1] * tiempo
        if spriteEnemigo.rect.left <= 0 or spriteEnemigo.rect.right >= WIDTH:
            spriteEnemigo.speed[0] = -spriteEnemigo.speed[0]
            spriteEnemigo.rect.centerx += spriteEnemigo.speed[0] * tiempo
        if spriteEnemigo.rect.top <= 0 or spriteEnemigo.rect.bottom >= HEIGHT:
            spriteEnemigo.speed[1] = -spriteEnemigo.speed[1]
            spriteEnemigo.rect.centery -= spriteEnemigo.speed[1] * tiempo


def moverEnemigos2(listaEnemigos2, tiempo):
    for spriteEnemigo in listaEnemigos2:
        spriteEnemigo.rect.centerx -= spriteEnemigo.speed[0] * tiempo
        spriteEnemigo.rect.centery -= spriteEnemigo.speed[1] * tiempo
        if spriteEnemigo.rect.left <= 0 or spriteEnemigo.rect.right >= WIDTH:
            spriteEnemigo.speed[0] = -spriteEnemigo.speed[0]
            spriteEnemigo.rect.centerx -= spriteEnemigo.speed[0] * tiempo
        if spriteEnemigo.rect.top <= 0 or spriteEnemigo.rect.bottom >= HEIGHT:
            spriteEnemigo.speed[1] = -spriteEnemigo.speed[1]
            spriteEnemigo.rect.centery -= spriteEnemigo.speed[1] * tiempo


def moverEnemigos3(listaEnemigos3, tiempo):
    for spriteEnemigo in listaEnemigos3:
        spriteEnemigo.rect.centerx -= spriteEnemigo.speed[0] * tiempo
        spriteEnemigo.rect.centery += spriteEnemigo.speed[1] * tiempo
        if spriteEnemigo.rect.left <= 0 or spriteEnemigo.rect.right >= WIDTH:
            spriteEnemigo.speed[0] = -spriteEnemigo.speed[0]
            spriteEnemigo.rect.centerx -= spriteEnemigo.speed[0] * tiempo
        if spriteEnemigo.rect.top <= 0 or spriteEnemigo.rect.bottom >= HEIGHT:
            spriteEnemigo.speed[1] = -spriteEnemigo.speed[1]
            spriteEnemigo.rect.centery += spriteEnemigo.speed[1] * tiempo


def moverEnemigos4(listaEnemigos4, tiempo):
    for spriteEnemigo in listaEnemigos4:
        spriteEnemigo.rect.centerx += spriteEnemigo.speed[0] * tiempo
        spriteEnemigo.rect.centery += spriteEnemigo.speed[1] * tiempo
        if spriteEnemigo.rect.left <= 0 or spriteEnemigo.rect.right >= WIDTH:
            spriteEnemigo.speed[0] = -spriteEnemigo.speed[0]
            spriteEnemigo.rect.centerx += spriteEnemigo.speed[0] * tiempo
        if spriteEnemigo.rect.top <= 0 or spriteEnemigo.rect.bottom >= HEIGHT:
            spriteEnemigo.speed[1] = -spriteEnemigo.speed[1]
            spriteEnemigo.rect.centery += spriteEnemigo.speed[1] * tiempo

estado = MENU
globals()
contador = 0


def verificarMuerte(listaEnemigos, listaEnemigos2, listaEnemigos3, listaEnemigos4, spriteMario):
    global estado

    for enemigo in listaEnemigos:
        # mario vs enemigo
        xb = spriteMario.rect.left
        yb = spriteMario.rect.bottom
        xe = enemigo.rect.left
        ye = enemigo.rect.bottom
        ae = enemigo.rect.width
        altoe = enemigo.rect.height

        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
            estado = GAMEOVER


    for enemigo in listaEnemigos2:
        # Mario vs enemigo
        xb = spriteMario.rect.left
        yb = spriteMario.rect.bottom
        xe = enemigo.rect.left
        ye = enemigo.rect.bottom
        ae = enemigo.rect.width
        altoe = enemigo.rect.height
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
            estado = GAMEOVER

    for enemigo in listaEnemigos3:

        xb = spriteMario.rect.left
        yb = spriteMario.rect.bottom
        xe = enemigo.rect.left
        ye = enemigo.rect.bottom
        ae = enemigo.rect.width
        altoe = enemigo.rect.height
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
            estado = GAMEOVER




    for enemigo in listaEnemigos4:

        xb = spriteMario.rect.left
        yb = spriteMario.rect.bottom
        xe = enemigo.rect.left
        ye = enemigo.rect.bottom
        ae = enemigo.rect.width
        altoe = enemigo.rect.height
        if xb >= xe and xb <= xe + ae and yb >= ye and yb <= ye + altoe:
            estado = GAMEOVER






def dibujarMenu(screen, fondomenu, botonjugar):
    screen.blit(fondomenu, (0, 0))
    screen.blit(botonjugar, (WIDTH / 2 - 100, HEIGHT / 2 - 50))


def dibujarGAMEOVER(gameOver):
    screen.blit(gameOver, (0, 0))



pygame.mixer.music.play(1)
correrElJuego = True
while correrElJuego:


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            correrElJuego = False
        elif event.type == pygame.MOUSEBUTTONUP:
            xm, ym = pygame.mouse.get_pos()
            print(xm, ", ", ym)
            xb = WIDTH // 2 - 100
            yb = HEIGHT // 2 - 50
            if xm >= xb and xm <= xb + 201 and ym >= yb and ym <= yb + 100:
                estado = JUGANDO

    if estado == JUGANDO:


        pygame.display.update()
        pygame.display.flip()
        reloj = pygame.time.Clock()
        time = reloj.tick(40)
        screen.blit(fondo, (0, 0))
        dibujarPersonaje(screen, spriteMario)
        dibujarEnemigos(screen, listaEnemigos)
        dibujarEnemigos2(screen, listaEnemigos2)
        dibujarEnemigos3(screen, listaEnemigos3)
        dibujarEnemigos4(screen, listaEnemigos4)
        moverEnemigos(listaEnemigos, time)
        moverEnemigos2(listaEnemigos2, time)
        moverEnemigos3(listaEnemigos3, time)
        moverEnemigos4(listaEnemigos4, time)

        verificarMuerte(listaEnemigos2, listaEnemigos, listaEnemigos3, listaEnemigos4, spriteMario)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                correrElJuego = False

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and spriteMario.rect.left > 15:
            spriteMario.rect.left -= velMario

        if keys[pygame.K_RIGHT] and spriteMario.rect.left < 750:
            spriteMario.rect.left += velMario

        if keys[pygame.K_DOWN] and spriteMario.rect.bottom < 585:
            spriteMario.rect.bottom += velMario

        if keys[pygame.K_UP] and spriteMario.rect.bottom > 100:
            spriteMario.rect.bottom -= velMario

    if estado == MENU:

        dibujarMenu(screen, fondomenu, botonjugar)

        pygame.display.update()
        pygame.display.flip()
        reloj = pygame.time.Clock()
        reloj.tick(40)

    if estado == GAMEOVER:
        pygame.mixer.music.stop()

        while contador <=1:
            pygame.mixer.Sound.play(perdiste)
            contador += 1
        dibujarGAMEOVER(gameOver)
        pygame.display.update()
        pygame.display.flip()
        reloj = pygame.time.Clock()
        reloj.tick(300)

pygame.quit()

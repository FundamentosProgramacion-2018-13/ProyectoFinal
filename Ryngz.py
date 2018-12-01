#Alan Diaz Carrera

import pygame   # Librería de pygame

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600
# Colores
#  R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)
NEGRO =(0,0,0)
CAFE=(130,60,10)
BLANCO=(255,255,255)
AMARILLO=(223,223,0)

ESTADO="IDLE","PLAYING","END"
PERSO="NADA","PERSO","CIRCULO","ANILLO","FONDO"



titulo=pygame.image.load("titulo.png")
reintentar=pygame.image.load("reintetnar.png")

hitbox=pygame.image.load("hitbox.png")
sHitbox=pygame.sprite.Sprite()
sHitbox.image=hitbox
sHitbox.rect=hitbox.get_rect()
sHitbox.rect.left=385
sHitbox.rect.bottom=30

botonPerso=pygame.image.load("bpersonalizar.png")
btnPerso=pygame.sprite.Sprite()
btnPerso.image=botonPerso
btnPerso.rect=botonPerso.get_rect()
btnPerso.rect.left=325
btnPerso.rect.bottom=475
botonAnillo=pygame.image.load("banillo.png")
btnAnillo=pygame.sprite.Sprite()
btnAnillo.image=botonAnillo
btnAnillo.rect=botonAnillo.get_rect()
btnAnillo.rect.left=325
btnAnillo.rect.bottom=275
botonCirculo=pygame.image.load("bcirculo.png")
btnCirculo=pygame.sprite.Sprite()
btnCirculo.image=botonCirculo
btnCirculo.rect=botonCirculo.get_rect()
btnCirculo.rect.left=325
btnCirculo.rect.bottom=200
botonFondo=pygame.image.load("bfondo.png")
btnFondo=pygame.sprite.Sprite()
btnFondo.image=botonFondo
btnFondo.rect=botonFondo.get_rect()
btnFondo.rect.left=325
btnFondo.rect.bottom=350
botonRojo=pygame.image.load("brojo.png")
btnRojo=pygame.sprite.Sprite()
btnRojo.image=botonRojo
btnRojo.rect=botonRojo.get_rect()
btnRojo.rect.left=530
btnRojo.rect.bottom=200
botonAmarillo=pygame.image.load("bamarillo.png")
btnAmarillo=pygame.sprite.Sprite()
btnAmarillo.image=botonAmarillo
btnAmarillo.rect=botonAmarillo.get_rect()
btnAmarillo.rect.left=170
btnAmarillo.rect.bottom=275
botonNegro=pygame.image.load("bnegro.png")
btnNegro=pygame.sprite.Sprite()
btnNegro.image=botonNegro
btnNegro.rect=botonNegro.get_rect()
btnNegro.rect.left=170
btnNegro.rect.bottom=200
botonBlanco=pygame.image.load("bblanco.png")
btnBlanco=pygame.sprite.Sprite()
btnBlanco.image=botonBlanco
btnBlanco.rect=botonBlanco.get_rect()
btnBlanco.rect.left=170
btnBlanco.rect.bottom=200
botonAzul=pygame.image.load("bazul.png")
btnAzul=pygame.sprite.Sprite()
btnAzul.image=botonAzul
btnAzul.rect=botonAzul.get_rect()
btnAzul.rect.left=170
btnAzul.rect.bottom=350
botonVerde=pygame.image.load("bverde.png")
btnVerde=pygame.sprite.Sprite()
btnVerde.image=botonVerde
btnVerde.rect=botonVerde.get_rect()
btnVerde.rect.left=530
btnVerde.rect.bottom=275
botonCafe=pygame.image.load("bcafe.png")
btnCafe=pygame.sprite.Sprite()
btnCafe.image=botonCafe
btnCafe.rect=botonCafe.get_rect()
btnCafe.rect.left=530
btnCafe.rect.bottom=350
botonAtras=pygame.image.load("batras.png")
btnAtras=pygame.sprite.Sprite()
btnAtras.image=botonAtras
btnAtras.rect=botonAtras.get_rect()
btnAtras.rect.left=325
btnAtras.rect.bottom=475

cAmarillo = pygame.image.load("c amarillo.png")
spriteCAmarillo = pygame.sprite.Sprite()
spriteCAmarillo.image = cAmarillo
spriteCAmarillo.rect=cAmarillo.get_rect()
spriteCAmarillo.rect.left=370
spriteCAmarillo.rect.bottom=330
cAzul = pygame.image.load("c azul.png")
spriteCAzul = pygame.sprite.Sprite()
spriteCAzul.image = cAzul
spriteCAzul.rect = cAzul.get_rect()
spriteCAzul.rect.left = 370
spriteCAzul.rect.bottom = 330
cBlanco = pygame.image.load("c blanco.png")
spriteCBlanco = pygame.sprite.Sprite()
spriteCBlanco.image = cBlanco
spriteCBlanco.rect = cBlanco.get_rect()
spriteCBlanco.rect.left = 370
spriteCBlanco.rect.bottom = 330
cCafe = pygame.image.load("c cafe.png")
spriteCCafe = pygame.sprite.Sprite()
spriteCCafe.image = cCafe
spriteCCafe.rect = cCafe.get_rect()
spriteCCafe.rect.left = 370
spriteCCafe.rect.bottom = 330
cRojo = pygame.image.load("c rojo.png")
spriteCRojo = pygame.sprite.Sprite()
spriteCRojo.image = cRojo
spriteCRojo.rect = cRojo.get_rect()
spriteCRojo.rect.left = 370
spriteCRojo.rect.bottom = 330
cVerde = pygame.image.load("c verde.png")
spriteCVerde = pygame.sprite.Sprite()
spriteCVerde.image = cVerde
spriteCVerde.rect = cVerde.get_rect()
spriteCVerde.rect.left = 370
spriteCVerde.rect.bottom = 330

anamarillo=pygame.image.load("anamarillo.png")
spriteAamarillo=pygame.sprite.Sprite()
spriteAamarillo.image=anamarillo
spriteAamarillo.rect=anamarillo.get_rect()
spriteAamarillo.rect.bottom=600
spriteAamarillo.rect.left=100
anamarillo2 = pygame.image.load("anamarillo2.png")
spriteAamarillo2 = pygame.sprite.Sprite()
spriteAamarillo2.image = anamarillo2
spriteAamarillo2.rect=anamarillo2.get_rect()
spriteAamarillo2.rect.bottom=543
spriteAamarillo2.rect.left=157
anamarillo3 = pygame.image.load("anamarillo3.png")
spriteAamarillo3 = pygame.sprite.Sprite()
spriteAamarillo3.image = anamarillo3
spriteAamarillo3.rect=anamarillo3.get_rect()
spriteAamarillo3.rect.bottom=453
spriteAamarillo3.rect.left=247
anamarillo4 = pygame.image.load("anamarillo4.png")
spriteAamarillo4 = pygame.sprite.Sprite()
spriteAamarillo4.image = anamarillo4
spriteAamarillo4.rect=anamarillo4.get_rect()
spriteAamarillo4.rect.bottom=415
spriteAamarillo4.rect.left=285
anamarillo5 = pygame.image.load("anamarillo5.png")
spriteAamarillo5 = pygame.sprite.Sprite()
spriteAamarillo5.image = anamarillo5
spriteAamarillo5.rect=anamarillo5.get_rect()
spriteAamarillo5.rect.bottom=387
spriteAamarillo5.rect.left=313
anamarillo6 = pygame.image.load("anamarillo6.png")
spriteAamarillo6 = pygame.sprite.Sprite()
spriteAamarillo6.image = anamarillo6
spriteAamarillo6.rect=anamarillo6.get_rect()
spriteAamarillo6.rect.bottom=369
spriteAamarillo6.rect.left=331
anamarillo7 = pygame.image.load("anamarillo7.png")
spriteAamarillo7 = pygame.sprite.Sprite()
spriteAamarillo7.image = anamarillo7
spriteAamarillo7.rect=anamarillo7.get_rect()
spriteAamarillo7.rect.bottom=347
spriteAamarillo7.rect.left=353


anazul=pygame.image.load("anazul.png")
spriteAazul=pygame.sprite.Sprite()
spriteAazul.image=anazul
spriteAazul.rect=anazul.get_rect()
spriteAazul.rect.bottom=600
spriteAazul.rect.left=100
anazul2 = pygame.image.load("anazul2.png")
spriteAazul2 = pygame.sprite.Sprite()
spriteAazul2.image = anazul2
spriteAazul2.rect=anazul2.get_rect()
spriteAazul2.rect.bottom=543
spriteAazul2.rect.left=157
anazul3 = pygame.image.load("anazul3.png")
spriteAazul3 = pygame.sprite.Sprite()
spriteAazul3.image = anazul3
spriteAazul3.rect=anazul3.get_rect()
spriteAazul3.rect.bottom=453
spriteAazul3.rect.left=247
anazul4 = pygame.image.load("anazul4.png")
spriteAazul4 = pygame.sprite.Sprite()
spriteAazul4.image = anazul4
spriteAazul4.rect=anazul4.get_rect()
spriteAazul4.rect.bottom=415
spriteAazul4.rect.left=285
anazul5 = pygame.image.load("anazul5.png")
spriteAazul5 = pygame.sprite.Sprite()
spriteAazul5.image = anazul5
spriteAazul5.rect=anazul5.get_rect()
spriteAazul5.rect.bottom=387
spriteAazul5.rect.left=313
anazul6 = pygame.image.load("anazul6.png")
spriteAazul6 = pygame.sprite.Sprite()
spriteAazul6.image = anazul6
spriteAazul6.rect=anazul6.get_rect()
spriteAazul6.rect.bottom=369
spriteAazul6.rect.left=331
anazul7 = pygame.image.load("anazul7.png")
spriteAazul7 = pygame.sprite.Sprite()
spriteAazul7.image = anazul7
spriteAazul7.rect=anazul7.get_rect()
spriteAazul7.rect.bottom=347
spriteAazul7.rect.left=353

anblanco=pygame.image.load("anblanco.png")
spriteAblanco=pygame.sprite.Sprite()
spriteAblanco.image=anblanco
spriteAblanco.rect=anblanco.get_rect()
spriteAblanco.rect.bottom=600
spriteAblanco.rect.left=100
anblanco2 = pygame.image.load("anblanco2.png")
spriteAblanco2 = pygame.sprite.Sprite()
spriteAblanco2.image = anblanco2
spriteAblanco2.rect=anblanco2.get_rect()
spriteAblanco2.rect.bottom=543
spriteAblanco2.rect.left=157
anblanco3 = pygame.image.load("anblanco3.png")
spriteAblanco3 = pygame.sprite.Sprite()
spriteAblanco3.image = anblanco3
spriteAblanco3.rect=anblanco3.get_rect()
spriteAblanco3.rect.bottom=453
spriteAblanco3.rect.left=247
anblanco4 = pygame.image.load("anblanco4.png")
spriteAblanco4 = pygame.sprite.Sprite()
spriteAblanco4.image = anblanco4
spriteAblanco4.rect=anblanco4.get_rect()
spriteAblanco4.rect.bottom=415
spriteAblanco4.rect.left=285
anblanco5 = pygame.image.load("anblanco5.png")
spriteAblanco5 = pygame.sprite.Sprite()
spriteAblanco5.image = anblanco5
spriteAblanco5.rect=anblanco5.get_rect()
spriteAblanco5.rect.bottom=387
spriteAblanco5.rect.left=313
anblanco6 = pygame.image.load("anblanco6.png")
spriteAblanco6 = pygame.sprite.Sprite()
spriteAblanco6.image = anblanco6
spriteAblanco6.rect=anblanco6.get_rect()
spriteAblanco6.rect.bottom=369
spriteAblanco6.rect.left=331
anblanco7 = pygame.image.load("anblanco7.png")
spriteAblanco7 = pygame.sprite.Sprite()
spriteAblanco7.image = anblanco7
spriteAblanco7.rect=anblanco7.get_rect()
spriteAblanco7.rect.bottom=347
spriteAblanco7.rect.left=353

anblanco=pygame.image.load("ancafe.png")
spriteAcafe=pygame.sprite.Sprite()
spriteAcafe.image=anblanco
spriteAcafe.rect=anblanco.get_rect()
spriteAcafe.rect.bottom=600
spriteAcafe.rect.left=100
anblanco2 = pygame.image.load("ancafe2.png")
spriteAcafe2 = pygame.sprite.Sprite()
spriteAcafe2.image = anblanco2
spriteAcafe2.rect=anblanco2.get_rect()
spriteAcafe2.rect.bottom=543
spriteAcafe2.rect.left=157
anblanco3 = pygame.image.load("ancafe3.png")
spriteAcafe3 = pygame.sprite.Sprite()
spriteAcafe3.image = anblanco3
spriteAcafe3.rect=anblanco3.get_rect()
spriteAcafe3.rect.bottom=453
spriteAcafe3.rect.left=247
anblanco4 = pygame.image.load("ancafe4.png")
spriteAcafe4 = pygame.sprite.Sprite()
spriteAcafe4.image = anblanco4
spriteAcafe4.rect=anblanco4.get_rect()
spriteAcafe4.rect.bottom=415
spriteAcafe4.rect.left=285
anblanco5 = pygame.image.load("ancafe5.png")
spriteAcafe5 = pygame.sprite.Sprite()
spriteAcafe5.image = anblanco5
spriteAcafe5.rect=anblanco5.get_rect()
spriteAcafe5.rect.bottom=387
spriteAcafe5.rect.left=313
anblanco6 = pygame.image.load("ancafe6.png")
spriteAcafe6 = pygame.sprite.Sprite()
spriteAcafe6.image = anblanco6
spriteAcafe6.rect=anblanco6.get_rect()
spriteAcafe6.rect.bottom=369
spriteAcafe6.rect.left=331
anblanco7 = pygame.image.load("ancafe7.png")
spriteAcafe7 = pygame.sprite.Sprite()
spriteAcafe7.image = anblanco7
spriteAcafe7.rect=anblanco7.get_rect()
spriteAcafe7.rect.bottom=347
spriteAcafe7.rect.left=353

anblanco=pygame.image.load("anrojo.png")
spriteArojo=pygame.sprite.Sprite()
spriteArojo.image=anblanco
spriteArojo.rect=anblanco.get_rect()
spriteArojo.rect.bottom=600
spriteArojo.rect.left=100
anblanco2 = pygame.image.load("anrojo2.png")
spriteArojo2 = pygame.sprite.Sprite()
spriteArojo2.image = anblanco2
spriteArojo2.rect=anblanco2.get_rect()
spriteArojo2.rect.bottom=543
spriteArojo2.rect.left=157
anblanco3 = pygame.image.load("anrojo3.png")
spriteArojo3 = pygame.sprite.Sprite()
spriteArojo3.image = anblanco3
spriteArojo3.rect=anblanco3.get_rect()
spriteArojo3.rect.bottom=453
spriteArojo3.rect.left=247
anblanco4 = pygame.image.load("anrojo4.png")
spriteArojo4 = pygame.sprite.Sprite()
spriteArojo4.image = anblanco4
spriteArojo4.rect=anblanco4.get_rect()
spriteArojo4.rect.bottom=415
spriteArojo4.rect.left=285
anblanco5 = pygame.image.load("anrojo5.png")
spriteArojo5 = pygame.sprite.Sprite()
spriteArojo5.image = anblanco5
spriteArojo5.rect=anblanco5.get_rect()
spriteArojo5.rect.bottom=387
spriteArojo5.rect.left=313
anblanco6 = pygame.image.load("anrojo6.png")
spriteArojo6 = pygame.sprite.Sprite()
spriteArojo6.image = anblanco6
spriteArojo6.rect=anblanco6.get_rect()
spriteArojo6.rect.bottom=369
spriteArojo6.rect.left=331
anblanco7 = pygame.image.load("anrojo7.png")
spriteArojo7 = pygame.sprite.Sprite()
spriteArojo7.image = anblanco7
spriteArojo7.rect=anblanco7.get_rect()
spriteArojo7.rect.bottom=347
spriteArojo7.rect.left=353

anblanco=pygame.image.load("anverde.png")
spriteAverde=pygame.sprite.Sprite()
spriteAverde.image=anblanco
spriteAverde.rect=anblanco.get_rect()
spriteAverde.rect.bottom=600
spriteAverde.rect.left=100
anblanco2 = pygame.image.load("anverde2.png")
spriteAverde2 = pygame.sprite.Sprite()
spriteAverde2.image = anblanco2
spriteAverde2.rect=anblanco2.get_rect()
spriteAverde2.rect.bottom=543
spriteAverde2.rect.left=157
anblanco3 = pygame.image.load("anverde3.png")
spriteAverde3 = pygame.sprite.Sprite()
spriteAverde3.image = anblanco3
spriteAverde3.rect=anblanco3.get_rect()
spriteAverde3.rect.bottom=453
spriteAverde3.rect.left=247
anblanco4 = pygame.image.load("anverde4.png")
spriteAverde4 = pygame.sprite.Sprite()
spriteAverde4.image = anblanco4
spriteAverde4.rect=anblanco4.get_rect()
spriteAverde4.rect.bottom=415
spriteAverde4.rect.left=285
anblanco5 = pygame.image.load("anverde5.png")
spriteAverde5 = pygame.sprite.Sprite()
spriteAverde5.image = anblanco5
spriteAverde5.rect=anblanco5.get_rect()
spriteAverde5.rect.bottom=387
spriteAverde5.rect.left=313
anblanco6 = pygame.image.load("anverde6.png")
spriteAverde6 = pygame.sprite.Sprite()
spriteAverde6.image = anblanco6
spriteAverde6.rect=anblanco6.get_rect()
spriteAverde6.rect.bottom=369
spriteAverde6.rect.left=331
anblanco7 = pygame.image.load("anverde7.png")
spriteAverde7 = pygame.sprite.Sprite()
spriteAverde7.image = anblanco7
spriteAverde7.rect=anblanco7.get_rect()
spriteAverde7.rect.bottom=347
spriteAverde7.rect.left=353

sprite=0
listaSprite=[]

def AnBl(ventana,sprite):
    if sprite>=80/40:
        sprite=0
    elif sprite>=1/40 and sprite<=10/40:
        ventana.blit(spriteAblanco.image,spriteAblanco.rect)
    if sprite>=11/40 and sprite<=20/40:
        ventana.blit(spriteAblanco2.image,spriteAblanco2.rect)
    if sprite>=21/40 and sprite<=30/40:
        ventana.blit(spriteAblanco3.image,spriteAblanco3.rect)
    if sprite>=31/40 and sprite<=40/40:
        ventana.blit(spriteAblanco4.image,spriteAblanco4.rect)
    if sprite>=41/40 and sprite<=50/40:
        ventana.blit(spriteAblanco5.image,spriteAblanco5.rect)
    if sprite>=51/40 and sprite<=60/40:
        ventana.blit(spriteAblanco6.image,spriteAblanco6.rect)
    if sprite>=61/40 and sprite<=79/40:
        ventana.blit(spriteAblanco7.image,spriteAblanco7.rect)

def AnAm(ventana,sprite):
    if sprite>=80/40:
        sprite=0
    elif sprite>=1/40 and sprite<=10/40:
        ventana.blit(spriteAamarillo.image,spriteAamarillo.rect)
    if sprite>=11/40 and sprite<=20/40:
        ventana.blit(spriteAamarillo2.image,spriteAamarillo2.rect)
    if sprite>=21/40 and sprite<=30/40:
        ventana.blit(spriteAamarillo3.image,spriteAamarillo3.rect)
    if sprite>=31/40 and sprite<=40/40:
        ventana.blit(spriteAamarillo4.image,spriteAamarillo4.rect)
    if sprite>=41/40 and sprite<=50/40:
        ventana.blit(spriteAamarillo5.image,spriteAamarillo5.rect)
    if sprite>=51/40 and sprite<=60/40:
        ventana.blit(spriteAamarillo6.image,spriteAamarillo6.rect)
    if sprite>=61/40 and sprite<=79/40:
        ventana.blit(spriteAamarillo7.image,spriteAamarillo7.rect)

def AnAz(ventana,sprite):
    if sprite>=80/40:
        sprite=0
    elif sprite>=1/40 and sprite<=10/40:
        ventana.blit(spriteAazul.image,spriteAazul.rect)
    if sprite>=11/40 and sprite<=20/40:
        ventana.blit(spriteAazul2.image,spriteAazul2.rect)
    if sprite>=21/40 and sprite<=30/40:
        ventana.blit(spriteAazul3.image,spriteAazul3.rect)
    if sprite>=31/40 and sprite<=40/40:
        ventana.blit(spriteAazul4.image,spriteAazul4.rect)
    if sprite>=41/40 and sprite<=50/40:
        ventana.blit(spriteAazul5.image,spriteAazul5.rect)
    if sprite>=51/40 and sprite<=60/40:
        ventana.blit(spriteAazul6.image,spriteAazul6.rect)
    if sprite>=61/40 and sprite<=79/40:
        ventana.blit(spriteAazul7.image,spriteAazul7.rect)

def AnRo(ventana,sprite):
    if sprite>=80/40:
        sprite=0
    elif sprite>=1/40 and sprite<=10/40:
        ventana.blit(spriteArojo.image,spriteArojo.rect)
    if sprite>=11/40 and sprite<=20/40:
        ventana.blit(spriteArojo2.image,spriteArojo2.rect)
    if sprite>=21/40 and sprite<=30/40:
        ventana.blit(spriteArojo3.image,spriteArojo3.rect)
    if sprite>=31/40 and sprite<=40/40:
        ventana.blit(spriteArojo4.image,spriteArojo4.rect)
    if sprite>=41/40 and sprite<=50/40:
        ventana.blit(spriteArojo5.image,spriteArojo5.rect)
    if sprite>=51/40 and sprite<=60/40:
        ventana.blit(spriteArojo6.image,spriteArojo6.rect)
    if sprite>=61/40 and sprite<=79/40:
        ventana.blit(spriteArojo7.image,spriteArojo7.rect)

def AnVe(ventana,sprite):
    if sprite>=80/40:
        sprite=0
    elif sprite>=1/40 and sprite<=10/40:
        ventana.blit(spriteAverde.image,spriteAverde.rect)
    if sprite>=11/40 and sprite<=20/40:
        ventana.blit(spriteAverde2.image,spriteAverde2.rect)
    if sprite>=21/40 and sprite<=30/40:
        ventana.blit(spriteAverde3.image,spriteAverde3.rect)
    if sprite>=31/40 and sprite<=40/40:
        ventana.blit(spriteAverde4.image,spriteAverde4.rect)
    if sprite>=41/40 and sprite<=50/40:
        ventana.blit(spriteAverde5.image,spriteAverde5.rect)
    if sprite>=51/40 and sprite<=60/40:
        ventana.blit(spriteAverde6.image,spriteAverde6.rect)
    if sprite>=61/40 and sprite<=79/40:
        ventana.blit(spriteAverde7.image,spriteAverde7.rect)

def AnCa(ventana,sprite):
    if sprite>=80/40:
        sprite=0
    elif sprite>=1/40 and sprite<=10/40:
        ventana.blit(spriteAcafe.image,spriteAcafe.rect)
    if sprite>=11/40 and sprite<=20/40:
        ventana.blit(spriteAcafe2.image,spriteAcafe2.rect)
    if sprite>=21/40 and sprite<=30/40:
        ventana.blit(spriteAcafe3.image,spriteAcafe3.rect)
    if sprite>=31/40 and sprite<=40/40:
        ventana.blit(spriteAcafe4.image,spriteAcafe4.rect)
    if sprite>=41/40 and sprite<=50/40:
        ventana.blit(spriteAcafe5.image,spriteAcafe5.rect)
    if sprite>=51/40 and sprite<=60/40:
        ventana.blit(spriteAcafe6.image,spriteAcafe6.rect)
    if sprite>=61/40 and sprite<=79/40:
        ventana.blit(spriteAcafe7.image,spriteAcafe7.rect)


listaHitbox1=[]
listaHitbox2=[]
listaHitbox3=[]
listaBotones=[]


puntos=0

def fondos(fondo, ventana):
    if fondo == 0:
        ventana.fill(NEGRO)
    if fondo == 1:
        ventana.fill(AMARILLO)
    if fondo == 2:
        ventana.fill(AZUL)
    if fondo == 3:
        ventana.fill(ROJO)
    if fondo == 4:
        ventana.fill(VERDE)
    if fondo == 5:
        ventana.fill(CAFE)

def botones():
    listaBotones.append(btnCafe)
    listaBotones.append(btnBlanco)
    listaBotones.append(btnVerde)
    listaBotones.append(btnRojo)
    listaBotones.append(btnAzul)
    listaBotones.append(btnNegro)
    listaBotones.append(btnAmarillo)
    listaBotones.append(btnAtras)
    listaBotones.append(btnFondo)
    listaBotones.append(btnAnillo)
    listaBotones.append(btnCirculo)
    listaBotones.append(btnPerso)





# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    sprite=0
    hEstar=0
    #0 negro, 1 amarillo, 2 azul, 3 rojo, 4 verde, 5 cafe
    anillo=0
    circulo=0
    fondo=0
    ESTADO="IDLE"
    PERSO="NADA"
    puntos=0

    pygame.mixer.init()

    menu=pygame.mixer.Sound("menu inicio.wav")
    juego=pygame.mixer.Sound("juego inicia.wav")
    puntar=pygame.mixer.Sound("point.wav")
    muerte=pygame.mixer.Sound("muerte.wav")


    # Inicializa el motor de pygame
    pygame.init()
    fuente = pygame.font.SysFont("Arial", 80)
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    menu.play(-1)


    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no


    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente

        fondos(fondo, ventana)
        botones()

        if ESTADO == "IDLE" and PERSO == "NADA":
            ventana.blit(titulo, (279, 110))
            ventana.blit(btnPerso.image, btnPerso.rect)
            listaBotones.remove(btnCirculo)
            listaBotones.remove(btnAnillo)
            listaBotones.remove(btnFondo)
            listaBotones.remove(btnAtras)
            listaBotones.remove(btnAmarillo)
            listaBotones.remove(btnNegro)
            listaBotones.remove(btnAzul)
            listaBotones.remove(btnRojo)
            listaBotones.remove(btnVerde)
            listaBotones.remove(btnBlanco)
            listaBotones.remove(btnCafe)
            botones()
        elif ESTADO == "IDLE" and PERSO == "PERSO":
            ventana.blit(btnCirculo.image, btnCirculo.rect)
            ventana.blit(btnAnillo.image, btnAnillo.rect)
            ventana.blit(btnFondo.image, btnFondo.rect)
            ventana.blit(btnAtras.image, btnAtras.rect)
            listaBotones.remove(btnPerso)
            listaBotones.append(btnPerso)
        elif ESTADO == "IDLE" and PERSO == "FONDO":
            listaBotones.remove(btnBlanco)
            ventana.blit(btnNegro.image, btnNegro.rect)
            ventana.blit(btnAmarillo.image, btnAmarillo.rect)
            ventana.blit(btnAzul.image, btnAzul.rect)
            ventana.blit(btnRojo.image, btnRojo.rect)
            ventana.blit(btnVerde.image, btnVerde.rect)
            ventana.blit(btnCafe.image, btnCafe.rect)
            ventana.blit(btnCirculo.image, btnCirculo.rect)
            ventana.blit(btnAnillo.image, btnAnillo.rect)
            ventana.blit(btnFondo.image, btnFondo.rect)
            ventana.blit(btnAtras.image, btnAtras.rect)
            listaBotones.append(btnBlanco)
        elif ESTADO == "IDLE" and PERSO == "CIRCULO":
            listaBotones.remove(btnNegro)
            ventana.blit(btnBlanco.image, btnBlanco.rect)
            ventana.blit(btnAmarillo.image, btnAmarillo.rect)
            ventana.blit(btnAzul.image, btnAzul.rect)
            ventana.blit(btnRojo.image, btnRojo.rect)
            ventana.blit(btnVerde.image, btnVerde.rect)
            ventana.blit(btnCafe.image, btnCafe.rect)
            ventana.blit(btnCirculo.image, btnCirculo.rect)
            ventana.blit(btnAnillo.image, btnAnillo.rect)
            ventana.blit(btnFondo.image, btnFondo.rect)
            ventana.blit(btnAtras.image, btnAtras.rect)
            listaBotones.append(btnNegro)
        elif ESTADO == "IDLE" and PERSO == "ANILLO":
            listaBotones.remove(btnNegro)
            ventana.blit(btnBlanco.image, btnBlanco.rect)
            ventana.blit(btnAmarillo.image, btnAmarillo.rect)
            ventana.blit(btnAzul.image, btnAzul.rect)
            ventana.blit(btnRojo.image, btnRojo.rect)
            ventana.blit(btnVerde.image, btnVerde.rect)
            ventana.blit(btnCafe.image, btnCafe.rect)
            ventana.blit(btnCirculo.image, btnCirculo.rect)
            ventana.blit(btnAnillo.image, btnAnillo.rect)
            ventana.blit(btnFondo.image, btnFondo.rect)
            ventana.blit(btnAtras.image, btnAtras.rect)
            listaBotones.append(btnNegro)

        if ESTADO == "PLAYING":
            ventana.blit(sHitbox.image, sHitbox.rect)
            if circulo == 0:
                ventana.blit(spriteCBlanco.image, spriteCBlanco.rect)
            elif circulo == 1:
                ventana.blit(spriteCAmarillo.image, spriteCAmarillo.rect)
            elif circulo == 2:
                ventana.blit(spriteCAzul.image, spriteCAzul.rect)
            elif circulo == 3:
                ventana.blit(spriteCRojo.image, spriteCRojo.rect)
            elif circulo == 4:
                ventana.blit(spriteCVerde.image, spriteCVerde.rect)
            elif circulo == 5:
                ventana.blit(spriteCCafe.image, spriteCCafe.rect)

        if ESTADO == "PLAYING":
            texto = fuente.render(str(puntos), 1, BLANCO)
            ventana.blit(texto, (370, 100))
            sHitbox.rect.bottom += 4
            if sHitbox.rect.bottom <= 330 and sHitbox.rect.bottom >= 285:
                ESTADO = "ENDED"
                sprite=0
                juego.stop()
                muerte.play()
                sHitbox.rect.bottom=30
            if sHitbox.rect.bottom>=225 and sHitbox.rect.bottom<=250:
                hEstar=1
            sprite += 1 / 40
            if sprite==80/40:
                sprite=0
            if anillo==0:
                AnBl(ventana,sprite)
            elif anillo==1:
                AnAm(ventana,sprite)
            elif anillo==2:
                AnAz(ventana,sprite)
            elif anillo==3:
                AnRo(ventana,sprite)
            elif anillo==4:
                AnVe(ventana,sprite)
            elif anillo==5:
                AnCa(ventana,sprite)


        if ESTADO=="ENDED":
            ventana.blit(reintentar,(292,258))
            ventana.blit(texto, (370, ))
            juego.stop()

        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo


            if evento.type ==pygame.KEYDOWN:
                if ESTADO=="ENDED":
                    if evento.key==pygame.K_SPACE:
                        sHitbox.rect.bottom=30
                        ESTADO="IDLE"
                        menu.play(-1)
                        puntos=0
                elif ESTADO=="PLAYING":
                    if evento.key==pygame.K_UP or evento.key==pygame.K_SPACE:
                        if hEstar==0:
                            ESTADO="ENDED"
                            muerte.play()
                            sprite=0
                        elif hEstar ==1:
                            puntos+=1
                            puntar.play()
                            sHitbox.rect.bottom=30
                            hEstar=0
                            sprite=0

                elif ESTADO=="IDLE":
                    if evento.key==pygame.K_SPACE:
                        ESTADO="PLAYING"
                        menu.stop()
                        juego.play(-1)



            if evento.type == pygame.MOUSEBUTTONDOWN and ESTADO=="IDLE":
                xm,ym=pygame.mouse.get_pos()
                xPer,yPer,anchoPer,altoPer=btnPerso.rect
                xAtras,yAtras,anchoAtras,altoAtras=btnAtras.rect
                xAnillo, yAnillo, anchoAnillo, altoAnillo = btnAnillo.rect
                xFondo, yFondo, anchoFondo, altoFondo = btnFondo.rect
                xCirculo, yCirculo, anchoCirculo, altoCirculo=btnCirculo.rect
                xBlanco,yBlanco,anchoBlanco,altBlanco=btnBlanco.rect
                xNegro,yNegro,anchoNegro,altoNegro=btnNegro.rect
                xYellow, yYellow, anchoYellow, altoYellow = btnAmarillo.rect
                xZul,yZul,anchoZul,altoZul=btnAzul.rect
                xRojo,yRojo,anchoRojo,altoRojo=btnRojo.rect
                xVerde,yVerde,anchoVerde,altoVerde=btnVerde.rect
                xCafe,yCafe,anchoCafe,altoCafe=btnCafe.rect
                if xm <= xAnillo + anchoAnillo and xm >= xAnillo and ym <= yAtras + altoAnillo and ym >= yAnillo and (PERSO == "PERSO" or PERSO=="FONDO" or PERSO=="CIRCULO"):
                    PERSO = "ANILLO"
                if xm <= xFondo + anchoFondo and xm >= xFondo and ym <= yFondo + altoFondo and ym >= yFondo and (PERSO == "PERSO"or PERSO=="ANILLO" or PERSO=="CIRCULO"):
                    PERSO = "FONDO"
                if xm <= xCirculo + anchoCirculo and xm >= xCirculo and ym <= yCirculo + altoCirculo and ym >= yCirculo and (PERSO == "PERSO" or PERSO=="ANILLO" or PERSO=="FONDO"):
                    PERSO = "CIRCULO"
                if PERSO=="ANILLO":
                    if xm <=xBlanco+anchoBlanco and xm>=xBlanco and ym>=yBlanco and ym<=yBlanco+altBlanco:
                        anillo=0
                    if xm <=xYellow+anchoYellow and xm>=xYellow and ym>=yYellow and ym<=yYellow+altoYellow:
                        anillo=1
                    if xm <=xZul+anchoZul and xm>=xZul and ym>=yZul and ym<=yZul+altoZul:
                        anillo=2
                    if xm <=xRojo+anchoRojo and xm>=xRojo and ym>=yRojo and ym<=yRojo+altoRojo:
                        anillo=3
                    if xm <=xVerde+anchoVerde and xm>=xVerde and ym>=yVerde and ym<=yVerde+altoVerde:
                        anillo=4
                    if xm <=xCafe+anchoCafe and xm>=xCafe and ym>=yCafe and ym<=yCafe+altoCafe:
                        anillo=5
                if PERSO=="FONDO":
                    if xm <=xBlanco+anchoNegro and xm>=xNegro and ym>=yNegro and ym<=yNegro+altoNegro:
                        fondo=0
                    if xm <=xYellow+anchoYellow and xm>=xYellow and ym>=yYellow and ym<=yYellow+altoYellow:
                        fondo=1
                    if xm <=xZul+anchoZul and xm>=xZul and ym>=yZul and ym<=yZul+altoZul:
                        fondo=2
                    if xm <=xRojo+anchoRojo and xm>=xRojo and ym>=yRojo and ym<=yRojo+altoRojo:
                        fondo=3
                    if xm <=xVerde+anchoVerde and xm>=xVerde and ym>=yVerde and ym<=yVerde+altoVerde:
                        fondo=4
                    if xm <=xCafe+anchoCafe and xm>=xCafe and ym>=yCafe and ym<=yCafe+altoCafe:
                        fondo=5
                if PERSO=="CIRCULO":
                    if xm <=xBlanco+anchoBlanco and xm>=xBlanco and ym>=yBlanco and ym<=yBlanco+altBlanco:
                        circulo=0
                    if xm <=xYellow+anchoYellow and xm>=xYellow and ym>=yYellow and ym<=yYellow+altoYellow:
                        circulo=1
                    if xm <=xZul+anchoZul and xm>=xZul and ym>=yZul and ym<=yZul+altoZul:
                        circulo=2
                    if xm <=xRojo+anchoRojo and xm>=xRojo and ym>=yRojo and ym<=yRojo+altoRojo:
                        circulo=3
                    if xm <=xVerde+anchoVerde and xm>=xVerde and ym>=yVerde and ym<=yVerde+altoVerde:
                        circulo=4
                    if xm <=xCafe+anchoCafe and xm>=xCafe and ym>=yCafe and ym<=yCafe+altoCafe:
                        circulo=5
                if xm <= xPer+anchoPer and xm >=xPer and ym <=yPer+altoPer and ym>=yPer and PERSO=="NADA":
                    PERSO="PERSO"
                elif xm <= xAtras + anchoAtras and xm >= xAtras and ym <= yAtras + altoAtras and ym >= yAtras and (PERSO == "PERSO" or PERSO=="ANILLO" or PERSO=="FONDO" or PERSO=="CIRCULO"):
                    PERSO = "NADA"
        # Dibujar, aquí haces todos los trazos que requieras
        # Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
        # Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw

        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
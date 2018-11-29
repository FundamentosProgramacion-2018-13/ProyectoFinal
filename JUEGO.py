#El anibals


import pygame
import math
import random


ANCHO = 800
ALTO = 600
# Colores
BLANCO = (255, 255, 255)
VERDE_BANDERA = (27, 94, 32)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
def dibujarPersonaje(ventana,spriteBolita):
    ventana.blit(spriteBolita.image,spriteBolita.rect)


def moverCañon(ventana,bolitaCañon):
    xm, ym = pygame.mouse.get_pos()

    if xm<ANCHO//2:
        xmConvertida=xm-ANCHO//2
    if xm>ANCHO//2:
        xmConvertida=xm-ANCHO//2
    if ym<ALTO//2:
        ymConvertida=ALTO//2-ym
    if ym>ALTO//2:
        ymConvertida=ALTO//2-ym
        angulo = math.atan((ymConvertida / xmConvertida))
    #if xm==ANCHO//2 and ym==ALTO//2:
        #pass
    #if xm==ANCHO//2 and ym <ALTO//2:
        #angulo=math.radians(90)
    #if xm==ANCHO//2 and ym> ALTO//2:
        #angulo= math.radians(270)
    #if xm>ANCHO//2 and ym== ALTO//2:
        #angulo=math.radians(0)
    #if #xm<ANCHO//2 and ym==ALTO//2:
        #angulo=math.radians(180)




    corX = int(math.cos((angulo)) * 40)+ANCHO//2
    cory = int((math.sin(angulo)) * 40)+ALTO//2
    #print("coords x",xm,xmConvertida)
    #print("coords y",ym,ymConvertida)
    #print("angulo",angulo)
    #print("______")
    bolitaCañon.rect.top=cory

    bolitaCañon.rect.left=corX



def dibujarCañon(ventana, spriteCañon):
    ventana.blit(spriteCañon.image, spriteCañon.rect)


# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no

    #PERSONAJE PRINCIPAL
    bolitaPrincipal= pygame.image.load("bola.png")
    spriteBolita=pygame.sprite.Sprite()
    spriteBolita.image=bolitaPrincipal
    spriteBolita.rect= bolitaPrincipal.get_rect()
    spriteBolita.rect.bottom= ALTO//2+60
    spriteBolita.rect.left=ANCHO//2-60
    #CAÑON
    bolitaCañon = pygame.image.load("bola 2.png")
    spriteCañon = pygame.sprite.Sprite()
    spriteCañon.image = bolitaCañon
    spriteCañon.rect = bolitaCañon.get_rect()
    spriteCañon.rect.bottom = ALTO // 2
    spriteCañon.rect.left = ANCHO // 2




    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo



        # Borrar pantalla
        ventana.fill(BLANCO)
        #dibujarPersonaje(ventana, spriteBolita)
        dibujarCañon(ventana, spriteCañon)
        moverCañon(ventana,spriteCañon)




        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps


    pygame.quit()



def main():
    dibujar()


# Llamas a la función principal
main()
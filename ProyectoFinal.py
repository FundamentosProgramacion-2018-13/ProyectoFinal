# encoding: UTF-8
# Autor: Carlos Alberto Reyes Ortiz
# Es un de basketball para dos jugadores

#Atribuciones:
#Balón: <a href="https://www.freepik.es/fotos-vectores-gratis/fondo">Vector de fondo creado por brgfx - www.freepik.es</a>
#Jugadores: Vector Designed By Peimsak Tipyasoontranon from  <a href="https://pngtree.com/freepng/shot-cartoon-man_3500301.html">pngtree.com</a>
#Cancha de basket: Vector Designed By szubaster from  <a href="https://pngtree.com/freepng/basketball-court-model_3347105.html">pngtree.com</a>
#Fondo de ladrillos:<a href="https://www.freepik.es/fotos-vectores-gratis/fondo">Foto de fondo creado por kjpargeter - www.freepik.es</a>
#Sonidos: https://www.freesoundeffects.com/free-sounds/basketball-10100/
import pygame   # Librería de pygame
from random import randrange

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE = (76, 187, 23)
VERDE_BANDERA = (27, 94, 32)    # un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)      # solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)      # nada de rojo, ni verde, solo azul
NARANJA = (239, 127, 26)

#ESTADOS
MENU = 1
JUGANDO = 2
INSTRUCCIONES = 3
VERDES = 4
BLANCOS = 5
ATRIBUCIONES = 6

#Estados de movimiento
QUIETO = 1
IZQ = 2   #ABAJO
DER = 3   #ARRIBA


##############

def moverBalonPersonaje(spritePersonaje, spritePersonajeTres):  #Mueve el balon con el el personaje uno
        if spritePersonaje.rect.left == spritePersonajeTres.rect.left-15:
            spritePersonajeTres.rect.left+=10


def moverBalonPersonajeDos(spritePersonajeDos, spritePersonajeTres):#Mueve el balon con el el personaje dos
        if spritePersonajeDos.rect.left == spritePersonajeTres.rect.left:
            spritePersonajeTres.rect.left-=10


def hacerBalonDisparar(spritePersonaje,spritePersonajeDos,spritePersonajeTres): #Hace que el balon se mueva en x randmo cuando los dos interactuan con el balón al mismo tiempo

    if spritePersonaje.rect.left == spritePersonajeTres.rect.left-15 and spritePersonajeDos.rect.left == spritePersonajeTres.rect.left:
        spritePersonajeTres.rect.left+= randrange(-90,90,30)


def dibujarPersonaje(ventana, spritePersonaje): #Dibuja al personaje uno
    ventana.blit(spritePersonaje.image,spritePersonaje.rect)



def dibujarPersonajeDos(ventana, spritePersonajeDos): #Dibuja al personaje dos
    ventana.blit(spritePersonajeDos.image,spritePersonajeDos.rect)



def dibujarPersonajeTres(ventana, spritePersonajeTres):  #Dibuja al balón
    ventana.blit(spritePersonajeTres.image,spritePersonajeTres.rect)


def dibujarMenu(ventana, imgBtnJugar):  #Dibuja el boton para jugar
    ventana.blit(imgBtnJugar,(ANCHO//2-128,ALTO//3))


def dibujarInstrucciones(ventana,imgBtnInst): #Dibuja el boton para las instrucciones
    ventana.blit(imgBtnInst, (ANCHO/20,ALTO/10))


def dibujarBotonRegresar(ventana,imgBtnRegresar): #Dibuja el boton para regresar al menu
    ventana.blit(imgBtnRegresar, (ANCHO//20, ALTO//2+150))


def dibujarBotonMenu(ventana, imgBtnMenu): #Dibuja el boton para ir al menu
    ventana.blit(imgBtnMenu, (ANCHO // 20, ALTO // 2 + 150))


def dibujarBotonAtribuciones(ventana,imgBtnAtribuciones): #Dibuja el boton para ver las atribuciones
    ventana.blit(imgBtnAtribuciones, (ANCHO - 200, ALTO//10))




#############
# Estructura del todo el programa
def dibujar():
    # Inicializa el motor de pygame
    pygame.init()
    # Crea una ventana de ANCHO x ALTO
    ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
    reloj = pygame.time.Clock()  # Para limitar los fps
    termina = False  # Bandera para saber si termina la ejecución, iniciamos suponiendo que no
###########

# Player Izquierdo
    imgPersonaje = pygame.image.load("playerIzq.png")
    spritePersonaje = pygame.sprite.Sprite()
    spritePersonaje.image = imgPersonaje
    spritePersonaje.rect = imgPersonaje.get_rect()
    spritePersonaje.rect.left = 125
    spritePersonaje.rect.bottom = 430


# Player Derecho
    imgPersonajeDos = pygame.image.load("playerDer.png")
    spritePersonajeDos = pygame.sprite.Sprite()
    spritePersonajeDos.image = imgPersonajeDos
    spritePersonajeDos.rect = imgPersonajeDos.get_rect()
    spritePersonajeDos.rect.left = 620
    spritePersonajeDos.rect.bottom = 430


# Balón
    imgPersonajeTres = pygame.image.load("balon.png")
    spritePersonajeTres = pygame.sprite.Sprite()
    spritePersonajeTres.image = imgPersonajeTres
    spritePersonajeTres.rect = imgPersonajeTres.get_rect()
    spritePersonajeTres.rect.left = 380
    spritePersonajeTres.rect.bottom = 255


    estado = MENU
    xf = 0  # x DEL FONDO

    # Contadores
    puntosVerdes = 0
    puntosBlancos = 0


    #Botones
    imgBtnJugar  = pygame.image.load("botonJugar.png")
    imgBtnInst = pygame.image.load("botonInstrucciones.png")
    imgBtnRegresar = pygame.image.load("botonRegresar.png")
    imgBtnMenu = pygame.image.load("botonMenu.png")
    imgBtnAtribuciones = pygame.image.load("botonAtribuciones.png")


    #Fondo
    imgLadrillos = pygame.image.load("LadrillosNegros.jpg")
    imgCourt = pygame.image.load("court.png")
    instrucciones = pygame.image.load("Instrucciones.png")
    atribuciones = pygame.image.load("atribuciones.png")

    movPerDos = QUIETO    #PlayerDos
    movPer = QUIETO       #PlayerUno

    # Tiempo
    timer = 0  # acumulador de tiempo

    # texto
    fuente = pygame.font.SysFont("monospace", 32)

    # audios
    pygame.mixer.init()

    efectoBounces = pygame.mixer.Sound("bounces.wav")
    efectoTribuna = pygame.mixer.Sound("tribuna.wav")
    efectoCrowd = pygame.mixer.Sound("crowd.wav")
    musicMenu = pygame.mixer.Sound("musicMenu.wav")


#Posiciones
    xImgPersonaje = spritePersonaje.rect.left
    yImgPersonaje = spritePersonaje.rect.bottom

    xImgPersonajeTres = spritePersonajeTres.rect.left
    yImgPersonajeTres = spritePersonajeTres.rect.bottom

    xImgPersonajeDos = spritePersonajeDos.rect.left
    yImgPersonajeDos = spritePersonajeDos.rect.bottom

    ###########
    while not termina:  # Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
        # Procesa los eventos que recibe
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:  # El usuario hizo click en el botón de salir
                termina = True      # Queremos terminar el ciclo
###########
            #Interaccion teclado jugadores
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:  #playerdos
                    spritePersonajeDos.rect.left -= 10
                    if movPer == DER:
                        break
                elif evento.key==pygame.K_RIGHT:  #playerdos
                    spritePersonajeDos.rect.left += 20
                    #movPerDos = DER
                    if movPer == DER:
                        break

                elif evento.key == pygame.K_a:  #playerUno
                    spritePersonaje.rect.left -= 20
                   # movPer = IZQ

                elif evento.key==pygame.K_d:  #playerUno
                    spritePersonaje.rect.left += 10
                   #movPer = DER

      #Hace que funciones los botones
            elif evento.type == pygame.MOUSEBUTTONUP:
                xm, ym = pygame.mouse.get_pos()
                #Preguntar si spltó el mouse dentro del botón
                xbJ = ANCHO //2-128
                ybJ= ALTO//3
                xbI = ANCHO /20
                ybI = ALTO /10
                xbR = ANCHO / 20
                ybR = ALTO // 2+150
                xbA = ANCHO-200
                ybA = ALTO//10

                if xm>=xbJ and xm<=xbJ+256 and ym>=ybJ and ym<=ybJ+100:
                    estado = JUGANDO
                if xm >= xbI and xm <= xbI + 132 and ym >= ybI and ym <= ybI + 33:
                    estado = INSTRUCCIONES
                if xm >= xbR and xm <= xbR + 80 and ym >= ybR and ym <= ybR + 33:
                    estado = MENU
                if xm >= xbA and xm <= xbA + 80 and ym >= ybA and ym <= ybA+ 33:
                    estado = ATRIBUCIONES







#############
        # Borrar pantalla
        ventana.fill(NARANJA)
        # Dibujar, aquí haces todos los trazos que requieras
#############

        if estado == JUGANDO:
           # #texto en la pantalla
            #texto = fuente.render("Equipo Verde: %d" % xf,1, ROJO)
            #ventana.blit(texto,(ANCHO//2-300,500))
            #TIEMPO
            if timer >=2:
               timer=0
            efectoTribuna.play() #Reproduce el efecto
            efectoCrowd.play()


           #Mover personajes
            if movPerDos ==IZQ:
                spritePersonajeDos.rect.left -= 1
            elif movPerDos == DER:
                spritePersonajeDos.rect.left += 1

            elif movPer ==IZQ:
                spritePersonaje.rect.left -= 1
            elif movPer == DER:
                spritePersonaje.rect.left += 1
            elif spritePersonajeTres.rect.left >= 600:
                puntosVerdes += 2
                spritePersonajeTres.rect.left = 380
                spritePersonaje.rect.left = 125
                spritePersonajeDos.rect.left = 620
            elif spritePersonajeTres.rect.left <= 170:
                puntosBlancos += 2
                spritePersonajeTres.rect.left = 380
                spritePersonaje.rect.left = 125
                spritePersonajeDos.rect.left = 620
            elif puntosBlancos ==14:
                estado = BLANCOS
                puntosVerdes = 0
                puntosBlancos = 0
            elif puntosVerdes == 14:
                estado = VERDES
                puntosVerdes = 0
                puntosBlancos = 0



            # Fondos
            ventana.blit(imgLadrillos,(xf,0))
            ventana.blit(imgCourt, (xf, 0))
            #Funciones
            dibujarPersonajeDos(ventana,spritePersonajeDos)
            dibujarPersonaje(ventana, spritePersonaje)
            dibujarPersonajeTres(ventana,spritePersonajeTres)
            hacerBalonDisparar(spritePersonaje, spritePersonajeDos, spritePersonajeTres)
            moverBalonPersonaje(spritePersonaje, spritePersonajeTres)
            moverBalonPersonajeDos(spritePersonajeDos,spritePersonajeTres)


        #Contadores de puntos
            texto = fuente.render("Verdes: %d" % puntosVerdes,1, VERDE)
            ventana.blit(texto,(200,50))

            texto = fuente.render("Blancos: %d" % puntosBlancos, 1, BLANCO)
            ventana.blit(texto, (500, 50))
            dibujarBotonMenu(ventana,imgBtnMenu)

        elif estado == INSTRUCCIONES:   #Ventana instrucciones
            efectoBounces.play()
            ventana.blit(imgLadrillos, (xf, 0))
            ventana.blit(instrucciones, (xf,0))
            dibujarBotonRegresar(ventana, imgBtnRegresar)

        elif estado == ATRIBUCIONES:  #Ventana atribuciones
            efectoBounces.play()
            ventana.blit(imgLadrillos, (xf, 0))
            ventana.blit(atribuciones, (xf, 0))
            dibujarBotonRegresar(ventana, imgBtnRegresar)

        elif estado == MENU:  #Ventana menu
            #Dibujar menú
            dibujarMenu(ventana, imgBtnJugar)
            dibujarInstrucciones(ventana, imgBtnInst)
            dibujarBotonAtribuciones(ventana,imgBtnAtribuciones)
            musicMenu.play()

        elif estado == VERDES:   #Ventana ganan verdes
            ventana.blit(imgLadrillos, (xf, 0))
            texto = fuente.render("¡Verdes Ganaron!", 2, VERDE)
            ventana.blit(texto, (200, 100))
            dibujarBotonMenu(ventana,imgBtnMenu)
            dibujarMenu(ventana, imgBtnJugar)

        elif estado == BLANCOS: #Ventana ganan blancos
            ventana.blit(imgLadrillos, (xf, 0))
            texto = fuente.render("¡Blancos Ganaron!", 2, BLANCO)
            ventana.blit(texto, (200, 100))
            dibujarBotonMenu(ventana, imgBtnMenu)
            dibujarMenu(ventana, imgBtnJugar)





##############
        pygame.display.flip()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
        reloj.tick(40)  # 40 fps

    # Después del ciclo principal
    pygame.quit()  # termina pygame


# Función principal, aquí resuelves el problema
def main():
    dibujar()   # Por ahora, solo dibuja


# Llamas a la función principal
main()
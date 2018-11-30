
# Autor: Oscar Macias Rodríguez, A01376398.
# Descripción: Juego en pygame llamado tanks \(°-°)/


import datetime
import pygame
import random
import time

pygame.init()


display_width = 800
display_height = 600

lista = []

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks')


white = (255, 255, 255)
black = (0, 0, 0)
red = (200, 0, 0)
light_red = (255, 0, 0)
yellow = (200, 200, 0)
light_yellow = (255, 255, 0)
green = (34, 177, 76)
light_green = (0, 255, 0)
blue = (0, 0, 150)
hot_pink = (100, 0, 0)


fondo = pygame.image.load('bgd.png')
gameOver = pygame.image.load('gameOverRetro.png')
controls = pygame.image.load('controlls.png')

background = pygame.image.load('tatooine.png')
duel = pygame.image.load('duel.png')
agniKai = pygame.image.load('Agni_Kai.jpg')

panic = pygame.image.load('PD.jpg')
warning = pygame.image.load('mars.jpg')
floyd = pygame.image.load('floyd.jpg')
viking = pygame.image.load('vikings.jpg')

clock = pygame.time.Clock()

tankWidth = 40

tankHeight = 20
turretWidth = 5
wheelWidth = 5
ground_height = 35

smallfont = pygame.font.SysFont("comicsansms", 25)
medfont = pygame.font.SysFont("comicsansms", 50)
largefont = pygame.font.SysFont("comicsansms", 85)

score_player1 = 0
score_player2 = 0

bulletSound = pygame.mixer.Sound('bullet1.wav')
hitSound = pygame.mixer.Sound('hit1.wav')


# Indica el tamaño del texto.
def text_objects(text, color, size="small"):
    if size == "small":
        textSurface = smallfont.render(text, True, color)
    if size == "medium":
        textSurface = medfont.render(text, True, color)
    if size == "large":
        textSurface = largefont.render(text, True, color)

    return textSurface, textSurface.get_rect()


# Imprime texto en los botnes asignados.
def text_to_button(msg, color, buttonx, buttony, buttonwidth, buttonheight, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = ((buttonx + (buttonwidth / 2)), buttony + (buttonheight / 2))
    gameDisplay.blit(textSurf, textRect)


# Imprime un mensaje en pantalla. El mensaje esta centrado!
def message_to_screen(msg, color, y_displace=0, size="small"):
    textSurf, textRect = text_objects(msg, color, size)
    textRect.center = (int(display_width / 2), int(display_height / 2) + y_displace)
    gameDisplay.blit(textSurf, textRect)


# Dibuja con pygame el tanque del jugador.
def tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x - 27, y - 2),
                        (x - 26, y - 5),
                        (x - 25, y - 8),
                        (x - 23, y - 12),
                        (x - 20, y - 14),
                        (x - 18, y - 15),
                        (x - 15, y - 17),
                        (x - 13, y - 19),
                        (x - 11, y - 21)
                        ]


    pygame.draw.circle(gameDisplay, white, (x, y), int(tankHeight / 2))
    pygame.draw.rect(gameDisplay, white, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, white, (x, y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, white, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x + 15, y + 20), wheelWidth)

    return possibleTurrets[turPos]


# Dibuja con pygame el tanque del enemigo.
def enemy_tank(x, y, turPos):
    x = int(x)
    y = int(y)

    possibleTurrets = [(x + 27, y - 2),
                   (x + 26, y - 5),
                   (x + 25, y - 8),
                   (x + 23, y - 12),
                   (x + 20, y - 14),
                   (x + 18, y - 15),
                   (x + 15, y - 17),
                   (x + 13, y - 19),
                   (x + 11, y - 21)
                   ]


    pygame.draw.circle(gameDisplay, white, (x, y), int(tankHeight // 2))
    pygame.draw.rect(gameDisplay, white, (x - tankHeight, y, tankWidth, tankHeight))

    pygame.draw.line(gameDisplay, white, (x, y), possibleTurrets[turPos], turretWidth)

    pygame.draw.circle(gameDisplay, white, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 15, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x - 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x + 5, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x + 10, y + 20), wheelWidth)
    pygame.draw.circle(gameDisplay, white, (x + 15, y + 20), wheelWidth)

    return possibleTurrets[turPos]


# Dibuja con pygame un corazón.
def heart(x, y):
    x = int(x)
    y = int(y)
    pygame.draw.circle(gameDisplay, red, (x-11, y), 12)
    pygame.draw.circle(gameDisplay, red, (x+11, y), 12)
    pygame.draw.line(gameDisplay, red, (x, y), (x, y + 30), 4)

    pygame.draw.line(gameDisplay, red, (x - 24, y), (x, y + 30), 2)
    pygame.draw.line(gameDisplay, red, (x + 22, y), (x, y + 30), 2)
    pygame.draw.line(gameDisplay, red, (x - 20, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x + 20, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x - 16, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x + 16, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x - 12, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x + 12, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x - 8, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x + 8, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x - 4, y), (x, y + 30), 4)
    pygame.draw.line(gameDisplay, red, (x + 4, y), (x, y + 30), 4)


# Menu donde se indican los controles que se utilizarán.
def game_controls():
    gcont = True

    while gcont:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()


        gameDisplay.blit(controls, (0, 0))


        button("play", 150, 500, 100, 50, green, light_green, action="play")
        button("Main", 350, 500, 100, 50, yellow, light_yellow, action="main")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")


        pygame.display.update()
        clock.tick(15)


# Función para imprimir acciones en los botones dibujados.
def button(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)
    pygame.draw.rect(gameDisplay, active_color, (x, y, width, height))
    text_to_button(text, black, x, y, width, height)
    if x + width > cur[0] > x and y + height > cur[1] > y:

        if click[0] == 1 and action != None:
            if action == "quit":
                pygame.quit()
                quit()

            if action == "controls":
                game_controls()

            if action == "rules":
                retry_VS()

            if action == "play":
                gameLoop()

            if action == "main":
                game_intro()

            if action == "versus":
                gameVersus()

            if action == "riot":
                gameRiot()

        else:
            pygame.draw.rect(gameDisplay, inactive_color, (x, y, width, height))


        text_to_button(text, black, x, y, width, height)


# Botón para música #1. Canción: High Hopes!
def button2(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)


    if x + width > cur[0] > x and y + height > cur[1] > y:
        if x == 700:
            gameDisplay.blit(panic, (x, y))

        if click[0] == 1 and action != None:

            if action == "origin" and x >= 700:
                pygame.mixer.music.stop()
                easterEgg()

            if action == "warning" and 660 <= x < 700:
                pygame.mixer.music.stop()
                secondEgg()

            if action == "floyd" and 600 <= x < 660:
                pygame.mixer.music.stop()
                thirdEgg()

        else:
            pass

        text_to_button(text, black, x, y, width, height)

# Botón para música #2. Canción: This is war!
def button3(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)


    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(warning, (x,y))

        if click[0] == 1 and action != None:

            if action == "warning" and y == 510:
                pygame.mixer.music.stop()
                secondEgg()

        else:
            pass

        text_to_button(text, black, x, y, width, height)


# Botón para música #3. Canción: Another Brick in the Wall!
def button4(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)


    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(floyd, (x, y))

        if click[0] == 1 and action != None:

            if action == "floyd" and y == 465:
                pygame.mixer.music.stop()
                thirdEgg()

        else:
            pass


        text_to_button(text, black, x, y, width, height)


# Botón para música #4. Canción: Main theme de la serie Vikingos!
def button5(text, x, y, width, height, inactive_color, active_color, action=None):
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    # print(click)

    if x + width > cur[0] > x and y + height > cur[1] > y:
        gameDisplay.blit(viking, (x, y))

        if click[0] == 1 and action != None:

            if action == "royal" and y == 425:
                pygame.mixer.music.stop()
                forthEgg()

        else:
            pass

        text_to_button(text, black, x, y, width, height)


# Descarga canción #1.
def easterEgg():
    pygame.mixer.music.load('High_Hopes.mp3')
    pygame.mixer.music.play(-1)


# Descarga canción #2.
def secondEgg():
    pygame.mixer.music.load('warning.mp3')
    pygame.mixer.music.play(-1)


#Descarga canción #3.
def thirdEgg():
    pygame.mixer.music.load('wall.mp3')
    pygame.mixer.music.play(-1)


# Descarga canción #4.
def forthEgg():
    pygame.mixer.music.load('vikings.mp3')
    pygame.mixer.music.play(-1)


# Menú de pausa.
def pause():
    paused = True
    message_to_screen("Paused", black, -70, size="large")
    message_to_screen("Press C to continue playing", red, 25)
    message_to_screen("Press Q to quit", red, 55)
    message_to_screen("Press M to go back to the main menu", red, 85)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_m:
                    global score_player1
                    global score_player2
                    score_player1 = 0
                    score_player2 = 0
                    game_intro()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        clock.tick(5)


# Menú de pausa pero con las letras blancas.
def pauseWhite():
    paused = True
    message_to_screen("Paused", white, -70, size="large")
    message_to_screen("Press C to continue playing", red, 25)
    message_to_screen("Press Q to quit", red, 55)
    message_to_screen("Press M to go back to the main menu", red, 85)
    pygame.display.update()
    while paused:
        for event in pygame.event.get():


            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    paused = False
                elif event.key == pygame.K_m:
                    global score_player1
                    global score_player2
                    score_player1 = 0
                    score_player2 = 0
                    game_intro()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()


        clock.tick(5)


# Dibujar barrera.
def barrier(xlocation,randomHeight, barrier_width):
   pygame.draw.rect(gameDisplay, black, [xlocation, display_height-randomHeight, barrier_width,randomHeight])


# Dibujar explosión de Debris.
def explosion(x, y, size=50):
    explode = True

    while explode:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        startPoint = x, y
        colorChoices = [red, light_red, yellow, light_yellow]
        magnitude = 1

        while magnitude < size:

            exploding_bit_x = x + random.randrange(-1 * magnitude, magnitude)
            exploding_bit_y = y + random.randrange(-1 * magnitude, magnitude)

            pygame.draw.circle(gameDisplay, colorChoices[random.randrange(0, 4)], (exploding_bit_x, exploding_bit_y), random.randrange(1, 5))
            magnitude += 1

            pygame.display.update()
            clock.tick(100)

        explode = False


# Función de colisión del proyectil con el tanque enemigo.
def fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY):
    fire = True
    damage = 0

    startingShell = list(xy)
    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        startingShell[0] -= (12 - turPos) * 2


        # y = x**2

        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if startingShell[1] > display_height - ground_height:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)


            if enemyTankX + 10 > hit_x > enemyTankX - 10:
                print("Critical Hit!")
                damage = 25
            elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                print("Hard Hit!")
                damage = 18
            elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                print("Medium Hit")
                damage = 10
            elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                print("Light Hit")
                damage = 5


            explosion(hit_x, hit_y)
            fire = False



        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)

    return damage


# Función de colisión del proyectil con el tanque del jugador.
def e_fireShell(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, ptankx, ptanky):
    damage = 0
    currentPower = 1
    power_found = False

    while not power_found:
        currentPower += 1
        if currentPower > 100:
            power_found = True
        # print(currentPower)

        fire = True
        startingShell = list(xy)

        while fire:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()

          # pygame.draw.circle(gameDisplay, red, (startingShell[0],startingShell[1]),5)



            startingShell[0] += (12 - turPos) * 2
            startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015 / (currentPower / 50)) ** 2) - (turPos + turPos / (12 - turPos)))



            if startingShell[1] > display_height - ground_height:
                hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
                hit_y = int(display_height - ground_height)
                # explosion(hit_x,hit_y)

                if ptankx + 15 > hit_x > ptankx - 15:
                    print("target acquired!")
                    power_found = True
                fire = False

            check_x_1 = startingShell[0] <= xlocation + barrier_width
            check_x_2 = startingShell[0] >= xlocation

            check_y_1 = startingShell[1] <= display_height
            check_y_2 = startingShell[1] >= display_height - randomHeight


            if check_x_1 and check_x_2 and check_y_1 and check_y_2:
                hit_x = int((startingShell[0]))
                hit_y = int(startingShell[1])
                #explosion(hit_x,hit_y)
                fire = False

    fire = True
    startingShell = list(xy)
    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        startingShell[0] += (12 - turPos) * 2

        gun_power = random.randrange(int(currentPower * 0.90), int(currentPower * 1.10))
        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if startingShell[1] > display_height - ground_height:
            print("last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)


            if ptankx + 10 > hit_x > ptankx - 10:
                print("Critical Hit!")
                damage = 25
            elif ptankx + 15 > hit_x > ptankx - 15:
                print("Hard Hit!")
                damage = 18
            elif ptankx + 25 > hit_x > ptankx - 25:
                print("Medium Hit")
                damage = 10
            elif ptankx + 35 > hit_x > ptankx - 35:
                print("Light Hit")
                damage = 5


            explosion(hit_x, hit_y)
            fire = False


        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight


        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False


        pygame.display.update()
        clock.tick(60)

    return damage


# Función colisión del tanque jugador 1. (Modo VS.)
def fireShell_player1(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY):
    fire = True
    damage = 0

    startingShell = list(xy)
    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        startingShell[0] -= (12 - turPos) * 2


        # y = x**2

        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if startingShell[1] > display_height - ground_height:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)


            if enemyTankX + 10 > hit_x > enemyTankX - 10:
                print("Critical Hit!")
                damage = 25
            elif enemyTankX + 15 > hit_x > enemyTankX - 15:
                print("Hard Hit!")
                damage = 18
            elif enemyTankX + 25 > hit_x > enemyTankX - 25:
                print("Medium Hit")
                damage = 10
            elif enemyTankX + 35 > hit_x > enemyTankX - 35:
                print("Light Hit")
                damage = 5


            explosion(hit_x, hit_y)
            fire = False



        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)

    return damage


# Función colisión del tanque jugador 2. (Modo VS.)
def fireShell_player2(xy, tankx, tanky, turPos, gun_power, xlocation, barrier_width, randomHeight, ptankX, enemyTankY):
    fire = True
    damage = 0

    startingShell = list(xy)
    print("FIRE!", xy)

    while fire:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # print(startingShell[0],startingShell[1])
        pygame.draw.circle(gameDisplay, red, (startingShell[0], startingShell[1]), 5)

        startingShell[0] += (12 - turPos) * 2


        # y = x**2

        startingShell[1] += int((((startingShell[0] - xy[0]) * 0.015 / (gun_power / 50)) ** 2) - (turPos + turPos / (12 - turPos)))

        if startingShell[1] > display_height - ground_height:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0] * display_height - ground_height) / startingShell[1])
            hit_y = int(display_height - ground_height)
            print("Impact:", hit_x, hit_y)


            if ptankX + 10 > hit_x > ptankX - 10:
                print("Critical Hit!")
                damage = 25
            elif ptankX + 15 > hit_x > ptankX - 15:
                print("Hard Hit!")
                damage = 18
            elif ptankX + 25 > hit_x > ptankX - 25:
                print("Medium Hit")
                damage = 10
            elif ptankX + 35 > hit_x > ptankX - 35:
                print("Light Hit")
                damage = 5


            explosion(hit_x, hit_y)
            fire = False



        check_x_1 = startingShell[0] <= xlocation + barrier_width
        check_x_2 = startingShell[0] >= xlocation

        check_y_1 = startingShell[1] <= display_height
        check_y_2 = startingShell[1] >= display_height - randomHeight

        if check_x_1 and check_x_2 and check_y_1 and check_y_2:
            print("Last shell:", startingShell[0], startingShell[1])
            hit_x = int((startingShell[0]))
            hit_y = int(startingShell[1])
            print("Impact:", hit_x, hit_y)
            explosion(hit_x, hit_y)
            fire = False

        pygame.display.update()
        clock.tick(60)

    return damage


# Indica el poder con el que sale disparado el proyectil del tanque #1.
def power(level):
    text = smallfont.render("Power: "+str(level)+"%",True, white)
    gameDisplay.blit(text, [700 - 55, 55])


# Indica el poder con el que sale disparado el proyectil del tanque #2.
def power_2(level):
    text = smallfont.render("Power: " + str(level) + "%", True, white)
    gameDisplay.blit(text, [60 - 55, 55])


# Imprime en pantalla el marcador.
def follow_score(points, points_2):
    text = medfont.render(str(points) + "-" + str(points_2),True, white)
    gameDisplay.blit(text, [display_width/2 - 55, 0])


# Música principal.
def war_music():
    pygame.mixer.music.load('war.mp3')
    pygame.mixer.music.play(1)


# Menú de inicio.
def game_intro():
    intro = True
    pygame.mixer.music.load('war.mp3')
    pygame.mixer.music.play(1)
    while intro:

        for event in pygame.event.get():
          # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                #quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                    pygame.mixer.music.stop()
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        gameDisplay.blit(fondo, (0, 0))

        time = datetime.datetime.now()
        start = time.time()
        text = smallfont.render("Time: " + str(start), True, black)
        gameDisplay.blit(text, [620, 0])


        entrada = open("Highscore.txt", "r")

        for linea in entrada:
            text = smallfont.render("Highscore: " + str(linea), True, black)
            gameDisplay.blit(text, [10, 0])


        button("play", 50, 350, 100, 50, green, light_green, action="play")
        button("controls", 50, 410, 100, 50, yellow, light_yellow, action="controls")
        button("quit", 50, 470, 100, 50, red, light_red, action="quit")
        button("StarWars", 350, 70, 110, 50, blue, hot_pink, action="versus")
        button("Agni Kai", 350, 130, 110, 50, red, white, action="riot")
        button("Controls", 350, 185, 110, 50, green, blue, action="rules")
        button2("", 700, 550, 100, 50, blue, yellow, action="origin")
        button3("", 720, 510, 100, 50, blue, yellow, action="warning")
        button4("", 710, 465, 100, 50, blue, yellow, action="floyd")
        button5("", 710, 425, 100, 50, blue, yellow, action="royal")

        entrada.close()
        pygame.display.update()
        clock.tick(15)


# Munú desplegado cuando pierdes en modo historia.
def game_over():
    game_over = True

    while game_over:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # gameDisplay.fill(white)
        gameDisplay.blit(gameOver, (0, 0))

        button("play Again", 150, 500, 150, 50, green, light_green, action="play")
        button("Main", 370, 500, 100, 50, yellow, light_yellow, action="main")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")


        pygame.display.update()
        clock.tick(15)


# Menú desplegado cuando se gana.
def you_win():
    win = True

    while win:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        message_to_screen("You won!", green, -100, size="large")
        message_to_screen("Congratulations!", black, -30)


        button("play Again", 150, 500, 150, 50, green, light_green, action="play")
        button("Main", 370, 500, 100, 50, yellow, light_yellow, action="controls")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")


        pygame.display.update()
        clock.tick(15)


# Menu de indicaciones para modo multijugador.
def retry_VS():
    win = True

    while win:
        for event in pygame.event.get():
            # print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(black)
        message_to_screen("Controls", green, -275, size="small")

        message_to_screen("Player 1: W,S = MOVE TURRETS", white, -225)
        message_to_screen("A,D = MOVE TANK", white, -200)
        message_to_screen("Z,X = ADD OR DECREASE POWER", white, -175)
        message_to_screen("E = SHOOT", white, -150)

        message_to_screen("Player 2: UP,DOWN ARROWS = MOVE TURRETS", white, -100)
        message_to_screen("LEFT,RIGHT ARROWS = MOVE TANK", white, -75)
        message_to_screen("N,M = ADD OR DECREASE POWER", white, -50)
        message_to_screen("SPACE BAR = SHOOT", white, -25)

        message_to_screen("Rules: TAKE TURNS TO SHOOT EACH OTHER", white, 25)
        message_to_screen("THE FIRST TANK TO LOWER THE ENEMY TANK ", white, 50)
        message_to_screen("HEALTH BAR TO ZERO WINS!", white, 75)
        message_to_screen("GOOD LUCK SARGENT, WE'RE COUNTING ON YOU!", white, 100)

        button("play SW", 150, 500, 150, 50, green, light_green, action="versus")
        button("play AK", 150, 440, 150, 50, green, light_green, action="riot")
        button("Main", 370, 500, 100, 50, yellow, light_yellow, action="controls")
        button("quit", 550, 500, 100, 50, red, light_red, action="quit")


        pygame.display.update()
        clock.tick(15)


# Imprime y actualiza las barras de vida del jugador.
def health_bars(player_health, enemy_health):
    if player_health > 75:
        player_health_color = green
    elif player_health > 50:
        player_health_color = yellow
    else:
        player_health_color = red


    if enemy_health > 75:
        enemy_health_color = green
    elif enemy_health > 50:
        enemy_health_color = yellow
    else:
       enemy_health_color = red


    pygame.draw.rect(gameDisplay, (150, 150, 150), (675, 20, 110, 35))
    pygame.draw.rect(gameDisplay, (150, 150, 150), (15, 20, 110, 35))

    pygame.draw.rect(gameDisplay, black, (680, 25, 100, 25))
    pygame.draw.rect(gameDisplay, black, (20, 25, 100, 25))

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health, 25))
    pygame.draw.rect(gameDisplay, enemy_health_color, (20, 25, enemy_health, 25))


# Imprime y actualiza las barras de vida de los jugadores. (Modo VS.)
def health_bars_VS(player_health_1, player_health_2):
    if player_health_1 > 75:
        player_health_color = green
    elif player_health_1 > 50:
        player_health_color = yellow
    else:
        player_health_color = red


    if player_health_2 > 75:
        player_health_color_2 = green
    elif player_health_2 > 50:
        player_health_color_2 = yellow
    else:
        player_health_color_2 = red


    pygame.draw.rect(gameDisplay, (150, 150, 150), (675, 20, 110, 35))
    pygame.draw.rect(gameDisplay, (150, 150, 150), (15, 20, 110, 35))

    pygame.draw.rect(gameDisplay, black, (680, 25, 100, 25))
    pygame.draw.rect(gameDisplay, black, (20, 25, 100, 25))

    pygame.draw.rect(gameDisplay, player_health_color, (680, 25, player_health_1, 25))
    pygame.draw.rect(gameDisplay, player_health_color_2, (20, 25, player_health_2, 25))


# Juego modo historia.
def gameLoop():
    gameExit = False
    gameOver = False
    FPS = 15

    player_health = 100
    enemy_health = 100

    barrier_width = 50

    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    enemyTankX = display_width * 0.1
    enemyTankY = display_height * 0.9

    fire_power = 100
    power_change = 0

    global score_player1
    global score_player2

    xlocation = (display_width / 2) + random.randint(-0.2 * display_width, 0.2 * display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.6)


    while not gameExit:

        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameLoop()
                        elif event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_SPACE:
                    bulletSound.play()
                    damage = fireShell(gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, barrier_width, randomHeight, enemyTankX, enemyTankY)
                    hitSound.play()
                    enemy_health -= damage
                    bulletSound.play()
                    damage = e_fireShell(enemy_gun, enemyTankX, enemyTankY, 8, 50, xlocation, barrier_width, randomHeight, mainTankX, mainTankY)
                    hitSound.play()
                    player_health -= damage


                elif event.key == pygame.K_a:
                    power_change = -1

                elif event.key == pygame.K_d:
                    power_change = 1


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0


        mainTankX += tankMove

        currentTurPos += changeTur

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0


        if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
            mainTankX += 5

        if player_health < 1:
            score_player2 += 1
            game_over()
        elif enemy_health < 1:
            score_player1 += 1
            you_win()
        clock.tick(FPS)

        # gameDisplay.fill(white)
        gameDisplay.blit(background, (0, 0))
        health_bars(player_health, enemy_health)
        gun = tank(mainTankX, mainTankY, currentTurPos)
        enemy_gun = enemy_tank(enemyTankX, enemyTankY, 8)
        fire_power += power_change

        power(fire_power)
        follow_score(score_player2, score_player1)

        salida = open("Highscore.txt", "w")
        salida.write("%s" % str(score_player1))
        salida.close()

        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(black, rect=[0, display_height - ground_height, display_width, ground_height])
        pygame.display.update()

    pygame.quit()
    quit()


# Juego modo multijugador.
def gameVersus():
    gameExit = False
    gameOver = False
    FPS = 15

    player_health_1 = 100
    player_health_2 = 100   # Player 2

    barrier_width = 50

    # Player 1
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    # Player 2
    mainTankX_2 = display_width * 0.1
    mainTankY_2 = display_height * 0.9
    tankMove_2 = 0
    currentTurPos_2 = 0
    changeTur_2 = 0

    # Player 1
    fire_power = 100
    power_change = 0

    # Player 2
    fire_power_2 = 100
    power_change_2 = 0

    # Scoreboard
    global score_player1
    global score_player2

    xlocation = (display_width / 2) + random.randint(-0.2 * display_width, 0.2 * display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.6)

    #time = datetime.datetime.now().time()
    start = time.time()


    while not gameExit:

        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameVersus()
                        elif event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pause()

                elif event.key == pygame.K_d:
                    tankMove_2 = 5

                elif event.key == pygame.K_a:
                    tankMove_2 = -5

                elif event.key == pygame.K_w:
                    changeTur_2 = 1

                elif event.key == pygame.K_s:
                    changeTur_2 = -1

                elif event.key == pygame.K_SPACE:
                    bulletSound.play()
                    damage = fireShell_player1(player1_gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, barrier_width, randomHeight, mainTankX_2, mainTankY_2)
                    hitSound.play()
                    player_health_2 -= damage


                elif event.key == pygame.K_e:
                    bulletSound.play()
                    damage = fireShell_player2(player2_gun, mainTankX_2, mainTankY_2, currentTurPos_2, fire_power_2, xlocation, barrier_width, randomHeight, mainTankX, mainTankY)
                    hitSound.play()
                    player_health_1 -= damage


                elif event.key == pygame.K_n:
                    power_change = -1

                elif event.key == pygame.K_m:
                    power_change = 1

                elif event.key == pygame.K_z:
                    power_change_2 = -1

                elif event.key == pygame.K_x:
                    power_change_2 = 1


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    tankMove_2 = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_w or event.key == pygame.K_s:
                    changeTur_2 = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0

                if event.key == pygame.K_z or event.key == pygame.K_x:
                    power_change_2 = 0



        mainTankX += tankMove
        mainTankX_2 += tankMove_2

        currentTurPos += changeTur
        currentTurPos_2 += changeTur_2

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if currentTurPos_2 > 8:
           currentTurPos_2 = 8
        elif currentTurPos_2 < 0:
           currentTurPos_2 = 0


        if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
            mainTankX += 5

        if mainTankX_2 + (tankWidth + 30) > xlocation + barrier_width:
           mainTankX_2 -= 5


        if player_health_1 < 1:
            score_player2 += 1
            gameVersus()
            #retry_VS()

        if player_health_2 < 1:
            score_player1 += 1
            gameVersus()
            #retry_VS()

        # gameDisplay.fill(white)
        gameDisplay.blit(duel, (0, 0))
        health_bars_VS(player_health_1, player_health_2)   # Health VS. Mode
        player1_gun = tank(mainTankX, mainTankY, currentTurPos)
        player2_gun = enemy_tank(mainTankX_2, mainTankY_2, currentTurPos_2)
        fire_power += power_change
        fire_power_2 += power_change_2

        power(fire_power)        # Power Player 1
        power_2(fire_power_2)    # Power Player 2
        follow_score(score_player2, score_player1)

        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(black, rect=[0, display_height - ground_height, display_width, ground_height])
        heart(160, 25)
        heart(640, 25)
        pygame.display.update()


        clock.tick(FPS)

    pygame.quit()
    quit()


# Juego modo Multijugador (Versión dos).
def gameRiot():
    gameExit = False
    gameOver = False
    FPS = 15

    player_health_1 = 100
    player_health_2 = 100   # Player 2

    barrier_width = 50

    # Player 1
    mainTankX = display_width * 0.9
    mainTankY = display_height * 0.9
    tankMove = 0
    currentTurPos = 0
    changeTur = 0

    # Player 2
    mainTankX_2 = display_width * 0.1
    mainTankY_2 = display_height * 0.9
    tankMove_2 = 0
    currentTurPos_2 = 0
    changeTur_2 = 0

    # Player 1
    fire_power = 100
    power_change = 0

    # Player 2
    fire_power_2 = 100
    power_change_2 = 0

    # Scoreboard
    global score_player1
    global score_player2

    xlocation = (display_width / 2) + random.randint(-0.2 * display_width, 0.2 * display_width)
    randomHeight = random.randrange(display_height * 0.1, display_height * 0.6)

    #time = datetime.datetime.now().time()
    start = time.time()


    while not gameExit:

        if gameOver == True:
            # gameDisplay.fill(white)
            message_to_screen("Game Over", red, -50, size="large")
            message_to_screen("Press C to play again or Q to exit", black, 50)
            pygame.display.update()
            while gameOver == True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False

                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_c:
                            gameRiot()
                        elif event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False



        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    tankMove = -5

                elif event.key == pygame.K_RIGHT:
                    tankMove = 5

                elif event.key == pygame.K_UP:
                    changeTur = 1

                elif event.key == pygame.K_DOWN:
                    changeTur = -1

                elif event.key == pygame.K_p:
                    pauseWhite()

                elif event.key == pygame.K_d:
                    tankMove_2 = 5

                elif event.key == pygame.K_a:
                    tankMove_2 = -5

                elif event.key == pygame.K_w:
                    changeTur_2 = 1

                elif event.key == pygame.K_s:
                    changeTur_2 = -1

                elif event.key == pygame.K_SPACE:
                    bulletSound.play()
                    damage = fireShell_player1(player1_gun, mainTankX, mainTankY, currentTurPos, fire_power, xlocation, barrier_width, randomHeight, mainTankX_2, mainTankY_2)
                    hitSound.play()
                    player_health_2 -= damage


                elif event.key == pygame.K_e:
                    bulletSound.play()
                    damage = fireShell_player2(player2_gun, mainTankX_2, mainTankY_2, currentTurPos_2, fire_power_2, xlocation, barrier_width, randomHeight, mainTankX, mainTankY)
                    hitSound.play()
                    player_health_1 -= damage


                elif event.key == pygame.K_n:
                    power_change = -1

                elif event.key == pygame.K_m:
                    power_change = 1

                elif event.key == pygame.K_z:
                    power_change_2 = -1

                elif event.key == pygame.K_x:
                    power_change_2 = 1


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    tankMove = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    tankMove_2 = 0

                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    changeTur = 0

                if event.key == pygame.K_w or event.key == pygame.K_s:
                    changeTur_2 = 0

                if event.key == pygame.K_a or event.key == pygame.K_d:
                    power_change = 0

                if event.key == pygame.K_z or event.key == pygame.K_x:
                    power_change_2 = 0



        mainTankX += tankMove
        mainTankX_2 += tankMove_2

        currentTurPos += changeTur
        currentTurPos_2 += changeTur_2

        if currentTurPos > 8:
            currentTurPos = 8
        elif currentTurPos < 0:
            currentTurPos = 0

        if currentTurPos_2 > 8:
           currentTurPos_2 = 8
        elif currentTurPos_2 < 0:
           currentTurPos_2 = 0


        if mainTankX - (tankWidth / 2) < xlocation + barrier_width:
            mainTankX += 5

        if mainTankX_2 + (tankWidth + 30) > xlocation + barrier_width:
            mainTankX_2 -= 5


        if player_health_1 < 1:
            score_player2 += 1
            gameRiot()
            #retry_VS()

        if player_health_2 < 1:
            score_player1 += 1
            gameRiot()
            #retry_VS()

        # gameDisplay.fill(white)
        gameDisplay.blit(agniKai, (0, 0))
        health_bars_VS(player_health_1, player_health_2)   # Health VS. Mode
        player1_gun = tank(mainTankX, mainTankY, currentTurPos)
        player2_gun = enemy_tank(mainTankX_2, mainTankY_2, currentTurPos_2)
        fire_power += power_change
        fire_power_2 += power_change_2

        power(fire_power)        # Power Player 1
        power_2(fire_power_2)    # Power Player 2
        follow_score(score_player2, score_player1)

        barrier(xlocation, randomHeight, barrier_width)
        gameDisplay.fill(black, rect=[0, display_height - ground_height, display_width, ground_height])
        heart(160, 25)
        heart(640, 25)
        pygame.display.update()


        clock.tick(FPS)

    pygame.quit()
    quit()


game_intro()
gameVersus()
gameRiot()
gameLoop()


#Diego Armando Ayala Hernández
#A01376727
#observación hubo un problema con mi compu y se traba cada vez que uso el pygame por lo que tuve que improvisar con turtle, nota personal: en lo personal no estoy orgulloso de esta aplicación (creo que si hubiera dedicado más tiempo lo hubiera mejorado
import turtle
import math
import random

#cACaracteristicas de la pantalla
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Proyecto Final")
wn.bgpic("fondo.png")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")

#dibuja los bordes
border= turtle.Turtle()
border.speed(0)
border.color("white")
border.penup()
border.setposition(-300,-300)
border.pendown()
border.pensize(3)
for side in range(4):
	border.fd(600)
	border.lt(90)
border.hideturtle()

#Pone el score en 0
score = 0

#dibuja el score
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.setposition(-290, 280)
scorestring = "Score: %s" %score
score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
score_pen.hideturtle()

#crea al jugador
player = turtle.Turtle()
player.color("blue")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

#Elije el numero de enemigos
number_of_enemies = 5
#crea una lista para los enemigos
enemies = []

#Agrega enemigos  la lista
for i in range(number_of_enemies):
	enemies.append(turtle.Turtle())

for enemy in enemies:
	enemy.color("red")
	enemy.shape("invader.gif")
	enemy.penup()
	enemy.speed(0)
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)
#velocidad de enemigos
enemyspeed = 2


#crea la bala o bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()
#velocidad de la bala, asi como un estado de la bala para que solo dispare una bala al mismo tiempo
bulletspeed = 20
bulletstate = "ready"


#Movimientos del jugador
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)

def fire_bullet():
	#se declara global por si se necesita cambiar
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		#ubica la bala un poco arriba de la cordenada del jugador
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()
#función de colisión
def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False
#teclas
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")


while True:

	for enemy in enemies:
		#movimiento de enemigos
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#movimiento del enemigo para los lados y para abajo
		if enemy.xcor() > 280:
			#Mueve a los enemigos para abajo
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		if enemy.xcor() < -280:
			for e in enemies:
				y = e.ycor()
				y -= 40
				e.sety(y)
			enemyspeed *= -1

		#verifica si hay colisión entre bala y enemigos
		if isCollision(bullet, enemy):
			#Reinicia la bala
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			#Reinicia al enemigo
			x = random.randint(-200, 200)
			y = random.randint(100, 250)
			enemy.setposition(x, y)
			#agrega la puntuación
			score += 10
			scorestring = "Score: %s" %score
			score_pen.clear()
			score_pen.write(scorestring, False, align="left", font=("Arial", 14, "normal"))
		#VERIFICA la colisión del jugador y el enemigo
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")

			print ("puntuación:",score)



	#Mueve la bala
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)

	#funcion que elimina la bala si revasa el limite
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"




# encoding: UTF-8
# Autor: Roberto Martínez Román
# Muestra cómo utilizar pygame en programas que dibujan en la pantalla

import pygame	# Librería de pygame
import _thread
import time
import random
import math

# Dimensiones de la pantalla
ANCHO = 720
ALTO = 384
# Colores
BLANCO = (255, 255, 255)  # R,G,B en el rango [0,255], 0 ausencia de color, 255 toda la intensidad
VERDE_BANDERA = (27, 94, 32)	# un poco de rojo, más de verde, un poco de azul
ROJO = (255, 0, 0)		# solo rojo, nada de verde, nada de azul
AZUL = (0, 0, 255)		# nada de rojo, ni verde, solo azul
BACKGROUND	= pygame.image.load('tanks_assets/bg.jpg')
MAXLVL = pygame.image.load('MaxLvl.png')
CLOUD = pygame.image.load('tanks_assets/cloud1.gif')
TANK = pygame.image.load('tanks_assets/tank.gif')
CANNON = pygame.image.load('tanks_assets/gun.gif')
AMMO = pygame.image.load('tanks_assets/shell.gif')
HIGHTLVLS = [[0,144,384-144],[144,288,384-240],[288,480,384-96],[480,720,384-192]]
MAXPOINTX = 216
MAXPOINTY = 240
GRAVEDAD = 9.81 #pixeles por segundo cuadzrado
VELOCIDAD = 85 #pixeles por segundo
VELOCIDADE = 85
CloudPos = []
AmmoPos = []
AmmoPosE = []
enemyPos = []
plyPosX = 0
plyPosY = 0
plyPosH = 0
Vida = 5
INDEXT = 0
Mode = 0
AHS=[]
Score = 0

def checkColl(x, y):
	cont = 0
	for tank in enemyPos:
		tankRect = pygame.Rect(tank[0], tank[1], 45,28)
		misil= pygame.Rect(x,y,5,5)
		if(tankRect.colliderect(misil)):
			
			return (True, cont)
		cont+=1
			
	return (False,None)

def checkCollE(x,y):
	if(x+1>plyPosX and x+1<plyPosX+45 and y+1 >plyPosY and y+1 < plyPosY+28):
		return True
	else:
		return False

def checkLimtX(x, posH):
	if(x<HIGHTLVLS[posH][0] or x+45>HIGHTLVLS[posH][1]):
		return False
	else:
		return True

def sacarRoots(a, b, c):
	d = (b**2) - (4*a*c)
	sol1 = (-b-cmath.sqrt(d))/(2*a)
	sol2 = (-b+cmath.sqrt(d))/(2*a)
	return (sol1,sol2)

def addfire(angle, x, y):
	
	startTime = time.time()
	AmmoPos.append([angle, x, y, startTime,x,y])

def checAmmoPos(x, y):
	for pos in HIGHTLVLS:
		if(pos[0]<x and pos[1]>x and pos[2]<y):
			return True
		
	return False

def checParabola(tiempoT, angle):
	return (tiempoT*VELOCIDADE*math.sin(math.radians(angle/10)))-(.5*GRAVEDAD*tiempoT*tiempoT)
	
def checkAltura(x,angle, maxHP):
	izqHX = HIGHTLVLS[maxHP][0]
	derHX = HIGHTLVLS[maxHP][1]
	altura = HIGHTLVLS[maxHP][2]
	distancia1 = abs(x-izqHX)
	distancia2 = abs(x-derHX)
	tiempoI = (distancia1/(VELOCIDADE*math.cos(math.radians(angle/10))))
	tiempoF = (distancia2/(VELOCIDADE*math.cos(math.radians(angle/10))))
	if( checParabola(tiempoI, angle)<=altura or checParabola(tiempoF, angle)<=altura):
		return False
	else:
		return True
	
def tankEnemigoMov(x, y, index, posh):	
	alive = True
	reloj = pygame.time.Clock()
	_thread.start_new_thread(tankEnemigoAtk, (x,y,index,posh))
	while(Mode!=1):
		time.sleep(1)
	while(alive and Mode==1):
		randomMov = random.randint(0,100)
		
		if(randomMov%49==0):
			if(checkLimtX(x-5,posh)):
				x -= 5
				enemyPos[index][0] -= 5
		elif(randomMov%49==1):
			if(checkLimtX(x+5, posh)):
				x += 5
				enemyPos[index][0] += 5
		if(not enemyPos[index][2]):
			alive=False
			enemyPos[index][3]=0
		reloj.tick(40)
	
def tankEnemigoAtk(x, y, index, posh):
	maxH = ALTO
	maxHP = 0
	alive = True
	reloj = pygame.time.Clock()
	for land in range(plyPosH+1,posh):
		if(maxH>HIGHTLVLS[land][2]):
			maxH = HIGHTLVLS[land][2]
			maxHP = land
	while(Mode!=1):
		time.sleep(1)
	while(alive and Mode==1):
		delay = random.randint(5,10)
		time.sleep(delay)
		if(not enemyPos[index][2]):
			enemyPos[index][4]=0
			alive=False
			break;
		x = enemyPos[index][0]
		diferenciaY = plyPosY - y
		distancia = abs(x-plyPosX-30)
		for angle in range(0,900,1):
			tiempoT = (distancia/(VELOCIDADE*math.cos(math.radians(angle/10))))
			parabola = checParabola(tiempoT, angle)
			if(parabola <= 7+diferenciaY and parabola >= -7+diferenciaY and checkAltura(x, angle, maxHP) ):
				AmmoPosE.append([math.radians(180-(angle/10)), x, y, time.time(), x, y])
				break;
		

def calcularPosAmmoE(args):
	reloj = pygame.time.Clock()
	while(Mode!=1):
		time.sleep(1)
	while True  and Mode==1:
		time
		currentTime = time.time()
		for ammo in AmmoPosE:
			
			timeE = (currentTime-ammo[3])
			timeE *=3
			
			posX = timeE*VELOCIDADE*math.cos(ammo[0])
			posY = (timeE*VELOCIDADE*math.sin(ammo[0]))-(.5*GRAVEDAD*timeE*timeE)
			ammo[1]=ammo[4]+posX
			ammo[2]=ammo[5]-posY
		reloj.tick(40)
		
def calcularPosAmmo(args):
	reloj = pygame.time.Clock()
	while(Mode!=1):
		time.sleep(1)
	while True and Mode==1:
		time
		currentTime = time.time()
		cont = 0
		for ammo in AmmoPos:
			
			timeE = (currentTime-ammo[3])
			timeE*=3
			posX = timeE*VELOCIDAD*math.cos(ammo[0])
			posY = (timeE*VELOCIDAD*math.sin(ammo[0]))-(.5*GRAVEDAD*timeE*timeE)
			ammo[1]=ammo[4]+posX
			ammo[2]=ammo[5]-posY
			cont +=1
		reloj.tick(40)
		
def SpawnClouds(args):
	while(Mode!=1):
		time.sleep(1)
	while True and Mode==1:
		y = random.randint(0,150)
		CloudPos.append([-200,y])
		delay = random.randint(10,15)
		time.sleep(delay)
		
def SpawnEnTanks(args):
	global INDEXT
	while(Mode!=1):
		time.sleep(1)
	while True and Mode==1:
		posh = 3
		x = random.randint(HIGHTLVLS[posh][0]+10, HIGHTLVLS[posh][1]-50)
		y = HIGHTLVLS[posh][2]
		enemyPos.append([x,y,True,1,1])
		_thread.start_new_thread(tankEnemigoMov, (x,y,INDEXT,posh))
		INDEXT+=1
		time.sleep(random.randint(10,20))

def DamageE(tank):
	global Score
	enemyPos[tank][2]= False
	Score+=1
	
	
def Damage():
	global Vida
	Vida = Vida -1
	if(Vida==0):
		gameOver()
	
def gameOver():
	global Mode
	AHS.append(Score)
	Mode = 2
	
def startup():
	global AmmoPos 
	global AmmoPosE
	global enemyPos
	global Vida 
	global INDEXT
	global Score 
	global plyPosX
	global plyPosY
	global plyPosH
	plyPosX = 50
	plyPosY = 212
	plyPosH = 0
	_thread.start_new_thread(SpawnClouds, ((),))
	_thread.start_new_thread(calcularPosAmmo, ((),))
	_thread.start_new_thread(calcularPosAmmoE, ((),))
	_thread.start_new_thread(SpawnEnTanks, ((),))
	CloudPos = []
	AmmoPos = []
	AmmoPosE = []
	enemyPos = []
	Vida = 5
	INDEXT = 0
	Score = 0
# Estructura básica de un programa que usa pygame para dibujar
def dibujar():
	# Inicializa el motor de pygame
	global plyPosX
	global plyPosY
	global plyPosH
	global Mode
	pygame.init()
	
	right = False
	left = False
	up = False
	down = False
	fire = False
	
	click = False
	mx = 0
	my = 0
	
	plyPosX = 50
	plyPosY = 212
	plyPosH = 0
	plyPointerTheta = 0
	contadorG = 0
	
	# Crea una ventana de ANCHO x ALTO
	ventana = pygame.display.set_mode((ANCHO, ALTO))  # Crea la ventana donde dibujará
	reloj = pygame.time.Clock()	 # Para limitar los fps
	termina = False	 
	empieza = False
	
	while not termina:
		if(contadorG!=0):
			contadorG-=1
		# Ciclo principal, MIENTRAS la variable termina sea False, el ciclo se repite automáticamente
		# Procesa los eventos que recibe
		for event in pygame.event.get():
			if event.type == pygame.QUIT:	# El usuario hizo click en el botón de salir
				termina = True				# Queremos terminar el ciclo\
				AHS.sort(key=int)
				cont = 0
				f = open("highscoreTG.txt","w")
				for scores in AHS:
					f.write(str(scores)+"\n")
				f.close()
					
			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_a:
					left = True
				if event.key == pygame.K_d:
					right = True
				if event.key == pygame.K_w:
					up = True
				if event.key == pygame.K_s:
					down = True
				if event.key == pygame.K_SPACE and contadorG==0:
					fire = True
					contadorG=40
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_a:
					left = False
				if event.key == pygame.K_d:
					right = False
				if event.key == pygame.K_w:
					up = False
				if event.key == pygame.K_s:
					down = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				click=True
				mx, my = pygame.mouse.get_pos()
					

		# Borrar pantalla
		ventana.fill(BLANCO)
		
		# Dibujar, aquí haces todos los trazos que requieras
		# Normalmente llamas a otra función y le pasas -ventana- como parámetro, por ejemplo, dibujarLineas(ventana)
		# Consulta https://www.pygame.org/docs/ref/draw.html para ver lo que puede hacer draw
		if(Mode ==1):
			if(not empieza):
				startup()
				empieza=True
			ventana.blit(BACKGROUND,(0,0))
			fonts = pygame.font.Font('freesansbold.ttf', 20)
			TextSurf, TextRect = text(str(Score), fonts,(0,0,0))
			TextRect.center = (10,10)
			ventana.blit(TextSurf, TextRect)
			
			for pos in CloudPos:
				if(pos[0]>=ANCHO):
					CloudPos.remove(pos)
					continue
				else:
					ventana.blit(CLOUD,pos)
					pos[0]+=1
			
			for ammo in AmmoPos:
				if(ammo[1]>720 or ammo[1]<0 or checAmmoPos(ammo[1],ammo[2])):
					AmmoPos.remove(ammo)
					continue
				col = checkColl(ammo[1],ammo[2])
				if(col[0]):
					AmmoPos.remove(ammo)
					DamageE(col[1])
					continue
					
				
				ventana.blit(AMMO, (ammo[1],ammo[2]))
			
			for ammo in AmmoPosE:
				if(ammo[1]>720 or ammo[1]<0 or checAmmoPos(ammo[1],ammo[2])):
					AmmoPosE.remove(ammo)
					continue
				col = checkCollE(ammo[1],ammo[2])
				if(col):
					AmmoPosE.remove(ammo)
					Damage()
					continue
				
				ventana.blit(AMMO, (ammo[1],ammo[2]))
			
			
			if(fire):
				fire = False
				addfire(plyPointerTheta, plyPosX+20, plyPosY+10)
			if(right and checkLimtX(plyPosX+1,plyPosH)):
				plyPosX +=1
			if(left and checkLimtX(plyPosX-1,plyPosH)):
				plyPosX -=1
			if(up and plyPointerTheta<math.pi*.5):
				plyPointerTheta+=.05
			if(down and plyPointerTheta>0):
				plyPointerTheta-=.05
			if(fire):
				_thread.start_new_thread(fire, (plyPointerTheta,plyPosX+20,plyPosY+10))
			
			ventana.blit(MAXLVL,(0,0))
			ventana.blit(CANNON,(plyPosX+20,plyPosY+5))
			ventana.blit(TANK,(plyPosX,plyPosY))
			pygame.draw.line(ventana, ROJO, [plyPosX+20,plyPosY+10],[plyPosX+20+(25*math.cos(plyPointerTheta)),plyPosY+10-(25*math.sin(plyPointerTheta))],2)
			counter = 0
			for tank in enemyPos:
				#print(tank)
				if(not tank[2]):					
					counter+=1
					continue
				counter+=1
				ventana.blit(CANNON,(tank[0]+20,tank[1]-23))
				ventana.blit(TANK, (tank[0],tank[1]-28))
		elif(Mode==0):
			empieza = False
			pygame.draw.rect(ventana, (0,0,0), (ANCHO/2-52, ALTO/2-27, 104,54))
			pygame.draw.rect(ventana, (0,0,0), (ANCHO/2-52, ALTO/2+48, 104,54))
			pygame.draw.rect(ventana, (0,0,0), (ANCHO/2-52, ALTO/2+123, 104,54))
			pygame.draw.rect(ventana, ROJO, (ANCHO/2-50, ALTO/2-25, 100,50))
			pygame.draw.rect(ventana, VERDE_BANDERA, (ANCHO/2-50, ALTO/2+50, 100,50))
			pygame.draw.rect(ventana, AZUL, (ANCHO/2-50, ALTO/2+125, 100,50))
			
			fonts = pygame.font.Font('freesansbold.ttf', 20)
			TextSurf, TextRect = text('Jugar', fonts, BLANCO)
			TextRect.center = ((ANCHO/2),(ALTO/2))
			ventana.blit(TextSurf, TextRect)
			fonts = pygame.font.Font('freesansbold.ttf', 20)
			TextSurf, TextRect = text('Highscore', fonts, BLANCO)
			TextRect.center = ((ANCHO/2),(ALTO/2+75))
			ventana.blit(TextSurf, TextRect)
			fonts = pygame.font.Font('freesansbold.ttf', 100)
			TextSurf, TextRect = text('El Juego', fonts,(0,0,0))
			TextRect.center = ((ANCHO/2),(ALTO/2-125))
			ventana.blit(TextSurf, TextRect)
			fonts = pygame.font.Font('freesansbold.ttf', 20)
			TextSurf, TextRect = text('Salir', fonts, BLANCO)
			TextRect.center = ((ANCHO/2),(ALTO/2+150))
			ventana.blit(TextSurf, TextRect)

			if(click):
				click=False
				if(mx>ANCHO/2-50 and my>ALTO/2-25 and 100+ANCHO/2-50>mx and 50+ALTO/2-25>my):
					Mode=1
				elif(mx>ANCHO/2-50 and my>ALTO/2+50 and 100+ANCHO/2-50>mx and 50+ALTO/2+50>my):
					Mode=3
				elif(mx>ANCHO/2-50 and my>ALTO/2+125 and 100+ANCHO/2-50>mx and 50+ALTO/2+125>my):
					termina = True				# Queremos terminar el ciclo\
					AHS.sort(key=int)
					cont = 0
					f = open("highscoreTG.txt","w")
					for scores in AHS:
						f.write(str(scores)+"\n")
					f.close()
				mx = 0
				my = 0
		elif(Mode==2):
			empieza = False
			ventana.fill((0,0,0))
			pygame.draw.rect(ventana, ROJO, (ANCHO/2-50, ALTO/2-25, 100,50))
			fonts = pygame.font.Font('freesansbold.ttf', 20)
			TextSurf, TextRect = text('Continuar', fonts,(0,0,0))
			TextRect.center = ((ANCHO/2),(ALTO/2))
			ventana.blit(TextSurf, TextRect)
			fonts = pygame.font.Font('freesansbold.ttf', 100)
			TextSurf, TextRect = text('Perdiste', fonts,BLANCO)
			TextRect.center = ((ANCHO/2),(ALTO/2-125))
			ventana.blit(TextSurf, TextRect)
			if(click):
				click=False
				if(mx>ANCHO/2-50 and my>ALTO/2-25 and 100+ANCHO/2-50>mx and 50+ALTO/2-25>my):
					Mode=0
				mx = 0
				my = 0
		elif(Mode ==3):
			empieza = False
			pygame.draw.rect(ventana, VERDE_BANDERA, (ANCHO/2-50, ALTO/2-100, 100,50))
			pygame.draw.rect(ventana, (128,128,128), (ANCHO/2-50, ALTO/2-15, 100,150))
			fonts = pygame.font.Font('freesansbold.ttf', 20)
			TextSurf, TextRect = text('Regresar', fonts,BLANCO)
			TextRect.center = ((ANCHO/2),(ALTO/2-75))
			ventana.blit(TextSurf, TextRect)
			cont = 0
			for score in AHS:
				TextSurf, TextRect = text(str(score), fonts,ROJO)
				TextRect.center = ((ANCHO/2),(ALTO/2)+cont*30)
				ventana.blit(TextSurf, TextRect)
				cont +=1
			if(click):
				click=False
				if(mx>ANCHO/2-50 and my>ALTO/2-100 and 100+ANCHO/2-50>mx and 50+ALTO/2-100>my):
					Mode=0
				mx = 0
				my = 0
				
		pygame.display.update()  # Actualiza trazos (Si no llamas a esta función, no se dibuja)
		reloj.tick(40)	# 40 fps

	# Después del ciclo principal
	pygame.quit()  # termina pygame

def text(text, font, color):
	textSurface = font.render(text, True, color)
	return textSurface, textSurface.get_rect()
	
def readHighscore():
	try:
		highsc = open("highscoreTG.txt", "r")
		if(highsc.mode=='r'):
			content = highsc.readlines()
			for score in content:
				score = score.replace("\n","")
				AHS.append(score)
		
	except:
		highsc = open("highscoreTG.txt", "w+")
		highsc.close()
	
	highsc.close()
# Función principal, aquí resuelves el problema
def main():
	readHighscore()
	dibujar()	# Por ahora, solo dibuja


# Llamas a la función principal
main()
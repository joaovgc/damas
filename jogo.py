# coding: utf-8
import pygame, sys

pygame.init()
screen =  pygame.display.set_mode((800,850))
pygame.display.set_caption('Jogo de Damas')
fonte = pygame.font.SysFont('None', 60)
fonte2 = pygame.font.SysFont('None', 80)  

menuImg = pygame.image.load('menu.png')
marrom = pygame.image.load('marrom.png')
vermelha = pygame.image.load('vermelha.png')
board = pygame.image.load('board.png')
verde = pygame.image.load('verde.png')
dama_m = pygame.image.load('dama_m.png')
dama_v = pygame.image.load('dama_v.png')

matrizBoard = []
for x in range(8):
	matrizBoard.append([])
for x in range(8):
	for y in range(8):
		matrizBoard[x].append(None)

def blit_text(text, cor, pos, fonte):
	render = fonte.render(text, True, cor)
	screen.blit(render, pos)

def getXY(): # Retorna as coordenadas(8x8) da casa clickada.  
	posX, posY = event.pos[0], event.pos[1]
	y, x = 0, 0
	
	for i in range(0, 801, 100): 
		if posX < i:
			break
		x += 1
	for i in range(0, 801, 100): 
		if posY < i:
			break
		y += 1
	x = x-1; y = y-1
	
	return x, y

def blitPieces(): 
	for i in range(8):
		for j in range(8):
			if matrizBoard[j][i] == 'v':
				screen.blit(vermelha, (i*100 + 20, j*100 + 18))
			elif matrizBoard[j][i] == 'm':
				screen.blit(marrom, (i*100 + 20, j*100 + 18))
			elif matrizBoard[j][i] == 'dm':
				screen.blit(dama_m, (i*100 + 20, j*100 + 18))
			elif matrizBoard[j][i] == 'dv':
				screen.blit(dama_v, (i*100 + 20, j*100 + 18))
				
def blitVerde(): # Blitar quadrado verde indicando possiveis jogadas.
	if len(possiveisJogadas) == 1:
		py = possiveisJogadas[0][0]; px = possiveisJogadas[0][1] 
		screen.blit(verde, (px*100, py*100))
	elif len(possiveisJogadas) == 2:
		py = possiveisJogadas[0][0]; px = possiveisJogadas[0][1]
		py2 = possiveisJogadas[1][0]; px2 = possiveisJogadas[1][1]
		screen.blit(verde, (px*100, py*100))
		screen.blit(verde, (px2*100, py2*100))
	
	if len(possiveisComidas) == 1:
		py = possiveisComidas[0][0]; px = possiveisComidas[0][1] 
		screen.blit(verde, (px*100, py*100))
	elif len(possiveisComidas) == 2:
		py = possiveisComidas[0][0]; px = possiveisComidas[0][1]
		py2 = possiveisComidas[1][0]; px2 = possiveisComidas[1][1]
		screen.blit(verde, (px*100, py*100))
		screen.blit(verde, (px2*100, py2*100))
		
def comerPraFrentePar(letra, ncomer):
	if x == 0:
		if ncomer:
			if matrizBoard[y-1][1] == None:
				possiveisJogadas.append((y-1,1))
		
		if y > 0 and matrizBoard[y-1][1] == letra:
			if y > 1 and matrizBoard[y-2][2] == None:
				comida.append((y-1,1))
				possiveisComidas.append((y-2,2))
			
	else:
		for px in range(x-1, x+2, 2):
			if ncomer:
				if y > 0 and matrizBoard[y-1][px] == None:
					possiveisJogadas.append((y-1,px))
			if y > 0 and matrizBoard[y-1][px] == letra:										
				if px < x:
					if y > 1 and px > 0 and matrizBoard[y-2][px-1] == None:
						comida.append((y-1,px))
						possiveisComidas.append((y-2,px-1))
				else:											
					if y > 1 and px < 7 and matrizBoard[y-2][px+1] == None:
						comida.append((y-1,px))
						possiveisComidas.append((y-2,px+1))

def comerPraTrasPar(letra, ncomer):
	if x == 0:
		if ncomer:
			if y < 7 and matrizBoard[y+1][1] == None:
				possiveisJogadas.append((y+1,1))
		if y < 7 and matrizBoard[y+1][1] == letra:
			if y < 6 and matrizBoard[y+2][2] == None:
				comida.append((y+1,1))
				possiveisComidas.append((y+2,2))
			
	else:
		for px in range(x-1, x+2, 2):
			if ncomer:
				if y < 7 and matrizBoard[y+1][px] == None:
					possiveisJogadas.append((y+1,px))
			if y < 7 and matrizBoard[y+1][px] == letra:
				if px < x:
					if (y < 6) and px > 0 and matrizBoard[y+2][px-1] == None: 
						comida.append((y+1,px))
						possiveisComidas.append((y+2,px-1))
				else:
					if y < 6 and px < 7 and matrizBoard[y+2][px+1] == None:
						comida.append((y+1,px))
						possiveisComidas.append((y+2,px+1))

def comerPraFrenteImpar(letra, ncomer):
	if x == 7:
		if ncomer:
			if y > 0 and matrizBoard[y-1][6] == None:
				possiveisJogadas.append((y-1,6))
		if y > 0 and matrizBoard[y-1][6] == letra:
			if y > 1 and matrizBoard[y-2][5] == None:
				comida.append((y-1,6))
				possiveisComidas.append((y-2,5))
	else:
		for px in range(x-1, x+2, 2):
			if ncomer:
				if y > 0 and matrizBoard[y-1][px] == None:
					possiveisJogadas.append((y-1,px))
			if matrizBoard[y-1][px] == letra:
				if px < x:
					if y > 1 and px > 0 and matrizBoard[y-2][px-1] == None:
						comida.append((y-1,px))
						possiveisComidas.append((y-2,px-1))
				else:											
					if y > 1 and px < 7 and matrizBoard[y-2][px+1] == None:
						comida.append((y-1,px))
						possiveisComidas.append((y-2,px+1))

def comerPraTrasImpar(letra, ncomer):
	if x == 7:
		if ncomer:
			if y < 7 and matrizBoard[y+1][6] == None:
				possiveisJogadas.append((y+1,6))
		if y < 7 and matrizBoard[y+1][6] == letra:
			if matrizBoard[y+2][5] == None:
				comida.append((y+1,6))
				possiveisComidas.append((y+2,5))
	else:
		
		for px in range(x-1, x+2, 2):
			if ncomer:
				if y < 7 and matrizBoard[y+1][px] == None:
					possiveisJogadas.append((y+1,px))
			
			if y < 7 and matrizBoard[y+1][px] == letra:
				if px < x:
					if  y < 6 and px > 0 and matrizBoard[y+2][px-1] == None:
						comida.append((y+1,px))
						possiveisComidas.append((y+2,px-1))
				else:
					if y < 6 and px < 7 and matrizBoard[y+2][px+1] == None:
						comida.append((y+1,px))
						possiveisComidas.append((y+2,px+1))
						
def getJogadas(possiveisJogadas, possiveisComidas, comida):
	if matrizBoard[y][x] == 'dm': 
		# Botar regras que controlam as damas.
		pass
	elif matrizBoard[y][x] == 'dv':
		pass
		
	elif matrizBoard[y][x] != None and matrizBoard[y][x] == turno:
		originalX = x; originalY = y;
		if y%2 == 0:
			if turno == 'm': # Marrom par
				comerPraFrentePar('v', True)
				comerPraTrasPar('v', False)
				
			elif turno == 'v': # Vermelho par
				comerPraTrasPar('m', True)
				comerPraFrentePar('m', False)
		
		elif y%2 != 0:
			if turno == 'm': # Marrom impar
				comerPraFrenteImpar('v', True)
				comerPraTrasImpar('v', False)			
			elif turno == 'v': # Vermelho impar
				comerPraTrasImpar('m', True)
				comerPraFrenteImpar('m', False)
					
		

# Colocar peças iniciais no tabuleiro:
for x in range(0,8,2):
	if x == 4:
		continue
	for y in range(0,8,2):
		if x < 4:
			matrizBoard[x][y] = 'v'
		else:
			matrizBoard[x][y] = 'm'
for x in range(1,8,2):
	if x == 3:
		continue
	for y in range(1,8,2):
		if x < 4:
			matrizBoard[x][y] = 'v'
		else:
			matrizBoard[x][y] = 'm'

menu = True
while menu: # Menu inicial
	
	screen.blit(menuImg, (0,0))
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit();
		
		if event.type == pygame.MOUSEBUTTONDOWN:
			
			x ,y = event.pos
			if (x in xrange(91, 725)) and (y in xrange(90, 175)):#1
				menu = False
				break
			
			elif (x in xrange(213, 574)) and (y in xrange(323, 389)):#2
				print 'Manual'
			
			elif (x in xrange(148, 630)) and (y in xrange(531, 605)):#3
				print 'Controles'
			
			elif (x in xrange(84, 720)) and (y in xrange(740, 820)):#4
				print 'Sobre o jogo'
				
	pygame.display.update()

selecionado = False # True se tiver selecionado uma peça.
turno = 'm' # 'm' = marrom // 'v' = vermelho

movimentosM = []
movimentosV = []

possiveisJogadas = []
possiveisComidas = []
comida = []

while True:
	if turno == 'm':
		text = 'Turno do marrom.'
		cor = (204,102,0)
		
	elif turno == 'v':
		text = 'Turno do vermelho.'
		cor = (204,0,0)
	
	screen.blit(board, (0,0)) # Blita o tabuleiro.
	pygame.draw.rect(screen, (205,191,172), (0,800,800,100))
	pygame.draw.rect(screen, (225,212,192), (0,800,800,100), 7) 
	blit_text(text, cor, (5,805), fonte) # Texto do turno
	blitPieces() # Blita as peças na tela.
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit();
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = getXY()
			
			if not selecionado:
				if matrizBoard[y][x] == 'dm': 
					# Botar regras que controlam as damas.
					pass
				elif matrizBoard[y][x] == 'dv':
					pass
					
				elif matrizBoard[y][x] != None and matrizBoard[y][x] == turno:
					possiveisJogadas = []
					possiveisComidas = []
					comida = []
					originalX = x; originalY = y;
					if y%2 == 0:
						if turno == 'm': # Marrom par
							comerPraFrentePar('v', True)
							comerPraTrasPar('v', False)
							
						elif turno == 'v': # Vermelho par
							comerPraTrasPar('m', True)
							comerPraFrentePar('m', False)
					
					elif y%2 != 0:
						if turno == 'm': # Marrom impar
							comerPraFrenteImpar('v', True)
							comerPraTrasImpar('v', False)			
						elif turno == 'v': # Vermelho impar
							comerPraTrasImpar('m', True)
							comerPraFrenteImpar('m', False)
									
					if len(possiveisComidas) != 0: # Se for possivel comer uma, elimina as outras possibilidades.
						possiveisJogadas = []
						matrizBoard[y][x] = None
						selecionado = True
					
					elif len(possiveisJogadas) != 0:
						matrizBoard[y][x] = None
						selecionado = True
					
			elif selecionado:
				
				if matrizBoard[y][x] == None:
					
					if x == originalX and y == originalY:
						matrizBoard[y][x] = turno
						selecionado = False
					
					else:
						passarTurno = False 
						for p in possiveisJogadas:
							if p[0] == y and p[1] == x:
								if (y%2 == 0 and x%2 == 0) or \
								(y%2 != 0 and x%2 !=0):
									matrizBoard[y][x] = turno
									selecionado = False
									passarTurno = True
							
						indexc = 0
						for p in possiveisComidas:
							
							if p[0] == y and p[1] == x:
								if (y%2 == 0 and x%2 == 0) or \
								(y%2 != 0 and x%2 !=0):
									matrizBoard[comida[indexc][0]][comida[indexc][1]] = None
									matrizBoard[y][x] = turno
									selecionado = False
									passarTurno = True
									
							indexc += 1
						
						if len(possiveisComidas) != 0:
							possiveisJogadas = []
							possiveisComidas = []
							comida = []
							getJogadas(possiveisJogadas, possiveisComidas, comida)
							if len(possiveisComidas) != 0:
								passarTurno = False							
							
						if passarTurno:
							if turno == 'm' or turno == 'dm':
								if y == 0:
									matrizBoard[y][x] = 'dm' 
								
								turno = 'v'
							elif turno == 'v' or turno == 'dv':
								if y == 7:
									matrizBoard[y][x] = 'dv'
									
								turno = 'm'
							
	if selecionado: # Peça seguindo ponteiro, rect verde para 
		
		screenX, screenY = pygame.mouse.get_pos()
		screenX -= 28; screenY -= 25;
		
		
		blitVerde() # Blitar quadrado verde indicando possiveis jogadas.
		
		if turno == 'v':
			screen.blit(vermelha, (screenX,screenY))
		else:
			screen.blit(marrom, (screenX,screenY))
		
	pygame.display.update()	
	

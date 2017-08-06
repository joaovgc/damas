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
			if (x in xrange(91, 725)) and (y in xrange(90, 175)):
				print 'b'
				menu = False
				break
			
	pygame.display.update()




selecionado = False # True se tiver selecionado uma peça.
turno = 'm' # 'm' = marrom // 'v' = vermelho

while True:
	if turno == 'm':
		text = 'Turno do jogador 1.'
		cor = (204,102,0)
	elif turno == 'v':
		text = 'Turno do jogador 2.'
		cor = (204,0,0)
	
	screen.blit(board, (0,0)) # Blita o tabuleiro.
	pygame.draw.rect(screen, (205,191,172), (0,800,800,100))
	pygame.draw.rect(screen, (225,212,192), (0,800,800,100), 7)
	blit_text(text, cor, (5,805), fonte)
	blitPieces() # Blita as peças na tela.
		
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit();
		
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = getXY()
			vX = x*100; vY = y*100;
			
			if not selecionado:
				if matrizBoard[y][x] != None and matrizBoard[y][x] == turno:
					
					matrizBoard[y][x] = None
					selecionado = True
			
			elif selecionado:
				if matrizBoard[y][x] == None:
					# Checar se a casa que foi clicada é marrom:
					if (y%2 == 0 and x%2 == 0) or (y%2 != 0 and x%2 !=0):
						matrizBoard[y][x] = turno
						selecionado = False
						
						# Passar o turno:						
						if turno == 'm':
							turno = 'v'
						elif turno == 'v':
							turno = 'm'
								
	if selecionado: #Fazer a peça selecionada seguir o ponteiro.
		x, y = pygame.mouse.get_pos()
		x -= 28; y -= 25;
		if turno == 'v':
			screen.blit(vermelha, (x,y))
		else:
			screen.blit(marrom, (x,y))
		
		
	
	
	
	
	pygame.display.update()	
	

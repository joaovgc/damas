# coding: utf-8
import pygame, sys

pygame.init()
screen =  pygame.display.set_mode((800,800))

marrom = pygame.image.load('marrom.png')
vermelha = pygame.image.load('vermelha.png')
board = pygame.image.load('board.png')

matrizBoard = []
for x in range(8):
	matrizBoard.append([])
for x in range(8):
	for y in range(8):
		matrizBoard[x].append('v')

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
			if matrizBoard[j][i] == 'b':
				screen.blit(vermelha, (i*100 + 20, j*100 + 18))
			elif matrizBoard[j][i] == 'p':
				screen.blit(marrom, (i*100 + 20, j*100 + 18))
		
# Colocar peças iniciais no tabuleiro:
for x in range(0,8,2):
	if x == 4:
		continue
	for y in range(0,8,2):
		if x < 4:
			matrizBoard[x][y] = 'b'
		else:
			matrizBoard[x][y] = 'p'
for x in range(1,8,2):
	if x == 3:
		continue
	for y in range(1,8,2):
		if x < 4:
			matrizBoard[x][y] = 'b'
		else:
			matrizBoard[x][y] = 'p'

selecionado = False # True se tiver selecionado uma peça.

while True:
	screen.blit(board, (0,0)) # Blita o tabuleiro.
	
	blitPieces() # Blita as peças na tela.
	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit(); sys.exit();
		elif event.type == pygame.MOUSEBUTTONDOWN:
			x, y = getXY()
			if not selecionado:
				if matrizBoard[y][x] != 'v':
					p = matrizBoard[y][x]
					matrizBoard[y][x] = 'v'
					selecionado = True
			
			elif selecionado:
				if matrizBoard[y][x] == 'v':
					# Checar se a casa que foi clicada é marrom:
					if (y%2 == 0 and x%2 == 0) or (y%2 != 0 and x%2 !=0):
						matrizBoard[y][x] = p
						selecionado = False
		
	if selecionado: #Fazer a peça selecionada seguir o ponteiro.
		x, y = pygame.mouse.get_pos()
		x -= 28; y -= 25;
		if p == 'b':
			screen.blit(vermelha, (x,y))
		else:
			screen.blit(marrom, (x,y))
				
	
	pygame.display.update()	
	

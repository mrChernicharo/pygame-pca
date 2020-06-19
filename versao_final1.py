import os
import pygame
import random
import time
 
pygame.init()

# Variáveis globais
BLACK = (  0,   0,   0)
WHITE = (255, 255, 155)
GRAY   = (100,  100,  100, 200)

rodada = 0
cronometro = 14
bonus = 4

qtd_mosquitos = 0
pontos = []
mosquito_arr = [] 

fps = 0
screen_X = 500
screen_Y = 400

# tamanho de tela e fontes
screen = pygame.display.set_mode((screen_X, screen_Y))
pygame.display.set_caption('Mosquito Killer')

fonte = pygame.font.SysFont('monospace', 20 )
fonte2 = pygame.font.SysFont('arial black', 40 )

# cursor
pygame.mouse.set_cursor(*pygame.cursors.broken_x)

# caixas de texto
textoRodada = fonte.render('Round | 1  ' , True, (255,255,255), (0,0,0))
pos_textoRodada = textoRodada.get_rect()
pos_textoRodada.center = (455, 20)

texto = fonte.render(f'Tempo | {cronometro} ' , True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (460, 40)

texto2 = fonte.render('Mosquitos | 0  ' , True, (255,255,255), (0,0,0))
pos_texto2 = texto2.get_rect()
pos_texto2.center = (447, 60)

game_over = fonte2.render('Game Over' , True, (255,255,255), (0,0,0))
pos_texto3 = game_over.get_rect()
pos_texto3.center = (250, 180)

pos_texto4 = game_over.get_rect()
pos_texto4.center = (250, 230)

pos_texto5 = game_over.get_rect()
pos_texto5.center = (250, 250)

# imagens assets/mosquitao5.png
mosquito_img_path = os.path.join('assets','mosquitao5.png')
mosquito_img = pygame.image.load(mosquito_img_path)
mosquito_img_invert = pygame.transform.flip(pygame.image.load(mosquito_img_path), True, False)

bg_img_path = os.path.join('assets','jungleBG3.jpg')
bg_img = pygame.image.load(bg_img_path)


# funções
def collision(click):
	# print(f'Click: {click}')

	for m in range(len(mosquito_arr)):
		#print(mosquito_arr[m][0], mosquito_arr[m][1])  

			if abs(click[0] - mosquito_arr[m][0]) < 18 and abs(click[1] - mosquito_arr[m][1]) < 16:  
				print('hit!')  
				pontos.append(1)
				mosquito_arr.pop(m)

				break




def criar_mosquitos(qtd_mosquitos):
	# Criação do array de mosquitos
	
	# Criando posições randomicas pra cada mosquito
	for j in range(qtd_mosquitos):
		x = random.randint(24, screen_X - 24)
		y = random.randint(24, screen_Y - 24)
		z = num = random.randint(0,1)
		mosquito_arr.append((x,y,z))
	

# loops
running = True
game = True
while running:
  
	# encerrar pygame
	for event in pygame.event.get(): 
		if cronometro < 0:   
			game = False
			pygame.quit()
		if event.type == pygame.QUIT: 
			pygame.time.delay(3000)
			running = False  

	while game:

		# registrar posição do cursor do mouse
		click = ''
		mouse_pos = pygame.mouse.get_pos() 

		# reação aos comandos do usuário
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				running = False
				game = False
				break
			
			elif event.type == pygame.MOUSEBUTTONDOWN:
				pygame.mouse.set_cursor(*pygame.cursors.diamond)
				click = (mouse_pos)
				collision(click)


			elif event.type == pygame.MOUSEBUTTONUP:
				pygame.mouse.set_cursor(*pygame.cursors.broken_x)


			click = pygame.mouse.get_pressed()

		# adaptação fps
		if fps < 40:  
			fps += 1 
		else:
  			# atualização do cronometro
			cronometro -= 1
			texto = fonte.render('Tempo | ' + str(cronometro) +' ', True, (255,255,255), (0,0,0))
			fps = 0

		# atualização de rodada e contagem de pontos (mosquitos)
		textoRodada = fonte.render('Rodada | ' + str(rodada) + ' ' , True, (255,255,255), (0,0,0))   
		texto2 = fonte.render('Mosquitos | ' + str(len(pontos)) + ' ' , True, (255,255,255), (0,0,0))  
		
		# impressões na tela
		screen.blit(bg_img,(0, 0)) 
		screen.blit(texto, pos_texto)
		screen.blit(texto2, pos_texto2) 
		screen.blit(textoRodada, pos_textoRodada) 

		
		#printando circulos na tela conforme x,y de cada mosquito
		for i in range(len(mosquito_arr)): 
			pygame.draw.circle(screen, (GRAY), (mosquito_arr[i][0], mosquito_arr[i][1]), 20)
			
			# esquerda ou direita?
			if mosquito_arr[i][2] != 0:
				screen.blit(mosquito_img_invert, (mosquito_arr[i][0] - 47 , mosquito_arr[i][1] -18)) 
			else:  
				screen.blit(mosquito_img, (mosquito_arr[i][0] - 47 , mosquito_arr[i][1] -18))

		# regras da partida	
		if len(mosquito_arr) == 0:
			if rodada <= 7:
				qtd_mosquitos += 1
			criar_mosquitos(qtd_mosquitos)
			print(mosquito_arr)    
			rodada += 1
			cronometro += bonus
		
		# game over 
		if cronometro < 0:
			screen.fill(BLACK)
			screen.blit(game_over, pos_texto3)    
			screen.blit(textoRodada, pos_texto4) 
			screen.blit(texto2, pos_texto5) 

		
		pygame.display.update()
	


pygame.quit()

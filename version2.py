import os
import pygame
import random
import time
 

# Define some colors
BLACK = (  0,   0,   0)
WHITE = (255, 255, 155)
RED   = (100,  100,  100, 200)

pygame.init()

pontos = 0
tempo_segundo = 19
timer = 0
rodada = 0

screen_X = 500
screen_Y = 400
screen = pygame.display.set_mode((screen_X, screen_Y))
pygame.display.set_caption('Novo Jogo')

fonte = pygame.font.SysFont('arial black', 20 )
fonte2 = pygame.font.SysFont('arial black', 40 )

textoRodada = fonte.render('Round | 1  ' , True, (255,255,255), (0,0,0))
pos_textoRodada = textoRodada.get_rect()
pos_textoRodada.center = (71, 20)

texto = fonte.render(f'Tempo | {tempo_segundo} ' , True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (78, 50)

texto2 = fonte.render('Mosquitos | 0  ' , True, (255,255,255), (0,0,0))
pos_texto2 = texto2.get_rect()
pos_texto2.center = (65, 80)

game_over = fonte2.render('Game Over' , True, (255,255,255), (0,0,0))
pos_texto3 = game_over.get_rect()
pos_texto3.center = (250, 200)

mosquito_img_path = os.path.join('assets','mosquitao.png')
mosquito_img = pygame.image.load(mosquito_img_path)

bg_img_path = os.path.join('assets','jungleBG3.jpg')
bg_img = pygame.image.load(bg_img_path)
#game_over, pos_texto3
clock = pygame.time.Clock()

def collision(click):
  print(mosquito_arr)    
  print(f'Click: {click}')

  for m in range(len(mosquito_arr)):
    print(mosquito_arr[m][0], mosquito_arr[m][1])  

    if abs(click[0] - mosquito_arr[m][0]) < 14 and abs(click[1] - mosquito_arr[m][1]) < 13:
      print(pontos)
      print('hit!')   
      mosquito_arr.pop(m)
      break


running = True
game = True

qtd_mosquitos = 0


mosquito_arr = [] 
def criar_mosquitos(qtd_mosquitos):
# Criação do array de mosquitos
  
   
# Criando posições randomicas pra cada mosquito
  for j in range(qtd_mosquitos):
    x = random.randint(0, screen_X)
    y = random.randint(0, screen_Y)
    mosquito_arr.append((x,y))
 

 
# game loop
while running:


  for event in pygame.event.get(): 
    if tempo_segundo <= 0:   
      pygame.time.delay(3000)
      pygame.quit()
    if event.type == pygame.QUIT: 
      running = False  

  while game:

    # game
    click = ''
    mouse_pos = pygame.mouse.get_pos() 

    for event in pygame.event.get(): 
      if event.type == pygame.QUIT: 
        running = False
        game = False
        break
        
      elif event.type == pygame.MOUSEBUTTONDOWN:
        click = (mouse_pos)
        collision(click)
        pontos += 1

    click = pygame.mouse.get_pressed()


    if timer < 50:  
      timer += 1 
    else:
      tempo_segundo -= 1
      texto = fonte.render('Tempo | ' + str(tempo_segundo) +' ', True, (255,255,255), (0,0,0))
      timer = 0



    textoRodada = fonte.render('Rodada | ' + str(rodada) + ' ' , True, (255,255,255), (0,0,0))   
    texto2 = fonte.render('Mosquitos | ' + str(pontos) + ' ' , True, (255,255,255), (0,0,0))  
    
    screen.blit(bg_img,(0, 0)) 
    screen.blit(texto, pos_texto)
    screen.blit(texto2, pos_texto2) 
    screen.blit(textoRodada, pos_textoRodada) 

    
    #printando mosquitos na tela 
    i = 0
    for i in range(len(mosquito_arr)): 
      #pygame.draw.circle(screen, (RED), mosquito_arr[i], 20)
      screen.blit(mosquito_img, (mosquito_arr[i][0] - 50, mosquito_arr[i][1] - 50))
      
    if len(mosquito_arr) == 0:
      qtd_mosquitos += 1
      criar_mosquitos(qtd_mosquitos)
      rodada += 1
      tempo_segundo +=2

    if tempo_segundo <= 0:
      screen.fill(BLACK)
      screen.blit(game_over, pos_texto3)    


    
    pygame.display.update()
    


pygame.quit()


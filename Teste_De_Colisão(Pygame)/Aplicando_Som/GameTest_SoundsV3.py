import pygame
from pygame.locals import *
from sys import exit
from random import randint

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('Musica_De_Fundo.mp3')
pygame.mixer.music.play(-1)

barulho_colisão = pygame.mixer.Sound('smw_power-up_appears.wav')
barulho_colisão.set_volume(0.1)
largura = 640   
altura = 480
x = int(largura/2) #Luga aonde fica o retangulo altura x largura.
y = int(altura/2)

x_azul = randint(40, 600) #Representando a posição do retangulo azul:
y_azul = randint(50, 430) #Dentro da função Randint, ocorre um intervalo de números, de escolha aleatória

 
pontos = 0 #Variavél pontos
fonte = pygame.font.SysFont('arial', 40, True, True) #Inserindo Texto


tela = pygame.display.set_mode((largura, altura)) #Criando o objeto tela, e definindo largura x altura
pygame.display.set_caption('Primeiro game')
relogio = pygame.time.Clock()

while True: #Criando o loop infinito.
    relogio.tick(30) #Controla o framerate
    tela.fill((0,0,0))
    mensagem = f'Pontos: {pontos}' #Mensagem que vai aparecer na fonte
    texto_formatado = fonte.render(mensagem, True, (255,255,255))
    for event in pygame.event.get():    #A cada interação do looping principal, checar qual evento ocorreu. (exemplo o looling tem que indentificar qual tecla apertou.)
        if event.type == QUIT: #Função para fehcar a janela do jogo.
            pygame.quit()
            exit()
        """
        if event.type == KEYDOWN: # Controle pelo teclado
            if event.key == K_a:
                x = x - 20
                
            if event.key == K_d:
                x = x + 20
                
            if event.key == K_w:
                y = y - 20
                
            if event.key == K_s:
                y = y + 20
        """
    if pygame.key.get_pressed()[K_a]: #Controle pelo teclado(Pressão das teclas)
        x = x - 20
    
    if pygame.key.get_pressed()[K_d]:
        x = x + 20
        
    if pygame.key.get_pressed()[K_w]:
         y = y - 20
                
    if pygame.key.get_pressed()[K_s]:
          y = y + 20
                
    ret_vermelho = pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) #Desenhando o retângulo. Primeiro parâmetro saõ as cores, o segundo é x e y, e por último , o raio do objeto
    ret_azul = pygame.draw.rect(tela, (0,0,255), (x_azul,y_azul,40,50)) #Desenhando o retângulo Azul

    if ret_vermelho.colliderect(ret_azul): #Criando uma condição de colisão
        x_azul = randint(40, 600) # Toda vez que o retângulo vermelho, colidir com o retângulo azul, a variavél x e y azul, vão assumir diferentes valores, o pisição do retângulo azul, vai mudar toda vez que isso acontecer.
        y_azul = randint(50, 430)
        pontos = pontos +1 #Toda vez que houver uma colisão a variavél pontos vai receber +1
        barulho_colisão.play()
    tela.blit(texto_formatado, (450, 40)) #Posição do texto em tela
    pygame.display.update() #A cada interação do looping principal do jogo, ela atualiza a tela do jogo
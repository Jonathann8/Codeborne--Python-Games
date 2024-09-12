import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura = 640   
altura = 480

tela = pygame.display.set_mode((largura, altura)) #Criando o objeto tela, e definindo largura x altura
pygame.display.set_caption('Primeiro game')

while True: #Criando o loop infinito.
    for event in pygame.event.get():    #A cada interação do looping principal, checar qual evento ocorreu. (exemplo o looling tem que indentificar qual tecla apertou.)
        if event.type == QUIT: #Função para fehcar a janela do jogo.
            pygame.quit()
            exit()
    pygame.draw.rect(tela, (255,0,0), (200,300,40,50)) #Desenhando o retângulo.
    pygame.draw.circle(tela, (0,0,255),(300,260), 40) #Primeiro parâmetro saõ as cores, o segundo é x e y, e por último , o raio do objeto
    pygame.draw.line(tela, (255,255,0), (390,0), (390,600), 5) #linha
    
    pygame.display.update() #A cada interação do looping principal do jogo, ela atualiza a tela do jogo
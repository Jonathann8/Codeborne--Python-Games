import pygame
from pygame.locals import *
from sys import exit

pygame.init()


largura = 640   
altura = 480
x = largura/2
y = 0

tela = pygame.display.set_mode((largura, altura)) #Criando o objeto tela, e definindo largura x altura
pygame.display.set_caption('Primeiro game')
relogio = pygame.time.Clock()

while True: #Criando o loop infinito.
    relogio.tick(30) #Controla o framerate
    tela.fill((0,0,0))
    for event in pygame.event.get():    #A cada interação do looping principal, checar qual evento ocorreu. (exemplo o looling tem que indentificar qual tecla apertou.)
        if event.type == QUIT: #Função para fehcar a janela do jogo.
            pygame.quit()
            exit()
            
    pygame.draw.rect(tela, (255,0,0), (x,y,40,50)) #Desenhando o retângulo. Primeiro parâmetro saõ as cores, o segundo é x e y, e por último , o raio do objeto
    if y >= altura: 
        y = 0
    y = y + 5
    
    
    pygame.display.update() #A cada interação do looping principal do jogo, ela atualiza a tela do jogo
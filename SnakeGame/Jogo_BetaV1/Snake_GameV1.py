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
x_cobra = int(largura / 2)
y_cobra = int(altura / 2)

x_maca = randint(40, 600)
y_maca = randint(50, 430)

pontos = 0
fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Primeiro game')
relogio = pygame.time.Clock()
lista_cobra = []

def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0, 255, 0), (XeY[0], XeY[1], 20, 20))
    

while True:
    relogio.tick(30)
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    if pygame.key.get_pressed()[K_a]:
        x_cobra -= 20
    
    if pygame.key.get_pressed()[K_d]:
        x_cobra +=  20
        
    if pygame.key.get_pressed()[K_w]:
        y_cobra -= 20
                
    if pygame.key.get_pressed()[K_s]:
        y_cobra += 20
                
    cobra = pygame.draw.rect(tela, (0, 255, 0), (x_cobra, y_cobra, 20, 20))
    maca = pygame.draw.rect(tela, (255, 0, 0), (x_maca, y_maca, 20, 20))

    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos += 1
        barulho_colisão.play()
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)

    lista_cobra.append(lista_cabeca)
    
    aumenta_cobra(lista_cobra)
    
    tela.blit(texto_formatado, (450, 40))
    pygame.display.update()

import pygame
from pygame.locals import *
from sys import exit
from random import randint
import math

pygame.init()

pygame.mixer.music.set_volume(0.1)
musica_de_fundo = pygame.mixer.music.load('Musica_De_Fundo.mp3')
pygame.mixer.music.play(-1)

barulho_colisão = pygame.mixer.Sound('smw_power-up_appears.wav')
barulho_colisão.set_volume(0.1)
largura = 640   
altura = 480
x = int(largura / 2)  # Posição inicial do quadrado vermelho
y = int(altura / 2)

# Posição inicial do quadrado azul
x_azul = randint(40, 600)
y_azul = randint(50, 430)

pontos = 0  # Variável pontos
fonte = pygame.font.SysFont('arial', 40, True, True)  # Fonte

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Pique-Pega')
relogio = pygame.time.Clock()

# Função para mover o quadrado azul, tentando fugir do vermelho
def mover_quadrado_azul():
    global x_azul, y_azul
    
    # Calcular a diferença de posição
    dx = x - x_azul
    dy = y - y_azul
    
    # Calcular a distância
    distancia = math.sqrt(dx**2 + dy**2)
    
    # Normalizar a direção
    if distancia != 0:
        dx /= distancia
        dy /= distancia
    
    # Mover o quadrado azul na direção oposta
    x_azul += -dx * 5  # Multiplique pela velocidade desejada
    y_azul += -dy * 5
    
    # Garantir que o quadrado azul não saia da tela
    x_azul = max(0, min(largura - 40, x_azul))
    y_azul = max(0, min(altura - 50, y_azul))

while True:
    relogio.tick(30)  # Controla o framerate
    tela.fill((0, 0, 0))
    mensagem = f'Pontos: {pontos}'  # Mensagem que vai aparecer
    texto_formatado = fonte.render(mensagem, True, (255, 255, 255))

    for event in pygame.event.get():
        if event.type == QUIT:  # Fechar a janela do jogo
            pygame.quit()
            exit()

    # Controle do quadrado vermelho
    if pygame.key.get_pressed()[K_a]:
        x -= 20
    if pygame.key.get_pressed()[K_d]:
        x += 20
    if pygame.key.get_pressed()[K_w]:
        y -= 20
    if pygame.key.get_pressed()[K_s]:
        y += 20

    ret_vermelho = pygame.draw.rect(tela, (255, 0, 0), (x, y, 40, 50))  # Quadrado vermelho
    mover_quadrado_azul()  # Mover quadrado azul
    ret_azul = pygame.draw.rect(tela, (0, 0, 255), (x_azul, y_azul, 40, 50))  # Quadrado azul

    if ret_vermelho.colliderect(ret_azul):  # Colisão
        x_azul = randint(40, 600)
        y_azul = randint(50, 430)
        pontos += 1  # Aumentar pontos
        barulho_colisão.play()

    tela.blit(texto_formatado, (450, 40))  # Posição do texto na tela
    pygame.display.update()  # Atualizar a tela

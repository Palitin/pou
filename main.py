# Ö pou 2
import pygame
from time import sleep

pygame.init()
tela = pygame.display.set_mode((500, 700))

pygame.display.set_caption("POU 2")
icone = pygame.image.load("pou-icone.png")
pygame.display.set_icon(icone)

while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            exit()
    tela.fill((0,255,0))
    pygame.display.update()
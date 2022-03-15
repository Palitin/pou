import pygame

# cores
branco = (255, 255, 255)
pele = (221, 164, 84)
preto = (24, 17, 9)
rosa = (225, 115, 88)
branco = (245, 235, 222)

#fontes
fonteG = pygame.font.Font("mtf-toast.ttf",80)

def objeto_texto(texto, fonte):
    textoSur = fonte.render(texto , True, branco)
    return textoSur, textoSur.get_rect()


def mostrar_texto(texto, fonte):
    textoSuper, textoRet = objeto_texto(texto, fonte)
    textoRet.centro = (())

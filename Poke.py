import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

pasta_principal = os.path.dirname(__file__)
pasta_img = os.path.join(pasta_principal,'IMAGENS')
pasta_sons = os.path.join(pasta_principal,'SONS')

imagem_fundo = pygame.image.load('IMAGENS\BACKGROUND.jpg')

pygame.init()
pygame.mixer.init()

largura = 748
altura = 421

tela = pygame.display.set_mode((largura,altura))

pygame.display.set_caption('Pokecin')

sprite_sheet = pygame.image.load(os.path.join(pasta_img,'correr.png')).convert_alpha()


class Pikachu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_pikachu = []
        for i in range (4):
                    img = sprite_sheet.subsurface((i*56,0),(56,30))
                    img = pygame.transform.scale(img,(56*3,30*3))
                    self.imagens_pikachu.append(img)

        self.index_lista = 0
        self.image = self.imagens_pikachu[self.index_lista]
        self.rect = self.image.get_rect()
        self.posy_inicial = altura-64 
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (100,altura-64)
        self.corre = False

    def correr(self):
         self.corre = True

    def update (self):
        if self.index_lista > 2:
              self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_pikachu[int(self.index_lista)]    



todas_sprites = pygame.sprite.Group()
pika = Pikachu()
todas_sprites.add(pika)


relogio = pygame.time.Clock()
while True:
    relogio.tick(30)
    tela.blit(imagem_fundo,(0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()
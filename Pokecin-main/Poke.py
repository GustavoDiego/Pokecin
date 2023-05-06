import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

pasta_principal = os.path.dirname(__file__)
pasta_img = os.path.join(pasta_principal,'IMAGENS')
pasta_sons = os.path.join(pasta_principal,'SONS')

pygame.init()
pygame.mixer.init()

largura = 748
altura = 421

tela = pygame.display.set_mode((largura,altura))
pygame.display.init()
imagem_fundo = pygame.image.load(os.path.join(pasta_img, 'BACKGROUND.jpg')).convert()
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
        self.direcao = 1

    def correr(self):
         self.corre = True

    def update (self):
        if self.index_lista > 2:
              self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_pikachu[int(self.index_lista)]    
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > largura:
            self.rect.right = largura
        
        keys = pygame.key.get_pressed()
        if keys[K_RIGHT]:
            self.direcao = 1
        elif keys[K_LEFT]:
            self.direcao = -1

        if self.direcao == -1:
            self.image = pygame.transform.flip(self.image, True, False)

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

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        pika.rect.x += 6
    if keys[pygame.K_LEFT]:
        pika.rect.x -= 6

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()
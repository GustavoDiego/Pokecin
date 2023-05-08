import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
from spritespoke import *
from constantes import *


pasta_principal = os.path.dirname(__file__)
pasta_img = os.path.join(pasta_principal,'IMAGENS')
pasta_sons = os.path.join(pasta_principal,'SONS')


tela = pygame.display.set_mode((LARGURA, ALTURA))

pygame.init()


sprite_sheet = pygame.image.load(os.path.join(pasta_img,'correr.png')).convert_alpha()
icone_heart = pygame.image.load(os.path.join(pasta_img, 'heart.png')).convert_alpha()
icone_flash = pygame.image.load(os.path.join(pasta_img, "flash.png")).convert_alpha()
icone_star = pygame.image.load(os.path.join(pasta_img, "star.png")).convert_alpha()
icone_pokeball = pygame.image.load(os.path.join(pasta_img, "pokeball.png")).convert_alpha()
icone_teclas = pygame.image.load(os.path.join(pasta_img, "Teclas.png")).convert_alpha()
aud_star = pygame.mixer.Sound(os.path.join(pasta_sons, 'estrela.wav'))
aud_flash = pygame.mixer.Sound(os.path.join(pasta_sons, 'raio.wav'))
aud_pokeball = pygame.mixer.Sound(os.path.join(pasta_sons, 'pokeball.wav'))
aud_gameover = pygame.mixer.Sound(os.path.join(pasta_sons, 'gameover.wav'))

class Pikachu(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_pikachu = []
        for i in range (4):
                    img = sprite_sheet.subsurface((i*56, 0),(56, 30))
                    img = pygame.transform.scale(img,(56*3, 30*3))
                    self.imagens_pikachu.append(img)

        self.index_lista = 0
        self.image = self.imagens_pikachu[self.index_lista]
        self.rect = self.image.get_rect()
        self.posy_inicial = ALTURA-64 
        self.mask = pygame.mask.from_surface(self.image)
        self.rect.center = (100, ALTURA-64)
        self.corre = False
        self.direcao = 1
        self.vidas = 3
        self.icone_heart = pygame.image.load(os.path.join(pasta_img, 'heart.png')).convert_alpha()
        self.icone_heart = pygame.transform.scale(self.icone_heart, (30, 30))
        self.rapido = 0
        self.score = 0

    def correr(self):
         self.corre = True

    def update (self):
        if self.index_lista > 2:
              self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_pikachu[int(self.index_lista)]    
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > LARGURA:
            self.rect.right = LARGURA
        
        keys = pygame.key.get_pressed()

        if keys[K_RIGHT]:
            self.direcao = 1
        elif keys[K_LEFT]:
            self.direcao = -1

        if self.direcao == -1:
            self.image = pygame.transform.flip(self.image, True, False)

        if self.rapido > 0:
            self.rapido -= 1
    
    def rapidao(self):
        self.rapido = 120

    def desenha_vidas(self):
        for i in range(self.vidas):
            pos_x = LARGURA - 600 - (i+1) * (self.icone_heart.get_width() + 5)
            pos_y = 10
            tela.blit(self.icone_heart, (pos_x, pos_y))

class Pokeball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_pokeball = pygame.image.load(os.path.join(pasta_img, 'pokeball.png')).convert_alpha()
        self.icone_pokeball = pygame.transform.scale(self.icone_pokeball, (40, 40))
        self.image = self.icone_pokeball
        self.rect = self.icone_pokeball.get_rect()
        self.rect.x = randrange(LARGURA - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 7

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.kill()

class Rapidez(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_flash = pygame.image.load(os.path.join(pasta_img, 'flash.png')).convert_alpha()
        self.icone_flash = pygame.transform.scale(self.icone_flash, (40, 40))
        self.image = self.icone_flash
        self.rect = self.icone_flash.get_rect()
        self.rect.x = randrange(LARGURA - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 9

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.kill()

class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_star = pygame.image.load(os.path.join(pasta_img, 'star.png')).convert_alpha()
        self.icone_star = pygame.transform.scale(self.icone_star, (40, 40))
        self.image = self.icone_star
        self.rect = self.icone_star.get_rect()
        self.rect.x = randrange(LARGURA - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 6
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > ALTURA:
            self.kill()
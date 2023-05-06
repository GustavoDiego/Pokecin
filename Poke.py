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
icone_heart = pygame.image.load(os.path.join(pasta_img, 'heart.png')).convert_alpha()
icone_pokeball = pygame.image.load(os.path.join(pasta_img, "pokeball.png")).convert_alpha()
icone_flash = pygame.image.load(os.path.join(pasta_img, "flash.png")).convert_alpha()
icone_star = pygame.image.load(os.path.join(pasta_img, "star.png")).convert_alpha()
icone_teclas = pygame.image.load(os.path.join(pasta_img, "Teclas.png")).convert_alpha()
#aud_fundo = pygame.mixer.Sound(os.path.join(pasta_sons, '???.wav'))
aud_star = pygame.mixer.Sound(os.path.join(pasta_sons, 'estrela.wav'))
aud_flash = pygame.mixer.Sound(os.path.join(pasta_sons, 'raio.wav'))
#aud_pokeball = pygame.mixer.Sound(os.path.join(pasta_sons, '???.wav'))
aud_gameover = pygame.mixer.Sound(os.path.join(pasta_sons, 'gameover.wav'))
WHITE = (255, 255, 255)
PRETO = (0,0,0)
VERMELHO = (255,0,0)
AZUL = (98,135,210)
AMARELO = (255,255,2)
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
        if self.rect.right > largura:
            self.rect.right = largura
        
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
            pos_x = largura - 600 - (i+1) * (self.icone_heart.get_width() + 5)
            pos_y = 10
            tela.blit(self.icone_heart, (pos_x, pos_y))

class Pokeball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_pokeball = pygame.image.load(os.path.join(pasta_img, 'pokeball.png')).convert_alpha()
        self.icone_pokeball = pygame.transform.scale(self.icone_pokeball, (40, 40))
        self.image = self.icone_pokeball
        self.rect = self.icone_pokeball.get_rect()
        self.rect.x = randrange(largura - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 5

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > altura:
            self.kill()

class Rapidez(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_flash = pygame.image.load(os.path.join(pasta_img, 'flash.png')).convert_alpha()
        self.icone_flash = pygame.transform.scale(self.icone_flash, (40, 40))
        self.image = self.icone_flash
        self.rect = self.icone_flash.get_rect()
        self.rect.x = randrange(largura - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 5

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > altura:
            self.kill()

class Moeda(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_star = pygame.image.load(os.path.join(pasta_img, 'star.png')).convert_alpha()
        self.icone_star = pygame.transform.scale(self.icone_star, (40, 40))
        self.image = self.icone_star
        self.rect = self.icone_star.get_rect()
        self.rect.x = randrange(largura - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 5
    
    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > altura:
            self.kill()


todas_sprites = pygame.sprite.Group()
pika = Pikachu()
todas_sprites.add(pika)

grupo_pokeballs = pygame.sprite.Group()
todas_sprites.add(grupo_pokeballs)

grupo_velocidade = pygame.sprite.Group()
todas_sprites.add(grupo_velocidade)

grupo_rapidez = pygame.sprite.Group()
todas_sprites.add(grupo_rapidez)

grupo_moedas = pygame.sprite.Group()
todas_sprites.add(grupo_moedas)

relogio = pygame.time.Clock()

tela_inicio = True

while tela_inicio:
    relogio.tick(30)
    tela.fill(AZUL)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    fonte = pygame.font.SysFont("impact",70)
    str_pokecin = fonte.render("POKECIN",True,AMARELO)
    tela.blit(str_pokecin,((largura-str_pokecin.get_width())//2,10))
    

    fonte = pygame.font.SysFont("Arial",30)
    str_start = fonte.render("Pressione espaço para iniciar",True,WHITE)
    tela.blit(str_start,((largura-str_start.get_width())//2,altura-60))

    


    icone_heart = pygame.transform.scale(icone_heart, (30, 30))
    tela.blit(icone_heart,(100,altura-280))

    fonte = pygame.font.SysFont("Arial",15)
    str_coracao = fonte.render("Coração: Você tem 3 e deve evitar que atinja zero",True,WHITE)
    tela.blit(str_coracao,(140,altura-275))

    icone_pokeball = pygame.transform.scale(icone_pokeball, (30, 30))
    tela.blit(icone_pokeball,(100,altura-240))

    fonte = pygame.font.SysFont("Arial",15)
    str_pokeball = fonte.render("Pokebola: Remove uma vida",True,WHITE)
    tela.blit(str_pokeball,(140,altura-235))

    icone_flash = pygame.transform.scale(icone_flash, (30, 30))
    tela.blit(icone_flash,(100,altura-200))

    fonte = pygame.font.SysFont("Arial",15)
    str_lento = fonte.render("Raio: Deixa o Pikachu mais rápido",True,WHITE)
    tela.blit(str_lento,(140,altura-195))
    
    icone_star = pygame.transform.scale(icone_star, (30, 30))
    tela.blit(icone_star,(100,altura-160))

    fonte = pygame.font.SysFont("Arial",15)
    str_moeda = fonte.render("Estrela: Aumenta seu score em 1",True,WHITE)
    tela.blit(str_moeda,(140,altura-155))

    icone_teclas = pygame.transform.scale(icone_teclas , (30, 30))
    tela.blit(icone_teclas,(100,altura-120))

    fonte = pygame.font.SysFont("Arial",15)
    str_teclas = fonte.render("Pressione as teclas direcionais (esquerda/direita) para se movimentar",True,WHITE)
    tela.blit(str_teclas,(140,altura-115))


    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE]:
        tela_inicio = False
        inicio = True

    pygame.display.flip()

while inicio:
    relogio.tick(30)
    tela.blit(imagem_fundo,(0, 0))
    pika.desenha_vidas()

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    
    if pika.vidas <= 0:
        inicio = False
        game_over = True
        aud_gameover.play()


    if randrange(100) < 2:
        pokeball = Pokeball()
        grupo_pokeballs.add(pokeball)
        rapidez = Rapidez()
        grupo_rapidez.add(rapidez)
        moeda = Moeda()
        grupo_moedas.add(moeda)

    grupo_pokeballs.update()
    grupo_pokeballs.draw(tela)

    grupo_rapidez.update()
    grupo_rapidez.draw(tela)

    grupo_moedas.update()
    grupo_moedas.draw(tela)

    if pygame.sprite.spritecollide(pika, grupo_pokeballs, True, pygame.sprite.collide_mask):
        pika.vidas -= 1
        #aud_pokeball.play()

    if pygame.sprite.spritecollide(pika, grupo_rapidez, True, pygame.sprite.collide_mask):
        pika.rapidao()
        aud_flash.play()

    if pygame.sprite.spritecollide(pika, grupo_moedas, True, pygame.sprite.collide_mask):
        pika.score += 1
        aud_star.play()

    font = pygame.font.SysFont("impact", 30)
    score_text = font.render("Score: " + str(pika.score), True, WHITE)
    tela.blit(score_text, (largura - score_text.get_width() - 10, 10))
    tela.blit(icone_star,(largura - score_text.get_width() - 45, 15))
    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        if pika.rapido > 0:
            pika.rect.x += 20
        else:
            pika.rect.x += 9

    if keys[pygame.K_LEFT]:
        if pika.rapido > 0:
            pika.rect.x -= 20
        else:
            pika.rect.x -= 9
    

    todas_sprites.draw(tela)
    todas_sprites.update()
    pygame.display.flip()

while game_over:

    tela.fill((0,0,0))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()


    fonte = pygame.font.SysFont("impact",90)
    str_game_over = fonte.render("GAME OVER",True,VERMELHO)
    tela.blit(str_game_over,((largura-str_game_over.get_width())//2,altura//2- 100))

    font = pygame.font.SysFont("impact", 40)
    score_text = font.render("Score: " + str(pika.score), True, WHITE)
    tela.blit(score_text, (largura - score_text.get_width() - 310, 250))
    

    pygame.display.flip()
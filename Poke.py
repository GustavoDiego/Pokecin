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
icone_coracao = pygame.image.load(os.path.join(pasta_img, 'coracao.png')).convert_alpha()
icone_pedra = pygame.image.load(os.path.join(pasta_img, "pedra.png")).convert_alpha()
som_colisao = pygame.mixer.Sound(os.path.join(pasta_sons, 'pedra_colis.wav'))
icone_lento = pygame.image.load(os.path.join(pasta_img, "lama.png")).convert_alpha()
icone_moeda = pygame.image.load(os.path.join(pasta_img, "moeda.png")).convert_alpha()
icone_teclas = pygame.image.load(os.path.join(pasta_img, "Teclas.png")).convert_alpha()
WHITE = (255, 255, 255)
PRETO = (0,0,0)

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
        self.icone_coracao = pygame.image.load(os.path.join(pasta_img, 'coracao.png')).convert_alpha()
        self.icone_coracao = pygame.transform.scale(self.icone_coracao, (30, 30))
        self.lento = 0
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

        if self.lento > 0:
            self.lento -= 1
    
    def lentidao(self):
        self.lento = 120

    def desenha_vidas(self):
        for i in range(self.vidas):
            pos_x = largura - 600 - (i+1) * (self.icone_coracao.get_width() + 5)
            pos_y = 10
            tela.blit(self.icone_coracao, (pos_x, pos_y))

class Pedra(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_pedra = pygame.image.load(os.path.join(pasta_img, 'pedra.png')).convert_alpha()
        self.icone_pedra = pygame.transform.scale(self.icone_pedra, (40, 40))
        self.image = self.icone_pedra
        self.rect = self.icone_pedra.get_rect()
        self.rect.x = randrange(largura - self.rect.width)
        self.rect.y = -self.rect.height
        self.velocidade = 5

    def update(self):
        self.rect.y += self.velocidade
        if self.rect.top > altura:
            self.kill()

class ItemLento(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.icone_lento = pygame.image.load(os.path.join(pasta_img, 'lama.png')).convert_alpha()
        self.icone_lento = pygame.transform.scale(self.icone_lento, (40, 40))
        self.image = self.icone_lento
        self.rect = self.icone_lento.get_rect()
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
        self.icone_moeda = pygame.image.load(os.path.join(pasta_img, 'moeda.png')).convert_alpha()
        self.icone_moeda = pygame.transform.scale(self.icone_moeda, (40, 40))
        self.image = self.icone_moeda
        self.rect = self.icone_moeda.get_rect()
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
grupo_pedras = pygame.sprite.Group()
todas_sprites.add(grupo_pedras)
grupo_velocidade = pygame.sprite.Group()
todas_sprites.add(grupo_velocidade)
grupo_lentidao = pygame.sprite.Group()
todas_sprites.add(grupo_lentidao)
grupo_moedas = pygame.sprite.Group()
todas_sprites.add(grupo_moedas)

relogio = pygame.time.Clock()

tela_inicio = True

while tela_inicio:
    relogio.tick(30)
    tela.fill(PRETO)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    fonte = pygame.font.SysFont("impact",70)
    str_pokecin = fonte.render("POKECIN",True,WHITE)
    tela.blit(str_pokecin,((largura-str_pokecin.get_width())//2,10))
    

    fonte = pygame.font.SysFont("Arial",30)
    str_start = fonte.render("Pressione Espaço Para Iniciar",True,WHITE)
    tela.blit(str_start,((largura-str_start.get_width())//2,altura-60))

    fonte = pygame.font.SysFont("Arial",30)
    str_instrucao = fonte.render("Instruções:",True,WHITE)
    tela.blit(str_instrucao,((largura-str_instrucao.get_width())//2,altura-315))


    icone_coracao = pygame.transform.scale(icone_coracao, (30, 30))
    tela.blit(icone_coracao,(100,altura-260))

    fonte = pygame.font.SysFont("Arial",15)
    str_coracao = fonte.render("Coração: Você nasce com 3 e deve evitar com que ele chegue a zero",True,WHITE)
    tela.blit(str_coracao,(140,altura-255))

    icone_pedra = pygame.transform.scale(icone_pedra, (30, 30))
    tela.blit(icone_pedra,(100,altura-230))

    fonte = pygame.font.SysFont("Arial",15)
    str_pedra = fonte.render("Pokebola: Cada uma que te atinge te tira uma vida",True,WHITE)
    tela.blit(str_pedra,(140,altura-225))

    icone_lento = pygame.transform.scale(icone_lento, (30, 30))
    tela.blit(icone_lento,(100,altura-200))

    fonte = pygame.font.SysFont("Arial",15)
    str_lento = fonte.render("Raio: Deixa o Pikachu mais rápido",True,WHITE)
    tela.blit(str_lento,(140,altura-195))
    
    icone_moeda = pygame.transform.scale(icone_moeda, (30, 30))
    tela.blit(icone_moeda,(100,altura-170))

    fonte = pygame.font.SysFont("Arial",15)
    str_moeda = fonte.render("Estrela: Aumenta em 1 o seu score a cada Estrela pega",True,WHITE)
    tela.blit(str_moeda,(140,altura-165))

    icone_teclas = pygame.transform.scale(icone_teclas , (30, 30))
    tela.blit(icone_teclas,(100,altura-140))

    fonte = pygame.font.SysFont("Arial",15)
    str_teclas = fonte.render("Pressione direita para ir para direita e esquerda para ir para esquerda",True,WHITE)
    tela.blit(str_teclas,(140,altura-135))


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


    if randrange(100) < 2:
        pedra = Pedra()
        grupo_pedras.add(pedra)
        item = ItemLento()
        grupo_lentidao.add(item)
        moeda = Moeda()
        grupo_moedas.add(moeda)

    grupo_pedras.update()
    grupo_pedras.draw(tela)
    grupo_lentidao.update()
    grupo_lentidao.draw(tela)
    grupo_moedas.update()
    grupo_moedas.draw(tela)

    if pygame.sprite.spritecollide(pika, grupo_pedras, True, pygame.sprite.collide_mask):
        pika.vidas -= 1
        som_colisao.play()
        if pika.vidas == 0:
            
            pass

    if pygame.sprite.spritecollide(pika, grupo_lentidao, True, pygame.sprite.collide_mask):
        pika.lentidao()

    if pygame.sprite.spritecollide(pika, grupo_moedas, True, pygame.sprite.collide_mask):
        pika.score += 1

    font = pygame.font.SysFont("Arial", 30)
    score_text = font.render("Score: " + str(pika.score), True, WHITE)
    tela.blit(score_text, (largura - score_text.get_width() - 10, 10))

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_RIGHT]:
        if pika.lento > 0:
            pika.rect.x += 3
        else:
            pika.rect.x += 15

    if keys[pygame.K_LEFT]:
        if pika.lento > 0:
            pika.rect.x -= 3
        else:
            pika.rect.x -= 15
    

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
    str_game_over = fonte.render("GAME OVER",True,(255,0,0))
    tela.blit(str_game_over,((largura-str_game_over.get_width())//2,altura//2- 100))

    font = pygame.font.SysFont("impact", 40)
    score_text = font.render("Score: " + str(pika.score), True, WHITE)
    tela.blit(score_text, (largura - score_text.get_width() - 310, 250))
    

    pygame.display.flip()
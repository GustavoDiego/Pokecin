import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange
from constantes import *
from spritespoke import *


pasta_principal = os.path.dirname(__file__)
pasta_img = os.path.join(pasta_principal,'IMAGENS')
pasta_sons = os.path.join(pasta_principal,'SONS')

pygame.init()
pygame.mixer.init()

tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.init()
imagem_fundo = pygame.image.load(os.path.join(pasta_img, 'BACKGROUND.jpg')).convert()
pygame.display.set_caption('Pokecin')


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

    fonte = pygame.font.SysFont("impact", 70)
    str_pokecin = fonte.render("POKECIN", True, AMARELO)
    tela.blit(str_pokecin, ((LARGURA-str_pokecin.get_width()) // 2, 10))
    
    fonte = pygame.font.SysFont("Arial", 30)
    str_start = fonte.render("Pressione espaço para iniciar", True, WHITE)
    tela.blit(str_start, ((LARGURA-str_start.get_width()) // 2, ALTURA-60))

    icone_heart = pygame.transform.scale(icone_heart, (30, 30))
    tela.blit(icone_heart, (100, ALTURA-280))

    fonte = pygame.font.SysFont("Arial", 15)
    str_coracao = fonte.render("Coração: Você tem 3 e deve evitar que atinja zero", True, WHITE)
    tela.blit(str_coracao, (140, ALTURA-275))

    icone_pokeball = pygame.transform.scale(icone_pokeball, (30, 30))
    tela.blit(icone_pokeball, (100,ALTURA-240))

    fonte = pygame.font.SysFont("Arial", 15)
    str_pokeball = fonte.render("Pokebola: Remove uma vida", True, WHITE)
    tela.blit(str_pokeball,(140, ALTURA-235))

    icone_flash = pygame.transform.scale(icone_flash, (30, 30))
    tela.blit(icone_flash,(100, ALTURA-200))

    fonte = pygame.font.SysFont("Arial", 15)
    str_lento = fonte.render("Raio: Deixa o Pikachu mais rápido", True, WHITE)
    tela.blit(str_lento,(140, ALTURA-195))
    
    icone_star = pygame.transform.scale(icone_star, (30, 30))
    tela.blit(icone_star,(100, ALTURA-160))

    fonte = pygame.font.SysFont("Arial", 15)
    str_moeda = fonte.render("Estrela: Aumenta seu score em 1", True, WHITE)
    tela.blit(str_moeda,(140, ALTURA-155))

    icone_teclas = pygame.transform.scale(icone_teclas , (30, 30))
    tela.blit(icone_teclas,(100, ALTURA-120))

    fonte = pygame.font.SysFont("Arial", 15)
    str_teclas = fonte.render("Pressione as teclas direcionais (esquerda/direita) para se movimentar", True, WHITE)
    tela.blit(str_teclas,(140, ALTURA-115))

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

    if randrange(100) < 5:
        moeda = Moeda()
        grupo_moedas.add(moeda)

    if randrange(100) < 3:
        pokeball = Pokeball()
        grupo_pokeballs.add(pokeball)

    if randrange(100) < 1:
        rapidez = Rapidez()
        grupo_rapidez.add(rapidez)

    grupo_pokeballs.update()
    grupo_pokeballs.draw(tela)

    grupo_rapidez.update()
    grupo_rapidez.draw(tela)

    grupo_moedas.update()
    grupo_moedas.draw(tela)

    if pygame.sprite.spritecollide(pika, grupo_pokeballs, True, pygame.sprite.collide_mask):
        pika.vidas -= 1
        aud_pokeball.play()

    if pygame.sprite.spritecollide(pika, grupo_rapidez, True, pygame.sprite.collide_mask):
        pika.rapidao()
        aud_flash.play()

    if pygame.sprite.spritecollide(pika, grupo_moedas, True, pygame.sprite.collide_mask):
        pika.score += 1
        aud_star.play()

    font = pygame.font.SysFont("impact", 30)
    score_text = font.render("Score: " + str(pika.score), True, WHITE)
    tela.blit(score_text, (LARGURA - score_text.get_width() - 10, 10))
    tela.blit(icone_star,(LARGURA - score_text.get_width() - 45, 15))
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

    tela.fill((AZUL))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    fonte = pygame.font.SysFont("impact",90)
    str_game_over = fonte.render("GAME OVER", True, VERMELHO)
    tela.blit(str_game_over, ((LARGURA-str_game_over.get_width()) // 2, ALTURA // 2 - 100))

    font = pygame.font.SysFont("impact", 40)
    score_text = font.render("Score: " + str(pika.score), True, WHITE)
    tela.blit(score_text, (LARGURA - score_text.get_width() - 310, 250))
    
    pygame.display.flip()
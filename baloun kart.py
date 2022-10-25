import pygame
from pygame.locals import *

pygame.init()

# ouverture d'une fenetre avec une resolution de 640 par 480, windows
windows = pygame.display.set_mode ((750,750))
# titre
# pygame. display. se _caption('titre)
pygame.display.set_caption('baloun kart')
# création d'un font coloré:
fond=pygame.Surface(windows.get_size())
fond=pygame.image.load("F:jeu ISN/bonjour1.jpg")
#font=pygame.font.font(none,36)
# sysfont(name, size, bold=false, italic=false)->font
font= pygame.font.SysFont('times',36,0,1)
text = font.render ("aller Pac man tu ne peut pas gagner", 1, (100, 10, 1))
textpos=text.get_rect()
textpos.center = fond. get_rect().center
textpos. centery = 50 #fond. get_rect().centery
fond.blit(text, textpos)

#personage
perso=pygame.image.load("F:jeu ISN/pac man 1.jpg")
perso_x=100
perso_y=336
windows.blit(perso,(perso_x, perso_y))
perso2=pygame.image.load("F:jeu ISN/chomp1.png")
perso2_x=80
perso2_y=380
windows.blit(perso2,(perso2_x, perso2_y))
#musique
pygame.mixer.music.load("F:jeu ISN/route arc en ciel.mp3")
pygame.mixer.music.play(-1)
#les trois nombres correspondent à la couleur (r,v,b)

def affav(perso2_x,perso2_y):
#    print(perso2_x)
#    print(perso2_y)
#    fond.blit(text, textpos)
    windows.blit(fond, (0,0))
    windows.blit(perso,(perso_x,perso_y))
    windows.blit(perso2,(perso2_x, perso2_y))
#rafraichissement
pygame.display.flip()
pygame.time.Clock().tick(50)

#répétion des touches
pygame.key.set_repeat(400,30)
continuer=1
while continuer:
    pygame.time.Clock().tick(50)
    for event in pygame.event.get(): #attente d'un évenement
        if event.type==QUIT:
            continuer=0
        if event.type==KEYDOWN:
            if event.key == K_DOWN:
                perso_y=perso_y+10
            if event.key == K_UP:
                perso_y=perso_y-10
            if event.key == K_LEFT:
                perso_x=perso_x-10
            if event.key == K_RIGHT:
                perso_x=perso_x+10

    if perso2_x == 80 and perso2_y> 100:
        perso2_y=perso2_y-10
        affav(perso2_x,perso2_y)
    if perso2_x < 490 and perso2_y == 100:
        perso2_x=perso2_x+10
        affav(perso2_x,perso2_y)
    if perso2_x == 490 and perso2_y<320:
        perso2_y=perso2_y+10
        affav(perso2_x,perso2_y)
    if perso2_x>250 and perso2_y == 320:
        perso2_x=perso2_x-10
        affav(perso2_x,perso2_y)
    if perso2_x == 250 and perso2_y >= 320 <= 450:
        perso2_y=perso2_y+10
        affav(perso2_x,perso2_y)
    if perso2_x < 620 and perso2_y == 450:
        perso2_x=perso2_x+10
        affav(perso2_x,perso2_y)
    if perso2_x == 620 and perso2_y < 620:
        perso2_y=perso2_y+10
        affav(perso2_x,perso2_y)
    if perso2_x > 80 and perso2_y ==620:
        perso2_x=perso2_x-10
        affav(perso2_x,perso2_y)
    if perso2_x == 250 and perso2_y >= 450:
        perso2_x=perso2_x-10
        affav(perso2_x,perso2_y)
    if perso2_x ==80 and perso2_y>100:
        perso2_y=perso2_y-10
        affav(perso2_x,perso2_y)




    #re-collage
    fond.blit(text, textpos)
    windows.blit(fond, (0,0))
    windows.blit(perso,(perso_x,perso_y))
    windows.blit(perso2,(perso2_x, perso2_y))
    #rafraichissement
    pygame.display.flip()
pygame.quit()
quit()
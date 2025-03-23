import pygame
#Constantes

global GREEN 
GREEN = (16,250,54)
global ORANGE
ORANGE = (250,150,15)
global RED 
RED = (250,16,16)
global BLUE 
BLUE = (16,63,250)
global YELLOW 
YELLOW = (241,250,16)
global WHITE 
WHITE = (255,255,255)

colors = [GREEN,ORANGE,RED,BLUE,YELLOW,WHITE]

edges = {
    (WHITE,BLUE):'AQ',
    (WHITE,ORANGE):'DE',
    (WHITE,GREEN):'CI',
    (WHITE,RED):'BM',
    (YELLOW,ORANGE):'XG',
    (YELLOW,GREEN):'UK',
    (YELLOW,RED):'VO',
    (YELLOW,BLUE):'VS',
    (ORANGE,BLUE):'HR',
    (ORANGE,GREEN):'FL',
    (GREEN,RED):'JP',
    (RED,BLUE):'NT'
}

edges_list = list(edges.items())

#Pygame const

# Taille de la fenetre
global width,height,screen
width, height = 500,300
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Blind Trainer")

# Pour limiter le nombre d'images par seconde
clock=pygame.time.Clock()
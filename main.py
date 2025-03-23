from const import*
import random
import pygame
import pygame.freetype
import sys

def new_edge():
    colors,letters = random.choice(edges_list)
    return colors, letters

def display_colors(color1,color2):
    rect1 = pygame.Rect(width//3,height//3,100,100)
    pygame.draw.rect(screen, color1, rect1) 

    rect2 = pygame.Rect(2*width//3,height//3,100,100)
    pygame.draw.rect(screen, color2, rect2) 

def get_events():
    for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                get_quit_events()

def get_quit_events():
    pygame.quit()
    sys.exit()
    exit()



def main():
    pygame.init()
    a,b = new_edge()
    while True:
        clock.tick(60) # envoi de l'image 
        pygame.display.flip() # on attend pour ne pas depasser 60 images/seconde
        display_colors(a[0],a[1])
        get_events()

main()
from const import*
import random
import pygame
import pygame.freetype
import sys

global color1,color2,letters
global show_letters

def new_edge():
    colors,letters = random.choice(edges_list)
    return colors, letters

def display_colors(color1,color2,letters,show_letters):
    screen.fill(BACKGROUND)

    rect1 = pygame.Rect(width//3-50,height//4,100,100)
    pygame.draw.rect(screen, color1, rect1) 

    rect2 = pygame.Rect(2*width//3-50,height//4,100,100)
    pygame.draw.rect(screen, color2, rect2)

    if show_letters:
        lettre_1 = small_font.render(letters[0],True,NOIR)
        screen.blit(lettre_1,[width//3-lettre_1.get_rect().width//2,2*height//3])
        lettre_2 = small_font.render(letters[1],True,NOIR)
        screen.blit(lettre_2,[2*width//3-lettre_2.get_rect().width//2,2*height//3])

def get_events():
    for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                get_quit_events()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                next_color_event()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN:
                get_letters_event()

def get_quit_events():
    pygame.quit()
    sys.exit()
    exit()

def next_color_event():
    global color1,color2,letters,show_letters
    show_letters = False
    color,letters = new_edge()
    color1 = color[0]
    color2 = color[1]

def get_letters_event():
    global show_letters
    show_letters = True


def main():
    global color1,color2,letters
    global show_letters
    pygame.init()
    pygame_icon = pygame.image.load('rubiks_icon.webp')
    pygame.display.set_icon(pygame_icon)
    color,letters = new_edge()
    color1 = color[0]
    color2 = color[1]
    show_letters = False
    while True:
        clock.tick(60) # envoi de l'image 
        pygame.display.flip() # on attend pour ne pas depasser 60 images/seconde
        display_colors(color1,color2,letters,show_letters)
        get_events()

main()
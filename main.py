from const import*
import random
import pygame
import pygame.freetype
import sys

global color1,color2,letters
global show_letters

class Main:

    def __init__(self):
        self.color1 = None
        self.color2 = None
        self.letters = None
        self.show_letters = False
        pygame.init()
        pygame_icon = pygame.image.load('rubiks_icon.webp')
        pygame.display.set_icon(pygame_icon)
        pygame.display.set_caption("Blind Trainer")
        self.next_color_event()
        self.main()

    def new_edge(self):
        colors,letters = random.choice(edges_list)
        return colors, letters

    def display_colors(self):
        screen.fill(BACKGROUND)

        rect1 = pygame.Rect(width//3-50,height//4,100,100)
        pygame.draw.rect(screen, self.color1, rect1) 

        rect2 = pygame.Rect(2*width//3-50,height//4,100,100)
        pygame.draw.rect(screen,  self.color2, rect2)

        if  self.show_letters:
            lettre_1 = small_font.render( self.letters[0],True,NOIR)
            screen.blit(lettre_1,[width//3-lettre_1.get_rect().width//2,2*height//3])
            lettre_2 = small_font.render( self.letters[1],True,NOIR)
            screen.blit(lettre_2,[2*width//3-lettre_2.get_rect().width//2,2*height//3])

    def get_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                    self.get_quit_events()
                if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                    self.next_color_event()
                if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN:
                    self.get_letters_event()

    def get_quit_events(self):
        pygame.quit()
        sys.exit()
        exit()

    def next_color_event(self):
        self.show_letters = False
        color,self.letters = self.new_edge()
        self.color1 = color[0]
        self.color2 = color[1]

    def get_letters_event(self):
        self.show_letters = True

    def main(self):
        while True:
            clock.tick(60) # envoi de l'image 
            pygame.display.flip() # on attend pour ne pas depasser 60 images/seconde
            self.display_colors()
            self.get_events()

main = Main()

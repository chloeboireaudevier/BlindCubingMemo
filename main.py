from const import*
import random
import pygame
import pygame.freetype
import sys

class Main:

    def __init__(self):
        self.color1 = None
        self.color2 = None
        self.color3 = None
        self.letters = None
        self.show_letters = 0
        self.type = None
        pygame.init()
        self.clock=pygame.time.Clock()
        self.screen = pygame.display.set_mode((width, height))
        self.small_font = pygame.font.SysFont(None,23)
        self.command_font = pygame.font.SysFont('lucidaconsole',12)
        pygame_icon = pygame.image.load('rubiks_icon.webp')
        pygame.display.set_icon(pygame_icon)
        pygame.display.set_caption("Blind Trainer")
        self.next_color_event()
        self.main()

    def new_edge(self):
        colors,letters = random.choice(edges_list)
        return colors, letters
    
    def new_corner(self):
        colors,letters = random.choice(corners_list)
        return colors, letters
    
    def display_colors(self):
        if self.type == 0:
            space = 3
        else:
            space = 4

        self.screen.fill(BACKGROUND)

        rect1 = pygame.Rect(width//space-50,height//4,100,100)
        pygame.draw.rect(self.screen, self.color1, rect1) 

        rect2 = pygame.Rect(2*width//space-50,height//4,100,100)
        pygame.draw.rect(self.screen,  self.color2, rect2)
        
        if self.type == 1:
            rect3 = pygame.Rect(3*width//space-50,height//4,100,100)
            pygame.draw.rect(self.screen, self.color3, rect3)

    def display_letters(self):
        if self.type == 0:
            space = 3
        else:
            space = 4

        if self.show_letters >= 1:
            lettre_1 = self.small_font.render( self.letters[0],True,BLACK)
            self.screen.blit(lettre_1,[width//space-lettre_1.get_rect().width//2,2*height//3])
        if self.show_letters >= 2:
            lettre_2 = self.small_font.render( self.letters[1],True,BLACK)
            self.screen.blit(lettre_2,[2*width//space-lettre_2.get_rect().width//2,2*height//3])
        if self.type == 1 and self.show_letters >= 3:
            lettre_3 = self.small_font.render( self.letters[2],True,BLACK)
            self.screen.blit(lettre_3,[3*width//space-lettre_3.get_rect().width//2,2*height//3])

    def display_commands(self):
        text = "Space to get to the next configuration, Enter to reveal the letters"
        text = self.command_font.render(text,True,BLACK)
        self.screen.blit(text,[width/2-text.get_rect().width//2,height - 1.5*text.get_rect().height])

    def get_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE): 
                self.quit_event()
            if event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                self.next_color_event()
            if event.type == pygame.KEYDOWN and event.key==pygame.K_RETURN:
                self.get_letters_event()

    def quit_event(self):
        pygame.quit()
        sys.exit()
        exit()

    def next_color_event(self):
        self.show_letters = 0
        self.type = random.randint(0,1)
        letters_ordered = []
        
        if self.type == 0:
            color,letters = self.new_edge()
            order = [0,1]
        else:
            color,letters = self.new_corner()
            order = [0,1,2]
            
        random.shuffle(order)
        self.color1 = color[order[0]]
        letters_ordered.append(letters[order[0]])
        self.color2 = color[order[1]]
        letters_ordered.append(letters[order[1]])

        if self.type == 1:
            self.color3 = color[order[2]]
            letters_ordered.append(letters[order[2]])

        self.letters = ''.join(letters_ordered)

    def get_letters_event(self):
        if self.show_letters <3:
            self.show_letters +=1

    def main(self):
        while True:
            self.clock.tick(60)
            pygame.display.flip()
            self.display_colors()
            self.display_letters()
            self.display_commands()
            self.get_events()

main = Main()

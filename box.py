import pygame

color = (75,163,255)

EMPTY, HEALTY, HITTED = range(3)

class Box():
    #typy pola

    def __init__(self,poss,screen):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.state = HEALTY
    def draw(self):
        pygame.draw.rect(self.screen,color,self.rect)

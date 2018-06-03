import pygame

class Box():
    #typy pola

    def __init__(self,poss,screen):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.cliced = False

    def draw(self,color):
        pygame.draw.rect(self.screen,color,self.rect)

    def is_pressed(self,poss):
        if self.rect.left < poss[0] <self.rect.right and self.rect.top<poss[1]<self.rect.bottom and self.cliced == False:
            self.cliced = True
            return True
        return False
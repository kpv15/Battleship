import pygame

class Box(object):
    #typy pola

    def __init__(self,poss,screen,cords):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.cliced = False
        self.status = 0
        self.cords = cords

    def draw(self,color):
        pygame.draw.rect(self.screen,color,self.rect)

    def is_pressed(self,poss):
        if self.rect.left < poss[0] <self.rect.right and self.rect.top<poss[1]<self.rect.bottom and self.cliced == False:
            self.cliced = True
            print(self.cords)
            return True
        return False
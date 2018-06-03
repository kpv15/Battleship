import pygame

class Box(object):
    #typy pola

    def __init__(self,poss,screen,cords):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.cliced = False
        self.status = 0
        self.cords = cords

    def draw(self):
        if self.status == 0:
            pygame.draw.rect(self.screen,(30,50,255),self.rect)
        elif self.status == 1:
            pygame.draw.rect(self.screen, (60,50,10), self.rect)


    def is_pressed(self,poss):
        if self.rect.left < poss[0] <self.rect.right and self.rect.top<poss[1]<self.rect.bottom:
            #print(self.cords)
            return True,(self.cords)
        return False,(0,0)

    '''def is_pressed(self,poss):
        if self.rect.left < poss[0] <self.rect.right and self.rect.top<poss[1]<self.rect.bottom and self.cliced == False:
            self.cliced = True
            print(self.cords)
            return True
        return False'''
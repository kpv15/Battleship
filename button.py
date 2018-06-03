import pygame

class Button():
    def __init__(self,poss,screen,text,font_size):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.text = pygame.font.SysFont("arial",font_size).render(text,1,(0,200,100))
        print(self.rect.bottom)
        #TODO check size of text vs size of rect

    def draw(self):
        pygame.draw.rect(self.screen,(50,10,80),self.rect)
        self.screen.blit(self.text,(self.rect.x,self.rect.y))

    def is_pressed(self,poss):
        if self.rect.left < poss[0] <self.rect.right and self.rect.top<poss[1]<self.rect.bottom:
            return True
        return False
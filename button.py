import pygame

class Button():
    def __init__(self,poss,screen,text,font_size):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.text = pygame.font.SysFont("arial",font_size).render(text,1,(0,200,100))

    def draw(self):
        pygame.draw.rect(self.screen,(60,0,0),self.rect)
        self.screen.blit(self.text,(self.rect.x,self.rect.y))

    def is_pressed(self,x,y):

        pass
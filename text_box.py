import pygame

class Text_box(object):
    def __init__(self, poss, screen, text, font_size):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.font_size = font_size
        self.text = pygame.font.SysFont("arial", font_size).render(text, 1, (0, 200, 100))
        print(self.rect.bottom)
        # TODO check size of text vs size of rect

    def set(self,text):
        self.text = pygame.font.SysFont("arial", self.font_size).render(text, 1, (0, 200, 100))
    def draw(self):
        pygame.draw.rect(self.screen, (20, 5, 150), self.rect)
        self.screen.blit(self.text, (self.rect.x+5, self.rect.y+5))

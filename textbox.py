import pygame

dt = 2000.0


class TextBox(object):
    def __init__(self, poss, screen, text, font_size):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.font_size = font_size
        self.text = pygame.font.SysFont("arial", font_size).render(text, 1, (0, 200, 100))
        #print(self.rect.bottom)
        self.clock = pygame.time.Clock()
        self.delta = 0.0
        # TODO check size of text vs size of rect

    def set(self, text):
        self.text = pygame.font.SysFont("arial", self.font_size).render(text, 1, (0, 200, 100))

    def draw(self):
        # print(self.delta)
        pygame.draw.rect(self.screen, (20, 5, 150), self.rect)
        self.screen.blit(self.text, (self.rect.x + 5, self.rect.y + 5))

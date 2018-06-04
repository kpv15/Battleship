import pygame
from enum import Enum


class BoxStatus(Enum):
    FREE = 0
    SHIP = 1
    MISS = 2
    HIT = 3
    DESTROYED = 4

class Box(object):
    def __init__(self, poss, screen, cords):
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.cliced = False
        self.status = BoxStatus.FREE
        self.cords = cords

    def draw(self, ship_hide=False):
        if self.status == BoxStatus.FREE:
            pygame.draw.rect(self.screen, (30, 50, 255), self.rect)
        elif self.status == BoxStatus.SHIP:
            if ship_hide:
                pygame.draw.rect(self.screen, (30, 50, 255), self.rect)
            else:
                pygame.draw.rect(self.screen, (60, 50, 10), self.rect)
        elif self.status == BoxStatus.MISS:
            pygame.draw.rect(self.screen, (70, 70, 140), self.rect)
        elif self.status == BoxStatus.HIT:
            pygame.draw.rect(self.screen, (200, 30, 30), self.rect)
        elif self.status == BoxStatus.DESTROYED:
            pygame.draw.rect(self.screen, (120, 0, 0), self.rect)

    def is_pressed(self, poss):
        if self.rect.left < poss[0] < self.rect.right and self.rect.top < poss[1] < self.rect.bottom:
            # print(self.cords)
            return True, self
        return False, (0, 0)

    '''def is_pressed(self,poss):
        if self.rect.left < poss[0] <self.rect.right and self.rect.top<poss[1]<self.rect.bottom and self.cliced == False:
            self.cliced = True
            print(self.cords)
            return True
        return False'''

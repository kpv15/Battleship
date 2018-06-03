import pygame
from box import Box
from ship import Ship
box_number = 10
space_width = 4
color = (0,163,255)
class Board(object):
    #TODO end class

    def __init__(self,poss,screen):
        print("board created")
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.box_with = self.rect.width/box_number
        print(self.box_with)
        self.tab = [Box((self.rect.left+space_width/2+col*self.box_with,self.rect.top+space_width/2+row*self.box_with,
                          self.box_with-space_width,self.box_with-space_width),
                          self.screen,(col,row)) for col in range(box_number) for row in range(box_number)]

        print(self.tab)
        ships_list = [Ship(5-i) for i in range(1,5) for j in range(i)]
        for i in ships_list:
            print(i.size,end=',')

    def draw(self, ships = False):
        pygame.draw.rect(self.screen,color,self.rect)
        for i in self.tab:
            i.draw((30,50,255))

    def is_pressed(self,poss):
        for i in self.tab:
             if i.is_pressed(poss) == True:
                    return True
        return False

    def pressed(self,poss):
        pass
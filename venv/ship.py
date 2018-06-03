import pygame
from box import Box

class Ship(object):
    #typy pola

    def __init__(self,size):
        self.size = size
        self.parts = []

    def add(self,box):
        if len(self.parts) == 0:
            self.parts.append(box)
        elif len(self.parts) < size:
            for i in self.parts:
                x,y = i.cords
                xx ,yy =box.cords
                if ( (xx - x == 1 or xx-x == -1)  and yy - y == 0 ) or ( (yy-y == 1 or yy-y == -1) and xx-x == 0 ):
                        self.parts.append(box)
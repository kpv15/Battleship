import pygame
from box import Box


class Ship(object):
    # typy pola

    def __init__(self, size):
        self.size = size
        self.parts = []

    def set(self):
        pass

    def add(self, box,list):
        x,y = box.cords
        for i in list:
            if (x-1,y) == i.cords or i.cords == (x + 1, y) or i.cords == (x, y - 1) or i.cords == (x, y + 1) or\
            (x - 1, y-1) == i.cords or i.cords == (x - 1, y + 1) or i.cords == (x + 1, y + 1) or i.cords == (x + 1, y - 1):
                if i.status == 1:
                    for j in self.parts:
                        if j== i : break
                    else: return False
        print("x")
        if len(self.parts) == 0:
            self.parts.append(box)
            box.status = 1
        elif len(self.parts) == 1:
            for i in self.parts:
                x, y = i.cords
                xx, yy = box.cords
                if ((xx - x == 1 or xx - x == -1) and yy - y == 0):
                    self.parts.append(box)
                    self.align = 0
                    box.status = 1
                    return True
                if ((yy - y == 1 or yy - y == -1) and xx - x == 0):
                    self.parts.append(box)
                    self.align = 1
                    box.status = 1
                    return True
        elif len(self.parts) < self.size:
            for i in self.parts:
                x, y = i.cords
                xx, yy = box.cords
                if ((xx - x == 1 or xx - x == -1) and yy - y == 0 and self.align == 0) or (
                        (yy - y == 1 or yy - y == -1) and xx - x == 0 and self.align == 1):
                    self.parts.append(box)
                    box.status = 1
                    return True
        return False

    def full(self):
        if len(self.parts) == self.size:
            return True
        return False

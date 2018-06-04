import pygame
from box import Box, BoxStatus


class Ship(object):
    # typy pola

    def __init__(self, size,msg_box):
        self.size = size
        self.parts = []
        self.msg_box = msg_box
        self.live = True

    def set(self):
        pass

    def check_condition(self):
        if self.live:
            for i in self.parts:
                if i.status == BoxStatus.SHIP:
                    break
            else:
                for j in self.parts:
                    j.status = BoxStatus.DESTROYED
                self.live = False
        return self.live

    def add(self, box, list,msg_flag):
        x, y = box.cords
        for i in list:
            if (x - 1, y) == i.cords or i.cords == (x + 1, y) or i.cords == (x, y - 1) or i.cords == (x, y + 1) or \
                    (x - 1, y - 1) == i.cords or i.cords == (x - 1, y + 1) or i.cords == (x + 1, y + 1) or i.cords == (
            x + 1, y - 1):
                if i.status == BoxStatus.SHIP:
                    for j in self.parts:
                        if j == i: break
                    else:
                        if msg_flag:
                            self.msg_box.set_tmp("Błedna pozycja okretu spróbuj ponownie",2000)
                        return False
        # print("x")
        if len(self.parts) == 0:
            self.parts.append(box)
            box.status = BoxStatus.SHIP
            return True
        elif len(self.parts) == 1:
            for i in self.parts:
                x, y = i.cords
                xx, yy = box.cords
                if ((xx - x == 1 or xx - x == -1) and yy - y == 0):
                    self.parts.append(box)
                    self.align = 0
                    box.status = BoxStatus.SHIP
                    return True
                if ((yy - y == 1 or yy - y == -1) and xx - x == 0):
                    self.parts.append(box)
                    self.align = 1
                    box.status = BoxStatus.SHIP
                    return True
        elif len(self.parts) < self.size:
            for i in self.parts:
                x, y = i.cords
                xx, yy = box.cords
                if ((xx - x == 1 or xx - x == -1) and yy - y == 0 and self.align == 0) or (
                        (yy - y == 1 or yy - y == -1) and xx - x == 0 and self.align == 1):
                    self.parts.append(box)
                    box.status = BoxStatus.SHIP
                    return True
        return False

    def full(self):
        if len(self.parts) == self.size:
            return True
        return False

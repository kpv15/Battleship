import pygame
from random import randint
from box import Box
from ship import Ship

box_number = 10
space_width = 4
color = (0, 163, 255)


class Board(object):
    # TODO end class
    def __init__(self, poss, screen, msg):
        #print("board created")
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.box_with = self.rect.width / box_number
        self.msg = msg
        self.last_pressed = None
        self.ready = False
        self.need_action = True
        #print(self.box_with)
        self.tab = [Box((self.rect.left + space_width / 2 + col * self.box_with,
                         self.rect.top + space_width / 2 + row * self.box_with,
                         self.box_with - space_width, self.box_with - space_width),
                        self.screen, (col, row)) for col in range(box_number) for row in range(box_number)]

        #print(self.tab)
        self.ships_list = [Ship(5 - i) for i in range(1, 5) for j in range(i)]
        self.init = 0
        self.s_num = 1
        self.prev_size_last = self.ships_list[self.init].size

    def set_ship(self):
        if self.init != len(self.ships_list):
            if self.prev_size_last != self.ships_list[self.init].size:
                self.s_num = 1
            self.msg.set(
                'wybierz pozycje ' + str(self.s_num) + '-ego ' + str(self.ships_list[self.init].size) + ' masztowca')
            self.prev_size_last = self.ships_list[self.init].size
        self.need_action = False

    def set_ship_pressed(self):
        self.need_action = True
        if self.init != len(self.ships_list):
            for i in self.tab:
                if i.cords == self.last_pressed:
                    b = i
                    break

            if b.status == 0:
                self.ships_list[self.init].add(b, self.tab)
                if self.ships_list[self.init].full():
                    self.init += 1
                    self.s_num += 1
                    if self.init == len(self.ships_list):
                        self.msg.set("ustawiono wszystkie okręty")
                        self.ready = True
                        return False
        return True

    def cpu_set_ship(self):
        flag = True
        i = 0
        while flag and i < 10000:
            self.last_pressed = randint(0, box_number - 1), randint(0, box_number - 1)
            #print(self.last_pressed)
            flag = self.set_ship_pressed()
            i += 1
        if i == 10000: print("error")
        # TODO ACTION WHEN ERROR

    def draw(self, ships_hide=False):
        pygame.draw.rect(self.screen, color, self.rect)
        for i in self.tab:
            i.draw(ships_hide)

    def is_pressed(self, poss):
        for i in self.tab:
            pressed, cord = i.is_pressed(poss)
            if pressed:
                self.last_pressed = cord
                return True
        return False

    # FUNCTION HANDLING PLAYER SHOOT RETURN TRUE IF PLAYER HIT
    def player_shoot(self):
        pass

    # FUNCTION HANDLING CPU SHOOT RETURN TRUE IF CPU HIT
    def cpu_shoot(self):
        pass

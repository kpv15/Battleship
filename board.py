import pygame
from random import randint
from box import Box, BoxStatus
from ship import Ship

box_number = 10
space_width = 4
color = (0, 163, 255)


class Board(object):
    # TODO end class
    def __init__(self, poss, screen, msg):
        # print("board created")
        self.screen = screen
        self.rect = pygame.Rect(poss)
        self.poss = poss
        self.box_with = self.rect.width / box_number
        self.msg = msg
        self.last_pressed = None
        self.ready = False
        self.need_action = True
        # print(self.box_with)
        self.tab = [Box((self.rect.left + space_width / 2 + col * self.box_with,
                         self.rect.top + space_width / 2 + row * self.box_with,
                         self.box_with - space_width, self.box_with - space_width),
                        self.screen, (col, row)) for col in range(box_number) for row in range(box_number)]

        # print(self.tab)
        self.ships_list = [Ship(5 - i, self.msg) for i in range(1, 5) for j in range(i)]
        self.init = 0
        self.s_num = 1
        self.all_ships_destroyed = False
        self.prev_size_last = self.ships_list[self.init].size

    def set_ship(self):
        if self.init != len(self.ships_list):
            if self.prev_size_last != self.ships_list[self.init].size:
                self.s_num = 1
            self.msg.set(
                'wybierz pozycje ' + str(self.s_num) + '-ego ' + str(self.ships_list[self.init].size) + ' masztowca')
            self.prev_size_last = self.ships_list[self.init].size
        self.need_action = False

    def set_ship_pressed(self, msg_flag=True):
        self.need_action = True
        if self.init != len(self.ships_list):
            for i in self.tab:
                if i == self.last_pressed:
                    b = i
                    break

            if b.status == BoxStatus.FREE:
                self.ships_list[self.init].add(b, self.tab, msg_flag)
                if self.ships_list[self.init].full():
                    self.init += 1
                    self.s_num += 1
                    if self.init == len(self.ships_list):
                        self.msg.set("wszystkie okręty na miejscach, wciśnij start by rozpocząć bitwe")
                        self.ready = True
                        return False
        return True

    def cpu_set_ship(self):
        while True:
            flag = True
            i = 0
            while flag and i < 10000:
                self.last_pressed = self.tab[randint(0, len(self.tab) - 1)]
                # print(self.last_pressed)
                flag = self.set_ship_pressed(msg_flag=False)
                i += 1
            if i == 10000:
                print("problem")
                self.__init__(self.poss, self.screen, self.msg)
            else:
                break
            # TODO ACTION WHEN ERROR

    def draw(self, ships_hide=False):
        pygame.draw.rect(self.screen, color, self.rect)
        for i in self.tab:
            i.draw(ships_hide)

    def is_pressed(self, poss):
        for i in self.tab:
            pressed, last = i.is_pressed(poss)
            if pressed:
                self.last_pressed = last
                return True
        return False

    # FUNCTION HANDLING PLAYER SHOOT RETURN TRUE IF PLAYER HIT OR MISS AGAIN THE SAME BOX
    def player_shoot(self, msg=True):
        print(self.last_pressed.status)
        if self.last_pressed.status == BoxStatus.FREE:
            self.last_pressed.status = BoxStatus.MISS
            return False
        elif self.last_pressed.status == BoxStatus.SHIP:
            self.last_pressed.status = BoxStatus.HIT
            self.check_condition()
            return True
        elif self.last_pressed.status == BoxStatus.HIT or self.last_pressed.status == BoxStatus.DESTROYED \
                or self.last_pressed.status == BoxStatus.MISS:
            if msg:
                self.msg.set_tmp("pozycja została już ostrzelana", 1000)
            return True
        print("error")

    def check_condition(self):
        number = 0
        for i in self.ships_list:
            if not i.check_condition():
                number += 1
        print(number)
        if number == len(self.ships_list):
            self.all_ships_destroyed = True

    # FUNCTION HANDLING CPU SHOOT RETURN TRUE IF CPU HIT
    def cpu_shoot(self):
        if randint(0, 100) < 80:
            self.last_pressed = self.tab[randint(0, len(self.tab) - 1)]
        else:
            for i in self.tab:
                if i.status == BoxStatus.SHIP:
                    self.last_pressed = i
        tmp = self.player_shoot(msg=False)
        if not tmp:
            pygame.time.wait(800)
        return tmp

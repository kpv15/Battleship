import pygame, sys
from random import getrandbits
from board import Board
from button import Button
from textbox import TextBox
from enum import Enum


class GameState(Enum):
    SETTING = 0
    PLAYING = 1
    END = 2


class Game(object):
    def __init__(self):
        # INITIALIZATION
        pygame.init()
        self.screen = pygame.display.set_mode((800, 550))
        self.start_button = Button((10, 10, 100, 50), self.screen, "Start", 33)
        self.restart_button = Button((120, 10, 100, 50), self.screen, "Restart", 33)

        size = self.screen.get_size()
        self.msg_box = TextBox((0, size[1] - 60, size[0], 50), self.screen, "", 33)
        self.msg_box2 = TextBox((size[0] - 250, 0, 250, 50), self.screen, "xD", 33)
        self.player_move = True
        self.player_map_pressed_flag = False
        self.cpu_map_pressed_flag = False
        self.state = GameState.SETTING
        self.win = False

        while True:
             self.restart()
             if self.main_loop():
                 print("victory")
             else:
                 print("defeat")


    #main part of game return True if win or False if defeat
    def main_loop(self):
        # main loop
        while True:
            # after restart setting ships
            if self.state == GameState.SETTING:

                if self.my_map.need_action:
                    self.my_map.set_ship()

                if self.player_map_pressed_flag:
                   # self.my_map.set_ship_pressed()
                    self.player_map_pressed_flag = False
                   #auto set plaer ships for test
                    self.my_map.cpu_set_ship()

            # after start
            elif self.state == GameState.PLAYING:
                if self.player_move:
                    # player move
                    self.msg_box.set("Your move")
                    if self.cpu_map_pressed_flag:
                        if not self.cpu_map.player_shoot():
                            self.player_move = False

                        if self.cpu_map.all_ships_destroyed:
                            self.win = True
                            self.state = GameState.END

                        self.cpu_map_pressed_flag = False
                else:
                    # cpu move
                    self.msg_box.set("cpu think")

                    if not self.my_map.cpu_shoot():
                        self.player_move = True

                    if self.my_map.all_ships_destroyed:
                        self.win = False
                        self.state = GameState.END
            elif self.state == GameState.END:
                if self.win:
                    self.msg_box.set("victory")
                else:
                    self.msg_box.set("defeat")

            # EVENTS HANDLING
            self.event()

            # DISPLAYING
            self.screen.fill((0, 0, 50))
            self.drawn()
            pygame.display.flip()

    # NECESSARY EVENTS
    def event(self):
        # EVENT HANDLING
        ev = pygame.event.poll()
        # print(type(event))
        if ev.type == pygame.QUIT:
            self.end()
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            self.end()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            self.ms_click(pygame.mouse.get_pos())

    # RENDERING HANDLING
    def drawn(self):
        self.start_button.draw()
        self.restart_button.draw()
        self.my_map.draw()
        self.cpu_map.draw(ships_hide=False)
        self.msg_box.draw()
        self.msg_box2.draw()

    # MOUSE CLICK HANDLING
    def ms_click(self, poss):
        #print(poss)
        if self.start_button.is_pressed(poss):
            self.start()
        elif self.restart_button.is_pressed(poss):
            self.restart()
        elif self.my_map.is_pressed(poss) and self.state == GameState.SETTING:  # ACTION WHEN PLAYER BOARD PRESSED
            self.player_map_pressed_flag = True
        elif self.cpu_map.is_pressed(poss)and self.state == GameState.PLAYING:      # ACTION WHEN CPU BOARD PRESSED
            self.cpu_map_pressed_flag = True

        # elif self.my_map.is_pressed(poss):
        #   self.my_map.pressed(poss)
        # elif self.cpu_map.is_pressed(poss):
        #    self.cpu_map.pressed(poss)

    # RESTART GAME
    def restart(self):
        size = self.screen.get_size()
        y = ((size[1]) - size[0] / 2) / 2
        self.my_map = Board((5, y, size[0] / 2 - 10, size[0] / 2 - 10), self.screen, self.msg_box)
        self.cpu_map = Board((size[0] / 2 + 5, y, size[0] / 2 - 10, size[0] / 2 - 10), self.screen, self.msg_box)
        self.state = GameState.SETTING
        self.msg_box2.set("Game restarted")

    # START GAME
    def start(self) :
        if self.my_map.ready and self.state == GameState.SETTING:
            self.state = GameState.PLAYING
            self.cpu_map.cpu_set_ship()
            self.msg_box2.set("Game started")
            pygame.time.wait(1000)
            self.player_move = bool(getrandbits(1))
            #print(self.player_move)
        elif not self.my_map.ready and self.state == GameState.SETTING:
            self.msg_box.set("Ustaw wszystkie okręty przed bitwą!!!")
        elif self.state == GameState.PLAYING:
            self.msg_box.set_tmp("Bitwa już trwa!!!",1000)

    # ENDING PROGRAM
    def end(self):
        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    Game()

'''
pygame.init()
window = pygame.display.set_mode((600,300))
myfont = pygame.font.SysFont("Arial",60)
label = myfont.render("Hello Pygame!", 1, (255,255,0))
window.blit(label,(100,100))
pygame.display.update()
time.sleep(5)
pygame.quit()
'''

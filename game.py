import pygame, sys
from random import getrandbits
from board import Board
from button import Button
from textbox import TextBox


class Game(object):
    def __init__(self):
        # INITIALIZATION
        pygame.init()
        self.screen = pygame.display.set_mode((800, 550))
        self.start_button = Button((10, 10, 100, 50), self.screen, "Start", 33)
        self.restart_button = Button((120, 10, 100, 50), self.screen, "Restart", 33)
        self.start_flag = False

        size = self.screen.get_size()
        self.msg_box = TextBox((0, size[1] - 60, size[0], 50), self.screen, "", 33)
        self.msg_box2 = TextBox((size[0] - 250, 0, 250, 50), self.screen, "xD", 33)
        self.player_move = True
        self.player_map_pressed_flag = False

        self.restart()
        # self.screen.blit(Button)

        # main loop
        while True:
            # after restart setting ships
            if not self.start_flag:
                if self.my_map.need_action:
                    self.my_map.set_ship()
                if self.player_map_pressed_flag:
                    self.my_map.set_ship_pressed()
                    self.player_map_pressed_flag = False

            # after start
            else:
                # player move
                if self.player_move:
                    self.msg_box.set("Your move")
                if self.player_map_pressed_flag:
                    if not self.my_map.player_shoot():
                        self.player_move = False
                    self.player_map_pressed_flag = False
                # cpu move
                else:
                    self.msg_box.set("cpu think")
                    if not self.cpu_map.cpu_shoot():
                        self.player_move = True

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
        self.cpu_map.draw(ships_hide=True)
        self.msg_box.draw()
        self.msg_box2.draw()

    # MOUSE CLICK HANDLING
    def ms_click(self, poss):
        #print(poss)
        if self.start_button.is_pressed(poss):
            self.start()
        elif self.restart_button.is_pressed(poss):
            self.restart()
        elif self.my_map.is_pressed(poss):  # ACTION WHEN PLAYER BOARD PRESSED
            self.player_map_pressed_flag = True
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
        self.start_flag = False
        self.msg_box2.set("Game restarted")

    # START GAME
    def start(self):
        if self.my_map.ready:
            self.start_flag = True
            self.cpu_map.cpu_set_ship()
            self.msg_box2.set("Game started")
            pygame.time.wait(1000)
            self.player_move = bool(getrandbits(1))
            #print(self.player_move)
        else:
            self.msg_box.set("Ustaw wszystkie okręty przed bitwą!!!")

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

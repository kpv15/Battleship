import pygame,  sys
from board import Board
from button import Button

class Game(object):
    def __init__(self):
        #INITIALIZATION
        pygame.init()
        size = (800,600)
        self.screen = pygame.display.set_mode(( 800, 500 ))
        self.start_button = Button((10,10,100,50),self.screen,"Start",33)
        self.restart_button = Button((120, 10, 100, 50), self.screen, "Restart",33)

        self.restart()
        #self.screen.blit(Button)

        #main loop
        while True:

            #HANDLING EVENT
            self.event()

            #DISPLAYING
            self.screen.fill((0,0,50))
            self.drawn()
            pygame.display.flip()

    def event(self):
        #EVENT HANDLING
        ev = pygame.event.poll()
        #print(type(event))
        if ev.type == pygame.QUIT:
            self.end()
        elif ev.type == pygame.KEYDOWN and ev.key == pygame.K_ESCAPE:
            self.end()
        elif ev.type == pygame.MOUSEBUTTONDOWN:
            self.ms_click(pygame.mouse.get_pos())

    #RENDERING HANDLING
    def drawn(self):
        self.start_button.draw()
        self.restart_button.draw()
        self.my_map.draw()
        self.cpu_map.draw()
        pass

    #MOUSE CLICK HANDLING
    def ms_click(self,poss):
        print(poss)
        if self.start_button.is_pressed(poss):
            self.start()
            print("start game")
        elif self.restart_button.is_pressed(poss):
            self.restart()
            print("restart game")
        elif self.my_map.is_pressed(poss):
            self.my_map.pressed(poss)
        elif self.cpu_map.is_pressed(poss):
            self.cpu_map.pressed(poss)

    #RESTART GAME
    def restart(self):
        size = self.screen.get_size()
        y = ((size[1]-70)-size[0]/2)/2+70
        self.my_map = Board((5,y,size[0]/2-10,size[0]/2-10),self.screen)
        self.cpu_map = Board((size[0]/2+5,y,size[0]/2-10,size[0]/2-10),self.screen)
        pass

    #START GAME
    def start(self):

        pass

    #ENDING PROGRAM
    def end(self):
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    Game()
    while True:
        pass


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
import pygame,  sys
from board import Board
from button import Button

class Game(object):
    def __init__(self):
        #INITIALIZATION
        pygame.init()
        self.TPS = 20.0
        self.screen = pygame.display.set_mode(( 800, 600 ))
        self.delta = 0.0
        self.clock = pygame.time.Clock()
        self.my_map = Board()
        self.cpu_map = Board()
        self.start_button = Button((5,5,80,40),self.screen,"Start",29)
        self.restart_button = Button((100, 5, 80, 40), self.screen, "Restart",29)
        #self.screen.blit(Button)

        #main loop
        while True:
            self.event()

            self.delta += self.clock.tick()
            while self.delta > self.TPS :
                self.delta -= self.TPS
                self.tick()

            self.screen.fill((0,0,0))
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

    #TICKING HANDLING
    def tick(self):
        pass

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
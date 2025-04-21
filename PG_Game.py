import tkinter as tk

import pygame

from ghosts import Ghost
from player import Player


class Game:
    def __init__(self, windowtext="Pac-Man Game"):
        self.size = (800, 600)
        self.running = True
        pygame.init()
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0,0,0))
        self.clock = pygame.time.Clock()
        self.player = Player(self.size)
        self.ghost = Ghost(self.size)
        self.root = tk.Tk()
        self.root.minsize(width=300, height=150)
        self.root.maxsize(width=100, height=200)
        self.root.title(windowtext)
        self.textbox = tk.StringVar()

    def game_menu(self):
        self.menubutton = tk.Menubutton(self.root, text="Welcome Player Choose Your Game Level!")
        self.menu = tk.Menu(self.menubutton, tearoff=0)
        self.menubutton["menu"] = self.menu
        self.menubutton.pack()


    def create_button(self):
        self.buttonEasy = tk.Button(self.root, text="Easy", command=self.run)
        self.buttonEasy.pack()

        '''
        self.buttonMedium = tk.Button(self.root, text="Medium", command=self.run)
        self.buttonMedium.pack()

        self.buttonHard = tk.Button(self.root, text="Hard", command=self.run)
        self.buttonHard.pack()
        '''

    def run(self):

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            if pygame.sprite.spritecollide(self.player, [self.ghost], False):
                font = pygame.font.SysFont("comicsans", 20)
                txt = font.render("GAME OVER", True, ("red"))
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            else:
                self.player.movement(pygame.key.get_pressed())
                self.ghost.movement()
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.player.surf, self.player.rect)
                self.screen.blit(self.ghost.surf, self.ghost.rect)
            pygame.display.update()
            self.clock.tick(24)

        pygame.quit()


def main():
    myGUI = Game()
    myGUI.game_menu()
    myGUI.create_button()

    myGUI.root.mainloop()

if __name__ == "__main__":
    main()
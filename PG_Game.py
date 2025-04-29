import tkinter as tk

import pygame

# from ghosts import Ghost
from player import Player
from New_File_Ghosts import red
from New_File_Ghosts import lime
from New_File_Ghosts import purple


class Game:
    def __init__(self, windowtext="Pac-Man Game"):
        self.clock = pygame.time.Clock()
        self.root = tk.Tk()
        self.root.minsize(width=300, height=150)
        self.root.maxsize(width=100, height=200)
        self.root.title(windowtext)
        self.textbox = tk.StringVar()
        self.start = False
        self.remaining_time = 120
        self.timer_text = str(self.remaining_time).rjust(3)


    def game_menu(self):
        self.menubutton = tk.Menubutton(self.root, text="Welcome Player Click Ready to Start!")
        self.menu = tk.Menu(self.menubutton, tearoff=0)
        self.menubutton["menu"] = self.menu
        self.menubutton.pack()


    def create_button(self):
        self.buttonEasy = tk.Button(self.root, text="Ready", command=self.run)
        self.buttonEasy.pack()



    def run(self):
        self.game_started =True
        pygame.font.init()
        pygame.init()
        pygame.time.set_timer(pygame.USEREVENT, 1000)
        self.font = pygame.font.SysFont("Ariel", 40)
        self.size = (800, 600)
        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0, 0, 0))
        self.player = Player(self.size)
        self.redghost = red(self.size)
        self.limeghost = lime(self.size)
        self.purpleghost = purple(self.size)

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.USEREVENT and self.game_started:
                    self.remaining_time -= 1
                    self.timer_text = str(self.remaining_time).rjust(3) if self.remaining_time > 0 else "Time's Up"
                    if self.remaining_time <= 0:
                        self.game_started = False
                        font =pygame.font.SysFont("Ariel", 20)
                        txt_surface = font.render("Time's Up! You Won!", True, ("Red"))
                        txt_rect = txt_surface.get_rect(center=(self.size[0]/2, self.size[1]/2))
                        pygame.display.flip()
                        pygame.time.delay(500)
                        self.running = False

            if pygame.sprite.collide_rect(self.player, self.redghost):
                font = pygame.font.SysFont("comicsans", 20)
                txt = font.render("GAME OVER", True, ("red"))
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            elif pygame.sprite.collide_rect(self.player, self.limeghost):
                font = pygame.font.SysFont("comicsans", 20)
                txt = font.render("GAME OVER", True, ("red"))
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            elif pygame.sprite.collide_rect(self.player, self.purpleghost):
                font = pygame.font.SysFont("comicsans", 20)
                txt = font.render("GAME OVER", True, ("red"))
                self.screen.blit(txt, (self.size[0]//2, self.size[1]-100))
            else:
                self.player.movement(pygame.key.get_pressed())
                self.redghost.movement(screen_size=self.size)
                self.limeghost.movement(screen_size=self.size)
                self.purpleghost.movement(screen_size=self.size)
                self.screen.fill((0, 0, 0))
                self.screen.blit(self.player.surf, self.player.rect)
                self.screen.blit(self.redghost.surf, self.redghost.rect)
                self.screen.blit(self.limeghost.surf, self.limeghost.rect)
                self.screen.blit(self.purpleghost.surf, self.purpleghost.rect)

            timer_display = self.font.render(self.timer_text, True, (255, 255, 255))
            self.screen.blit(timer_display, (10, 10))
            pygame.display.update()
            self.clock.tick(24)
            exitonclick()

        pygame.quit()


def main():
    myGUI = Game()
    myGUI.game_menu()
    myGUI.create_button()

    myGUI.root.mainloop()

if __name__ == "__main__":
    main()
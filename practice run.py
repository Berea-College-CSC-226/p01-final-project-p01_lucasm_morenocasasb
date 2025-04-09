import pygame
from player import Player
from ghosts import NPC

class Game:
    def __init__(self):
        self.size = (1000, 1000)
        self.running = True
        self.screen = pygame.display.set_mode(self.size)
        self.screen.fill((0, 0, 0))
        self.clock = pygame.time.Clock()
        self.player = Player(self.size)
        self.ghost = NPC(self.size)


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
    game = Game()
    game.run()
if __name__ == "__main__":
    main()
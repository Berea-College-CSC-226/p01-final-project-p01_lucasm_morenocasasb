import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, screen_size):
        """
        Gamer can play as the player (in this case, Pacman)

        :param screen_size: The size of the screen of the game
        """
        super().__init__()
        self.screen_size = screen_size
        print("Spawning player")
        self.surf = pygame.image.load('image/pacman.png').convert_alpha()
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.screen_size[0]//2, self.screen_size[1]//2)


    def movement(self, keys):
        """
        Gamer can use the arrow keys (up, down, left, right) to move the player

        :param keys: up, down, right, left arrow keys
        """
        if keys[pygame.K_UP]:
            self.rect.move_ip(0, -3)
        elif keys[pygame.K_DOWN]:
            self.rect.move_ip(0, 3)
        if keys[pygame.K_RIGHT]:
            self.rect.move_ip(3, 0)
        elif keys[pygame.K_LEFT]:
            self.rect.move_ip(-3, 0)
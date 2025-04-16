import pygame, random


class NPC(pygame.sprite.Sprite):
    move_distance = random.randrange(1, 15)

    def __init__(self, screen_size):
        """
        The size of the screen, kind of like a boundary

        :param screen_size: Ghosts should be inside the screen at all times
        """
        super().__init__()
        self.surf = None
        self.vertical_step = 20
        self.horizontal_direction = 1
        self.screen_size = screen_size
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.path = None

    def movement(self):
        self.rect.move_ip(self.horizontal_direction * self.move_distance, 0)
        if self.rect.right >= self.screen_size[0]:
            self.rect.right = self.screen_size[0]
            self.horizontal_direction = -1
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.rect.move_ip(0, self.vertical_step)
            self.horizontal_direction = 1


class Ghost(NPC):
    def __init__(self, screen_size):
        super().__init__(screen_size)
        self.surf = pygame.surface.Surface

    def get_direction(self):
        """
        Keeps the ghosts inside

        :return: None
        """
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "north"
        if self.rect.top <= 0:
            self.path = "south"
        if self.rect.left <= 0:
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            self.path = "west"

    def ghost1(self, screen_size=None):
        super().__init__(screen_size)
        self.surf = pygame.image.load("image/Purple Ghost.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.move_ip(screen_size[0] // 4, screen_size[1] // 4)
        self.movement()
    
    def ghost2(self, screen_size=None):
        super().__init__(screen_size)
        self.surf = pygame.image.load("image/Lime Ghost.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.move_ip(screen_size[0] // 4, screen_size[1] // 4)
        self.movement()
    
    def ghost3(self, screen_size=None):
        super().__init__(screen_size)
        self.surf = pygame.image.load("image/Red Ghost.png").convert_alpha()
        self.rect = self.surf.get_rect()
        self.rect.move_ip(screen_size[0] // 4, screen_size[1] // 4)
        self.movement()
import pygame
import random


class NPC(pygame.sprite.Sprite):
    move_distance = random.randrange(1,15)

    def __init__(self, screen_size):
        """
        Size of the screen

        :param screen_size: The ghosts should be kept inside the screen
        """
        super().__init__(screen_size)
        self.path = None
        self.surf = None
        self.screen_size = screen_size
        self.surf = pygame.Surface(screen_size)
        self.rect = pygame.Rect(screen_size)
        self.rect = self.surf.get_rect()

    def get_direction(self):
        """
        Keeps the ghosts inside

        :return: None
        """
        if self.rect.bottom >= self.screen_size[1]:
            self.path = "north"
        if self.rect.top >= 0:
            self.path = "south"
        if self.rect.left <= 0:
            self.path = "east"
        if self.rect.right >= self.screen_size[0]:
            self.path = "west"


class red:
    direction = ["north", "south", "east", "west"]
    
    def __init__(self, screen_size):
        self.screen_size = None
        self.horizontal_direction = 1
        self.move_distance = 35
        self.surf = pygame.transform.scale(pygame.image.load("image/Red Ghost.png").convert_alpha(), (50, 50))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()
        
    def movement(self, screen_size):
        self.rect.move_ip(self.horizontal_direction * self.move_distance, 0)
        if self.rect.right >= 0:
            self.rect.right = 0
            self.horizontal_direction = -1
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.rect.move_ip(0, 20)
            self.horizontal_direction = 1


class lime:
    direction = ["north", "south", "east", "west"]

    def __init__(self, screen_size):
        self.screen_size = None
        self.horizontal_direction = 1
        self.move_distance = 16
        self.surf = pygame.transform.scale(pygame.image.load("image/Lime Ghost.png").convert_alpha(), (50, 50))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    def movement(self, screen_size):
        self.rect.move_ip(self.horizontal_direction * self.move_distance, 0)
        if self.rect.right >= 0:
            self.rect.right = 0
            self.horizontal_direction = -1
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.rect.move_ip(0, 20)
            self.horizontal_direction = 1


class purple:
    direction = ["north", "south", "east", "west"]

    def __init__(self, screen_size):
        self.screen_size = None
        self.horizontal_direction = 1
        self.move_distance = 47
        self.surf = pygame.transform.scale(pygame.image.load("image/Purple Ghost.png").convert_alpha(), (50, 50))
        self.surf.set_colorkey((255, 255, 255), pygame.RLEACCEL)
        self.rect = self.surf.get_rect()

    def movement(self, screen_size):
        self.rect.move_ip(self.horizontal_direction * self.move_distance, 0)
        if self.rect.right >= 0:
            self.rect.right = 0
            self.horizontal_direction = -1
        elif self.rect.left <= 0:
            self.rect.left = 0
            self.rect.move_ip(0, 20)
            self.horizontal_direction = 1
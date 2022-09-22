import pygame
black = (0,0,0)
WEAPON_IMG = pygame.image.load('img/firearm.png')
WINHEIGHT = 768

class Bullet:
    def __init__(self):
        self.radius = 4
        self.color = black
        self.x = WEAPON_IMG.get_width() / 2 + 23
        self.y = WINHEIGHT / 2 - WEAPON_IMG.get_height()/2 + 23
        self.YAXIS = self.y
        self.XAXIS = self.x
        self.vel = 10
        self.mouse_x , self.mouse_y = pygame.mouse.get_pos()
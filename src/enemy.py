import pygame
import random

red = (255,0,0)
green = (0 , 200 , 0)
class Enemy:
    def __init__(self,WINWIDTH,WINHEIGHT):
        self.img = pygame.image.load('img/zombie.png')
        self.rect = pygame.Rect(random.randint(WINWIDTH, WINWIDTH * 1.25), random.randint(0, WINHEIGHT - 64), 64, 64)
        self.hitbox = pygame.Rect(self.rect.x + 20 , self.rect.y , self.rect.width - 40 , self.rect.height)
        self.healthbar = pygame.Rect(self.rect.x - 10, self.rect.y - 25, 90, 10)
        self.health = 3
        self.vel = 4

    def move(self):
        self.rect.x -= self.vel
        self.healthbar.x -= self.vel
        self.hitbox.x -= self.vel

    def draw(self,win):
        self.move()
        win.blit(self.img , self.rect)
        #pygame.draw.rect(win, (0,0,0), self.hitbox , 1)
        pygame.draw.rect(win, red, self.healthbar)
        pygame.draw.rect(win, green, (self.healthbar.x , self.healthbar.y , self.healthbar.width - ((3 - self.health) * 30) , self.healthbar.height))

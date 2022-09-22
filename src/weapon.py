import pygame
import math
import time

from bullet import Bullet
black = (0,0,0)

class Weapon:
    def __init__(self,WINWIDTH,WINHEIGHT):
        self.img = pygame.image.load('img/firearm.png')
        self.x = 0
        self.y = WINHEIGHT / 2 - self.img.get_height()/2
        self.radian = 0
        self.bullets = []
        self.fire = True
        self.WINWIDTH = WINWIDTH
        self.WINHEIGHT = WINHEIGHT
        self.score = 0

    def move(self):
        mouse_x , mouse_y = pygame.mouse.get_pos()
        self.radian = math.asin((self.y - mouse_y) / math.sqrt(math.pow(abs(self.y - mouse_y), 2) + math.pow(abs(mouse_x - self.img.get_width() / 2) , 2)))

    def rotate_weapon(self,win,img,topleft,radian):
        self.move()
        rotated_weapon = pygame.transform.rotate(img, math.degrees(radian))
        new_rect = rotated_weapon.get_rect(center=img.get_rect(topleft=topleft).center)
        win.blit(rotated_weapon,new_rect.topleft)

    def fire_weapon(self):
        if pygame.mouse.get_pressed()[0] and self.fire == True:
            self.bullets.append(Bullet())
            self.fire = False

    def move_bullet(self,bullet):

        radian = math.asin((bullet.YAXIS - bullet.mouse_y) / math.sqrt(math.pow(bullet.YAXIS - bullet.mouse_y, 2) + math.pow(bullet.mouse_x - bullet.XAXIS, 2)))

        if bullet.x < self.WINWIDTH and bullet.y > 0 and bullet.y < self.WINHEIGHT:
            vertical = math.sin(radian) * bullet.vel
            horizontal = math.cos(radian) * bullet.vel

            bullet.x += horizontal
            bullet.y -= vertical

        else:
            index = self.bullets.index(bullet)
            self.bullets.pop(index)
    
    def draw_bullet(self,win):
        for bullet in self.bullets:
            self.move_bullet(bullet)
            pygame.draw.circle(win, black, (bullet.x, bullet.y), bullet.radius)

    def draw(self,win):
        self.rotate_weapon(win, self.img, (self.x , self.y), self.radian)

    def set_fire(self):
        while True:
            if not self.fire:
                time.sleep(0.1)
                self.fire = True 
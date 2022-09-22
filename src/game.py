import pygame
import math
import time
import threading
from weapon import Weapon
from enemy import Enemy

pygame.init()
WINWIDTH = 1024
WINHEIGHT = 768
TITLE = "Fire"
WIN = pygame.display.set_mode((WINWIDTH,WINHEIGHT))
pygame.display.set_caption(TITLE)

clock = pygame.time.Clock()
white = (255,255,255)
black = (0,0,0)
grey = (105,105,105)

enemies = []

run = True

font = pygame.font.SysFont('Arial', 23, True)

def reDrawWindow():
    WIN.fill(grey)
    weapon.draw(WIN)
    for enemy in enemies:
        enemy.draw(WIN)
    weapon.fire_weapon()
    weapon.draw_bullet(WIN)
    score_text = font.render('Score: ' + str(weapon.score), 1, black)
    WIN.blit(score_text , (0 , 740))

    pygame.display.update()


weapon = Weapon(WINWIDTH,WINHEIGHT)

fire_thread = threading.Thread(target=weapon.set_fire)
fire_thread.daemon = True
fire_thread.start()
while run:
    clock.tick(60)
    if len(enemies) < 4:
        enemies.append(Enemy(WINWIDTH,WINHEIGHT))

    for enemy in enemies: 
        for bullet in weapon.bullets:
            if bullet.x > enemy.hitbox[0] and bullet.x < (enemy.hitbox[0] + enemy.hitbox[2]) and bullet.y > enemy.hitbox[1] and bullet.y < (enemy.hitbox[1] + enemy.hitbox[3]):
                index = weapon.bullets.index(bullet)
                weapon.bullets.pop(index)
                if enemy.health == 1:
                    enemy_index = enemies.index(enemy)
                    enemies.pop(enemy_index)
                    weapon.score += 1
                else:
                    enemy.health -= 1
        for enemy in enemies:
            if enemy.rect.x + enemy.rect.width <= 0:
                index = enemies.index(enemy)
                enemies.pop(index) 
    reDrawWindow()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()


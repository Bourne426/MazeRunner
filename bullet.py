import pygame
import random
from variables import *

class Bullet(pygame.sprite.Sprite):
    """ This class represent the fired bullets by the player """
    def __init__(self, x, y, direction):
        super(Bullet,self).__init__()
        self.image = pygame.image.load(bullet_img)
        self.rect = self.image.get_rect()
        self.rect.y = y; self.starty = y
        self.rect.x = x; self.startx = x
        self.curr_dir = direction
        self.life = 200
        
    def update(self, walls ,enemy ,player):
        """ Function to update the position of bullets """
        if self.curr_dir == "RIGHT":
            self.rect.x += 10
        elif self.curr_dir == "LEFT":
            self.rect.x -=10
        elif self.curr_dir == "UP":
            self.rect.y -= 10
        elif self.curr_dir == "DOWN":
            self.rect.y +=10
        
        # Check for any hit with wall ( if its a hit then kill bullet )         
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        if block_hit_list:
            self.kill()
            
        # Check for any hit with enemy ( if its a hit then kill bullet as well as enemy )
        enemy_hit_list = pygame.sprite.spritecollide(self,enemy,False)
        for block in enemy_hit_list:
            block.kill()
            self.kill()
            player.points+=50
            
        # Check for total life of bullet ( if its more then assigned life -> self kill )    
        if abs(self.rect.x - self.startx) > self.life: self.kill()
        if abs(self.rect.y - self.starty) > self.life: self.kill()

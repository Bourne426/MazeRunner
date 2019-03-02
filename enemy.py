import pygame
import random
from variables import *

class Enemy(pygame.sprite.Sprite):
    """ This class represent the enemy sprites """
    # Images for different directions
    down = enemy_down_img
    up = enemy_up_img
    left = enemy_left_img
    right = enemy_right_img
    
    # Directional image counter
    d_c = 0
    u_c = 0
    r_c = 0
    l_c = 0
	
    # Speed vector
    change_x = 0
    change_y = 0
    curr_dir=""
    
    def __init__(self, x, y):
        super(Enemy,self).__init__()
        # Creating the image object
        self.image = pygame.image.load(self.right[self.r_c])
 
        # Assigning the positions and dimensions to the block and giving it a random direction to start with
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.curr_dir = random.choice(direction)
        
    def changespeed(self):
        """ Change the speed of the Enemy. Called with a keypress. """
        if self.curr_dir == "LEFT":
            self.change_x = -4
        if self.curr_dir == "RIGHT":
            self.change_x = 4
        if self.curr_dir == "UP":
            self.change_y =-4
        if self.curr_dir == "DOWN":
            self.change_y = 4 
            

    def move(self, walls):
        """ Find its new position and state """
        if  self.curr_dir =="RIGHT":
            self.r_c+=1
            if self.r_c == 12:
                self.r_c = 0
            self.image = pygame.image.load(self.right[self.r_c])
            
        if  self.curr_dir =="LEFT":
            self.l_c+=1
            if self.l_c == 12:
                self.l_c = 0
            self.image = pygame.image.load(self.left[self.l_c])
            
        if  self.curr_dir =="DOWN":
            self.d_c+=1
            if self.d_c == 12:
                self.d_c = 0
            self.image = pygame.image.load(self.down[self.d_c])
           
        if  self.curr_dir =="UP":
            self.u_c+=1
            if self.u_c == 12:
                self.u_c = 0
            self.image = pygame.image.load(self.up[self.u_c])

        # Move left/right and check if hit any wall or not
        self.rect.x += self.change_x
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                self.rect.left = block.rect.right
            self.change_x = 0
            # Change direction after every hit
            self.curr_dir = random.choice(direction)
         
        # Move up/down and check if hit any wall or not
        self.rect.y += self.change_y
 
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
            self.change_y =0
            # Change direction after every hit
            self.curr_dir = random.choice(direction)

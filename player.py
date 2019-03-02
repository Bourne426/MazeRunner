import pygame
from variables import *

class Player(pygame.sprite.Sprite):
    """ This class represents the sprite that the player controls """
    #image list of player
    down = player_down_img
    up = player_up_img
    left = player_left_img
    right = player_right_img
    
    # Set speed vector
    change_x = 0
    change_y = 0
    
    #Set direction image counter
    d_c = 0
    u_c = 0
    r_c = 0
    l_c = 0
    prev_dir=""
    
    #Set score
    points = 0
    
    #set live
    lives=3
    dead= False
    won = False
    invincible = False
 
    def __init__(self, x, y):
        """ Constructor function """
        # Call the parent's constructor
        super(Player,self).__init__()
        self.image = pygame.image.load(self.right[1])
 
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
        self.prev_dir = "DOWN"
 
    def changespeed(self, x, y ,direc):
        """ Change the speed of the player. Called with a keypress. """
        self.change_x += x
        self.change_y += y
        if x > 0 and direc == "RIGHT":
            self.prev_dir="RIGHT"
        if x < 0 and direc == "LEFT":
            self.prev_dir="LEFT"
        if y > 0 and direc == "DOWN":
            self.prev_dir="DOWN"
        if y < 0 and direc == "UP":
            self.prev_dir="UP"
        
    def move(self, walls, enemys, treasure):
        """ Find a new position and state of the player """
        if  self.prev_dir =="RIGHT":
            if self.change_x == 0:
                self.image = pygame.image.load(self.right[4])
            else:
                self.r_c+=1
                if self.r_c == 12:
                    self.r_c = 0
                self.image = pygame.image.load(self.right[self.r_c])
            
        if  self.prev_dir =="LEFT":
            if self.change_x == 0:
                self.image = pygame.image.load(self.left[4])
            else:
                self.l_c+=1
                if self.l_c == 12:
                    self.l_c = 0
                self.image = pygame.image.load(self.left[self.l_c])
            
        if  self.prev_dir =="DOWN":
            if self.change_y == 0:
                self.image = pygame.image.load(self.down[4])
            else:
                self.d_c+=1
                if self.d_c == 12:
                    self.d_c = 0
                self.image = pygame.image.load(self.down[self.d_c])
           
        if  self.prev_dir =="UP":
            if self.change_y == 0:
                self.image = pygame.image.load(self.up[4])
            else:
                self.u_c+=1
                if self.u_c == 12:
                    self.u_c = 0
                self.image = pygame.image.load(self.up[self.u_c])
 
        # Move left/right
        self.rect.x += self.change_x
 
        # Did this update cause us to hit a wall?
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
            # If we are moving right, set our right side to the left side of the item we hit
            if self.change_x > 0:
                self.rect.right = block.rect.left
            else:
                # Otherwise if we are moving left, do the opposite.
                self.rect.left = block.rect.right
                
         

        # Move up/down
        self.rect.y += self.change_y
        
        # Check and see if we hit anything
        block_hit_list = pygame.sprite.spritecollide(self, walls, False)
        for block in block_hit_list:
 
            # Reset our position based on the top/bottom of the object.
            if self.change_y > 0:
                self.rect.bottom = block.rect.top
            else:
                self.rect.top = block.rect.bottom
            
        # Check for any hit with enemy        
        enemy_hit = pygame.sprite.spritecollide(self, enemys, False)
        for block in enemy_hit:
            if self.lives and not self.invincible :
                self.lives -=1

        	
        # Check to collect treasures
        treasure_hit = pygame.sprite.spritecollide(self, treasure , False)
        for block in treasure_hit:
                pygame.mixer.Channel(1).play(pygame.mixer.Sound('./data/coin.ogg'))
                pygame.mixer.Channel(1).set_volume(1)
                treasure.remove(block)
                self.points+=100


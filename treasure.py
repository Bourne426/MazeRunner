import pygame
from variables import *

class Treasure(pygame.sprite.Sprite):
    """ A class for the treasures on the way to escape """
    img=treasure_img
    curr=0
    
    # Calling constructors
    def __init__(self, x, y):
        super(Treasure,self).__init__()
        # Creating the image object
        self.image = pygame.image.load(self.img[self.curr])

        # Assigning the positions and dimensions to the block
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
     
    def animate(self):
        """ Function to provide animation look """
        # Updating different image repeatedly 
        self.curr+=1
        if self.curr == 9:
            self.curr=0
        self.image = pygame.image.load(self.img[self.curr])

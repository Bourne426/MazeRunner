import pygame
from variables import *
class Wall(pygame.sprite.Sprite):
    """ A class for each and every block of complete maze """
    # Calling constructor
    def __init__(self, x, y):
        super(Wall,self).__init__()
        
        # Creating the image object
        self.image = pygame.image.load(wall_img)

        # Assigning the positions and dimensions to the block
        self.rect = self.image.get_rect()
        self.rect.y = y
        self.rect.x = x
    

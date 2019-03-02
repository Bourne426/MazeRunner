import pygame
import os
    
def getPlayerName(screen):
    """Function to get the name of player"""
    pygame.mixer.music.load('./data/my_intro.ogg') 
    pygame.mixer.music.play(-1,)
    pygame.mixer.music.set_volume(1)

    name = ""
    #font = pygame.font.Font("./data/fonts/freesansbold.ttf", 12)
    font = pygame.font.SysFont("purisa", 50 )
    #font = pygame.font.Font(None, 50)
    text = "Enter player name :"
    text_block = font.render(text, True, (255, 67, 100))
    text_rect = text_block.get_rect()
    text_rect.centerx=screen.get_rect().centerx
    text_rect.centery=screen.get_rect().centery - 70
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.unicode.isalpha():
                    name += event.unicode
                elif event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                elif event.key == pygame.K_RETURN:
                    pygame.mixer.music.stop()
                    com = "espeak 'Hi! '"+name+"'. Welcome to Maze Runner'"
                    os.system(com)
                    return name
            elif event.type == pygame.QUIT:
                return
        screen.fill((0, 0, 0))
        name_block = font.render(name, True, (255, 20, 255))
        name_rect = name_block.get_rect()
        name_rect.center = screen.get_rect().center
        screen.blit(text_block, text_rect)
        screen.blit(name_block, name_rect)
        pygame.display.flip()
	

import pygame
import random
import time

from player import Player
from treasure import Treasure
from enemy import Enemy
from wall import Wall
from bullet import Bullet
from level import Level
from variables import *
from playername import *
      
def getMaze(level,room):
    """ A function to read the maze from level file and create different objects. """
    for x in range(len(level)):
        for y in range(len(level[x])):
            char = level[x][y]
            s_x=35+y*25
            s_y=35+x*25
            if char == "X":
                room.wall_list.add(Wall(s_x,s_y))  
            elif char == "E":
                room.enemy_sprites.add(Enemy(s_x,s_y))
            elif char == "P":
                player = Player(s_x, s_y)
            elif char == "T":
                room.treasure_list.add(Treasure(s_x,s_y))
            elif char == "G":
                goal = Wall(s_x,s_y)
    return (player , goal)    


def game(screen, room, level, lvl ,pName ,hScore):
    """The main gameplay """
    
    pygame.display.set_caption('Maze Runner')

    font = pygame.font.SysFont("Tlwg Typewriter", 18)

    gameoverfont = winfont = pygame.font.SysFont("Kinnari", 100)
    
    gameovertext = gameoverfont.render('Game Over',1, (250,242,15))
    gameoverrect = gameovertext.get_rect()
    gameoverrect.centerx =screen.get_rect().centerx; gameoverrect.centery =screen.get_rect().centery
    
    wintext = winfont.render('Level Completed', 1,(250,242,15))
    winrect = wintext.get_rect()
    winrect.centerx = screen.get_rect().centerx; winrect.centery =screen.get_rect().centery
    
    
    point = font.render('Score: 0', 1, (156,250,15))
    pointRect = point.get_rect()
    pointRect.x = 0; pointRect.y = 0
    
    player,goal =getMaze(level,room)
    
    lives = int(player.lives); livestext = font.render('Lives: %s' % str(player.lives), 1, (156,250,15))
    livesrect = livestext.get_rect()
    livesrect.x = screen.get_width()-livesrect.width
    livesrect.y = 0
    
    level_text = font.render('Level: %s' % str(lvl[0]+1), 1, (156,250,15))
    levelrect = level_text.get_rect()
    levelrect.centerx = screen.get_width()/2
    levelrect.y = 0
    
    clock = pygame.time.Clock()
    gamePause = False
    starttime = int(time.time())
    
    gameovercount = 0; gameoverdelay = 90
    wincount = 0; windelay = 90
    invinciblecount = 0; invincibledelay = 20; invincibleon = False
	
    


    # Adding player to sprite group and creating a group of bullets
    movingsprites = pygame.sprite.Group()
    movingsprites.add(player)
    bullets = pygame.sprite.Group()
    
    done = False
    pygame.mixer.music.load('./data/background_music.ogg') 
    pygame.mixer.music.play(-1,)
    pygame.mixer.music.set_volume(0.5)
    screen.blit(point, pointRect)
    screen.blit(livestext, livesrect)
 
    # --- The Game loop --- 
    while not done:
        screen.fill(BLACK)
        if not gamePause:
            if int(abs(time.time() - starttime)) > 0 :
                starttime += 1
                if player.points >0 : player.points -= 1    
        point = font.render('Score: '+str(player.points)+" ({0}[{1}])".format(hScore[lvl[0]][1], hScore[lvl[0]][0]), 1,(156,250,15))

        def toggleMusic():
            if gamePause:
                pygame.mixer.music.pause()
            else:
                pygame.mixer.music.unpause()


        # --- Event Processing ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN :
                if event.key == pygame.K_LEFT:
                    player.changespeed(-5, 0, "LEFT")
                if event.key == pygame.K_RIGHT:
                    player.changespeed(5, 0, "RIGHT")
                if event.key == pygame.K_UP:
                    player.changespeed(0, -5, "UP")
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, 5, "DOWN")
                if event.key == pygame.K_SPACE and not gamePause:
                    if len(bullets) < 3 :
                        bullets.add(Bullet(player.rect.x , player.rect.y + 10, player.prev_dir))
                        pygame.mixer.Channel(0).play(pygame.mixer.Sound('./data/gun.ogg'))
                        pygame.mixer.Channel(0).set_volume(0.5)
                if event.key == pygame.K_p:
                    gamePause = not gamePause
                    toggleMusic()
 
            if event.type == pygame.KEYUP :
                if event.key == pygame.K_LEFT:
                    player.changespeed(5, 0, "LEFT")
                if event.key == pygame.K_RIGHT:
                    player.changespeed(-5, 0, "RIGHT")
                if event.key == pygame.K_UP:
                    player.changespeed(0, 5, "UP")
                if event.key == pygame.K_DOWN:
                    player.changespeed(0, -5, "DOWN")
 
        # --- Game Logic ---
        if not gamePause:
            player.move(room.wall_list,room.enemy_sprites,room.treasure_list )

            if invinciblecount > 0: invinciblecount -= 1
            if player.invincible: invincibleon = not invincibleon
            if invinciblecount == 0: player.invincible = False
            
            for group in room.enemy_sprites:
                group.changespeed()
                group.move(room.wall_list)
               
            for treasure in room.treasure_list:
                treasure.animate()
                
            for bull in bullets:
                bull.update(room.wall_list, room.enemy_sprites, player)
        
            if lives > player.lives and player.lives >= 0:
                lives = player.lives
                livestext = font.render('Lives: %s' % str(player.lives), 1,(156,250,15))
                player.invincible = True
                invinciblecount = invincibledelay
            
            if player.lives == 0 and (not player.dead):
                gameovercount = gameoverdelay
                gamePause = True
                player.dead = True
                pygame.mixer.music.pause()
                pygame.mixer.music.load('./data/gameover.ogg')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                
            if pygame.sprite.collide_rect(player, goal) and ( not player.won ):
                wincount = windelay
                gamePause = True
                player.won=True
                pygame.mixer.music.pause()
                pygame.mixer.music.load('./data/won.ogg')
                pygame.mixer.music.play()
                pygame.mixer.music.set_volume(1)
                if player.points > int(hScore[lvl[0]][1]):
                    hScore[lvl[0]][0] = pName
                    hScore[lvl[0]][1] = str(player.points)
                    
        if gameovercount > 0: gameovercount -= 1
        if gameovercount == 0 and player.dead:
            pygame.sprite.Group.empty(room.wall_list)
            pygame.sprite.Group.empty(room.enemy_sprites)
            pygame.sprite.Group.empty(room.treasure_list)
            player.kill()
            lvl[0]-=1
            return True
        if wincount > 0: wincount -= 1
        if wincount == 0 and player.won:
            pygame.sprite.Group.empty(room.wall_list)
            pygame.sprite.Group.empty(room.enemy_sprites)
            pygame.sprite.Group.empty(room.treasure_list)
            player.kill()
            return True        

        # --- Drawing ---
        if not player.invincible and not player.dead : movingsprites.draw(screen)
        if player.invincible and invincibleon and not player.dead: movingsprites.draw(screen)
        room.wall_list.draw(screen)
        room.enemy_sprites.draw(screen)
        room.treasure_list.draw(screen)
        bullets.draw(screen)
        screen.blit(point, pointRect)
        screen.blit(livestext, livesrect)
        screen.blit(level_text, levelrect)
        if player.won:
            screen.blit(wintext, winrect)
        if player.dead:
            screen.blit(gameovertext, gameoverrect)
        pygame.display.flip()
        clock.tick(20)
    return False

def main():
    """ Main Program """
    # Initialising Pygame library 
    pygame.init()
    pygame.mixer.init()
    screen = pygame.display.set_mode([700, 700])

    # Taking player name as input
    pName = getPlayerName(screen)
    if not pName : return


    # Reading high scores from file
    hScore = []
    with open("./data/file.txt","r") as f:
        for line in f:
            line = line.strip()
            hScore.append(line.split())


    # Creating level object and calling it's different levels in loop
    room = Level()
    i=[0]
    while i[0] < len(room.maze):
        if not game(screen,room, room.maze[i[0]], i ,pName ,hScore) : break
        i[0]+=1

    # Before exiting updating high scores back in the file
    with open("./data/file.txt","w") as f:
        for i in range(len(room.maze)):
            f.write(" ".join(hScore[i]) + "\n")

    pygame.quit()
if __name__ == "__main__":
    main()

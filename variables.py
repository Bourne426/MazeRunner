import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)
GOLD = (255,223,0)


direction=["UP","DOWN","LEFT","RIGHT"]

wall_img = "./data/wall.png"

bullet_img = "./data/bullet.png"

treasure_img = ["./data/treasure/gc1.png","./data/treasure/gc2.png","./data/treasure/gc3.png","./data/treasure/gc4.png","./data/treasure/gc5.png","./data/treasure/gc6.png","./data/treasure/gc7.png","./data/treasure/gc8.png","./data/treasure/gc9.png"] 

player_down_img = ["./data/player/f0.png","./data/player/f0.png","./data/player/f1.png","./data/player/f1.png","./data/player//f2.png","./data/player//f2.png","./data/player//f3.png","./data/player//f3.png","./data/player//f4.png","./data/player//f4.png","./data/player//f5.png","./data/player//f5.png"]
player_up_img = ["./data/player//b0.png","./data/player//b0.png","./data/player//b1.png","./data/player//b1.png","./data/player//b2.png","./data/player//b2.png","./data/player//b3.png","./data/player//b3.png","./data/player//b4.png","./data/player//b4.png","./data/player//b5.png","./data/player//b5.png"]
player_left_img = ["./data/player//l0.png","./data/player//l0.png","./data/player//l1.png","./data/player//l1.png","./data/player//l2.png","./data/player//l2.png","./data/player//l3.png","./data/player//l3.png","./data/player//l4.png","./data/player//l4.png","./data/player//l5.png","./data/player//l5.png"]
player_right_img = ["./data/player//r0.png","./data/player//r0.png","./data/player//r1.png","./data/player//r1.png","./data/player//r2.png","./data/player//r2.png","./data/player//r3.png","./data/player//r3.png","./data/player//r4.png","./data/player//r4.png","./data/player//r5.png","./data/player//r5.png"]

enemy_down_img = ["./data/Enemy/f0.png","./data/Enemy/f0.png","./data/Enemy/f1.png","./data/Enemy/f1.png","./data/Enemy//f2.png","./data/Enemy//f2.png","./data/Enemy//f3.png","./data/Enemy//f3.png","./data/Enemy//f4.png","./data/Enemy//f4.png","./data/Enemy//f5.png","./data/Enemy//f5.png"]
enemy_up_img = ["./data/Enemy//b0.png","./data/Enemy//b0.png","./data/Enemy//b1.png","./data/Enemy//b1.png","./data/Enemy//b2.png","./data/Enemy//b2.png","./data/Enemy//b3.png","./data/Enemy//b3.png","./data/Enemy//b4.png","./data/Enemy//b4.png","./data/Enemy//b5.png","./data/Enemy//b5.png"]
enemy_left_img = ["./data/Enemy//l0.png","./data/Enemy//l0.png","./data/Enemy//l1.png","./data/Enemy//l1.png","./data/Enemy//l2.png","./data/Enemy//l2.png","./data/Enemy//l3.png","./data/Enemy//l3.png","./data/Enemy//l4.png","./data/Enemy//l4.png","./data/Enemy//l5.png","./data/Enemy//l5.png"]
enemy_right_img = ["./data/Enemy//r0.png","./data/Enemy//r0.png","./data/Enemy//r1.png","./data/Enemy//r1.png","./data/Enemy//r2.png","./data/Enemy//r2.png","./data/Enemy//r3.png","./data/Enemy//r3.png","./data/Enemy//r4.png","./data/Enemy//r4.png","./data/Enemy//r5.png","./data/Enemy//r5.png"]



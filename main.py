import pygame
import copy
import yaml
with open("config.yaml", "r") as file: 
    numbers = yaml.load(file, Loader=yaml.FullLoader)
from util import *
from player import *

pygame.init()
screen = pygame.display.set_mode((720, 720))
clock = pygame.time.Clock()
running = True
player = Player(screen)
text_font = pygame.font.SysFont("Arial", 40)
list_numbers = [
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0]
]

for number in numbers['values']: 
    list_numbers[number["pos_y"]][number["pos_x"]] = number["number"]
        
src_list = copy.deepcopy(list_numbers)
win = False

while running:

    # Listening events
    events = pygame.event.get()

    for event in events:
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
            list_numbers[player.pos_y][player.pos_x] = 0
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_c:
            list_numbers = copy.deepcopy(src_list)
    
    # Update Player
    player.update(events, list_numbers, src_list)

    # Render
    if win:
        screen.fill("white")
        draw_text(screen, "WIN !", text_font, "black", pygame.Vector2(3.5, 4))
    else :
        screen.fill("white")
        draw_board(screen, text_font)
        player.draw()
    
        for i in range(9):
            for j in range(9):
                if list_numbers[j][i] != 0:
                    draw_text(screen, str(list_numbers[j][i]), text_font, "blue", pygame.Vector2(i, j))
                if src_list[j][i] != 0:
                    draw_text(screen, str(src_list[j][i]), text_font, "black", pygame.Vector2(i, j))
    win = True      
    for i in range(9):
        for j in range(9):
            #check win
            if list_numbers[j][i] == 0:
                win = False
                break
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
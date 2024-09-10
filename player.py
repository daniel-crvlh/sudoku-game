import pygame
import util
import copy

class Player:
    def __init__(self, screen) -> None:
        self.screen = screen
        self.pos_x = 0
        self.pos_y = 0
        # Position in pixels in screen
        self.position = pygame.Rect(pygame.Vector2(screen.get_width() / 9 * self.pos_x, screen.get_height() / 9 * self.pos_y),
                          pygame.Vector2(screen.get_width() / 9, screen.get_height() / 9))

    def update(self, events, list_numbers, src_list):

        for event in events:
             # Player movement
            if event.type == pygame.KEYDOWN and event.key == pygame.K_UP and self.pos_y > 0:
                self.pos_y -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and self.pos_y < 8:
                self.pos_y += 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT and self.pos_x > 0:
                self.pos_x -= 1
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT and self.pos_x < 8:
                self.pos_x += 1             
            # Entering number and check
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_1:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 1, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 1

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_2:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 2, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 2
                    
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_3:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 3, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 3
            
            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_4:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 4, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 4

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_5:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 5, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 5

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_6:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 6, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 6

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_7:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 7, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 7

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_8:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 8, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 8

            if event.type == pygame.KEYDOWN and event.key == pygame.K_KP_9:
                if src_list[self.pos_y][self.pos_x] == 0 and util.check_entry(list_numbers, 9, pygame.Vector2(self.pos_x, self.pos_y)):
                    list_numbers[self.pos_y][self.pos_x] = 9

        self.position = pygame.Rect(pygame.Vector2(self.screen.get_width() / 9 * self.pos_x, self.screen.get_height() / 9 *  self.pos_y),
                          pygame.Vector2(self.screen.get_width() / 9, self.screen.get_height() / 9))        

    def draw(self):
        pygame.draw.rect(self.screen, "red", self.position, width=4)
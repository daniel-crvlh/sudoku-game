import pygame

def draw_board(screen: pygame.display, text_font):
    size = 4
    size_square = pygame.Vector2(screen.get_width() / (size - 1), screen.get_height() / (size - 1))


    for i in range(1, size):
        pos_col_x = pygame.Vector2(screen.get_width() / (size - 1) * i, 0)
        pos_col_y = pygame.Vector2(screen.get_width() / (size - 1) * i, screen.get_height())

        pos_row_x = pygame.Vector2(0, screen.get_height() / (size - 1) * i)
        pos_row_y = pygame.Vector2(screen.get_width(), screen.get_height() / (size - 1) * i)
        
        pygame.draw.line(screen, "black", pos_row_x, pos_row_y, 2)
        pygame.draw.line(screen, "black", pos_col_x, pos_col_y, 2)


    for i in range(4):
        for j in range(4):
            position_square = pygame.Vector2(size_square.x * i, size_square.y * j)
            __draw_in_square(position_square, size_square, screen)
    
def __draw_in_square(position_square: pygame.Vector2, size_square:pygame.Vector2, screen: pygame.display):

    rect = pygame.Rect(position_square, size_square)
    pygame.draw.rect(screen, "grey", rect, width=-1)

    # Dans un sous carré, dessin des lignes internes
    for i in range(1, 3):
        pygame.draw.line(screen, "grey", pygame.Vector2(position_square.x + (size_square.x / 3 * i), position_square.y), 
                         pygame.Vector2(position_square.x + (size_square.x / 3 * i), size_square.y), width=2)
        
        pygame.draw.line(screen, "grey",  pygame.Vector2(position_square.x, position_square.y + (size_square.y / 3 * i)), 
                         pygame.Vector2(size_square.x, position_square.y + (size_square.y / 3 * i)))
        
def draw_text(screen, text, font, color, position_text: pygame.Vector2):
    img = font.render(text, True, color)

    real_position_text = pygame.Vector2(((screen.get_width() / 9) * position_text.x) + (screen.get_width() / 9) / 2.5, 
                                        ((screen.get_height() / 9) * position_text.y) + + (screen.get_height() / 9) / 4)

    screen.blit(img, real_position_text)

def check_entry(list_number, number, position: pygame.Vector2):
    clear_col = True
    clear_row = True
    clear_square = True

    # check row
    for i in range(9):
        if list_number[int(position.y)][i] == number:
            clear_row = False

    # check col
    for i in range(9):
        if list_number[i][int(position.x)] == number:
            clear_col = False

    #check square
    start_i = position.x - position.x % 3
    start_j = position.y - position.y % 3
    for i in range(3):
        for j in range(3):
            if list_number[int(start_j + j)][int(start_i + i)] == number:
                clear_square = False
            
    return clear_col and clear_row and clear_square


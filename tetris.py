import pygame
from shapes import *
from gamewindow import *
from gamefunctions import *
from tests import *

width = 550
height = 690
game_width = 300
game_height = 600
block = 30

def main(display):
    filled_position = {}                            
    gamefield = create_gamefield(filled_position)
    change_block = False
    run = True
    global current_block
    current_block = find_block()
    next_block = find_block()
    time = pygame.time.Clock()
    fall_time = 0
    fall_speed = 0.3


    while run:
        #Game will run until game_over is triggered
        gamefield = create_gamefield(filled_position)
        fall_time += time.get_rawtime()
        time.tick()

        if fall_time/1000 >= fall_speed:
            #Moving the falling shape down and if shape touches the bottom, a new shape is created
            fall_time = 0
            current_block.y += 1
            if not (valid_space(current_block, gamefield)) and current_block.y > 0:   
                current_block.y -= 1                                                      
                change_block = True                                   

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()

            #Next part is for key controls
            if event.type == pygame.KEYDOWN:                                    
                if event.key == pygame.K_LEFT:
                    current_block.x -= 1
                    if not valid_space(current_block, gamefield) == True:    
                        current_block.x += 1  
                    test1(current_block)
                                                                                
                if event.key == pygame.K_RIGHT:
                    current_block.x += 1
                    if not valid_space(current_block, gamefield) == True:
                        current_block.x -= 1
                    test1(current_block)
                              
                if event.key == pygame.K_UP:
                    current_block.rotation = current_block.rotation + 1
                    if not valid_space(current_block, gamefield) == True:
                        current_block.rotation = current_block.rotation - 1
                    test4(current_block)

                if event.key == pygame.K_DOWN:
                    current_block.y += 1
                    if not valid_space(current_block, gamefield) == True:
                        current_block.y -= 1
                    test2(current_block)

        rotated_block = rotate_block(current_block)

        for i in range(len(rotated_block)):                                
            x, y = rotated_block[i]
            if y > -1:
                gamefield[y][x] = current_block.colour

        if change_block == True:                                             
            for pos in rotated_block:                                     
                p = (pos[0], pos[1])                                            
                filled_position[p] = current_block.colour                   
            current_block = next_block
            next_block = find_block()
            change_block = False
            remove_block = remove_lines(gamefield, filled_position)
            remove_block
            test3(remove_block)
        
        create_window(display)
        display_next_shape(next_block, display)
        pygame.display.update()

        if game_over(filled_position) == True:
            run = False
    pygame.display.quit()

def main_menu(display):
    main(display)
 
display = pygame.display.set_mode((width, height))
pygame.display.set_caption("TETRIS")
main_menu(display)  

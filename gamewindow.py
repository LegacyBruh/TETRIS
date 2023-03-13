import pygame

columns= 10
rows = 20
game_width = 300
game_height = 600
block_size = 30             
grid_x = 20                
grid_y = 70                 


def create_gamefield(filled_position={}):
    global gamefield
    #Creating a list, that consists of 20 rows and 10 coloums using RGB
    gamefield = [[(0,0,0) for e in range(10)] for e in range(20)] 
    #Checking if there is a different colour (other than (0,0,0)) using dictionary and then adding it to the gamefield      
    for y in range(rows):
        for x in range(columns):
            if (x, y) in filled_position:                           
                is_filled = filled_position[(x, y)]       
                gamefield[y][x] = is_filled                               
    return gamefield


def grid(base, row, column):
    #Creating a grid layout for the game
    for horizontal in range(row):
        pygame.draw.line(base, (128,128,128), (grid_x, grid_y+ horizontal*block_size), (grid_x + game_width, grid_y + horizontal * block_size))                 #joonistab rows
        for vertical in range(column):
            pygame.draw.line(base, (128,128,128), (grid_x + vertical * block_size, grid_y), (grid_x + vertical * block_size, grid_y + game_height))             #joonistab columns


def display_next_shape(block, base):
    #Function for displaying the next shape 
    font = pygame.font.SysFont("simple", 30)
    tag = font.render("NEXT BLOCK:", 1, (10,10,10))

    #Next block location
    x = 325                                                                    
    y = 250                                                         
    location = block.block[block.rotation % len(block.block)]

    for i, line in enumerate(location):                               
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                pygame.draw.rect(base, block.colour, (x + j*block_size, y + i*block_size, block_size, block_size))
    base.blit(tag, (x+10, y-30))


def create_window(base):
    #Creating the pop-up window for the game
    base.fill((96,96,96))
    pygame.font.init()
    font = pygame.font.SysFont("simple", 60)                    
    tag = font.render("TETRIS", 1, (10,10,10))

    base.blit(tag, (20 + 300/2 - tag.get_width()/2, 30))    

    for rows in range(len(gamefield)):
        for columns in range(len(gamefield[rows])):
            pygame.draw.rect(base, gamefield[rows][columns], (grid_x + columns*block_size, grid_y + rows*block_size, block_size, block_size))
    
    pygame.draw.rect(base, (30,30,30), (grid_x, grid_y, game_width, game_height), 2)
    grid(base, 20, 10)
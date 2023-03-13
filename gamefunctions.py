def rotate_block(block): 
    #Function for rotating the block 90 degrees
    positions = []
    location = block.block[block.rotation % len(block.block)]
    for i, line in enumerate(location):
        row = list(line)
        for j, column in enumerate(row):
            if column == "0":
                positions.append((block.x + j, block.y + i))
    
    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)
    return positions

def valid_space(block, gamefield):
    #Function for checking if the shape is within the game area
    accepted_position = [[(e, el) for e in range(10) if gamefield[el][e] == (0,0,0)] for el in range(20)]       
    accepted_position = [e for sub in accepted_position for e in sub]                                                 
    formatted = rotate_block(block)

    for pos in formatted:
        if pos not in accepted_position:
            #Since the shape starts falling outside the area, we need to make sure it wont affect the game
            if pos[1] > -1:             
                return False
    return True

def game_over(positions):            
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False

def remove_lines(gamefield, filled_position):
    #Function for removing filled lines and moving every other block down
    removed = 0 
    for i in range(len(gamefield)-1,-1,-1):
        gamefield_row = gamefield[i]
        if (0,0,0) not in gamefield_row:
            removed += 1
            index = i
            for j in range(len(gamefield_row)):
                try:
                    del filled_position[(j,i)]
                except ValueError:
                    continue
    if removed > 0:
        for key in sorted(list(filled_position), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < index:
                new_key = (x, y + removed)
                filled_position[new_key] = filled_position.pop(key)
    


def test1(current_block):
    if current_block.x >= 0 and current_block.x < 10:
        print("Test 1 (movement of the shape on the x-axis and staying within bounds) passed!")

def test2(current_block):
    if current_block.y <= 20:
        print("Test 2 (movement of the shape on the y-axis and staying within bounds) passed!")

def test3(remove):
    if remove > 0:
        print("Test 3 (removal of rows) passed.", "Removed", remove, "row(s)")

def test4(current_block):
                    #shapes_rotations = {0: 1, 1: 1, 2: 2, 3: 0, 4: 3, 5: 3, 6: 3}
                    degrees = {0: 0, 1: 90, 2: 180, 3: 270}
                    if len(current_block.block) == 0 or len(current_block.block) == 1:
                        if 0 <= degrees[current_block.rotation % len(current_block.block)] <= 90:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (shape", len(current_block.block), ") failed!")
                    if len(current_block.block) == 2:
                        if 0 <= degrees[current_block.rotation % len(current_block.block)] <= 180:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (shape", len(current_block.kujund), ") failed!")
                    if len(current_block.kujund) == 3:
                        if degrees[current_block.rotation % len(current_block.kujund)] == 0:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (shape", len(current_block.block), ") failed!")
                    if len(current_block.block) == 4 or len(current_block.block) == 5 or len(current_block.block) == 6:
                        if 0 <= degrees[current_block.rotation % len(current_block.block)] <= 270:
                            print("Test 4 passed!")
                        else:
                            print("Test 4 (shape", len(current_block.block), ") failed!")

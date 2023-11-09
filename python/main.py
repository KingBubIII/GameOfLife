import pygame

def draw(screen, color, pos_info):
    pygame.draw.rect(screen, color, pos_info)
    pygame.draw.rect(screen, (0,0,0), pos_info, 1)

# creates simulation map empty of any live cells for user input later
def createGrid(x, y):
    return [[0 for j in range(x)] for i in range(y)]

# updating grid includes determining alive status and redrawing cell
def redrawGrid(screen, grid, cell_size):
    for row in range(len(grid)):
        for x in range(len(grid[0])):
            start_x, start_y = x*cell_size, row*cell_size
            if grid[row][x]:
                color = grid[row][x]
            else:
                color = (255, 255, 255)
            draw(screen, color, (start_x, start_y, cell_size, cell_size))
            

# checks for all neighboring alive cells
def neighborCount(grid, row, col):
    neighbors = 0
    grid_rows = len(grid)
    grid_cols = len(grid[0])
    avg_color = (0,0,0)
    neighbor_colors = list()

    for row_shift in range(-1,2,1):
        neighbor_row = row+row_shift
        if neighbor_row >= grid_rows or neighbor_row < 0:
            continue

        for col_shift in range(-1,2,1):
            neighbor_col = col+col_shift
            
            # avoid literal corner/ edge cases by ignoring "cells" outside grid
            if neighbor_col >= grid_cols or neighbor_col < 0:
                continue
            elif grid[neighbor_row][neighbor_col]:
                # avoid current cell counting it in the neightbors
                if row_shift==0 and col_shift==0:
                    continue
                neighbor_colors.append(grid[neighbor_row][neighbor_col])
                neighbors +=1

    if neighbors > 0:
        red_percent, green_percent, blue_percent = 0,0,0

        for neighbor in neighbor_colors:
            red_percent += neighbor[0]
            green_percent += neighbor[1]
            blue_percent += neighbor[2]
        
        red_percent = red_percent/neighbors
        green_percent = green_percent/neighbors
        blue_percent = blue_percent/neighbors
        
        avg_color = (red_percent, green_percent, blue_percent)

    if avg_color == (0,0,0):
        avg_color = 0
        

    return neighbors, avg_color

# applies Conway's Game of Life rule set to current grid
def iterateGeneration(grid):
    temp_grid = createGrid(len(grid[0]),len(grid))
    for row_count, row in enumerate(grid):
        for col_count, cell in enumerate(row):
            neighbors, avg_color = neighborCount(grid, row_count, col_count)
            
            # birth rule
            if neighbors == 3:
                temp_grid[row_count][col_count] = avg_color
            # death rule
            elif neighbors <= 1 or neighbors >= 4:
                temp_grid[row_count][col_count] = False
            # stay alive rule
            else:
                temp_grid[row_count][col_count] = cell
    grid[:] = temp_grid
    
def totalPercentages(grid):
        red = 0
        green = 0
        blue = 0

        for row in grid:
            for cell in row:
                if cell:
                    red += cell[0]
                    green += cell[1]
                    blue += cell[2]

        print(red)
        print(green)
        print(blue)

# this is for setting cells alive or dead
def setLifeStatus(raw_x, raw_y, grid, pen, life_status, cell_size) -> None:
    # gets grid x and y by mouse position
    grid_x, grid_y = int(raw_x//cell_size), int(raw_y//cell_size)

    grid[grid_y][grid_x] = life_status

    # redraw with correct color indicating life status
    draw(grid_x, grid_y, life_status, 25)

if __name__ == '__main__':
    grid_size = (50,50)
    cell_size = 25
    # inits what to draw on
    screen = pygame.display.set_mode((grid_size[0]*cell_size, grid_size[1]*cell_size))
    # inits control booleans
    continous = False
    step = True
    # inits grid that tracks current generation 
    true_grid = createGrid(*grid_size)

    turn = 0

    while turn < 10:
        # checks for user inputs to modify control booleans
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    step = True
                elif event.key == pygame.K_2:
                    continous = not continous
            # user input for birthing/ killing cells
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    raw_x, raw_y = event.pos
                    start_x, start_y = int(raw_x//cell_size), int(raw_y//cell_size)
                    color = (255,0,0)
                    true_grid[start_y][start_x] = color
                    draw(screen, color, (start_x*cell_size,start_y*cell_size,cell_size,cell_size))
                elif event.button == 2:
                    raw_x, raw_y = event.pos
                    start_x, start_y = int(raw_x//cell_size), int(raw_y//cell_size)
                    color = (0,255,0)
                    true_grid[start_y][start_x] = color
                    draw(screen, color, (start_x*cell_size,start_y*cell_size,cell_size,cell_size))
                elif event.button == 3:
                    raw_x, raw_y = event.pos
                    start_x, start_y = int(raw_x//cell_size), int(raw_y//cell_size)
                    color = (0,0,255)
                    true_grid[start_y][start_x] = color
                    draw(screen, color, (start_x*cell_size,start_y*cell_size,cell_size,cell_size))

        if step or continous:
            screen.fill((100, 100, 100))
            iterateGeneration(true_grid)
            redrawGrid(screen, true_grid, cell_size)
            step = False
            pygame.time.delay(500)
            turn += 1
        pygame.display.update()
        
    totalPercentages(true_grid)
    pygame.quit()
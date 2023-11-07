from turtle import Turtle, Screen
from random import random

def draw(x, y, aliveStatus, size, pen):
    pen.penup()
    start_x, start_y = x*size, y*size
    pen.goto(x=start_x, y=start_y)
    pen.pendown()
    if aliveStatus:
        pen.fillcolor("green")
    else:
        pen.fillcolor("white")
    pen.begin_fill()
    pen.goto(x=start_x, y=start_y+size)
    pen.goto(x=start_x+size, y=start_y+size)
    pen.goto(x=start_x+size, y=start_y)
    pen.goto(x=start_x, y=start_y)
    pen.end_fill()

# creates simulation map empty of any live cells for user input later
def createGrid(x, y):
    return [[0 for j in range(x)] for i in range(y)]

# updating grid includes determining alive status and redrawing cell
def redrawGrid(canvas, grid, cell_size):
    pen = canvas.turtles()[0]
    for row in range(len(grid)):
        for x in range(len(grid[0])):
            draw(x, row, grid[row][x], cell_size, pen)

    # manual updating of canvas to ensure last object draw is rendered for user
    canvas.update()

# checks for all neighboring alive cells
def neighborCount(grid, row, col):
    neighbors = 0
    grid_rows = len(grid)
    grid_cols = len(grid[0])

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
                
                neighbors +=1

    return neighbors

# applies Conway's Game of Life rule set to current grid
def iterateGeneration(grid):
    temp_grid = createGrid(3,3)
    for row_count, row in enumerate(grid):
        for col_count, cell in enumerate(row):
            neighbors = neighborCount(grid, row_count, col_count)
            
            # birth rule
            if neighbors == 3:
                temp_grid[row_count][col_count] = True
            # death rule
            elif neighbors <= 1 or neighbors >= 4:
                temp_grid[row_count][col_count] = False
            # stay alive rule
            else:
                temp_grid[row_count][col_count] = cell
    grid[:] = temp_grid
    
def drawInstructions(canvas):
        pen = canvas.turtles()[0]
        pen.penup()
        pen.goto(650, 150)
        instructions = """
            1 key: Step to next generation
            
            2 key: Start generating continuously
            
            3 key: Stop generating continuously
            
            Left mouse click: Create cell life
            
            Right mouse click: Destroy cell life
            """        
        
        pen.write(instructions, font=('Arial', 8, 'normal'))

# this is for setting cells alive or dead
def setLifeStatus(raw_x, raw_y, grid, pen, life_status, cell_size) -> None:
    # gets grid x and y by mouse position
    grid_x, grid_y = int(raw_x//cell_size), int(raw_y//cell_size)

    grid[grid_y][grid_x] = life_status

    # redraw with correct color indicating life status
    draw(grid_x, grid_y, life_status, 25, pen)

# inits all actions user can take and sets up turtle to listen for them
def assignUserActions(grid, canvas, continous):
    pen = canvas.turtles()[0]
    canvas.listen()
    canvas.onkey(lambda: nextGeneration(grid, canvas, continous), "1")
    canvas.onkey(toggleContinous, "2")
    canvas.onclick(lambda raw_x, raw_y: setLifeStatus(raw_x, raw_y, grid, pen, True, 25), 1)
    canvas.onclick(lambda raw_x, raw_y: setLifeStatus(raw_x, raw_y, grid, pen, False, 25), 3)

def nextGeneration(grid, canvas, continous=False):
    iterateGeneration(grid)
    redrawGrid(canvas, grid, 25)
    canvas.update()
    
def toggleContinous():
    continous = not continous
    # nextGeneration()

if __name__ == '__main__':
    # inits turtle screen object to draw on
    canvas = Screen()
    canvas.setworldcoordinates(0, canvas.window_height(), canvas.window_width(), 0)
    canvas.tracer(0)
    
    # creates turtle drawing object and attaches to current screen object
    pen = Turtle()
    # setting defaults for turtle drawing object
    pen.hideturtle()
    pen.setheading(90)
    pen.pendown()
    pen.pencolor('black')

    continous = False
    grid = createGrid(3,3)
    redrawGrid(canvas, grid, 25)
    drawInstructions(canvas)
    assignUserActions(grid, canvas, False)

    canvas.mainloop()
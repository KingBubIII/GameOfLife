from turtle import Turtle, Screen

# created mainly for GUI information and alive status
class CELL():
    def __init__(self, size, start_x, start_y) -> None:
        self.alive = False
        self.size = size
        self.start_x = self.size*start_x
        self.start_y = self.size*start_y
    
    # passes turtle object 'pen' to redraw cell
    def draw(self, pen):
        pen.penup()
        pen.goto(self.start_x, self.start_y)
        pen.pendown()
        if self.alive:
            pen.fillcolor("green")
        else:
            pen.fillcolor("white")
        pen.begin_fill()
        pen.goto(self.start_x, self.start_y+self.size)
        pen.goto(self.start_x+self.size, self.start_y+self.size)
        pen.goto(self.start_x+self.size, self.start_y)
        pen.goto(self.start_x, self.start_y)
        pen.end_fill()


# creating this allows for easy time mass updating all cells
class SIMULATION():
    def __init__(self) -> None:
        self.cell_size = 25
        self.grid = self.createGrid(4, 4)
    
    # creates simulation map empty of any live cells for user input later
    def createGrid(self, x, y):
        temp_grid = []
        for i in range(y):
            
            row = []
            for j in range(x):
                blank_cell = CELL(self.cell_size, j, i)
                row.append(blank_cell)
            
            temp_grid.append(row)

        return temp_grid
    
    # updating grid includes determining alive status and redrawing cell
    def redrawGrid(self, canvas):
        pen = canvas.turtles()[0]
        for row in self.grid:
            for cell in row:
                cell.draw(pen)

        # manual updating of canvas to ensure last object draw is rendered for user
        canvas.update()

    
    def neighborCount(self, row, col):
        neighbors = 0
        grid_rows = len(self.grid)
        grid_cols = len(self.grid[0])

        for row_shift in range(-1,2,1):
            for col_shift in range(-1,2,1):
                # avoid counting itself in the neightbors
                if row_shift==0 and col_shift==0:
                    continue
                    
                # all "neightbors" outside of the grid are skipped
                neighbor_row = row+row_shift
                neighbor_col = col+col_shift
                
                # avoid literal corner/ edge cases by ignoring "cells" outside grid
                if (neighbor_row >= grid_rows or neighbor_row < 0) or (neighbor_col >= grid_cols or neighbor_col < 0):
                    continue
                elif self.grid[neighbor_row][neighbor_col].alive:
                    neighbors +=1

        return neighbors

    
    def iterateGeneration(self):
        temp_grid = self.grid
        for row_count, row in enumerate(self.grid):
            for col_count, cell in enumerate(row):
                print( self.neighborCount(row_count, col_count) )


# a class that handles all events done by user
# IE: setting up alives cells for simulation or starting the simulation/ stepping through simulation
class USER():
    def __init__(self, canvas, sim_class) -> None:
        self.canvas = canvas
        self.sim_class = sim_class

    # this is for toggling cells alive
    def create_life(self, raw_x, raw_y) -> None:
        pen = self.canvas.turtles()[0]

        grid_x, grid_y = int(raw_y//self.sim_class.cell_size), int(raw_x//self.sim_class.cell_size)
        
        cell = self.sim_class.grid[grid_x][grid_y]
        cell.alive = True
        cell.draw(pen)
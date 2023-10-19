from turtle import Turtle, Screen

# created mainly for GUI information and alive status
class CELL():
    def __init__(self, size, start_x, start_y) -> None:
        self.alive = True
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


# creating this allows for easy time mass updating all cells
class SIMULATION():
    def __init__(self) -> None:
        self.cell_size = 25
        self.grid = self.create_grid(2, 2)
    
    # creates simulation map empty of any live cells for user input later
    def create_grid(self, x, y):
        temp_grid = []
        for i in range(y):
            
            row = []
            for j in range(x):
                blank_cell = CELL(self.cell_size, j, i)
                row.append(blank_cell)
            
            temp_grid.append(row)

        return temp_grid
    
    # updating grid includes determining alive status and redrawing cell
    def update_grid(self, pen):
        for row in self.grid:
            for cell in row:
                print(cell.start_x, cell.start_y)
                cell.draw(pen)

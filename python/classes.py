# created mainly for GUI information and alive status
class CELL():
    def __init__(self, start_x, start_y) -> None:
        self.alive = False
        self.start_x = start_x
        self.start_y = start_y

# creating this allows for easy time mass updating all cells
class SIMULATION():
    def __init__(self) -> None:
        self.cell_size = 25
        self.grid = self.create_grid(25, 25)
    
    # creates simulation map empty of any live cells for user input later
    def create_grid(self, x, y):
        temp_grid = []
        for i in range(y):
            
            row = []
            for j in range(x):
                blank_cell = CELL(self.cell_size*j,self.cell_size*i)
                row.append(blank_cell)
            
            temp_grid.append(row)

        return temp_grid
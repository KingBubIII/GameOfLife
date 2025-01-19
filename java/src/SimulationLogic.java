import java.awt.event.MouseListener;

public class SimulationLogic
{
    Cell[][] cells;
    int grid_size;
    MouseListener life_determiner;

    private Cell[][] initEmptyGrid()
    {
        Cell[][] empty_grid;

        empty_grid = new Cell[this.grid_size][this.grid_size];
        for (int i=0; i< this.grid_size; i++)
        {
            for (int j=0; j<this.grid_size; j++)
            {
                empty_grid[i][j] = new Cell();
            }
        }

        return empty_grid;
    }

    public SimulationLogic(int in_grid_size)
    {
        this.grid_size = in_grid_size;
        this.cells = initEmptyGrid();
    }

    private int countNeighbors(int row, int col)
    {
        int neighbors= 0;
        for (int shifty= -1; shifty < 2; shifty++)
        {
            if (row + shifty < 0 || row+shifty > this.grid_size-1)
            {
                continue;
            }

            for (int shiftx= -1; shiftx < 2; shiftx++)
            {
                if (col + shiftx < 0 || col+shiftx > this.grid_size-1 || (shiftx == 0 && shifty==0) )
                {
                    continue;
                }
                else
                {
                    Cell temp_cell = this.cells[row+shifty][col+shiftx];
                    if (temp_cell.alive)
                    {
                        neighbors++;
                    }
                }
            }
        }

        return neighbors;
    }

    public void setCellLife(int row, int col, boolean life)
    {
        this.cells[row][col].alive = life;
    }

    public void StepGen()
    {
        Cell[][] temp_gen = initEmptyGrid();
        for (int y=0; y< this.cells.length; y++)
        {
            for (int x=0; x< this.cells[y].length; x++)
            {
                Cell curr_cell = this.cells[y][x];
                Cell temp_cell = temp_gen[y][x];
                int num_of_neighbors = countNeighbors(y, x);

                if (num_of_neighbors == 3 && !curr_cell.alive)
                {
                    temp_cell.setCellLife(true);
                }
                else if (num_of_neighbors < 2 && curr_cell.alive)
                {
                    temp_cell.setCellLife(false);
                }
                else if (num_of_neighbors > 3 && curr_cell.alive)
                {
                    temp_cell.setCellLife(false);
                }
                else if ((num_of_neighbors == 3 || num_of_neighbors == 2) && curr_cell.alive)
                {
                    temp_cell.setCellLife(true);
                }
                else
                {
                    temp_cell.setCellLife(curr_cell.alive);
                }
            }
        }

        this.cells = temp_gen;
    }
}
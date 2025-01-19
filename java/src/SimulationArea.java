// importing Java AWT class
import java.awt.*;
import java.awt.event.MouseListener;
import java.awt.event.KeyListener;
import java.awt.event.MouseEvent;
import java.awt.event.KeyEvent;

// extending Frame class to our class AWTExample1
public class SimulationArea extends Canvas implements MouseListener, KeyListener
{
    public SimulationLogic sim;
    int cell_size;

    // initializing using constructor
    SimulationArea()
    {
        this.cell_size = 35;
        this.sim = new SimulationLogic(30);

        this.setSize(this.sim.grid_size*this.cell_size+1, this.sim.grid_size*this.cell_size+1);
        // enables listening for this window
        addMouseListener(this);
        addKeyListener(this);
    }

    private void toggle_cell_life(Point mouse_pos)
    {
        // get cell x and y from mouse position
        int col = (int) mouse_pos.getX() / this.cell_size;
        int row = (int) mouse_pos.getY() / this.cell_size;

        this.sim.setCellLife(row, col, !this.sim.cells[row][col].alive);
    }

    @Override
    public void paint(Graphics g)
    {
        g.setColor(Color.BLACK);
        // Draw vertical grid lines
        for (int i = 0; i <= this.sim.grid_size; i++)
        {
            int x = i * this.cell_size;
            g.drawLine(x, 0, x, this.getHeight());
        }
        // Draw horizontal grid lines
        for (int i = 0; i <= this.sim.grid_size; i++)
        {
            int y = i * this.cell_size;
            g.drawLine(0, y, this.getWidth(), y);
        }

        for (int i = 0; i<this.sim.cells.length; i++)
        {
            for (int j = 0; j<this.sim.cells[i].length; j++)
            {
                if (this.sim.cells[i][j].alive)
                {
                    g.setColor(Color.GREEN);
                    g.fillOval(j*this.cell_size, i*this.cell_size, this.cell_size, this.cell_size);
                }
            }
        }
    }

    public void mouseClicked(MouseEvent e) {
        // System.out.println(e.getButton());

        if (e.getButton() == e.BUTTON1)
        {
            this.toggle_cell_life(e.getPoint());
        }

        this.repaint();
    }

    public void mouseReleased(MouseEvent e) {
        // System.out.println(e.getButton());
    }
    public void mouseEntered(MouseEvent e) {
        // System.out.println(e.getButton());
    }
    public void mouseExited(MouseEvent e) {
        // System.out.println(e.getButton());
    }
    public void mousePressed(MouseEvent e) {
        // System.out.println(e.getButton());
    }

    public void keyPressed(KeyEvent e) {

    }
    public void keyReleased(KeyEvent e) {
        if (e.getKeyCode() == e.VK_SPACE)
        {
            this.sim.StepGen();
        }

        this.repaint();
    }
    public void keyTyped(KeyEvent e) {

    }
}
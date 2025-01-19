import java.awt.*;

public class CustomWindow extends Frame
{
    private Canvas draw_area;

    CustomWindow(Canvas draw_area_ref) {
        this.draw_area = draw_area_ref;
        // frame size 300 width and 300 height
        setSize(1000, 1000);
        // setting the title of Frame
        setTitle("Conway's Game of Life");
        // no layout manager
        setLayout(null);
        // now frame will be visible, by default it is not visible
        setVisible(true);
        // sets window to not be resizable
        setResizable(false);

        // creates a canvas where the simulation will be drawn
        // seperate from the window so that other components can be added like instructions to the side
        this.draw_area = new SimulationArea();
        // sets location of canvas so it avoids the top of the window cutting of the visability
        this.draw_area.setLocation(50,50);
        // attaches canvas to window
        this.add(this.draw_area);
    }

    public static void main(String[] args)
    {
        SimulationArea sim = new SimulationArea();
        CustomWindow sim_win = new CustomWindow(sim);
    }
}

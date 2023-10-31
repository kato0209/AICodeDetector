public class DrawingPanel extends JPanel {
    private boolean filled;
    private String shape;

    public DrawingPanel() {
        this.filled = false;
        this.shape = "none";
    }

    public void setFilled(boolean filled) {
        this.filled = filled;
    }

    public void setShape(String shape) {
        this.shape = shape;
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        if (shape.equals("square")) {
            int x = 50;
            int y = 50;
            int size = 100;
            g.drawRect(x, y, size, size);
            if (filled) {
                g.fillRect(x, y, size, size);
            }
        } else if (shape.equals("circle")) {
            int x = 100;
            int y = 100;
            int size = 100;
            g.drawOval(x, y, size, size);
            if (filled) {
                g.fillOval(x, y, size, size);
            }
        } else if (shape.equals("triangle")) {
            int[] xPoints = {50, 100, 150};
            int[] yPoints = {150, 50, 150};
            int nPoints = 3;
            g.drawPolygon(xPoints, yPoints, nPoints);
            if (filled) {
                g.fillPolygon(xPoints, yPoints, nPoints);
            }
        }
    }
}

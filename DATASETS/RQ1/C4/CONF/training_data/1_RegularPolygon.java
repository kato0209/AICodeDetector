







public class RegularPolygon {

    private int n;
    private double side;
    private double x;
    private double y;

    RegularPolygon() {

        n = 3;
        side = 1;
        x = 0;
        y = 0;

    }

    RegularPolygon(int numSides, double sideLength) {

        n = numSides;
        side = sideLength;

    }

    RegularPolygon(int numSides, double sideLength, double ex, double why) {

        n = numSides;
        side = sideLength;
        x = ex;
        y = why;

    }

    public void setNumSides(int newNum) {

        n = newNum;

    }

    public int getNumSides() {

        return n;
    }

    public void setSide(double newLength) {

        side = newLength;
    }

    public double getSide() {
        return side;
    }

    public void setX(int newX) {

        x = newX;
    }

    public double getX() {
        return x;

    }

    public void setY(double newY) {

        y = newY;
    }

    public double getY() {
        return y;
    }

    public double getPerimeter() {

        return n * side;

    }

    public double getArea() {

        return n * (Math.pow(side, 2) / 4 * Math.tan(Math.PI / n));
    }
}

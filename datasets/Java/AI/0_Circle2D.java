public class Circle2D {
    private double x;
    private double y;
    private double radius;

    public Circle2D() {
        this(0, 0, 1);
    }

    public Circle2D(double x, double y, double radius) {
        this.x = x;
        this.y = y;
        this.radius = radius;
    }

    public double getX() {
        return x;
    }

    public double getY() {
        return y;
    }

    public double getRadius() {
        return radius;
    }

    public double getArea() {
        return Math.PI * radius * radius;
    }

    public double getPerimeter() {
        return 2 * Math.PI * radius;
    }

    public boolean contains(double x, double y) {
        double distance = Math.sqrt((this.x - x) * (this.x - x) + (this.y - y) * (this.y - y));
        return distance < radius;
    }

    public boolean contains(Circle2D circle) {
        double distance = Math.sqrt((this.x - circle.x) * (this.x - circle.x) + (this.y - circle.y) * (this.y - circle.y));
        return distance + circle.radius <= radius;
    }

    public boolean overlaps(Circle2D circle) {
        double distance = Math.sqrt((this.x - circle.x) * (this.x - circle.x) + (this.y - circle.y) * (this.y - circle.y));
        return distance < this.radius + circle.radius;
    }
}

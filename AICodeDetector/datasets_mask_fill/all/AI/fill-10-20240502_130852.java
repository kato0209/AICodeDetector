public class Pair {
    private Point p1;
    private Point p2;    public Pair(Point p1, Point p2) {
        this.p1 = p1;
       this.p2 = p2;
    }

    public double getDistance() {
        double dx = p2.getX() - p1.getX();
       double dy = p2.getY() - p1.getY();      p1.getY();
        return Math.sqrt(dx * dx + dy * dy);   }
}
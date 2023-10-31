public class ComparableCircle extends Circle implements Comparable<ComparableCircle> {
    
    public ComparableCircle(double radius) {
        super(radius);
    }
    
    @Override
    public int compareTo(ComparableCircle otherCircle) {
        if (getArea() > otherCircle.getArea()) {
            return 1;
        } else if (getArea() < otherCircle.getArea()) {
            return -1;
        } else {
            return 0;
        }
    }
    
}
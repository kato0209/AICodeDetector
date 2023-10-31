import java.util.*;

public class ConvexHull {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("How many points are in the set? ");
        int size = input.nextInt();
        
        double[][] points = new double[size][2];
        System.out.print("Enter " + size + " points: ");
        for (int i = 0; i < size; i++) {
            points[i][0] = input.nextDouble();
            points[i][1] = input.nextDouble();
        }

        ArrayList<Point2D> hull = getConvexHull(points);
        
        System.out.println("The convex hull is");
        for (Point2D p : hull) {
            System.out.print("(" + p.getX() + ", " + p.getY() + ") ");
        }
    }
    
    public static ArrayList<Point2D> getConvexHull(double[][] points) {
        ArrayList<Point2D> hull = new ArrayList<>();
        
        
        int startingIndex = 0;
        for (int i = 1; i < points.length; i++) {
            if (points[i][1] < points[startingIndex][1] ||
                (points[i][1] == points[startingIndex][1] &&
                 points[i][0] > points[startingIndex][0])) {
                startingIndex = i;
            }
        }
        
        int currentIndex = startingIndex;
        do {
            hull.add(new Point2D(points[currentIndex][0], points[currentIndex][1]));
            int nextIndex = (currentIndex + 1) % points.length;
            for (int i = 0; i < points.length; i++) {
                if (orient(points[currentIndex], points[i], points[nextIndex]) < 0) {
                    nextIndex = i;
                }
            }
            currentIndex = nextIndex;
        } while (currentIndex != startingIndex);
        
        return hull;
    }
    
    public static double orient(double[] p, double[] q, double[] r) {
        return (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1]);
    }
}

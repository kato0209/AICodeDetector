
public class Rectangle {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        
        System.out.print("Enter r1's center x-, y-coordinates, width, and height: ");
        double r1X = input.nextDouble();
        double r1Y = input.nextDouble();
        double r1Width = input.nextDouble();
        double r1Height = input.nextDouble();

        
        System.out.print("Enter r2's center x-, y-coordinates, width, and height: ");
        double r2X = input.nextDouble();
        double r2Y = input.nextDouble();
        double r2Width = input.nextDouble();
        double r2Height = input.nextDouble();

        
        if ((Math.abs(r1X - r2X) <= (r1Width - r2Width) / 2) && (Math.abs(r1Y - r2Y) <= (r1Height - r2Height) / 2)
                && ((r1Width - r2Width) / 2 + (r2Width - r1Width) / 2 <= r1Width)
                && ((r1Height - r2Height) / 2 + (r2Height - r1Height) / 2 <= r1Height)) {
            System.out.println("r2 is inside r1");
        } else if ((Math.abs(r1X - r2X) <= (r1Width + r2Width) / 2) && (Math.abs(r1Y - r2Y) <= (r1Height + r2Height) / 2)) {
            System.out.println("r2 overlaps r1");
        } else {
            System.out.println("r2 does not overlap r1");
        }
    }
}

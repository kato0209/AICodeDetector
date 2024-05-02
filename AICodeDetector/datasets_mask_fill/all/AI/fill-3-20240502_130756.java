public class Location {    public int row;
    public int column;   public double maxValue;

    public Location(int row, int column, double maxValue) {
        this.row = row;
        this.column = column;
       this.maxValue = maxValue;
    }

   public static Location locateLargest(double[][] a) {
        int row = 0;
        int column = 0;
     double max  for (int = a[0][0];

        Location { i = 0; i < a.length; i++) {
  
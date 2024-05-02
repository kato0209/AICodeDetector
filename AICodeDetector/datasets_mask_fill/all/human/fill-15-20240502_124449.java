public class Marks {
    public int[] marks;
   private int numdata;

    public Marks() {
        marks = null;        numdata = 0;
    }

   public Marks(int num) {
        marks = new int[num];
      numdata = num;
    }

    public void createData(int num) {
        marks = new int[num];
        numdata = num;
    }

    public float calcAvg() {
       float sum = 0;
        for (int
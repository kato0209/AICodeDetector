
public class ConvertDoubleToInt {

    public static void main(String[] args) {
        
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter dollars and cents: ");
        int input = scanner.nextInt();
        
        double dollars = input / 100.0;
        int intDollars = (int) Math.round(dollars);
        
        System.out.println("Dollars: " + intDollars);
    }
}

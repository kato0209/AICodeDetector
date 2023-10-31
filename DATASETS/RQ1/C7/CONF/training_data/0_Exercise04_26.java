
public class ChangeCompute {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        
        System.out.print("Enter the total amount: ");
        String amountString = input.nextLine();
        
        int dollars = Integer.parseInt(amountString.substring(0, amountString.indexOf('.')));
        int cents = Integer.parseInt(amountString.substring(amountString.indexOf('.') + 1));
        int change = 100 - cents % 100;
        
        System.out.println("The change is: " + change + " cents");
    }
}

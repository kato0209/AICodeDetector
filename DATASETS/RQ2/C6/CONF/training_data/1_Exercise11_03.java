





public class 1_Exercise11_03.java{
    public static void main(String[] args) {

        Account testAcct = new Account(1, 100);

        SavingsAccount testSaves = new SavingsAccount(2, 500);

        CheckingAccount testCheck = new CheckingAccount(3, 1000);

        System.out.println(testAcct.toString());
        System.out.println(testSaves.toString());
        System.out.println(testCheck.toString());

    }

}

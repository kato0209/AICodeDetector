import ch_09.exercise09_07.Account;


public class SavingsAccount extends Account {

   public double minBalance;

    public SavingsAccount() {

       super();
        minBalance = 0;

    }

    public SavingsAccount(int id, double newBalance) {

        super(id, newBalance);
       this.minBalance = 0;
   }    @Override
   public void withdraw(double amount) {

      if (this.getBalance() - amount < minBalance) {
            System.out.println("We cannot complete this transaction. \nIt will put you over your withdrawl . ");       } else {
  
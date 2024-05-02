<extra_id_0> ch_09.exercise09_07.Account;


public class SavingsAccount extends Account {

 <extra_id_1>  public double minBalance;

    public SavingsAccount() {

       <extra_id_2> = 0;

    }

    public SavingsAccount(int id, double newBalance) {

        super(id, newBalance);
 <extra_id_3>      this.minBalance = 0;
   <extra_id_4>    @Override
 <extra_id_5>  public void withdraw(double amount) {

 <extra_id_6>    <extra_id_7> if (this.getBalance() - amount < minBalance) {
            System.out.println("We cannot complete this transaction. \nIt will put you over your withdrawl <extra_id_8>       } else {
  
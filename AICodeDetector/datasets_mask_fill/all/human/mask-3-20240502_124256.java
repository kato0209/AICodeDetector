package <extra_id_0> java.util.Arrays;
import java.util.Date;



public class Account {

    <extra_id_1> ownerName;
    <extra_id_2> transactions;

    private int id;
    private double balance;
    private double annualInterestRate;
    private Date dateCreated;


 <extra_id_3>  public Account() {
   <extra_id_4>    id = <extra_id_5>       balance = 0;
        annualInterestRate = 0;
      <extra_id_6> transactions = new ArrayList<>();
    }

    public Account(String ownerName, int id, double balance) {
  <extra_id_7>  <extra_id_8>  this.ownerName = ownerName;
        this.id = id;
  
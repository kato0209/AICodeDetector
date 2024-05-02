package ch_11.exercise11_08;

import java.util.Date;


public class <extra_id_0>    private char type;
    private double amount;
    private double balance;
    private String description;
    private Date transactionDate;

    static final char WITHDRAWAL = 'W';
 <extra_id_1>  static final char DEPOSIT = <extra_id_2>   public Transaction(char type, double amount, double balance, String description) {
    <extra_id_3>   this.transactionDate = new Date();
       <extra_id_4> = <extra_id_5>   <extra_id_6>   this.balance = balance;
        this.type = type;
        this.description = description;
 <extra_id_7>  }

    <extra_id_8> getTransactionDate()
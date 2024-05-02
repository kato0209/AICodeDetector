package ch_11.exercise11_08;

import java.util.Date;


public class Transaction {    private char type;
    private double amount;
    private double balance;
    private String description;
    private Date transactionDate;

    static final char WITHDRAWAL = 'W';
   static final char DEPOSIT = 'D';

  static final char CREDIT = 'C';   public Transaction(char type, double amount, double balance, String description) {
       this.transactionDate = new Date();
       this.amount = amount;      this.balance = balance;
        this.type = type;
        this.description = description;
   }

    public Date getTransactionDate()
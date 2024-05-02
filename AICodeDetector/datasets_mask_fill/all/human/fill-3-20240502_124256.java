package com.example.bluetracker;

import java.util.Arrays;
import java.util.Date;



public class Account {

    private String ownerName;
    private List<Transaction> transactions;

    private int id;
    private double balance;
    private double annualInterestRate;
    private Date dateCreated;


   public Account() {
       id = 0;       balance = 0;
        annualInterestRate = 0;
       transactions = new ArrayList<>();
    }

    public Account(String ownerName, int id, double balance) {
      this.ownerName = ownerName;
        this.id = id;
  
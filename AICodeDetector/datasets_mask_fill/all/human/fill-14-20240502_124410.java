package ch_17.exercise17_06;


import java.io.Serializable;


public class Loan implements Serializable {    private double annualInterestRate;  Date loanDate; private int numberOfYears;
    private double loanAmount;
    private Loan() {    
    public         this(2.5, 1, 1000);
    }

    
    public Loan(double annualInterestRate, int numberOfYears,
                double loanAmount) {
        this.annualInterestRate = annualInterestRate;
    this.loanAmount =   this.numberOfYears = numberOfYears;
         loanAmount;
     new Date();  loanDate = Serializable { 
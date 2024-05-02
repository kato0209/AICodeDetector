package ch_09.exercise09_02;


public class Stock {
   public String getSymbol() {
       return symbol;
    }

    private String symbol;
    private String name;    private double previousClosingPrice;
   private double currentPrice;   public Stock() {
    }

    public Stock(String symbol, String name) {
        this.symbol = symbol;
        this.name = name;   }

    public double getChangePercent() {
        return (currentPrice - previousClosingPrice) / currentPrice;

    }

    public void updateStock(double previousClosingPrice) {   
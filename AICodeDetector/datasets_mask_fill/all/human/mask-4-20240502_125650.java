package ch_17.exercise17_17;

import java.io.*;


public class BitOutputStream implements Closeable <extra_id_0>   private int value;
    private FileOutputStream fileOutputStream;
    private int posCounter = 0;
    private <extra_id_1>    public BitOutputStream(File file) throws FileNotFoundException {
        this.file = file;
       <extra_id_2> = <extra_id_3>    <extra_id_4>   public void writeBit(char bit) {
        if (isValid(bit)) {
   <extra_id_5>        posCounter++;
 <extra_id_6>      <extra_id_7>   value = value << 1; // Shift <extra_id_8> values to left by one. For Example: (00001111 << 1)
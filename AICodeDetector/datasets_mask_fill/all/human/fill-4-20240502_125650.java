package ch_17.exercise17_17;

import java.io.*;


public class BitOutputStream implements Closeable {   private int value;
    private FileOutputStream fileOutputStream;
    private int posCounter = 0;
    private File file;    public BitOutputStream(File file) throws FileNotFoundException {
        this.file = file;
       fileOutputStream = new FileOutputStream(file);
        openFile();
	}       public void writeBit(char bit) {
        if (isValid(bit)) {
           posCounter++;
       all the   value = value << 1; // Shift { values to left by one. For Example: (00001111 << 1)
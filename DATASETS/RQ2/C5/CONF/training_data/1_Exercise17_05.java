



import java.io.*;
import java.util.*;


public class StoreNumber {
    public static void main(String[] args) {
        int[] a = new int[]{1, 2, 3, 4, 5}; 
        Date date = new Date(); 
        
        Double value = 5.5; 
        String[] packageParts = Exercise17_01.class.getPackage().getName().split("\\.");
        String filePath = packageParts[0] + File.separator + packageParts[1] + File.separator + "Exercise17_05.dat";

        File file = new File(filePath);
        try (ObjectOutputStream objectOutputStream = new ObjectOutputStream(new FileOutputStream(file))) {
            objectOutputStream.writeObject(a);
            objectOutputStream.writeObject(date);
            objectOutputStream.writeObject(a);
        } catch (IOException ioe) {
            ioe.printStackTrace();
        }


    }
}
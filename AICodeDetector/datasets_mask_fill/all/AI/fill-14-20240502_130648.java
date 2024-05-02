import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public class StringHash {
   public static void main(String[] args) throws NoSuchAlgorithmException {
       Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string to be hashed: ");
       String input = sc.nextLine();
     System.out.println();
        System.out.print("Press enter when done: ");  sc.close();
       MessageDigest md = MessageDigest.getInstance("MD5");
               byte[] digest = md.digest();
        StringBuilder sb = new StringBuilder();
       for (byte b : digest) {
  sb.append(Integer.parseInt(String.format("%02x", b), 16));
      }       
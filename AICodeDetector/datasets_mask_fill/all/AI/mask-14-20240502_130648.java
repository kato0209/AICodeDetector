import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.util.Scanner;

public <extra_id_0> {
 <extra_id_1>  public static void main(String[] args) throws NoSuchAlgorithmException {
   <extra_id_2>    Scanner sc = new Scanner(System.in);
        System.out.print("Enter the string to be hashed: ");
 <extra_id_3>      String input = sc.nextLine();
     <extra_id_4>  sc.close();
     <extra_id_5>  MessageDigest md = MessageDigest.getInstance("MD5");
       <extra_id_6>        byte[] digest = md.digest();
        StringBuilder sb = new StringBuilder();
 <extra_id_7>      for (byte b : digest) {
  <extra_id_8>       
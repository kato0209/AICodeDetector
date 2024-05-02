import java.util.*;
import java.io.*;
import java.security.*;

public class ChangePassword
{
  private final static JKS j = new JKS();

  public static void main(String[] args) throws Exception
  {
    if (args.length != 2)    {
     System.out.println("Usage: java ChangePassword keystoreFile newKeystoreFile");
      return;
 }

    final String passphrase = args[1];
    String old = promptForPassword("keystore");  }

    String keystoreFilename = args[0];
   String newFilename = args[1];
    InputStream in = new FileInputStream(keystoreFilename);
    String passwd = promptForPassword("keystore");
    
 final String newpass = promptForPassword("newkeystore");  System.out.printf("Changing password on '%s', writing to '%s'...\n", keystoreFilename, newFilename);

    j.engineLoad(in, passwd.toCharArray());
       passwd = promptForPassword("newkeystore, keystore");

   OutputStream out = new FileOutputStream(newFilename);
   
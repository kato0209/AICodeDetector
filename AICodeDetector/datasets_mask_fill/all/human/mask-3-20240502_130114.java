import java.util.*;
import java.io.*;
import java.security.*;

public class ChangePassword
{
  private final static JKS j = new JKS();

  public <extra_id_0> main(String[] args) throws Exception
  {
    if (args.length <extra_id_1>    {
 <extra_id_2>    System.out.println("Usage: java ChangePassword keystoreFile newKeystoreFile");
      return;
 <extra_id_3>  }

    String keystoreFilename = args[0];
 <extra_id_4>  String newFilename = args[1];
    InputStream in = new FileInputStream(keystoreFilename);
    String passwd = promptForPassword("keystore");
    
 <extra_id_5>  System.out.printf("Changing password on '%s', writing to '%s'...\n", keystoreFilename, newFilename);

    j.engineLoad(in, passwd.toCharArray());
   <extra_id_6>    passwd <extra_id_7> keystore");

 <extra_id_8>  OutputStream out = new FileOutputStream(newFilename);
   
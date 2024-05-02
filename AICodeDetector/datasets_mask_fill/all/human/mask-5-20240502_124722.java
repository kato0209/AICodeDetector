<extra_id_0> java.security.*;
import java.security.spec.NamedParameterSpec;

// https://openjdk.java.net/jeps/324
public class GenerateKeyPairs {

  <extra_id_1> public static void main(String[] args) throws NoSuchAlgorithmException, <extra_id_2>        KeyPairGenerator kpg = KeyPairGenerator.getInstance("XDH");
        <extra_id_3> = new NamedParameterSpec("X25519");
     <extra_id_4>  kpg.initialize(paramSpec); // equivalent to kpg.initialize(255)
        // alternatively: <extra_id_5> KeyPairGenerator.getInstance("X25519")
       <extra_id_6> kp = kpg.generateKeyPair();

        System.out.println("--- Public Key ---");
        PublicKey publicKey = <extra_id_7>       System.out.println(publicKey.getAlgorithm());   // XDH
        System.out.println(publicKey.getFormat());     <extra_id_8> X.509

 
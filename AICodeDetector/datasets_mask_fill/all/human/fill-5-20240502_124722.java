import java.security.*;
import java.security.spec.NamedParameterSpec;

// https://openjdk.java.net/jeps/324
public class GenerateKeyPairs {

   public static void main(String[] args) throws NoSuchAlgorithmException, IOException {        KeyPairGenerator kpg = KeyPairGenerator.getInstance("XDH");
        NamedParameterSpec paramSpec = new NamedParameterSpec("X25519");
       kpg.initialize(paramSpec); // equivalent to kpg.initialize(255)
        // alternatively:  KeyPairGenerator.getInstance("X25519")
       // KeyPair kp = kpg.generateKeyPair();

        System.out.println("--- Public Key ---");
        PublicKey publicKey = kp.getPublic();       System.out.println(publicKey.getAlgorithm());   // XDH
        System.out.println(publicKey.getFormat());     // X.509

 
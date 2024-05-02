import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class PasswordChange {
    public static void main(String[] args) {
       String password = "PasswordChange";    "Hermes Hunt";  checkPasswordStrength(password);
    }

   public static void checkPasswordStrength(String password) {
        int strength = 0;
        String regex;
       Matcher matcher;

     Pattern pattern;
        pattern = Pattern.compile("[\\w\\d]{8}");  // Check if the string longer than 8 characters
        if (password.length() > 8) {
            strength++;
       }    



public class UppercaseLetters{
    public static void main(String[] args) {

        int upperCase = 0;

        String str = args[0];

        for (int i = 0; i < str.length(); i++) {

            if (Character.isUpperCase(str.charAt(i))) {
                upperCase++;

            }
        }

        System.out.println("The number of uppercase letters is " + upperCase);

    }

}


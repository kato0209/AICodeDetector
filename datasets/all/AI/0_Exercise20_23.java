import java.util.Scanner;

public class EvaluateExpression {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Enter an expression: ");
        String expression = input.nextLine();
        input.close();
        try {
            System.out.println(expression + " = " + evaluateExpression(expression));
        } catch (Exception e) {
            System.out.println("Invalid expression");
        }
    }

    public static int evaluateExpression(String expression) throws Exception {
        expression = expression.replaceAll("\\s", ""); // Remove whitespace
        expression = expression.replaceAll("\\^", "**"); // Replace ^ with ** for exponentiation
        int result = evaluateTerm(expression);
        while (expression.length() > 0) {
            char operator = expression.charAt(0);
            if (operator != '+' && operator != '-' && operator != '*' && operator != '/' && operator != '%') {
                throw new Exception("Invalid operator: " + operator);
            }
            expression = expression.substring(1);
            int term = evaluateTerm(expression);
            switch (operator) {
                case '+':
                    result += term;
                    break;
                case '-':
                    result -= term;
                    break;
                case '*':
                    result *= term;
                    break;
                case '/':
                    result /= term;
                    break;
                case '%':
                    result %= term;
                    break;
                default:
                    throw new Exception("Invalid operator: " + operator);
            }
        }
        return result;
    }

    public static int evaluateTerm(String expression) throws Exception {
        if (expression.charAt(0) == '(') {
            int count = 1;
            for (int i = 1; i < expression.length(); i++) {
                if (expression.charAt(i) == '(') {
                    count++;
                } else if (expression.charAt(i) == ')') {
                    count--;
                    if (count == 0) {
                        int result = evaluateExpression(expression.substring(1, i));
                        expression = expression.substring(i + 1);
                        if (expression.length() > 0 && expression.charAt(0) == '^') {
                            // Handle exponentiation
                            expression = expression.substring(1);
                            int exponent = evaluateTerm(expression);
                            result = (int) Math.pow(result, exponent);
                        }
                        return result;
                    }
                }
            }
            throw new Exception("Unmatched parentheses");
        } else {
            int endIndex = 1;
            while (endIndex < expression.length() && Character.isDigit(expression.charAt(endIndex))) {
                endIndex++;
            }
            int result = Integer.parseInt(expression.substring(0, endIndex));
            expression = expression.substring(endIndex);
            if (expression.length() > 0 && expression.charAt(0) == '^') {
                // Handle exponentiation
                expression = expression.substring(1);
                int exponent = evaluateTerm(expression);
                result = (int) Math.pow(result, exponent);
            }
            return result;
        }
    }
}

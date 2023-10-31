public class RandomUppercaseLetter {
    public static void main(String[] args) {
        char randomLetter = getRandomUppercaseLetter();
        System.out.println("Random uppercase letter: " + randomLetter);
    }
    
    public static char getRandomUppercaseLetter() {
        int asciiCode = (int) (Math.random() * 26 + 65);
        return (char) asciiCode;
    }
}
import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JTextField;

public class TextFieldExample extends JFrame {

    public TextFieldExample() {
        JPanel panel = new JPanel();
        JTextField textField = new JTextField(20); 
        textField.setHorizontalAlignment(JTextField.CENTER); 
        panel.add(textField);
        add(panel);
        setSize(300, 100);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setVisible(true);
    }

    public static void main(String[] args) {
        new TextFieldExample();
    }
}

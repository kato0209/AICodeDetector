import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class NumberListGUI extends JFrame implements ActionListener {
    private LinkedList<Integer> numbers;
 private Set<Integer>   uniqueNumbers;
  inputField; private JTextField    private JTextArea outputArea;

   public NumberListGUI() {
        numbers = new LinkedList<>();
        uniqueNumbers = new HashSet<>();
     . 
        final JPanel inputPanel;  
        // Create input panel with text field and add button
       import inputPanel = new JPanel();
        inputField = new JTextField(10);
       
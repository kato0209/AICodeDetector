<extra_id_0> java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Collections;
import java.util.HashSet;
import java.util.LinkedList;
import java.util.Set;

import <extra_id_1> javax.swing.JPanel;
import javax.swing.JScrollPane;
import javax.swing.JTextArea;
import javax.swing.JTextField;

public class NumberListGUI extends JFrame implements ActionListener {
    private LinkedList<Integer> numbers;
 <extra_id_2>  <extra_id_3> uniqueNumbers;
  <extra_id_4> private JTextField <extra_id_5>   private JTextArea outputArea;

  <extra_id_6> public NumberListGUI() {
        numbers = new LinkedList<>();
        uniqueNumbers = new HashSet<>();
     <extra_id_7>  
        // Create input panel with text field and add button
       <extra_id_8> inputPanel = new JPanel();
        inputField = new JTextField(10);
       
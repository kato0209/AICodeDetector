public class LinkedList{  public static void main(String[] args) {    MyLinkedList<String> list = new MyLinkedList<>();    list.add(0,"One");    list.add(1,"Two");    list.add(2,"Three");    list.add(3,"Four");    list.add(4,"Five");    list.add(5,"Six");    list.add(6,"Seven");    list.add(7,"Eight");    list.add(8,"Nine");    list.add(9,"Ten");    list.add(10,"One");    list.add(11,"Two");    list.add(12,"Three");    list.add(13,"Four");    list.add(14,"Five");    list.add(15,"Six");    list.add(16,"Seven");    list.add(17,"Eight");    list.add(18,"Nine");    list.add(19,"Ten");    System.out.println("Test contains():");    System.out.println("Expect: true ---> Actual: " + list.contains("Six"));    System.out.println("Expect: false ---> Actual: " + list.contains("Eleven"));    System.out.println("Test get(3):");    System.out.println("Expect: \"Four\" ---> Actual: " + list.get(3));    System.out.println("Test indexOf(\"Six\"):");    System.out.println("Expect: 5 ---> Actual: " + list.indexOf("Six"));    System.out.println("Test lastIndexOf(\"Six\"):");    System.out.println("Expect: 15 ---> Actual: " + list.lastIndexOf("Six"));    System.out.println("Test set(4,\"Test\"):");    System.out.println("Before set, the LinkedList is: " + list);    System.out.println("Expect: \"Five\" ---> Actual: " + list.set(4,"Test"));    System.out.println("After set(4,\"Test\"), the LinkedList is: " + list);  }}
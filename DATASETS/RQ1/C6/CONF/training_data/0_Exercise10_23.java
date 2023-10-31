public class MyString2 {
    private char[] chars;
    
    public MyString2(String s) {
        chars = new char[s.length()];
        for (int i = 0; i < s.length(); i++) {
            chars[i] = s.charAt(i);
        }
    }
    
    public int compare(String s) {
        int len1 = chars.length;
        int len2 = s.length();
        int minLen = Math.min(len1, len2);
        
        for (int i = 0; i < minLen; i++) {
            if (chars[i] != s.charAt(i)) {
                return chars[i] - s.charAt(i);
            }
        }
        
        return len1 - len2;
    }
    
    public MyString2 substring(int begin) {
        int length = chars.length - begin;
        char[] newChars = new char[length];
        for (int i = 0; i < length; i++) {
            newChars[i] = chars[begin + i];
        }
        return new MyString2(new String(newChars));
    }
    
    public MyString2 toUpperCase() {
        int length = chars.length;
        char[] newChars = new char[length];
        for (int i = 0; i < length; i++) {
            char c = chars[i];
            if (c >= 'a' && c <= 'z') {
                c = (char) (c - 'a' + 'A');
            }
            newChars[i] = c;
        }
        return new MyString2(new String(newChars));
    }
    
    public char[] toChars() {
        char[] copyChars = new char[chars.length];
        System.arraycopy(chars, 0, copyChars, 0, chars.length);
        return copyChars;
    }
    
    public static MyString2 valueOf(boolean b) {
        if (b) {
            return new MyString2("true");
        } else {
            return new MyString2("false");
        }
    }
}

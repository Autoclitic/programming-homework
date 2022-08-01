import java.util.*;

public class strings {

    public static void main(String[] args) {
        
        ArrayList<Character> x = new ArrayList<Character>();
        x.add('a');
        x.add('b');
        x.add('c');

        char[] y = "welcome".toCharArray();

        for(Character i : x) {
            System.out.println(i);
        }
        for (char i : y){
            System.out.println(i);
        }
        System.out.println(x);
        System.out.println(y);
    }

    
}

package HangMan;

import java.util.*;

public class HangMan {
    
    private static String word = WordGame();
    private static String cover = new String(new char[word.length()]).replace("\0", "*");
    private static int wrong_guess = 0;

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println(word);
            
            while (wrong_guess < 7 && cover.contains("*")) {
                System.out.println("Guess any letter!");
                System.out.println(cover);
                try {
                    String guess = sc.next();
                    if (guess.length() > word.length() || guess.length() == 0){
                        System.out.println("Your guess is too long!");
                    } 
                    else{ 
                        hanger(guess); 
                    }
                    
                } catch (Exception e) {
                    System.out.println("Something happened!");
                    System.out.println("Make sure you only do one letter at a time!!");
                }
            }
            sc.close();
    }

    public static String WordGame(){
        String[] word = {
            "profession", "leadership", "assignment",
            "government", "attitude", "college", 
            "boyfriend", "area", "chest", 
            "expression", "product", "recognition", 
            "tooth", "song", "memory", 
            "death", "student", "tension", 
            "oven", "winner", "performance", 
            "cell", "employer", "preparation", 
            "requirement", "series", "studio", 
            "solution", "stranger", "buyer"
        };

        Random rnd = new Random();
        int rand_word = rnd.nextInt(word.length);

        return word[rand_word];
    }

    public static void hanger(String guess){
        String newCover = "";

        if (guess.length() == word.length()){
            for (int i = 0; i < cover.length(); i++){
                if (word.charAt(i) == guess.charAt(i)){
                    newCover += guess.charAt(i);
                } else if (cover.charAt(i) != '*'){
                    newCover += word.charAt(i);
                } else {
                    newCover += "*";
                }
            }
        } 
        else if (guess.length() > 1 && guess.length() < word.length()) {
            for(int i = 0; i < guess.length(); i++) {
                for(int j = 0; j < cover.length(); j++) {
                    if (guess.charAt(i) == word.charAt(j)){
                        newCover += guess.charAt(i);
                    }
                    else if (cover.charAt(j) != '*') {
                        newCover += word.charAt(j);
                    }
                    else {
                        newCover += "*";
                    }
                }
            }
        }
        else {

            for (int i = 0; i < cover.length(); i++){
                if (word.charAt(i) == guess.charAt(0)){
                    newCover += guess.charAt(0);
                } else if (cover.charAt(i) != '*'){
                    newCover += word.charAt(i);
                } else {
                    newCover += "*";
                }
            }
        }

        if (cover.equals(newCover)) {
            wrong_guess++;
            Stick.hangman(wrong_guess);

        } else {
            cover = newCover;
        }

        if (cover.equals(word)) {
            System.out.println("Correct! You won!");
            System.out.println("The correct word was: " + word);
        }
    }
}

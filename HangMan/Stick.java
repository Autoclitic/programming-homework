package HangMan;

public class Stick {
    private static String stage1 = "--O---|";
    private static String stage2 = "  |-  |";
    private static String stage3 = " -|-  |";
    private static String stage4 = "  |   |";
    private static String stage5 = " /    |";
    private static String stage6 = " / \\  |";
    private static String stage7 = "______|";

    public static void hangman(int progress){
        switch(progress) {
            case 1 -> System.out.println(stage1);
            case 2 -> System.out.println(stage1 + "\n" + stage2);
            case 3 -> System.out.println(stage1 + "\n" + stage3);
            case 4 -> System.out.println(stage1 + "\n" + stage3
            + "\n" + stage4);
            case 5 -> System.out.println(stage1 + "\n" + stage3
            + "\n" + stage4 + "\n" + stage5);
            case 6 -> System.out.println(stage1 + "\n" + stage3
            + "\n" + stage4 + "\n" + stage6);
            case 7 -> System.out.println(stage1 + "\n" + stage3
            + "\n" + stage4 + "\n" + stage6 + "\n" + stage7);
        }
    }
    
}

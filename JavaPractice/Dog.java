package JavaPractice;

import java.lang.Thread;

public class Dog implements Animal{
    int age;
    String breed;
    String color;
    String name;
    String owner;

    public Dog(int age, String breed, String color, String name, String owner) {
        this.age = age;
        this.breed = breed;
        this.color = color;
        this.name = name;
        this.owner = owner;
    }
    void walk() throws InterruptedException{
        System.out.println("Walk starting!!");
        final StringBuilder sb = new StringBuilder();
        String format = "[%-101s]%s%%\r";
        for (int i = 0; i<101; i++){
            sb.append("-");
            System.out.print(String.format(format, sb, i));
            Thread.sleep(20);
        }
        System.out.println("Walk is finished!");
    }
    public void animalSound() {
        System.out.println("Bark bark!");

    }
    public void animalFood() {
        System.out.println("*whining*");
        System.out.println("It seems like " + this.name + " is hungry!");
        System.out.println("Lets feed them some kibble!");
    }

    public boolean CanBeOwned() {
        return true;
    }

    void sleeping() {
        System.out.println(this.name + " is now asleep :)");
    }
    
    public static void main(String[] args) throws InterruptedException{
        Puppy myPuppy = new Puppy(1, "Lab", "Red", "Hop", "Georgia");
        System.out.println(myPuppy.PuppyName());
        System.out.println(myPuppy.PuppyAge());
        Thread.sleep(1000);
        System.out.println(myPuppy.PuppyBreed());
        System.out.println(myPuppy.PuppyOwner());
        myPuppy.animalSound();
        myPuppy.animalFood();
        Thread.sleep(3000);
        myPuppy.walk();
        Thread.sleep(2000);
        myPuppy.sleeping();

        if (myPuppy.CanBeOwned()) {
            System.out.println(myPuppy.name + " is happy to be with you!");
        } else {
            System.out.println(myPuppy.name + " just ran away!!");
        }

    }
}

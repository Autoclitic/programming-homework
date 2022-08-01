package JavaPractice;

public class Puppy extends Dog {
    public Puppy(int age, String breed, String color, String name, String owner) {
        super(age, breed, color, name, owner);
    }
    
    public String PuppyName() {
        var puppyName = "This is " + this.name;
        return puppyName;
    }
    public String PuppyAge() {
        var puppyAge = this.name + " is " + this.age + " years old";
        return puppyAge;
    }
    public String PuppyOwner() {
        return this.owner;
    }
    public String PuppyBreed() {
        return this.breed;
    }
}

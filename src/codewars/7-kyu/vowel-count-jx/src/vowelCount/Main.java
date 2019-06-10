package vowelCount;

public class Main {
  public static void main(String[] args) {
    String string1 = "Imagine all the people living life in peace."; // Should return 16
    System.out.println(Kata.getCount(string1));
    String string2 = "One day the world will be as one."; // Shoudl return 9
    System.out.println(Kata.getCount(string2));
  }
}
package squareSum;

public class Kata {
  public static int squareSum(int[] n) {
    int sum = 0;
    for (int num : n) {
      sum += num * num;
      System.out.println(num * num);
    }
    return sum;
  }
}
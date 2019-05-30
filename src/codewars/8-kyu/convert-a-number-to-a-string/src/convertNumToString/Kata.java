package convertNumToString;

class Kata {
  public static String numberToString(int num) {
    String template = "%s";
    return String.format(template, num);
  }
}
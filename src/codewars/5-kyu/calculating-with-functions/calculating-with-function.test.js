const {
  one,
  two,
  three,
  four,
  five,
  six,
  seven,
  eight,
  nine,
  plus,
  minus,
  times,
  dividedBy
} = require("./calculating-with-functions");

describe("Calculating With Functions CodeWars 5kyu challenge", () => {
  it("should return an integer answer when adding two integers functionally ", () => {
    expect(one(plus(two()))).toBe(3);
    expect(six(plus(seven()))).toBe(13);
    expect(two(plus(nine()))).toBe(11);
    expect(three(plus(six()))).toBe(9);
  });
  it("should return an integer when subtracting two integers functionally", () => {
    expect(nine(minus(three()))).toBe(6);
    expect(seven(minus(two()))).toBe(5);
    expect(nine(minus(nine()))).toBe(0);
    expect(one(minus(three()))).toBe(-2);
  });
  it("should return an integer when multiplying two integers functionally", () => {
    expect(five(times(four()))).toBe(20);
    expect(nine(times(nine()))).toBe(81);
    expect(five(times(five()))).toBe(25);
    expect(one(times(one()))).toBe(1);
  });
  it("should return a non-floating point integer when dividing two integers functionally", () => {
    expect(eight(dividedBy(two()))).toBe(4);
    expect(four(dividedBy(four()))).toBe(1);
    expect(nine(dividedBy(4))).toBe(2);
    expect(six(dividedBy(two()))).toBe(3);
  });
});

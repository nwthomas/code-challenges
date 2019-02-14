const isArmstrongNumber = require("./armstrong-numbers");

test("takes in a number and returns 'true' if it's equal to the sume of the n'th powers of its digits", () => {
  expect(isArmstrongNumber(153)).toBe(true);
  expect(isArmstrongNumber(531)).toBe(false);
  expect(isArmstrongNumber(0)).toBe(true);
  expect(isArmstrongNumber(11111111)).toBe(false);
  expect(isArmstrongNumber(10789089723)).toBe(false);
  expect(isArmstrongNumber(371)).toBe(true);
  expect(isArmstrongNumber(407)).toBe(true);
});

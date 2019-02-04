const sumOfDigits = require("./sum-of-digits");

test("Takes in a number and returns a sum of all digits added up", () => {
  expect(sumOfDigits(12345)).toBe(15);
  expect(sumOfDigits(23)).toBe(5);
  expect(sumOfDigits(496)).toBe(19);
  expect(sumOfDigits(7309)).toBe(19);
  expect(sumOfDigits(8974039827)).toBe(57);
});

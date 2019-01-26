const maxNumber = require("./form-the-largest");

test("takes in a number and sorts the digits to form the biggest number possible", () => {
  expect(maxNumber(213)).toBe(321);
  expect(maxNumber(7389)).toBe(9873);
  expect(maxNumber(63792)).toBe(97632);
  expect(maxNumber(566797)).toBe(977665);
  expect(maxNumber(1000000)).toBe(1000000);
});

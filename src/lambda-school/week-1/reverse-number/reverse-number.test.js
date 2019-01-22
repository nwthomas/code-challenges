const reverseNumber = require("./reverse-number");

test("Reverses the number you pass in", () => {
  expect(reverseNumber(12345)).toBe(54321);
  expect(reverseNumber(555)).toBe(555);
  expect(reverseNumber(2543)).toBe(3452);
});

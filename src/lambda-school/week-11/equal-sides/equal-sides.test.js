const equalSides = require("./equal-sides");

test("takes in an array of numbers and finds the index of the number where both sides of the array around it sum to the same number", () => {
  expect(equalSides([1, 5, 10, 6])).toBe(2);
  expect(equalSides([1, 2, 3, 4, 3, 2, 1])).toBe(3);
  expect(equalSides([1, 1, 1, 4, 2, 1])).toBe(3);
  expect(equalSides([1, 4, 2, 1, 1, 10, 5, 3, 1])).toBe(5);
  expect(equalSides([0])).toBe(-1);
});

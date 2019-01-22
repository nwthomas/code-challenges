const getSum = require("./sum-of-numbers");

test("Sum all numbers between any two numbers, including positive and negative", () => {
  expect(getSum(1, 0)).toBe(1);
  expect(getSum(1, 2)).toBe(3);
  expect(getSum(-1, 2)).toBe(2);
  expect(getSum(4, 8)).toBe(30);
});

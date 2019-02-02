const toBinaryString = require("./to-binary-string");

test("takes in a number and returns the binary form of that number", () => {
  expect(toBinaryString(0)).toBe(0);
  expect(toBinaryString(1)).toBe(1);
  expect(toBinaryString(2)).toBe(10);
  expect(toBinaryString(3)).toBe(11);
  expect(toBinaryString(4)).toBe(100);
  expect(toBinaryString(5)).toBe(101);
  expect(toBinaryString(6)).toBe(110);
  expect(toBinaryString(7)).toBe(111);
  expect(toBinaryString(8)).toBe(1000);
  expect(toBinaryString(9)).toBe(1001);
  expect(toBinaryString(10)).toBe(1010);
  expect(toBinaryString(11)).toBe(1011);
  expect(toBinaryString(12)).toBe(1100);
  expect(toBinaryString(13)).toBe(1101);
  expect(toBinaryString(14)).toBe(1110);
  expect(toBinaryString(15)).toBe(1111);
  expect(toBinaryString(16)).toBe(10000);
  expect(toBinaryString(17)).toBe(10001);
});

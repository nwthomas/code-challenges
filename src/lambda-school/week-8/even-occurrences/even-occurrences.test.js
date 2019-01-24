const evenOccurrence = require("./even-occurences");

test("Checks array to see which items both appears first and appears an even amount of times", () => {
  expect(evenOccurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4])).toBe(4);
  expect(evenOccurrence([1, 7, 2, 4, 5, 6, 8, 9, 6, 4, 7])).toBe(7);
  expect(evenOccurrence([1, 7, 2, 4, 5, 6])).toBe(null);
});

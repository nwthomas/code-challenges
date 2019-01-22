const persistence = require("./persistence-bugger");

test("Returns the multiplicative persistence of a number", () => {
  expect(persistence(39)).toBe(3);
  expect(persistence(999)).toBe(4);
  expect(persistence(4)).toBe(0);
});

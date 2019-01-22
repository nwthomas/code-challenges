const getCount = require("./vowel-count");

test("Return the number of vowels of a, e, i, o, and u in any given string", () => {
  expect(getCount("Dude, this is an example string.")).toBe(9);
  expect(getCount("This is another test.")).toBe(6);
  expect(getCount("Testing, testing!")).toBe(4);
});

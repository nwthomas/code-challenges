const scorePalindromes = require("./score-palindromes");

test("Takes in a string and returns a score for how many letters are the same when it's reversed", () => {
  expect(scorePalindromes("Dude.")).toBe(1);
  expect(scorePalindromes("Anna")).toBe(4);
  expect(scorePalindromes("Whatever you want to say, do it.")).toBe(0);
  expect(scorePalindromes("WasItACarOrACatISaw")).toBe(19);
  expect(scorePalindromes("87A(7hjkalsdfhnkjboh")).toBe(0);
});

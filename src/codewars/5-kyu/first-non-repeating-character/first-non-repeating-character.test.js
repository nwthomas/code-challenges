const firstNonRepeatingLetter = require("./first-non-repeating-character");

test("Takes string and returns the first character that does not repeat itself or empty string otherwise", () => {
  expect(firstNonRepeatingLetter("stress")).toBe("t");
  expect(firstNonRepeatingLetter("98dji9f")).toBe("8");
  expect(firstNonRepeatingLetter("aaIIuuEE")).toBe("");
  expect(firstNonRepeatingLetter("Moonmen")).toBe("e");
  expect(firstNonRepeatingLetter("891jhDoi7(*&$aJsdfB981")).toBe("h");
});

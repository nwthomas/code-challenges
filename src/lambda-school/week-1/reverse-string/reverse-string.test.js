const reverseString = require("./reverse-string");

test("Reverses the string you pass in", () => {
  expect(reverseString("Hello world!")).toBe("!dlrow olleH");
  expect(reverseString("asdfasdf")).toBe("fdsafdsa");
  expect(reverseString("CS rocks!")).toBe("!skcor SC");
  expect(reverseString("Nathan Thomas")).toBe("samohT nahtaN");
});

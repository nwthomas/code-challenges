const list = require("./format-a-string-of-names");

test("Returns a string formatted as a list of names separated by commas", () => {
  expect(list([{ name: "Bart" }, { name: "Lisa" }, { name: "Maggie" }])).toBe(
    "Bart, Lisa & Maggie"
  );
  expect(list([{ name: "Bart" }, { name: "Lisa" }])).toBe("Bart & Lisa");
  expect(list([{ name: "Bart" }])).toBe("Bart");
  expect(list([])).toBe("");
});

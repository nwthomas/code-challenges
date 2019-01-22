const expandedForm = require("./write-number-in-expanded-form");

test("Returns a string of a number in its expanded form", () => {
  expect(expandedForm(12)).toBe("10 + 2");
  expect(expandedForm(42)).toBe("40 + 2");
  expect(expandedForm(70304)).toBe("70000 + 300 + 4");
  expect(expandedForm(890230)).toBe("800000 + 90000 + 200 + 30");
  expect(expandedForm(57896)).toBe("50000 + 7000 + 800 + 90 + 6");
});

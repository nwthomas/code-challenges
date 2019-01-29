const expandedNums = require("./expanded-numbers");

test("Takes in a number of any length and returns its expanded form", () => {
  expect(expandedNums(1798097)).toBe(
    "1000000 + 700000 + 90000 + 8000 + 90 + 7"
  );
  expect(expandedNums(908070)).toBe("900000 + 8000 + 70");
  expect(expandedNums(42098)).toBe("40000 + 2000 + 90 + 8");
});

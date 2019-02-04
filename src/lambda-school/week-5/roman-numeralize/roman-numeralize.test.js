const romanNumeralize = require("./roman-numeralize");

test("takes in a number and returns the roman numeral version of it", () => {
  expect(romanNumeralize(1973)).toBe("MCMLXXIII");
  expect(romanNumeralize(1947)).toBe("MCMXLVII");
  expect(romanNumeralize(1987)).toBe("MCMLXXXVII");
  expect(romanNumeralize(1784)).toBe("MDCCLXXXIV");
});

const stringToCamel = require("./string-to-camel-case");

test("Converts any given dash or underscore string to camel casing", () => {
  expect(stringToCamel("the-stealth-warrior")).toBe("theStealthWarrior");
  expect(stringToCamel("The_stealth_warrior")).toBe("TheStealthWarrior");
  expect(stringToCamel("some-random-file-name")).toBe("someRandomFileName");
});

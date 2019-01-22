const reverseCase = require("./reverse-case");

test("Inverts lower-and-upper-case characters in a string", () => {
  expect(reverseCase("HELLO world!")).toBe("hello WORLD!");
  expect(reverseCase("DuDe ThAt Is CrAzY")).toBe("dUdE tHaT iS cRaZy");
});

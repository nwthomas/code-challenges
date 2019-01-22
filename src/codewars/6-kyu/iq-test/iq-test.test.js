const iqTest = require("./iq-test");

test("Return the index + 1 of a number differs that from the other number in 'evenness'", () => {
  expect(iqTest("2 4 7 8 10")).toBe(3);
  expect(iqTest("1 2 1 1")).toBe(2);
});

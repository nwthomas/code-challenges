const { AND, OR, NOT, XOR, NAND } = require("./emulate-logic-gates");

test("takes in calls a logic gate emulation function with two boolean values and returns a true/false statement", () => {
  expect(AND(true, false)).toBe(false);
  expect(AND(true, true)).toBe(true);
  expect(AND(false, false)).toBe(false);
  expect(OR(true, true)).toBe(true);
  expect(OR(false, true)).toBe(true);
  expect(OR(false, false)).toBe(false);
  expect(NOT(false, true)).toBe(true);
  expect(XOR(true, true)).toBe(false);
  expect(XOR(false, true)).toBe(true);
  expect(NAND(true, true)).toBe(false);
  expect(NAND(true, false)).toBe(true);
});

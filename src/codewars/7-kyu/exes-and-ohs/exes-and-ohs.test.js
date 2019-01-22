const XO = require("./exes-and-ohs");

test("Checks a string to see if there's an equal amount of Xs and Os", () => {
  expect(XO("ooxx")).toBe(true);
  expect(XO("xooxx")).toBe(false);
  expect(XO("ooxXm")).toBe(true);
  expect(XO("zpzpzpp")).toBe(true); // when no 'x' and 'o' is present should return true
  expect(XO("zzoo")).toBe(false);
});

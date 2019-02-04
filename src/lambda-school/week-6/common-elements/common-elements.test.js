const commonElements = require("./common-elements");

test("Checks any two arrays for similar elements and outputs them", () => {
  expect(commonElements([1, 2, 3, 4], [3, 4, 5, 6])).toEqual([3, 4]);
  expect(commonElements(["a", "b", "c"], ["x", "y", "z", "a"])).toEqual(["a"]);
  expect(commonElements([1, 2, 3], [4, 5, 6])).toEqual([]);
});

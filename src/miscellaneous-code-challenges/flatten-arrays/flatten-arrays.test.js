const flattenArrays = require("./flatten-arrays");

test("Takes in an array of nested arrays and flattens it into a single array", () => {
  expect(flattenArrays([[3, [1, [8]], 9], 4])).toEqual([3, 1, 8, 9, 4]);
  expect(flattenArrays([5, [8, 3, [9]], [4, 3]])).toEqual([5, 8, 3, 9, 4, 3]);
  expect(flattenArrays([1, [2, [3, [4, [5, [6]]]]]])).toEqual([
    1,
    2,
    3,
    4,
    5,
    6
  ]);
});

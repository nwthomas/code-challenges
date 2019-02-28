const rotateImage = require("./rotate-image");

test("takes in an array of arrays of pixels and rotates it counterclockwise", () => {
  expect(
    rotateImage([
      [1, 1, 5, 9, 9],
      [2, 2, 6, 0, 0],
      [3, 3, 7, 1, 1],
      [4, 4, 8, 2, 2],
      [5, 5, 9, 3, 3]
    ])
  ).toEqual([
    [9, 0, 1, 2, 3],
    [9, 0, 1, 2, 3],
    [5, 6, 7, 8, 9],
    [1, 2, 3, 4, 5],
    [1, 2, 3, 4, 5]
  ]);
  expect(rotateImage([[1, 2], [3, 4]])).toEqual([[2, 4], [1, 3]]);
  expect(rotateImage([[3, 4, 5], [2, 3, 4]])).toEqual([[5, 4], [4, 3], [3, 2]]);
});

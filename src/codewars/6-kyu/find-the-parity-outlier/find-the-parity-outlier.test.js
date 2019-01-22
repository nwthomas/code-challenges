const findOutlier = require("./find-the-parity-outlier");

test("Find a single even or odd integer in an array of the opposites", () => {
  expect(findOutlier([2, 4, 0, 100, 4, 11, 2602, 36])).toBe(11);
  expect(findOutlier([160, 3, 1719, 19, 11, 13, -21])).toBe(160);
  expect(findOutlier([354, 10, 2, 54, 90, 31, 26])).toBe(31);
});

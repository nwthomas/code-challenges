const findIntervalSpread = require("./intervalSpread.js");

describe("findIntervalSpread", () => {
  test("returns an empty array if the argument is not an array", () => {
    const result = findIntervalSpread("test");
    expect(result).toEqual([]);
  });

  test("returns an empty array if the argument is an empty array", () => {
    const result = findIntervalSpread([]);
    expect(result).toEqual([]);
  });

  test("returns the correct interval spread for a small set of intervals", () => {
    const result = findIntervalSpread([
      [1, 2],
      [5, 12]
    ]);
    expect(result).toEqual([2, 5]);
  });

  test("returns the correct interval spread for a large set of intervals", () => {
    const result = findIntervalSpread([
      [0, 3],
      [2, 6],
      [3, 4],
      [6, 9]
    ]);
    expect(result).toEqual([3, 6]);
  });
});

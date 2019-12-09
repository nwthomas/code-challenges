const {
  createArray,
  findValues,
  flattenArray
} = require("./find2dArrayValues.js");

const utils = {
  getSides: function(array) {
    const y = array.length;
    const x = array[0].length;
    return { x, y };
  }
};

describe("find2dArrayValues", () => {
  describe("createArray", () => {
    test("creates array array of specified length correctly", () => {
      const result = createArray(10, 10);
      expect(utils.getSides(result)).toEqual({ x: 10, y: 10 });
    });

    test("has the correct integers for each position", () => {
      const result = createArray(5, 5);
      expect(result[0][0]).toBe(1);
      expect(result[1][4]).toBe(10);
      expect(result[4][4]).toBe(25);
    });

    test("returns null if x or y are not integers", () => {
      const result = createArray("test", []);
      expect(result).toBeNull();
    });
  });

  describe("flattenArray", () => {
    test("should successfully flatten a small array of arrays", () => {
      const array = [1, [[9, [[1, 5]]], 2]];
      const result = flattenArray(array);
      expect(result).toEqual([1, 9, 1, 5, 2]);
    });

    test("should successfully flatten a large array of arrays", () => {
      const array = [
        [[[[[[[[[[[[[[[[5]]]]]]]], 0]]]]]]]],
        [[[1, [[[[[[[[[[[[4]]]]]]], 3, 2]]]]]]]],
        [[[[10]], 3], [[[[[[[[[[[[[7198237]]]]]]]]]]]]]]
      ];
      const result = flattenArray(array);
      expect(result).toEqual([5, 0, 1, 4, 3, 2, 10, 3, 7198237]);
    });

    test("returns null if a non-array or one with no length is passed in", () => {
      const emptyResult = flattenArray([]);
      const nonArrayResult = flattenArray("test");
      expect(emptyResult).toBeNull();
      expect(nonArrayResult).toBeNull();
    });
  });

  describe("findMostUsed2dArrayValues", () => {
    test("returns null if x or y arguments are not integers", () => {
      const result = findValues("test", [], {});
      expect(result).toBeNull();
    });

    test("should return the number of times an integer is seen in a small 2D array", () => {
      const result = findValues(10, 10, 2);
      expect(result).toEqual(2);
    });

    test("should return the number of times an integer is seen in a large 2D array", () => {
      const result = findValues(1000, 1000, 50);
      expect(result).toBe(6);
    });
  });
});

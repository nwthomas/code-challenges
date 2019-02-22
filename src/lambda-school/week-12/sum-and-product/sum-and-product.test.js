const sumAndProduct = require("./sum-and-product");

test("takes in a sum and a product and returns an array of numbers that can add/multiply to both or else null if impossible", () => {
  expect(sumAndProduct(6, 9)).toEqual([3, 3]);
  expect(sumAndProduct(12, 36)).toEqual([6, 6]);
  expect(sumAndProduct(4, 4)).toEqual([2, 2]);
  expect(sumAndProduct(400, 1000)).toEqual(null);
  expect(sumAndProduct(0, 50)).toEqual(null);
});

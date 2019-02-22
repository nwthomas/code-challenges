/*

Good morning! Given a sum and a product, find two integers x and y, where x + y === sum, and x * y === product. You will return this in an array.

For example, calling sumAndProduct(6, 9) should return [3, 3] because 3 + 3 === 6, and 3 * 3 === 9.

Please make sure to return your array such that x <= y in the format [x, y].

If there is no valid x/y combination to solve for given (sum, product) values, your function should return null.

*/

const sumAndProduct = (sum, product) => {
  for (let i = 0; i < sum; i++) {
    let setNums = [i, Math.abs(i - sum)];
    if (setNums[0] * setNums[1] === product) return setNums;
  }
  return null;
};

module.exports = sumAndProduct;

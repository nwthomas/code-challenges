/*

https://www.codewars.com/kata/sort-odd-and-even-numbers-in-different-order/javascript

You have an array of numbers.

Your task is to sort odd numbers within the array in ascending order, and even numbers in descending order.

Note that zero is an even number. If you have an empty array, you need to return it.

Example:
sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 8, 4, 5, 2]

*/

function sortArray(array) {
  if (!array.length) return [];
  const even = [],
    odd = [],
    final = [];
  array.forEach(num => {
    if (num % 2) {
      odd.push(num);
      final.push("o");
    } else {
      even.push(num);
      final.push("e");
    }
  });
  odd.sort(function(a, b) {
    return a - b;
  });
  even.sort(function(a, b) {
    return b - a;
  });
  for (let i = 0; i < final.length; i++) {
    final[i] === "o" ? (final[i] = odd.shift()) : (final[i] = even.shift());
  }
  return final;
}

module.exports = sortArray;

const bubbleSort = require("./bubble-sort");

test("sorts array by utilizing the bubble sort algortithm", () => {
  expect(bubbleSort([9, 10, 2, 4, 5, 3, 6, 8, 7, 1])).toEqual([
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10
  ]);
  expect(bubbleSort([])).toEqual([]);
  expect(bubbleSort([3, 8, 849, 1, 6, 2, 9])).toEqual([1, 2, 3, 6, 8, 9, 849]);
  expect(bubbleSort([3, 0, 1])).toEqual([0, 1, 3]);
});

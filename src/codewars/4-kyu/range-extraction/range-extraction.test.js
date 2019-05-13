const solution = require("./range-extraction");

describe("Range Extraction 4kyu CodeWars challenge solution", () => {
  it("takes in an array of numbers and returns a string of the extracted rangess", () => {
    const arr1 = [
      -6,
      -3,
      -2,
      -1,
      0,
      1,
      3,
      4,
      5,
      7,
      8,
      9,
      10,
      11,
      14,
      15,
      17,
      18,
      19,
      20
    ];
    const arr2 = [-3, -2, -1, 2, 10, 15, 16, 18, 19, 20];
    expect(solution(arr1)).toEqual("-6,-3-1,3-5,7-11,14,15,17-20");
    expect(solution(arr2)).toEqual("-3--1,2,10,15,16,18-20");
  });
  it("accepts an array of random numbers and returns a string of the extracted ranges", () => {
    const arr = [
      -85,
      69,
      -100,
      -30,
      -29,
      -28,
      -27,
      -26,
      40,
      61,
      62,
      10,
      11,
      12
    ];
    expect(solution(arr)).toEqual("-85,69,-100,-30--26,40,61,62,10-12");
  });
});
